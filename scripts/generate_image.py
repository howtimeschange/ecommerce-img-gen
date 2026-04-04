#!/usr/bin/env python3
"""
1xm.ai image generation client with retry logic.
Handles proxy issues by using urllib3 directly with retry mechanism.

Usage:
    python3 generate_image.py <prompt> <ref_image_path> [output_path] [model]

Environment:
    1XM_API_KEY - API key for 1xm.ai (or pass via config)
    Falls back to key in ~/.openclaw/workspace/image-gen-service/backend/.env
"""

import json, base64, os, time, re, sys
import urllib3

# API key MUST be provided via environment variable. No hardcoded key.
# Set: export 1XM_API_KEY=your_key_here
DEFAULT_API_KEY = None  # Must be set via environment
API_URL = "https://1xm.ai/v1/chat/completions"
TIMEOUT = 180
MAX_RETRIES = 10
RETRY_DELAY = 5

# ─────────────────────────────────────────────────────────────────────────────
# 用户-facing 模型映射 → 底层实际 API 模型 + 支持的分辨率
# ─────────────────────────────────────────────────────────────────────────────
# 模型命名（对用户友好）：
#   nano-banana-2   → gemini-3.1-flash-image-preview（快速，默认）
#   nano-banana-pro  → gemini-3-pro-image-preview（高质量，支持 4K）
MODEL_MAP = {
    "nano-banana-2": {
        "api_model": "gemini-3.1-flash-image-preview",
        "default_size": "2K",
        "supported_sizes": ["1K", "2K"],
        "speed": "fast",
    },
    "nano-banana-pro": {
        "api_model": "gemini-3-pro-image-preview",
        "default_size": "2K",
        "supported_sizes": ["1K", "2K", "4K"],
        "speed": "slow",
    },
}

# 默认用户模型
DEFAULT_USER_MODEL = "nano-banana-2"

# 分辨率档位 → Gemini API 的 imageSize 参数
SIZE_MAP = {
    "1K": "1K",
    "2K": "2K",
    "4K": "4K",
}


def get_api_key():
    """Read from env var, then .env file, then fail loudly."""
    key = os.environ.get("1XM_API_KEY") or os.environ.get("1XM_API_KEY")
    if key:
        return key
    env_path = os.path.expanduser(
        "~/.openclaw/workspace/image-gen-service/backend/.env"
    )
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "API_KEY" in line and "=" in line:
                        k, v = line.split("=", 1)
                        if "IMAGE_API_KEY" in k or "1XM" in k:
                            val = v.strip()
                            if val and val != "your_key_here":
                                return val
    # No valid key found — fail clearly
    print("ERROR: 1XM_API_KEY not set. Set it via:", flush=True)
    print("  export 1XM_API_KEY=your_api_key_here", flush=True)
    raise RuntimeError("1XM_API_KEY environment variable is not set")


def resolve_model(user_model: str = None):
    """
    Resolve user-facing model name → (api_model_str, resolved_size_str).
    Supports:
      - "nano-banana-2"   → gemini-3.1-flash-image-preview
      - "nano-banana-pro" → gemini-3-pro-image-preview
      - Direct api model names passed through unchanged
    Returns (api_model, size) tuple.
    """
    user_model = user_model or DEFAULT_USER_MODEL

    if user_model in MODEL_MAP:
        cfg = MODEL_MAP[user_model]
        return cfg["api_model"], cfg["default_size"], user_model

    # Pass-through: treat as direct API model name
    return user_model, "2K", user_model


def resolve_size(user_size: str, api_model: str):
    """Resolve user size → validated size supported by the model."""
    if not user_size:
        return "2K"

    # Validate against model's supported sizes
    for name, cfg in MODEL_MAP.items():
        if cfg["api_model"] == api_model:
            if user_size in cfg["supported_sizes"]:
                return user_size
            # Downgrade to highest supported
            supported = cfg["supported_sizes"]
            if user_size == "4K" and "4K" not in supported:
                print(f"⚠️  {api_model} does not support 4K, using 2K instead", flush=True)
                return "2K"
            return supported[-1]  # highest available

    return user_size


def encode_image(path):
    """Read image as base64 data URL."""
    with open(path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    ext = os.path.splitext(path)[-1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{b64}"


def extract_image(response_text):
    """Extract base64 image from model response."""
    # Try each known MIME type
    for mime in ["png", "jpeg", "webp"]:
        pattern = f"data:image/{mime};base64,([A-Za-z0-9+/\n]+)"
        match = re.search(pattern, response_text, re.IGNORECASE)
        if match:
            data = match.group(1).replace("\n", "").replace(" ", "")
            # Pad to multiple of 4
            padding = len(data) % 4
            if padding:
                data += "=" * (4 - padding)
            return base64.b64decode(data)
    return None


def generate(prompt, ref_image_path=None, model=None, save_path=None, size=None):
    """
    Generate image via 1xm.ai with retry logic.

    Args:
        prompt: Text prompt describing the image
        ref_image_path: Optional path to reference image (base64 injected)
        model: User-facing model name (nano-banana-2 / nano-banana-pro) or
               direct API model name (default: nano-banana-2)
        save_path: Optional path to save output PNG
        size: Resolution tier: 1K (draft) / 2K (iterate) / 4K (final).
              Default: model's default (2K for nano-banana-2, 2K for nano-banana-pro)

    Returns:
        bytes: PNG image data, or None on failure
    """
    api_key = get_api_key()

    # Resolve user model → API model
    api_model, default_size, user_model = resolve_model(model)

    # Resolve size
    resolved_size = resolve_size(size or default_size, api_model)
    size_api_val = SIZE_MAP.get(resolved_size, "2K")

    # Display info
    print(f"[Model] {user_model} → {api_model} | [Size] {resolved_size} ({size_api_val})", flush=True)

    ref_url = None
    if ref_image_path and os.path.exists(ref_image_path):
        ref_url = encode_image(ref_image_path)

    # Build message content
    if ref_url:
        content = [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": ref_url}},
        ]
    else:
        content = [{"type": "text", "text": prompt}]

    payload = {
        "model": api_model,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": 2000,
    }

    # Inject imageSize for Gemini API
    payload["imageSize"] = size_api_val

    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        # Fresh pool each attempt to avoid stale connections
        http = urllib3.PoolManager(num_pools=1, maxsize=1)

        try:
            t0 = time.time()
            resp = http.request(
                "POST",
                API_URL,
                body=json.dumps(payload),
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                timeout=urllib3.Timeout(TIMEOUT),
                retries=False,
            )
            elapsed = time.time() - t0

            if resp.status == 200:
                data = json.loads(resp.data)
                content_text = data["choices"][0]["message"]["content"]
                img_data = extract_image(content_text)
                if img_data:
                    print(f"✅ Generated in {elapsed:.1f}s ({len(img_data)} bytes)", flush=True)
                    if save_path:
                        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
                        with open(save_path, "wb") as f:
                            f.write(img_data)
                        print(f"📁 Saved to {save_path}", flush=True)
                    return img_data
                else:
                    print(f"⚠️  No image in response (attempt {attempt})", flush=True)
            else:
                err = resp.data[:100].decode("utf-8", errors="replace")
                print(f"⚠️  Error {resp.status}: {err} (attempt {attempt})", flush=True)
                last_error = f"HTTP {resp.status}"

        except Exception as e:
            err_str = f"{type(e).__name__}: {str(e)[:100]}"
            print(f"⚠️  {err_str} (attempt {attempt})", flush=True)
            last_error = err_str

        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY)

    print(f"❌ All {MAX_RETRIES} attempts failed. Last error: {last_error}", flush=True)
    return None


def batch_generate(tasks, max_concurrent=2):
    """
    Batch generate multiple images.

    Args:
        tasks: list of (prompt, ref_path, save_path, model, size) tuples
               model and size are optional (use defaults if None)
        max_concurrent: max parallel tasks (default 2)
    """
    import concurrent.futures
    results = []

    def safe_generate(args):
        prompt, ref_path, save_path = args[0], args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None
        model = args[3] if len(args) > 3 else None
        size = args[4] if len(args) > 4 else None
        try:
            return generate(prompt, ref_path, model, save_path, size)
        except Exception as e:
            print(f"Error: {e}", flush=True)
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        futures = [executor.submit(safe_generate, t) for t in tasks]
        for fut in concurrent.futures.as_completed(futures):
            results.append(fut.result())

    return results


def apply_compliance(prompt, market="东南亚"):
    """
    Auto-fix common compliance issues in prompts.
    
    Returns: (fixed_prompt, fixes_applied)
    """
    fixes = []
    fixed = prompt
    
    # Number replacements by market
    number_fixes = {
        "4": {"markets": ["中国", "日本", "韩国", "东南亚华人"], "replace": "6"},
        "9": {"markets": ["日本"], "replace": "7"},
        "13": {"markets": ["欧美", "巴西", "菲律宾"], "replace": "12"},
    }
    
    for num, rule in number_fixes.items():
        if any(m in market for m in rule["markets"]):
            if num in fixed:
                fixed = fixed.replace(num, rule["replace"])
                fixes.append(f"数字{num}→{rule['replace']}（{market}）")
    
    # Copyright/IP blocklist scan
    ip_blocklist = [
        "Mickey Mouse", "Frozen", "Spider-Man", "Hello Kitty",
        "Pokemon", "Doraemon", "Rilakkuma",
        "Chanel", "Gucci", "Louis Vuitton",
        "高仿", "复刻", "A货", "1:1", "fake", "replica", "counterfeit"
    ]
    
    for ip in ip_blocklist:
        if ip.lower() in fixed.lower():
            print(f"WARNING: IP/品牌侵权风险词 detected: {ip}", flush=True)
    
    return fixed, fixes


if __name__ == "__main__":
    # Parse CLI args with argparse for clean model/size support
    import argparse

    parser = argparse.ArgumentParser(description="1xm.ai image generation")
    parser.add_argument("prompt", nargs="?", help="Image generation prompt")
    parser.add_argument("ref_image", nargs="?", help="Reference image path")
    parser.add_argument("output_path", nargs="?", help="Output PNG path")
    parser.add_argument("--model", "-m", default=None,
                        help=f"Model: {', '.join(MODEL_MAP.keys())} or direct API name "
                             f"(default: {DEFAULT_USER_MODEL})")
    parser.add_argument("--size", "-s", default=None,
                        help="Resolution: 1K (draft) / 2K (iterate) / 4K (final, nano-banana-pro only)")
    parser.add_argument("--batch", dest="batch_json", metavar="JSON",
                        help="Batch mode: JSON string of [(prompt, ref, out, model, size), ...]")
    args = parser.parse_args()

    if args.batch_json:
        import json
        tasks = json.loads(args.batch_json)
        # Format: [(prompt, ref, out, model, size), ...]
        def safe_gen(t):
            prompt, ref, out = t[0], t[1] if len(t) > 1 else None, t[2] if len(t) > 2 else None
            model = t[3] if len(t) > 3 else None
            size = t[4] if len(t) > 4 else None
            try:
                return generate(prompt, ref, model, out, size)
            except Exception as e:
                print(f"Error: {e}", flush=True)
                return None
        results = batch_generate(tasks)
        print(f"Batch done: {sum(1 for r in results if r)}/{len(results)} successful")
        sys.exit(0)

    if not args.prompt:
        print("Usage:")
        print("  generate_image.py <prompt> [ref_image] [output_path] [--model nano-banana-2] [--size 2K]")
        print(f"  generate_image.py <prompt> [ref_image] [output_path] -m nano-banana-pro -s 4K")
        print(f"  generate_image.py --batch <json>")
        print(f"\nAvailable models:")
        for name, cfg in MODEL_MAP.items():
            sizes = "/".join(cfg["supported_sizes"])
            print(f"  {name:20s} → {cfg['api_model']} (supports: {sizes})")
        sys.exit(1)

    prompt = args.prompt
    ref_path = args.ref_image
    out_path = args.output_path
    model = args.model
    size = args.size
    
    # Apply compliance fixes
    market = os.environ.get("TARGET_MARKET", "东南亚")
    prompt, fixes = apply_compliance(prompt, market)
    for f in fixes:
        print(f"  [COMPLIANCE] {f}", flush=True)
    
    result = generate(prompt, ref_path, model, out_path)
    sys.exit(0 if result else 1)
