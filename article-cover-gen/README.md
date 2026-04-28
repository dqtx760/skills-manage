# Article Cover Generator

为公众号文章生成16:9封面图片的Claude Code Skill。

## 功能特点

- **尺寸**: 16:9横向格式 (1280x720px)
- **数量**: 每次生成2张不同设计的封面
- **设计系统**: Type × Style二维方法
- **风格**: 20+种专业风格可选
- **输出**: 固定目录，便于管理

## 目录结构

```
article-cover-gen/
├── .claude/
│   └── settings.json          # Skill配置
├── prompts/                    # 生成的封面prompt存储
├── references/
│   ├── workflow.md             # 详细工作流程
│   ├── usage.md               # 使用指南
│   ├── prompt-construction.md # Prompt构造指南
│   ├── styles.md              # 风格画廊
│   └── styles/                # 风格详细定义
│       ├── vector-illustration.md
│       ├── warm.md
│       ├── minimal.md
│       └── ... (20+ styles)
├── scripts/                   # 辅助脚本
├── SKILL.md                   # Skill主文档
├── EXTEND.md                  # 用户配置
└── README.md                  # 本文件
```

## Type × Style 二维设计

### Types (封面类型)

| Type | 中文 | 适用场景 |
|------|------|----------|
| `infographic` | 信息图 | 数据展示、技术文章、工具推荐 |
| `scene` | 场景 | 叙事性、情感类、生活方式 |
| `flowchart` | 流程图 | 教程步骤、操作指南 |
| `comparison` | 对比 | 产品对比、优缺点分析 |
| `framework` | 框架 | 架构图、模型框架 |
| `timeline` | 时间线 | 发展历史、演进过程 |

### Styles (风格)

| 核心风格 | 映射 | 适合场景 |
|----------|------|----------|
| `vector` | vector-illustration | 知识文章、教程 |
| `minimal-flat` | notion | 通用、知识分享 |
| `sci-fi` | blueprint | AI、前沿技术 |
| `hand-drawn` | sketch/warm | 轻松、休闲内容 |
| `editorial` | editorial | 流程、数据 |

完整风格列表参见 [references/styles.md](references/styles.md)

## 输出目录

```
D:\zhishiku\5️⃣输出\image\cover\
├── {topic}-01.png
└── {topic}-02.png
```

## 依赖

- **image skill**: `D:\zhishiku\.claude\skills\image\`
- **ModelScope API**: 通义千问AI图片生成

## 快速开始

### Claude Code 环境

```bash
/article-cover-gen
```

### 配置偏好风格

编辑 `EXTEND.md`:

```yaml
preferred_style:
  name: vector-illustration
  description: "扁平矢量插图风格"
```

## 相关Skills

- [baoyu-article-illustrator](../baoyu-article-illustrator/) - 文章配图生成
- [image](../image/) - AI图片生成基础
- [md2wechat](../md2wechat-skill/) - Markdown转微信格式

## License

MIT
