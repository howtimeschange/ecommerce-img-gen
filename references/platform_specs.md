# 电商平台图片规格参考（完整版 · 2025-2026）

基于各平台官方文档及调研最佳实践汇总。

---

## 7 平台主图规格总览

| 平台 | 最小尺寸 | 推荐尺寸 | 比例 | 背景 | 文字 | 产品占比 | 文件格式 | 最大文件 |
|------|---------|---------|------|------|------|---------|---------|---------|
| **Amazon** | 1000×1000 | 2000×2000 | 1:1 | 纯白#FFFFFF | ❌ 禁止 | ≥85% | JPEG/PNG/TIFF | 10MB |
| **Shopee** | 500×500 | 1024×1024 | 1:1 | 白/生活场景 | ✅≤20% | ≥70% | JPEG/PNG | 5MB |
| **TikTok Shop** | 600×600 | 800×800+ | 1:1 | 生活场景优先 | ✅≤15% | — | JPEG/PNG | 5MB |
| **Lazada** | 500×500 | 800×800+ | 1:1 | 白色 | ✅≤15% | ≥80% | JPG | — |
| **AliExpress** | 800×800 | 800×800 | 1:1 | 白/浅灰纯色 | ✅（仅A+内容） | — | JPG | — |
| **Temu** | 800×800 | 1200×1200 | 1:1 | 白色优先 | ✅≤20% | — | JPEG/PNG | — |
| **SHEIN** | 800×1066 | 1200×1600 | 3:4 | 白色为主 | ✅≤15% | — | JPEG/PNG | 10MB |

---

## Amazon（欧美精品市场）

### 核心规格
- **尺寸**：最小 1000×1000，推荐 **2000×2000 px**（支持高清缩放）
- **背景**：必须纯白 `#FFFFFF`（RGB 255,255,255），无边框/渐变/阴影
- **产品占比**：≥85% 画面，纯产品主体
- **比例**：1:1 正方形

### 绝对禁止
- ❌ 任何文字（促销语/价格/SKU）
- ❌ 品牌 LOGO / 水印
- ❌ 人物 / 模特（包括成人和儿童服装）
- ❌ 背景道具 / 布景 / 阴影 / 反射
- ❌ 多产品拼图
- ❌ 边框 / 框架

### 童装特殊规则
- **儿童服装禁止真人模特出镜**，必须平铺或假模展示

### 最佳实践
- 产品居中，纯白背景，**左上方45°软光箱打光**
- 无摩尔纹，无色偏，边缘锐利
- 变体图（Additional Images）允许生活场景/白底细节图

### Prompt 模板
```
Amazon product listing main image: [PRODUCT],
pure white studio background #FFFFFF exactly,
1:1 square format, aspect ratio 1:1,
product fills 85% of frame minimum, centered,
professional soft box lighting 45 degrees left upper,
no shadow, no reflection, no gradient,
no text, no logo, no watermark, no price,
no mannequin, no human model, no background props,
ultra sharp focus, retail-ready, photorealistic
```

---

## Shopee（东南亚主流市场）

### 核心规格
- **尺寸**：最小 500×500，推荐 **1024×1024 px**
- **背景**：白底或真实生活场景均可
- **产品占比**：≥70%（低于此比例影响搜索排名）
- **比例**：1:1 正方形
- **图册数量**：最多 **9张**

### 允许内容
- ✅ 价格标签（与实际售价一致，**禁止误导性定价**）
- ✅ 折扣标签（如 "20% OFF"）
- ✅ 评分/星级展示
- ✅ CTA 按钮文字

### 禁止内容
- ❌ 误导性定价（标价与实际售价不符）
- ❌ 夸大宣传（"最便宜"/"第一"等绝对词）
- ❌ 竞品品牌展示
- ❌ 色情/低俗内容
- ❌ 未授权 IP 形象

### 东南亚审美细分
| 市场 | 偏好 | 热门元素 |
|------|------|---------|
| 印尼 | 明亮色彩、实惠感 | 折扣标签、销量数字 |
| 菲律宾 | 高对比、活力感 | 星级评分、促销语 |
| 越南 | 简约清新 | 纯净背景、产品原色 |
| 马来西亚 | 多元文化 | 中东元素、双语标注 |
| 泰国 | 活泼俏皮 | emoji、卡通装饰 |

### 最佳实践
- **首图决定点击率**：纯白底或纯色底产品图最优
- 白色背景图片对搜索排名有正向影响
- 生活场景图放在第2-3张
- 细节/特写图展示产品亮点

### Prompt 模板
```
Shopee Southeast Asia main image: [PRODUCT],
[white background OR lifestyle scene],
1:1 square format,
product fills at least 70% of frame,
bright vibrant retail photography,
Southeast Asia marketplace style,
youthful energetic premium feel,
mobile-optimized thumbnail,
[optional text overlays: price/discount/rating - max 20% of image]
```

---

## TikTok Shop（短视频带货）

### 核心规格
- **尺寸**：最小 **600×600**，推荐 800×800+ 或更高
- **背景**：真实生活场景优先，体现产品使用感
- **文字**：允许，含≤15%
- **文件**：JPEG/PNG，最大 **5MB/张**
- **比例**：1:1 方图（部分视频封面用 9:16 竖版）

### 内容偏好
- ✅ UGC 真实感（随手拍感 > 精修商业图）
- ✅ 产品融入生活场景，展示真实使用效果
- ✅ 动态/活力感，高对比色彩
- ✅ 前3秒抓眼球（视频封面场景）

### 禁止内容
- ❌ 过度PS/不真实产品图
- ❌ 夸大/虚假功效宣称
- ❌ 色情低俗内容
- ❌ 暴力/歧视性内容

### 最佳实践
- 优先展示**真实用户使用场景**，非纯产品照
- 色彩饱和度高、构图有动感
- 产品不要被大面积遮挡

### Prompt 模板
```
TikTok Shop product image: [PRODUCT],
authentic lifestyle scene, real-world setting,
1:1 square format, bright natural lighting,
Gen-Z aesthetic, high energy, trendy,
showing product in real-use context,
mobile-first vertical-friendly composition,
text overlay allowed up to 15%,
no over-edited commercial photography,
genuine relatable UGC-style aesthetic
```

---

## Lazada（东南亚商场正规市场）

### 核心规格
- **尺寸**：500-2000 px，JPG格式，推荐 **800×800+**
- **背景**：纯白色背景
- **产品占比**：≥80%
- **比例**：1:1 正方形
- **图册数量**：最多 8张

### 允许内容
- ✅ 产品细节图
- ✅ 白底图为主，生活场景图辅助
- ✅ 尺码表/规格说明

### 禁止内容
- ❌ 竞品 LOGO 展示
- ❌ 误导性标注
- ❌ 水印/店名文字叠加在主图

### 最佳实践
- 纯白底主图决定搜索排名
- 可上传**模特穿戴图**（区别于 Amazon）
- 额外图册展示：角度图、细节图、尺寸对照

### Prompt 模板
```
Lazada product main image: [PRODUCT],
clean pure white background,
1:1 square format,
product fills at least 80% of frame,
professional retail photography,
Southeast Asian mall aesthetic,
clear product presentation,
no competitor branding,
no watermarks on main image,
high resolution sharp focus
```

---

## AliExpress（全球跨境市场）

### 核心规格
- **尺寸**：推荐 **800×800 px**
- **背景**：纯白或浅灰纯色背景（普通店铺）
- **比例**：1:1 正方形
- **主图文字**：❌ **普通店铺主图禁止任何文字**

### 重要规则（调研最新）
- 普通店铺主图：纯白/浅灰背景，**禁止任何文字**
- 认证品牌旗舰店（A+内容）：可使用白底+适当文字
- 禁止： 水印（包括店名/联系方式）、促销语（限时折扣/买一送一）、价格标签
- 纯色背景必须均匀，不能喧宾夺主

### 允许内容
- ✅ 白底细节特写图
- ✅ 产品各角度展示
- ✅ A+ 内容页允许信息图/对比图

### 禁止内容
- ❌ 主图任何文字/促销信息
- ❌ 渐变背景（普通店铺）
- ❌ 水印/LOGO叠加
- ❌ 场景化背景（普通店铺）

### Prompt 模板
```
AliExpress global product photo: [PRODUCT],
clean pure white studio background OR light gray solid background,
1:1 square format,
professional retail photography,
international e-commerce aesthetic,
no text, no watermark, no logo overlay on main image,
no promotional text, no price tags,
high resolution, sharp focus,
clean minimal aesthetic suitable for global marketplace
```

---

## Temu（新兴低价市场 · 欧美下沉）

### 核心规格
- **尺寸**：推荐 **1200×1200 px**
- **背景**：白色优先，可接受纯色背景
- **比例**：1:1 正方形
- **文字**：允许，含≤20%

### 内容偏好
- ✅ **高性价比感**的产品展示
- ✅ 专业摄影产品图，清晰展示产品
- ✅ 明亮色彩，吸睛但不浮夸

### 禁止内容
- ❌ 夸大/虚假宣传
- ❌ 未经认证的健康/功效宣称
- ❌ 使用未授权图片/盗图
- ❌ 误导性定价

### 最佳实践
- Temu 重图片质量，低质图片影响流量分配
- 产品图需要**真实感**，过度精修反而降低转化
- 主图与详情页图片风格保持一致

### Prompt 模板
```
Temu product listing photo: [PRODUCT],
bright clean white or light solid background,
1:1 square format,
high quality professional retail photography,
affordable-premium aesthetic - looks good value,
clear product presentation,
no misleading claims, no exaggerated advertising,
upbeat marketplace style,
mobile-optimized thumbnail,
text overlay allowed up to 20%
```

---

## SHEIN（快时尚 · 全球年轻市场）

### 核心规格
- **尺寸**：推荐 **1200×1600 px**（3:4 竖版）
- **背景**：白色为主，可接受简洁场景
- **文字**：允许，含≤15%
- **比例**：**3:4 竖版**（区别于其他平台）
- **文件**：JPEG/PNG，最大 **10MB**

### 内容偏好
- ✅ **快时尚审美**，年轻、潮流感
- ✅ **模特图优先**（真人穿戴展示）
- ✅ 潮流搭配感，非纯产品平铺
- ✅ 明亮/活力的色彩和氛围

### 禁止内容
- ❌ 背景过于杂乱
- ❌ 过多文字叠加
- ❌ 非时尚类（工具/工业品）不适合此平台

### 最佳实践
- 3:4 竖版模特全身/半身图最优
- 背景简洁（如纯色墙/简约室内）
- 产品在画面中占比适中，展示穿搭效果

### Prompt 模板
```
SHEIN fashion product photo: [PRODUCT],
worn by young model, fashion-forward styling,
3:4 vertical portrait format (1200x1600px preferred),
clean white or minimal background,
trendy youthful aesthetic,
fast fashion marketplace style,
bright energetic, stylish presentation,
no excessive text overlay (max 15%),
fashion editorial quality photography
```

---

## 各平台禁止元素速查

| 平台 | 绝对禁止 |
|------|---------|
| **Amazon** | 任何文字、LOGO、价格、人物、阴影、背景道具、边框、多产品拼图 |
| **Shopee** | 误导性定价、夸大宣传、竞品展示、色情内容 |
| **TikTok Shop** | 过度精修、夸大功效、色情低俗、暴力歧视内容 |
| **Lazada** | 竞品LOGO、误导标注、主图水印 |
| **AliExpress** | 主图任何文字、水印、促销语、价格标签（普通店铺） |
| **Temu** | 夸大宣传、虚假功效、未授权图片、误导定价 |
| **SHEIN** | 过多文字、杂乱背景、非时尚类内容 |

---

## 详情页比例参考

| 市场 | 推荐比例 |
|------|---------|
| Shopee | **1:8** 超长竖版（10+章节） |
| Lazada | 3:4 或 1:2 |
| TikTok Shop | 9:16 全屏竖版 |
| Amazon A+ | 3:4 横版（970×600px 标准） |
| AliExpress | 3:4 或 1:2 |
| Temu | 1:1 或 3:4 |
| SHEIN | 3:4 竖版 |
