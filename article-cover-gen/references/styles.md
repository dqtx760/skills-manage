# Style Reference - Article Cover

## Core Styles (核心风格)

简化的风格层级，便于快速选择:

| 核心风格 | 映射到 | 适合场景 |
|------------|---------|----------|
| `vector` | vector-illustration | 知识文章、教程、技术内容 |
| `minimal-flat` | notion | 通用、知识分享、SaaS |
| `sci-fi` | blueprint | AI、前沿技术、系统设计 |
| `hand-drawn` | sketch/warm | 轻松、反思、休闲内容 |
| `editorial` | editorial | 流程、数据、新闻 |
| `scene` | warm/watercolor | 叙事、情感、生活方式 |

大多数情况使用核心风格。下方完整风格画廊提供精细控制。

---

## Style Gallery (完整风格画廊)

| 风格 | 描述 | 适合场景 |
|-------|-------------|----------|
| `vector-illustration` | 扁平矢量艺术，清晰轮廓和复古柔和色彩 | 知识文章、教程、技术内容 |
| `notion` | 极简手绘线图风格 | 知识分享、SaaS、生产力 |
| `elegant` | 精致、成熟的设计 | 商业、思想领导力 |
| `warm` | 友好、亲切的风格 | 个人成长、生活方式、教育 |
| `minimal` | 超极简、禅意风格 | 哲学、极简主义、核心概念 |
| `blueprint` | 技术蓝图风格 | 架构、系统设计、工程 |
| `watercolor` | 柔和艺术效果，自然温暖 | 生活方式、旅行、创意 |
| `editorial` | 杂志风格信息图 | 科技解说、新闻 |
| `scientific` | 学术精确图表 | 生物、化学、技术研究 |
| `chalkboard` | 教室黑板绘画风格 | 教育、教学、解释 |
| `fantasy-animation` | 吉卜力/迪士尼风格手绘 | 故事书、魔法、情感 |
| `flat` | 现代大胆几何形状 | 现代数字、当代 |
| `flat-doodle` | 可爱扁平风格加粗轮廓 | 可爱、友好、亲切 |
| `intuition-machine` | 技术简报风格，陈旧纸张 | 技术简报、学术 |
| `nature` | 有机自然插图 | 环境、健康 |
| `pixel-art` | 复古8位游戏美学 | 游戏、复古科技 |
| `playful` | 异想天开粉笔画 | 有趣、休闲、教育 |
| `retro` | 80/90年代霓虹几何 | 80/90年代怀旧、大胆 |
| `sketch` | 原始铅笔笔记本风格 | 头脑风暴、创意探索 |
| `sketch-notes` | 柔和手绘温暖笔记 | 教育、温暖笔记 |
| `vintage` | 陈旧羊皮纸历史风格 | 历史、传承 |

完整规格: `references/styles/<style>.md`

---

## Type × Style Compatibility Matrix (类型×风格兼容性矩阵)

| | vector-illustration | notion | warm | minimal | blueprint | watercolor | elegant | editorial | scientific |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| infographic | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |
| scene | ✓ | ✓ | ✓✓ | ✓ | ✗ | ✓✓ | ✓ | ✓ | ✗ |
| flowchart | ✓✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✗ | ✓ | ✓✓ | ✓ |
| comparison | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✓✓ | ✓ |
| framework | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓✓ | ✗ | ✓✓ | ✓ | ✓✓ |
| timeline | ✓ | ✓✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ | ✓✓ | ✓ |

✓✓ = 高度推荐 | ✓ = 兼容 | ✗ = 不推荐

---

## Auto Selection by Type (按类型自动选择)

| Type | 主要风格 | 次要风格 |
|------|---------------|------------------|
| infographic | vector-illustration | notion, blueprint, editorial |
| scene | warm | watercolor, elegant |
| flowchart | vector-illustration | notion, blueprint |
| comparison | vector-illustration | notion, elegant |
| framework | blueprint | vector-illustration, notion |
| timeline | elegant | warm, editorial |

---

## Auto Selection by Content Signals (按内容信号自动选择)

| 内容信号 | 推荐Type | 推荐Style |
|-----------------|------------------|-------------------|
| API, metrics, data, comparison, numbers | infographic | blueprint, vector-illustration |
| 知识, 概念, 教程, 学习, 指南 | infographic | vector-illustration, notion |
| 技术, AI, 编程, 开发, 代码 | infographic | vector-illustration, blueprint |
| 如何, 步骤, 工作流, 过程, 教程 | flowchart | vector-illustration, notion |
| 框架, 模型, 架构, 原则 | framework | blueprint, vector-illustration |
| vs, 优缺点, 前后, 替代方案 | comparison | vector-illustration, notion |
| 故事, 情感, 旅程, 经验, 个人 | scene | warm, watercolor |
| 历史, 时间线, 进步, 演进 | timeline | elegant, warm |
| 生产力, SaaS, 工具, 应用, 软件 | infographic | notion, vector-illustration |
| 商业, 专业, 战略, 企业 | framework | elegant |
| 生物, 化学, 医疗, 科学 | infographic | scientific |
| 解说, 新闻, 杂志, 调查 | infographic | editorial |

---

## Style Characteristics by Type (按类型的风格特征)

### infographic + vector-illustration
- 干净扁平矢量形状，大胆几何形式
- 鲜艳但和谐的色彩调色板
- 清晰的视觉层级，图标和标签
- 现代、专业、高度可读
- 非常适合知识文章和教程

### scene + warm
- 黄金时段光照，舒适氛围
- 柔和渐变，自然纹理
- 亲切、个人感觉
- 非常适合讲故事

### flowchart + blueprint
- 技术精确，示意性线条
- 网格布局，清晰区域
- 等宽标签，数据导向
- 蓝/白配色方案

### comparison + vector-illustration
- 分割布局，清晰视觉分隔
- 大胆图标风格，每边一个
- 色彩编码区分
- 易于一目了然的对比

### framework + blueprint
- 精确节点连接
- 分层清晰
- 系统架构感觉
- 技术框架

---

## Cover-Specific Style Recommendations (封面专用风格推荐)

### 公众号封面最佳风格

| 内容类型 | 推荐风格 | 理由 |
|----------|---------|------|
| 技术教程 | vector-illustration | 清晰易读，专业感 |
| AI/前沿科技 | blueprint | 科技感，未来感 |
| 软件推荐 | notion | 简洁现代，突出内容 |
| 个人成长 | warm | 温暖亲切，情感共鸣 |
| 数据分析 | editorial | 专业可信，数据导向 |
| 设计/创意 | watercolor | 艺术感，创造力 |

### 封面设计原则

1. **视觉冲击**: 封面需要在feed中吸引注意
2. **文字清晰**: 如果包含标题，必须清晰可读
3. **风格一致**: 与文章内容风格匹配
4. **简洁干净**: 避免过度复杂的设计
5. **色彩和谐**: 使用风格定义的调色板

---

## Cover Layout Types (封面布局类型)

| 布局类型 | 描述 | 适合场景 |
|----------|------|----------|
| `centered` | 主体居中，对称布局 | 通用、正式内容 |
| `left-heavy` | 主体偏左，文字右侧 | 图文结合 |
| `top-heavy` | 主体偏上，底部文字 | 突出视觉效果 |
| `split` | 左右分割 | 对比类内容 |
| `full-bleed` | 全幅背景，文字覆盖 | 氛围感强 |
