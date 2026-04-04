# 6 层合规审查引擎

## 架构

```
用户输入 → L1意图过滤 → L2品牌合规 → L3版权检查 → L4文化适配 → L5平台规范 → L6发布授权 → 通过/拦截
```

## L1: 意图过滤（Intent Guard）

### 绝对禁止（Hard Block）

- 武器/仿真武器
- 毒品/未批准药品
- 色情/低俗内容
- 假冒品牌/山寨商品
- 野生动物制品

### 条件禁止（Conditional）

- 食品/保健品：需资质
- 化妆品：需成分说明
- 电子产品：需认证标志
- 儿童用品：需年龄标注

## L2: 品牌合规（Brand Compliance）

从 Brand.md 加载：品牌色/字体/LOGO规范/CTA语气

## L3: 版权检查（Copyright Guard）

### IP 黑名单

```
Mickey Mouse, Frozen, Spider-Man, Hello Kitty,
Pokemon, Doraemon, Rilakkuma,
Chanel 双C, Gucci 双G, Louis Vuitton 老花,
漫威所有角色, 迪士尼所有角色,
任何未授权的知名卡通形象
```

### 版权检测关键词（prompt/文案中）

```
高仿, 复刻, 原单, A货, 1:1,
fake, replica, counterfeit, knock-off
```

## L4: 文化适配（Cultural Adaptation）

详见 `cultural_compliance.md`，核心规则：

| 检查项 | 市场 | 规则 |
|--------|------|------|
| 数字4 | 中国/日本/韩国 | 替换为6/8 |
| 数字9 | 日本 | 替换为7/8 |
| 数字13 | 欧美/巴西 | 替换为12/14 |
| 颜色绿 | 日本 | 替换为浅绿 |
| 颜色紫 | 巴西/泰国 | 替换为紫罗兰 |
| 龙图案 | 东南亚华人 | ✅吉祥，可用 |
| 红色 | 东南亚华人 | ✅吉祥，促销可用 |

## L5: 平台规范（Platform Specs）

| 平台 | 背景 | 文字 | 产品占比 | 禁止元素 |
|------|------|------|---------|---------|
| Amazon | #FFFFFF纯白 | ❌ | ≥85% | 任何文字/LOGO/人物 |
| Shopee | 白/生活场景 | ✅≤20% | — | 误导性定价 |
| TikTok Shop | 生活场景 | ✅≤15% | — | 过度PS |
| Lazada | 白色 | ✅≤15% | — | 竞品LOGO |
| AliExpress | 白/浅灰 | ✅≤15% | — | 任何文字主图 |
| Temu | 白色优先 | ✅≤20% | — | 夸大宣传 |
| SHEIN | 白色 | ✅≤15% | — | 过多文字 |

## L6: 发布授权（Publish Auth）

确认：品牌授权/模特肖像/摄影版权/IP授权链路

## 审查报告格式

```yaml
design_id: "balabala-v1"
verdict: PASS  # PASS / WARN / BLOCK
overall_score: 95

layers:
  - layer: 1
    name: "IntentGuard"
    verdict: PASS
    score: 100
  - layer: 2
    name: "BrandCompliance"
    verdict: PASS
    score: 100
  - layer: 3
    name: "CopyrightGuard"
    verdict: PASS
    score: 100
  - layer: 4
    name: "CulturalAdaptation"
    verdict: WARN
    score: 85
    suggestions:
      - type: "数字替换"
        target: "尺码4Y"
        current: "4"
        suggested: "6"
        reason: "日本市场4=死"
  - layer: 5
    name: "PlatformSpecs"
    verdict: PASS
    score: 100
  - layer: 6
    name: "PublishAuth"
    verdict: PASS
    score: 100

blocking_layer: null
```

## 自动修复能力

| 层级 | 可自动修复 | 修复方式 |
|------|----------|---------|
| L1 意图 | ❌ | 人工确认 |
| L2 品牌 | ✅ | 替换色值/字体 |
| L3 版权 | ❌ | 删除侵权元素 |
| L4 文化 | ✅ | 替换禁忌数字/颜色 |
| L5 平台 | ✅ | 裁剪/调色 |
| L6 授权 | ❌ | 人工上传 |

## 合规检查自动化流程

生成 Prompt 后自动检查：

1. **L3版权扫描**：检测 prompt 中是否有 IP 黑名单词 → 有则拦截
2. **L4文化扫描**：检测数字4/9/13 → 自动替换为安全数字
3. **L4颜色扫描**：检测禁忌颜色 → 替换为安全替代色
4. **L5合规扫描**：检测平台禁止元素（文字/LOGO/人物）→ 移除或警告

```python
COMPLIANCE_AUTO_FIXES = {
    "number_4": {"replace_with": "6", "markets": ["中国", "日本", "韩国"]},
    "number_9": {"replace_with": "7", "markets": ["日本"]},
    "number_13": {"replace_with": "12", "markets": ["欧美", "巴西"]},
    "color_green": {"replace_with": "浅绿/薄荷绿", "markets": ["日本"]},
    "color_purple": {"replace_with": "紫罗兰", "markets": ["巴西", "泰国"]},
}
```
