# 🛒 跨境电商图片生成工具

> 从产品图 → 7平台合规主图 → 详情页长图，一站式生成

[![ClawHub](https://img.shields.io/badge/ClawHub-ecommerce--img--gen-v2.6.0-blue)](https://clawhub.ai/howtimeschange/ecommerce-img-gen)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://www.python.org/)

## ✨ 功能特点

| 能力 | 支持情况 |
|------|---------|
| **7平台主图** | Amazon · Shopee · TikTok Shop · Lazada · AliExpress · Temu · SHEIN |
| **6种视觉风格** | 极简白底 / 生活场景 / 轻奢简约 / 活力色彩 / 手绘插画 / UGC快节奏 |
| **详情页长图** | 5类场景 × 7平台组合，支持 1:4 / 1:8 超长竖版 |
| **6层合规审查** | 意图过滤 → 品牌合规 → 版权检查 → 文化适配 → 平台规范 → 发布授权 |
| **文化合规** | 数字/颜色/图案禁忌，覆盖东南亚/日本/欧美/中东 |
| **模型切换** | nano-banana-2（快速）/ nano-banana-pro（高质量 4K） |

## 🚀 快速开始

### 1. 安装依赖

```bash
# 克隆仓库
git clone https://github.com/howtimeschange/ecommerce-img-gen.git
cd ecommerce-img-gen

# 安装 Python 依赖（仅 urllib3 + pydantic，无其他外部依赖）
pip install urllib3 pydantic pydantic-settings
```

### 2. 配置 API Key

```bash
# 设置 1xm.ai API Key（必需）
export 1XM_API_KEY=your_1xm.ai_api_key_here
```

> 获取 1xm.ai API Key：https://1xm.ai（底层调用 Google Gemini 图像生成模型）

### 3. 生图

```bash
# 默认生图（nano-banana-2 + 2K）
python3 scripts/generate_image.py "<prompt>" "<ref_image.png>" "<output.png>"

# 高质量 4K 终稿
python3 scripts/generate_image.py "<prompt>" "<ref_image.png>" "<output.png>" \
  --model nano-banana-pro --size 4K

# 快速草稿 1K
python3 scripts/generate_image.py "<prompt>" "<ref_image.png>" "<draft.png>" \
  --model nano-banana-2 --size 1K
```

## 📐 模型与分辨率

| 模型 | 底层 API | 支持分辨率 | 适用场景 |
|------|---------|-----------|---------|
| `nano-banana-2` | gemini-3.1-flash-image-preview | 1K / 2K | 草稿、测图、多图批量 |
| `nano-banana-pro` | gemini-3-pro-image-preview | 1K / 2K / 4K | 高质量终稿、重点图 |

**分辨率档位：**

| 档位 | 说明 |
|------|------|
| `1K` | Draft 草稿：快速看构图，不追求细节 |
| `2K` | Iterate 迭代：（默认）质量与速度平衡 |
| `4K` | Final 终稿：仅 nano-banana-pro 支持，细节丰富 |

## 📋 平台规格速查

| 平台 | 推荐尺寸 | 比例 | 背景 | 注意事项 |
|------|---------|------|------|---------|
| **Amazon** | 2000×2000 | 1:1 | 纯白 | 主图禁任何文字/LOGO/人物 |
| **Shopee** | 1024×1024 | 1:1 | 白/场景 | 避免误导性定价 |
| **TikTok Shop** | 1080×1440 | 3:4 | 场景 | 避免过度PS |
| **Lazada** | 800×800 | 1:1 | 白色 | 禁止竞品LOGO |
| **AliExpress** | 800×800 | 1:1 | 白/浅灰 | 主图禁文字 |
| **Temu** | 1200×1200 | 1:1 | 白色 | 禁止夸大宣传 |
| **SHEIN** | 1200×1600 | 3:4 | 白色 | 避免过多文字 |

详情见 [references/platform_specs.md](references/platform_specs.md)

## 🎨 风格路由

根据品类自动推荐最优风格：

| 品类 | 推荐风格 |
|------|---------|
| 消费电子 / 工具 | 极简白底 |
| 美妆 / 个护 / 母婴 | 生活场景 |
| 服饰 / 时尚 | 生活场景 / UGC快节奏 |
| 儿童 / 文具 / 礼品 | 手绘插画 |
| 高客单礼品 / 珠宝 | 轻奢简约 |
| 促销 / 快消 / 配件 | 活力色彩 |

详情见 [references/styles_and_routing.md](references/styles_and_routing.md)

## 🛡️ 合规审查（自动）

### L3 版权扫描 — 一律拦截

```
高仿 / 复刻 / A货 / 1:1 / fake / replica / counterfeit
Mickey Mouse / Frozen / Spider-Man / Pokemon / Doraemon
Chanel双C / Gucci双G / LV老花 / 漫威角色 / 迪士尼角色
```

### L4 文化自动修复

| 检查项 | 市场 | 规则 |
|--------|------|------|
| 数字 4 | 中国 / 日本 / 韩国 | → 6 |
| 数字 9 | 日本 | → 7 |
| 数字 13 | 欧美 / 巴西 | → 12 |
| 绿色 | 日本 | → 浅绿 / 薄荷绿 |
| 紫色 | 巴西 / 泰国 | → 紫罗兰 |

详情见 [references/cultural_compliance.md](references/cultural_compliance.md)

## 📁 项目结构

```
ecommerce-img-gen/
├── SKILL.md                          # OpenClaw 技能入口
├── README.md                         # 本文件
├── .gitignore
├── scripts/
│   └── generate_image.py             # 核心生图脚本（支持模型切换 / 批量）
└── references/
    ├── platform_specs.md             # 7平台完整规格
    ├── styles_and_routing.md          # 6种风格 + 路由引擎
    ├── compliance_engine.md           # 6层合规审查引擎
    ├── cultural_compliance.md         # 文化禁忌规则库
    ├── main_image_workflow.md         # 8步主图工作流
    └── detail_page_workflow.md        # 详情页5场景模板
```

## 🔧 OpenClaw 集成

本项目设计为 [OpenClaw](https://github.com/openclaw/openclaw) 的技能（Skill），可在 OpenClaw 环境中使用自然语言驱动：

```bash
# 安装技能
clawhub install ecommerce-img-gen

# 自然语言使用示例
"帮我生成 Shopee + Lazada 的童装主图各5张"
"生成 Temu 详情页，1:8比例，目标市场东南亚"
"做一张 Amazon 主图，风格是极简白底"
```

## 📌 版本历史

| 版本 | 更新内容 |
|------|---------|
| 2.6.0 | 技能标题更新 |
| 2.5.0 | 新增模型切换：nano-banana-2/pro + 分辨率档位 1K/2K/4K |
| 2.4.0 | 更新详情页工作流参考文档 |
| 2.0.0 | 多平台 / 多风格路由 / 增强合规审查 |
| 1.0.0 | 初始版本 |

## 📄 License

MIT License
