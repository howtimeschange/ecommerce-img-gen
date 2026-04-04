# 电商主图完整工作流程（8步）

## 主流程

```
用户请求（发产品图 + 平台/市场）
    ↓
Step 1: Vision 分析商品
    ├─ 提取产品名/品牌/品类/颜色/材质/特征
    └─ 适用年龄/性别/使用场景
    ↓
Step 2: 确认平台
    ├─ 用户指定 → 直接使用
    └─ 未指定 → 根据品类/市场推荐
    ↓
Step 3: 风格路由
    ├─ 根据品类 → 推荐风格（见 styles_and_routing.md）
    └─ 用户确认或调整（默认推荐风格）
    ↓
Step 4: 合规审查（L1-L4）
    ├─ L1 意图过滤（违禁品类检测）
    ├─ L2 品牌合规（如有 Brand.md）
    ├─ L3 版权检查（IP黑名单/版权词扫描）
    └─ L4 文化适配（数字/颜色/图案禁忌）
    ↓
Step 5: 生成 Prompt
    ├─ 加载平台模板（见 platform_specs.md）
    ├─ 注入品牌上下文（如有）
    ├─ 注入风格参数
    └─ 注入合规修正（数字替换/颜色替换）
    ↓
Step 6: 调用 1xm.ai 生图
    ├─ 生成主图（无 reference）
    └─ 如需多张变体，依次生成
    ↓
Step 7: L5-L6 终审
    ├─ L5 平台规范（尺寸/背景/文字比例）
    └─ L6 发布授权确认
    ↓
Step 8: 交付
    └─ 图片路径 + 合规报告（YAML格式）
```

## Step 1: 商品信息解析

### Vision 分析输出格式

```
产品名: 巴拉巴拉龙年针织开衫
品牌: balabala（巴拉巴拉）
品类: 童装 > 上装 > 针织开衫
颜色: 正红色（中国红）
材质: 棉混纺针织
适用年龄: 中大童（4-12岁）
性别: 中性
主要特征: V领、纽扣、落肩、罗纹袖口、胸前龙年刺绣
使用场景: 节日/日常/校园/春秋外穿/冬季内搭
目标市场: 东南亚（华人市场）
```

## Step 2: 平台推荐逻辑

```
品类 → 市场 → 推荐平台

消费电子 → 北美/欧洲    → Amazon
消费电子 → 东南亚      → Shopee / Lazada
快消/服饰 → 全球        → TikTok Shop / SHEIN
低价货品 → 欧美        → Temu
时尚/快消 → 全球        → SHEIN / TikTok Shop
童装/儿童 → 东南亚华人  → Shopee / Lazada
```

## Step 3: 风格路由

```
童装/儿童产品 → 默认 Style 2（生活场景）
            → 可选 Style 5（手绘插画，适合节日款）

Follow参考路由表：styles_and_routing.md
```

## Step 4: 合规审查清单

```
□ L1: 非违禁品类 → 童装正常，通过
□ L2: 品牌色检查 → balabala红色系，正常
□ L3: 龙图案在东南亚华人市场 ✅吉祥，通过
□ L4: 数字检查 → 尺码4Y → 替换为6Y（日本市场）
□ L4: 红色在东南亚华人市场 ✅吉祥，通过
□ L4: 龙年刺绣 ✅正向节日元素，通过
```

## Step 5: Prompt 组装顺序

```
1. [SYSTEM] 固定系统指令
2. [PLATFORM] 平台规格（从 platform_specs.md 加载）
3. [BRAND] 品牌规范（如有，从 Brand.md 加载）
4. [PRODUCT] 产品信息（从 Step 1）
5. [STYLE] 视觉风格定义（从 styles_and_routing.md）
6. [COMPLIANCE] 合规修正（数字/颜色替换）
7. [TEXT_OVERLAY] 文字叠加内容（可选）
```

## Step 6: 生图参数

```yaml
aspect_ratio: "1:1"      # 或 "3:4" / "9:16"
quality: "2k"            # 1k / 2k / 4k
style: "photorealistic"  # photorealistic / illustration
reference_image: null    # 首张图无reference，变体用前一张
```

## Step 7: 终审

```python
# 检查最终图片
check_image_dimensions(image, platform.width, platform.height)
check_background_purity(image, platform.background)
check_text_ratio(image, platform.text_max_ratio)
```

## Step 8: 交付格式

```yaml
design_id: "balabala-knit-{timestamp}"
verdict: PASS
overall_score: 95

platform: shopee
market: 东南亚
style: lifestyle
variant_count: 5

images:
  - filename: "variant_1.png"
    type: "main_image"
    style: "white_background"
    size_bytes: 564581
    status: "PASS"
  - filename: "variant_2.png"
    type: "main_image"
    style: "lifestyle"
    size_bytes: 716217
    status: "PASS"
  ...

compliance:
  verdict: PASS
  layers_passed: 6
  warnings: 1
  suggestions:
    - "[L4] 尺码标签含数字4，建议替换为6（面向日本市场时）"
```

## 错误处理

| 错误类型 | 处理方式 |
|---------|---------|
| L1 违禁品类 | 立即拦截，要求用户确认 |
| L3 IP 侵权 | 立即拦截，列出侵权元素 |
| 品牌规范缺失 | WARN，仍可继续，注入默认值 |
| 平台不支持该品类 | 建议替代平台 |
| 生图失败 | 自动重试（脚本内置10次） |
| 文化禁忌冲突 | WARN，给出替代方案 |
