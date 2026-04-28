# 小红书笔记样式与设计指南

本文档描述小红书笔记的完整设计工作流，核心原则：**从文章提炼关键信息与隐喻，生成有文字的高级封面 + 精心设计的配图**。

---

## 一、内容提炼 (Extract)

收到文章后，必须执行以下提炼：

### 封面文字提炼

| 字段 | 规则 | 示例 |
|------|------|------|
| `主标题` | 核心冲突/价值，不超过10字 | "Typora配图床" |
| `副标题` | 核心利益/效果，不超过15字 | "3步搞定，写文档再不用手动传图" |

### 视觉隐喻提取

从文章内容中提取**一个核心视觉隐喻**：

| 文章类型 | 隐喻提取 | 视觉呈现 |
|----------|----------|----------|
| 教程攻略 | 步骤→路径/阶梯 | 楼梯、跑道、进度条 |
| 工具推荐 | 效率→加速器/火箭 | 火箭、翅膀、闪电 |
| 解决问题 | 痛点→障碍/锁 | 锁链、障碍物、钥匙 |
| 科技数码 | 技术→未来/芯片 | 芯片、电路、星空 |
| 生活技巧 | 便捷→魔法/开关 | 魔法棒、开关、遥控器 |
| OBS/直播 | 画面切换→导演 | 摄像机、导播台、推杆 |

---

## 二、封面设计 (Cover Design)

### 核心原则

1. **必须有文字**：主标题 + 副标题必须显示在封面上
2. **负空间布局**：画面只占2/3，另一侧1/3留白放文字
3. **文字位置**：严禁顶部/底部，必须在画面中间左侧或右侧
4. **电影感**：Cinematic Lighting + 8k高精细节 + 质感材质
5. **视觉隐喻**：画面要体现文章的核心隐喻，不是纯装饰

### 构图策略

```
策略A：视觉重心在右侧2/3，左侧1/3留白放文字
┌─────────────────────────────┐
│  预留文字空间    │  画面主体   │
│  主标题         │  (隐喻视觉) │
│  副标题         │             │
└─────────────────────────────┘

策略B：视觉重心在左侧2/3，右侧1/3留白放文字
┌─────────────────────────────┐
│  画面主体   │  预留文字空间   │
│  (隐喻视觉) │  主标题        │
│             │  副标题        │
└─────────────────────────────┘
```

### AI生图Prompt结构

```
[主体描述], 包含[隐喻元素], cinematic lighting, 8k resolution, high-detail texture.
Composition heavily weighted to the [right/left] 2/3, leaving significant empty negative space on the [left/right] for typography.
[配色描述], [风格描述]. No text or elements at the top or bottom edges.
```

### 封面生成命令

```bash
# AI生图（推荐：高级电影感）
python <image-skill>/scripts/generate_image.py \
  "A [主体描述], [隐喻元素], cinematic lighting, 8k resolution. \
  Composition heavily weighted to the right 2/3, leaving negative space on the left for typography. \
  Deep blue purple gradient, subtle glow, minimalist premium aesthetic. No text at edges." \
  -o cover.jpg -s 1080x1440
```

---

## 三、配图设计 (Card Design)

### 内容块分解

将文章正文分解为N个内容块，每个块生成一张配图：

```markdown
---
emoji: "🚀"
title: "主标题"
subtitle: "副标题"
---

# 第一张配图内容
要点1
要点2

---

# 第二张配图内容
要点3
要点4
```

### 配图版式选择

根据内容类型自动选择版式：

| 内容类型 | 版式 | 说明 |
|----------|------|------|
| 步骤教程 | 步骤时间轴 | 垂直步骤1→2→3 |
| 工具推荐 | 卡片堆叠 | 多个工具卡片错落 |
| 对比分析 | 左右对比 | Before/After |
| 清单列表 | 编号清单 | 1.2.3.4.清晰排列 |
| 核心要点 | 中心辐射 | 核心在中间，四周发散 |
| 场景展示 | 场景图+文字 | 大图+叠加文字 |
| 功能介绍 | 图标矩阵 | 图标排列+简短说明 |

### 配图风格建议

| 文章主题 | 风格 | 配色 |
|----------|------|------|
| 效率工具 | 科技感 | 蓝紫渐变 |
| 教程攻略 | 专业简洁 | 商务蓝 |
| 生活技巧 | 清新自然 | 薄荷绿/暖橙 |
| 科技数码 | 暗黑未来 | 深蓝+霓虹 |
| 情感生活 | 温暖柔和 | 粉橙渐变 |
| OBS/直播 | 导播风格 | 深色+高亮 |

### 配图生成命令

```bash
# HTML渲染（快速出图）
python scripts/render_xhs.py content.md -t neo-brutalism -m separator
```

---

## 四、完整生成流程

### Step 1: 提炼内容

阅读文章，提取：
- 主标题（≤10字）
- 副标题（≤15字）
- 核心视觉隐喻
- 内容块数量

### Step 2: 生成封面

```bash
# 方式A：AI生图（高级电影感）
python <image-skill>/scripts/generate_image.py \
  "A [隐喻主体], floating [相关元素], cinematic lighting. \
  Composition: right 2/3 visual, left 1/3 empty for text. \
  [配色], [风格]. No text at edges." \
  -o cover.png -s 1080x1440
```

### Step 3: 生成配图

```bash
# 方式A：HTML渲染
python scripts/render_xhs.py content.md -t sketch -m separator

# 方式B：AI生图（每张配图单独生成）
python <image-skill>/scripts/generate_image.py "prompt" -o card_1.png -s 1080x1440
```

### Step 4: 整理输出

```
output/
├── cover.png      # 封面（AI生图，有文字）
├── card_1.png     # 配图1
├── card_2.png     # 配图2
└── card_3.png     # 配图3
```

---

## 五、实战案例

### 案例：OBS摄像头一键移动插件

**提炼**：
- 主标题：OBS摄像头
- 副标题：一键移动+复位，直播录课更专业
- 隐喻：画面切换→导演推杆/摄像机运动

**封面Prompt**：
```
A professional live streaming studio with a high-quality webcam and broadcast control panel,
cinematic lighting, 8k resolution.
Composition heavily weighted to the right 2/3, leaving negative space on the left for typography.
Deep blue purple gradient, subtle ambient glow, minimalist tech aesthetic. No text at edges.
```

**配图规划**：
- card_1: 插件简介（核心功能）
- card_2: 安装步骤
- card_3: 配置流程

---

### 案例：Listary配置参考

**提炼**：
- 主标题：Listary
- 副标题：双Ctrl秒搜文件+网络搜索
- 隐喻：搜索→放大镜/闪电/全息搜索

**封面Prompt**：
```
A sleek laptop with floating search icons and holographic search results,
cinematic lighting, 8k resolution.
Composition heavily weighted to the right 2/3, leaving negative space on the left for typography.
Deep blue gradient, subtle glow, premium tech aesthetic. No text at edges.
```

---

### 案例：Typora图床教程

**提炼**：
- 主标题：Typora配图床
- 副标题：3步搞定，写文档再不用手动传图
- 隐喻：云端上传→翅膀/火箭/连接线

**封面Prompt**：
```
A sleek laptop with floating cloud icons and upload arrows,
cinematic lighting, 8k resolution.
Composition heavily weighted to the right 2/3, leaving negative space on the left for typography.
Deep blue purple gradient, subtle glow. No text at edges.
```

---

## 六、可视化检查清单

生成封面后，检查：

- [ ] 画面占2/3，留白占1/3
- [ ] 文字在画面左侧或右侧（不是顶部/底部）
- [ ] 画面有视觉隐喻（不是纯色/渐变）
- [ ] 整体风格统一（配色/光效）
- [ ] 配图与封面风格协调
- [ ] 主标题+副标题已提炼

---

## 七、样式选择速查

| 内容类型 | 封面风格 | 配图版式 | 推荐主题 |
|----------|----------|----------|----------|
| 教程攻略 | 负空间式 | 步骤时间轴 | sketch, neo-brutalism |
| 工具推荐 | 中心焦点式 | 卡片堆叠式 | playful-geometric |
| 干货分享 | 对比式 | 列表清单式 | professional |
| 情感生活 | 暖色调 | 问答式 | retro, botanical |
| 科技数码 | 电影感 | 卡片堆叠式 | terminal, dark |
| OBS/直播 | 导播风格 | 步骤时间轴 | neo-brutalism |

---

## 八、进阶技巧

### 负空间封面设计

核心原则：
1. 画面只占 2/3，另一侧 1/3 留白放文字
2. 文字严禁放在顶部或底部边缘
3. 预留空间必须在画面中间左侧或中间右侧

### 视觉层次

```
┌─────────────────────────────────┐
│           画面主体 2/3           │
│  ┌─────────────────────────────┐│
│  │       预留文字空间 1/3       ││
│  │   主标题（中间/右侧）       ││
│  │   副标题                    ││
│  └─────────────────────────────┘│
└─────────────────────────────────┘
```

### 隐喻提取练习

| 文章关键词 | 隐喻提取 | 视觉元素 |
|------------|----------|----------|
| 上传/图床 | 传输/连接 | 翅膀、火箭、云、箭头 |
| 搜索 | 探索/发现 | 放大镜、雷达、星光 |
| 快捷键 | 加速/掌控 | 闪电、翅膀、键盘 |
| 一键 | 魔法/简单 | 魔法棒、开关、按钮 |
| 直播 | 导演/舞台 | 摄像机、导播台、推杆 |
| 摄像头 | 眼睛/视角 | 眼睛、镜头、取景框 |
| 安装 | 搭建/启动 | 齿轮、钥匙、开关 |
| 配置 | 调校/定制 | 旋钮、仪表盘、滑块 |
