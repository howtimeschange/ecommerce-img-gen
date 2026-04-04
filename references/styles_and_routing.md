# 视觉风格定义库 + 风格路由引擎

## 6 种设计风格

---

## Style 1: 极简白底（Clean White）

| 属性 | 值 |
|------|------|
| 背景 | #FFFFFF 纯白 |
| 色彩 | 克制，1-2 色点缀 |
| 留白 | 30-40% |
| 适用平台 | Amazon, AliExpress, Temu, Lazada |
| 适用品类 | 数码/工具/家居/工业品 |

```
background: #FFFFFF pure white, no gradient, no shadow
product: centered, fills 85% frame
lighting: soft box, 45° left upper
style: clean, minimal, professional
```

---

## Style 2: 生活场景（Lifestyle）

| 属性 | 值 |
|------|------|
| 背景 | 真实使用场景 |
| 色彩 | 场景协调，色温一致 |
| 留白 | 10-20% |
| 适用平台 | Shopee, TikTok Shop, SHEIN |
| 适用品类 | 家居/美妆/服饰/母婴 |

```
background: {scene_description}, authentic setting, warm lighting
product: integrated into scene, natural placement
style: authentic, relatable, aspirational
```

---

## Style 3: 轻奢简约（Premium Minimal）

| 属性 | 值 |
|------|------|
| 背景 | 浅灰/米白/莫兰迪色 |
| 色彩 | 低饱和，有品质感 |
| 留白 | 40-50% |
| 适用平台 | Amazon A+, 高端品牌, AliExpress |
| 适用品类 | 珠宝/手表/高客单礼品 |

```
background: light gray #F0F0F0 or warm beige #F5F0EB
product: premium materials visible, elegant styling
lighting: soft directional, subtle shadow
style: editorial luxury, sophisticated
```

---

## Style 4: 活力色彩（Bold & Vibrant）

| 属性 | 值 |
|------|------|
| 背景 | 渐变/高饱和色块 |
| 色彩 | 鲜艳对比强 |
| 留白 | 5-15% |
| 适用平台 | Shopee, Temu, TikTok Shop |
| 适用品类 | 快消/促销/节日/配件 |

```
background: bold gradient or saturated color block
product: floating with drop shadow, high contrast
text: large bold fonts, sale tags, discount badges
style: high energy, impulse-buy, mobile thumb-stopping
```

---

## Style 5: 手绘插画（Illustrated）

| 属性 | 值 |
|------|------|
| 背景 | 白底或彩色均可 |
| 色彩 | 手绘质感，扁平 |
| 留白 | 视风格而定 |
| 适用平台 | Shopee, TikTok Shop |
| 适用品类 | 儿童/文具/礼品/创意产品 |

```
style: hand-drawn illustration, flat cartoon
colors: pastel or vibrant, cohesive palette
elements: doodles, decorative frames, handwritten text
mood: cute, fun, approachable, family-friendly
```

---

## Style 6: 快节奏带货（UGC Rush）

| 属性 | 值 |
|------|------|
| 背景 | 随手拍感 |
| 色彩 | 真实感，低调色 |
| 留白 | 0-10% |
| 适用平台 | TikTok Shop, 短视频 |
| 适用品类 | 一切冲动消费品 |

```
background: real-life setting, slightly messy, authentic
product: in-use shot or holding product
mood: excited, genuine reaction
style: unpolished, relatable, social proof feel
```

---

## 风格路由表（自动推荐）

```
品类信号 → 风格推荐

消费电子/工具/数码  → 极简白底
美妆/个护/母婴      → 生活场景
服饰/时尚           → 生活场景 / 快节奏带货
儿童/文具/礼品      → 手绘插画
高客单礼品/珠宝     → 轻奢简约
促销/快消/配件      → 活力色彩
```

## 平台 × 风格适配矩阵

| 风格 \ 平台 | Amazon | Shopee | TikTok | Lazada | Temu | AliExpress | SHEIN |
|------------|--------|--------|--------|--------|------|-----------|-------|
| 极简白底 | ✅主图 | ⚠️ | ❌ | ✅ | ✅ | ✅主图 | ❌ |
| 生活场景 | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| 轻奢简约 | ✅A+ | ⚠️ | ❌ | ⚠️ | ❌ | ✅ | ⚠️ |
| 活力色彩 | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ⚠️ |
| 手绘插画 | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| UGC Rush | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ |

✅=推荐  ⚠️=可用  ❌=不推荐
