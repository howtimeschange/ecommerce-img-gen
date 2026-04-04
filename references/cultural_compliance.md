# 跨境外贸文化合规规则

## 东南亚市场禁忌

### 数字禁忌
| 数字 | 禁忌市场 | 原因 | 替代 |
|------|---------|------|------|
| **4** | 中国/越南 | 谐音"死" | 6, 8 |
| **7** | 部分华人市场 | 不吉利 | 8, 9 |
| **13** | 菲律宾/部分基督教国家 | 西方禁忌 | 12, 14 |

### 颜色禁忌
| 颜色 | 禁忌市场 | 原因 | 替代 |
|------|---------|------|------|
| 黑色 | 部分 | 丧葬色 | 深灰/藏青 |
| 白色 | 越南（某些语境） | 丧葬 | 米白/象牙白 |
| 紫色 | 泰国 | 皇室哀悼 | 紫罗兰/深蓝 |
| 绿色 | 泰国（日常） | 不吉利 | 浅绿可接受 |

### 龙年/中国元素注意事项
- 龙图案在东南亚华人市场是**吉祥元素**，可正面使用
- 但需注意：不同国家的龙文化解读略有差异
- 红色在东南亚华人市场：**非常吉利**，适合促销/节日
- 避免在非华人东南亚市场使用过于强烈的中国元素

## 健康宣称禁用词（出海需避免）

```
cures, prevents, treats, reduces, eliminates, 
miracle cure, guaranteed, 100% effective,
clinically proven, doctor recommended,
这些词在 EU/US 广告法下属于医疗宣称，禁止使用
```

## 合规检查流程

生成 Prompt 后，自动检查：
1. 数字是否含禁忌（4/7/13）→ 替换为安全数字
2. 颜色是否符合目标市场
3. 文案是否含健康/医疗宣称
4. 节日元素是否符合当地节庆日历

## IP / 版权黑名单

检测到以下关键词 → 拦截（需用户确认）：

```
卡通/IP:
  Mickey Mouse, Frozen, Spider-Man, Hello Kitty,
  Pokemon, Doraemon, Rilakkuma, 漫威所有角色, 迪士尼所有角色

奢侈品牌:
  Chanel, Gucci, Louis Vuitton, Hermès, Prada, Dior

虚假宣传:
  高仿, 复刻, A货, 1:1, fake, replica, counterfeit
```

## 健康宣称禁用词（EU/US/CN）

```
治愈/预防/治疗:
  cures, prevents, treats, reduces, eliminates,
  miracle cure, guaranteed, 100% effective

医疗认证:
  clinically proven, doctor recommended,
  FDA approved（未认证时禁用）
```
