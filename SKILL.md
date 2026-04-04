---
name: ecommerce-img-gen
title: 跨境电商图片生成工具
description: 跨境电商图片生成工具。根据产品图生成各平台（Amazon / Shopee / TikTok Shop / Lazada / AliExpress / Temu / SHEIN）主图、详情页长图、生活场景图。内置6种视觉风格路由、6层合规审查（意图/品牌/版权/文化/平台/授权）。支持模型切换：nano-banana-2（快速，默认2K）和 nano-banana-pro（高质量，支持4K终稿）。触发场景：(1) 用户发产品图要求"做电商图"、"生成主图"、"详情页"；(2) 用户提到具体平台+主图或详情页；(3) 用户要求"全套图"、"多平台图"；(4) 用户发产品图后指定品牌和目标市场。
---

# ecommerce-img-gen 技能

端到端设计：从产品图 → 6平台合规主图 → 详情页长图。

## 能力矩阵

| 能力 | 说明 |
|------|------|
| **7平台主图** | Amazon · Shopee · TikTok Shop · Lazada · AliExpress · Temu · SHEIN |
| **6种风格** | 极简白底 / 生活场景 / 轻奢简约 / 活力色彩 / 手绘插画 / UGC快节奏 |
| **6层合规审查** | 意图过滤 → 品牌合规 → 版权检查 → 文化适配 → 平台规范 → 发布授权 |
| **详情页长图** | 5类场景 × 7平台组合，1:8超长竖版 |
| **文化合规** | 数字/颜色/图案禁忌规则库，覆盖东南亚/日本/欧美/中东 |
| **批量生成** | 多张变体一次生成，自动保存到品牌目录 |

## 核心流程（8步）

```
用户发产品图 + 目标平台/市场
    ↓
Step 1: Vision 分析商品
    → 提取品牌/品类/颜色/材质/特征/适用人群
    ↓
Step 2: 确认平台
    → 用户指定 → 直接用；未指定 → 根据品类/市场推荐
    ↓
Step 3: 风格路由
    → 根据品类自动推荐风格（见 references/styles_and_routing.md）
    ↓
Step 4: 合规审查（L1-L4）
    → L1 意图过滤 → L2 品牌合规 → L3 版权检查（IP黑名单）→ L4 文化适配（数字/颜色替换）
    ↓
Step 5: 生成 Prompt
    → 平台模板 + 品牌上下文 + 风格参数 + 合规修正
    ↓
Step 6: 调用 1xm.ai 生图
    → scripts/generate_image.py（自带10次重试）
    ↓
Step 7: L5-L6 终审
    → 平台规范 + 发布授权确认
    ↓
Step 8: 交付
    → 输出图片 + YAML合规报告
```

## 合规审查（自动）

**L3 版权扫描** — 检测以下关键词一律拦截：
```
高仿/复刻/A货/1:1/fake/replica/counterfeit
Mickey Mouse/Frozen/Spider-Man/Pokemon/Doraemon
Chanel双C/Gucci双G/LV老花/漫威角色/迪士尼角色
```

**L4 文化自动修复**：
```
数字4 → 6（中日韩）
数字9 → 7（日本）
数字13 → 12（欧美）
绿色 → 浅绿（日本）
紫色 → 紫罗兰（巴西/泰国）
```

## 平台推荐逻辑

```
童装/儿童 → Shopee / Lazada（东南亚华人）
时尚快消 → SHEIN / TikTok Shop
消费电子 → Amazon（欧美）/ Shopee（东南亚）
测品打法 → Temu + Amazon + TikTok Shop
```

## 用法示例

```bash
# 基础：单平台主图
帮我做一张 Shopee 主图，产品是巴拉巴拉红色针织开衫

# 多平台主图
生成 Shopee + Lazada + TikTok Shop 的童装主图

# 详情页长图
帮我生成 Shopee 的详情页，1:8比例

# 全套：主图5张 + 详情页
生成全套 Shopee 东南亚市场的图，包括主图5张和详情页

# 指定风格
做一张 TikTok Shop 主图，风格是UGC快节奏带货风
```

## 平台规格速查

详见 `references/platform_specs.md`

| 平台 | 尺寸 | 比例 | 背景 | 禁止 |
|------|------|------|------|------|
| Amazon | 2000×2000 | 1:1 | 纯白 | 任何文字/LOGO/人物 |
| Shopee | 1024×1024 | 1:1 | 白/场景 | 误导性定价 |
| TikTok Shop | 1080×1440 | 3:4 | 场景 | 过度PS |
| Lazada | 800×800 | 1:1 | 白色 | 竞品LOGO |
| AliExpress | 800×800 | 1:1 | 白/浅灰 | 主图文字 |
| Temu | 1200×1200 | 1:1 | 白色 | 夸大宣传 |
| SHEIN | 1200×1600 | 3:4 | 白色 | 过多文字 |

## 设计风格路由

详见 `references/styles_and_routing.md`

| 品类 | 推荐风格 |
|------|---------|
| 消费电子/工具 | 极简白底 |
| 美妆/个护/母婴 | 生活场景 |
| 服饰/时尚 | 生活场景 / UGC快节奏 |
| 儿童/文具/礼品 | 手绘插画 |
| 高客单礼品/珠宝 | 轻奢简约 |
| 促销/快消/配件 | 活力色彩 |

## 输出目录

图片保存到工作区：
```
~/.openclaw/workspace/image-gen-service/backend/outputs/<品牌名>_<平台>/
variant_1.png
variant_2.png
...
detail_page_1to8.png
compliance_report.yaml
```

## 模型切换

支持两种模型，按需选择：

| 用户模型名 | 底层 API | 速度 | 支持分辨率 | 适用场景 |
|-----------|---------|------|-----------|---------|
| `nano-banana-2` | gemini-3.1-flash-image-preview | 快（默认） | 1K / 2K | 草稿、测图、多图批量 |
| `nano-banana-pro` | gemini-3-pro-image-preview | 慢 | 1K / 2K / **4K** | 高质量终稿、重点图 |

**分辨率档位（隐式工作流）：**
- `1K` — Draft 草稿：快速看构图，不追求细节
- `2K` — Iterate 迭代：（默认）质量与速度平衡
- `4K` — Final 终稿：仅 `nano-banana-pro` 支持，细节丰富

## API Key 配置

**必须设置环境变量** `1XM_API_KEY`：
```bash
export 1XM_API_KEY=your_1xm.ai_api_key_here
```

不支持硬编码 key，脚本启动时会检查，未设置则报错。

## 核心脚本

```bash
# 默认（nano-banana-2 + 2K）
python3 scripts/generate_image.py "<prompt>" "<ref_image>" "<output.png>"

# 指定模型 + 分辨率
python3 scripts/generate_image.py "<prompt>" "<ref_image>" "<output.png>" \
  --model nano-banana-pro --size 4K

# 快速草稿（1K + nano-banana-2）
python3 scripts/generate_image.py "<prompt>" "<ref_image>" "<output_draft.png>" \
  --model nano-banana-2 --size 1K

# 批量生图（每张可独立指定模型和分辨率）
python3 scripts/generate_image.py --batch '[
  ["<prompt_main>", "<ref>", "out/main.png", "nano-banana-pro", "4K"],
  ["<prompt_variant>", "<ref>", "out/v2.png", "nano-banana-2", "2K"]
]'
```

## 参考文件索引

```
references/
├── platform_specs.md        # 7平台完整规格
├── styles_and_routing.md  # 6种风格 + 路由引擎
├── compliance_engine.md   # 6层合规审查
├── cultural_compliance.md  # 文化禁忌规则
├── main_image_workflow.md  # 8步主图工作流
├── detail_page_workflow.md # 详情页5场景模板
└── platforms/
    └── shein.md           # SHEIN平台规格
```

---

_基于电商设计 Agent 实战经验 × 跨境合规规则库_
