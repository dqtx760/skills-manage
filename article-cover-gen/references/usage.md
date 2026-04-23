# Usage Guide - Article Cover Generator

## Quick Start (快速开始)

### Claude Code 环境

```bash
# 直接使用skill
/article-cover-gen
```

### 其他环境 (Claudian/Obsidian)

```bash
# 使用Python脚本
python D:\zhishiku\.claude\skills\image\scripts\generate_image.py "<prompt>" -o "<output>" -s 1280x720
```

---

## Command Syntax (命令语法)

### Claude Code (/image skill)

```bash
/image "<prompt>" -o "<output_path>" -s 1280x720
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `<prompt>` | 图片描述prompt | `"A vector illustration cover about AI tools"` |
| `-o` | 输出路径 (必需) | `"D:/zhishiku/5️⃣输出/image/cover/ai-tools-01.png"` |
| `-s` | 尺寸 (可选) | `1280x720` (默认) |

**路径格式**: 使用正斜杠 `/` 或双反斜杠 `\\`

### Python Script

```bash
python scripts/generate_image.py "<prompt>" -o "<output>" -s 1280x720
```

**完整路径**:
```bash
python D:\zhishiku\.claude\skills\image\scripts\generate_image.py "<prompt>" -o "D:/zhishiku/5️⃣输出/image/cover/output.png" -s 1280x720
```

---

## Output Directory (输出目录)

```
D:\zhishiku\5️⃣输出\image\cover\
├── {topic}-01.png
└── {topic}-02.png
```

### 文件命名规则

| 格式 | 说明 | 示例 |
|------|------|------|
| `{topic}-{01|02}.png` | 主题 + 序号 | `ai-tools-01.png` |
| `{topic}-YYYYMMDD-HHMMSS-{01|02}.png` | 带时间戳 | `ai-tools-20260214-143000-01.png` |

**冲突处理**: 文件存在时自动添加时间戳

---

## Type Selection Guide (类型选择指南)

### By Content Type (按内容类型)

| 内容类型 | 推荐Type | 理由 |
|----------|----------|------|
| 数据分析、指标对比 | `infographic` | 清晰展示数据 |
| 工具推荐、软件列表 | `infographic` | 结构化呈现 |
| 技术教程、操作指南 | `flowchart` | 流程步骤清晰 |
| 产品对比、优缺点 | `comparison` | 对比直观 |
| 架构设计、系统模型 | `framework` | 层次分明 |
| 发展历程、版本演进 | `timeline` | 时间线清晰 |
| 个人故事、情感表达 | `scene` | 氛围感强 |

### Keyword Triggers (关键词触发)

| 关键词 | 推荐Type |
|--------|----------|
| 数据、统计、分析、报告 | infographic |
| 步骤、流程、教程、如何、指南 | flowchart |
| vs、对比、区别、优缺点 | comparison |
| 架构、框架、模型、体系 | framework |
| 历史、演进、发展、时间线 | timeline |
| 故事、经历、感受、场景 | scene |

---

## Style Selection Guide (风格选择指南)

### By Article Category (按文章分类)

| 文章分类 | 推荐风格 | 备选风格 |
|----------|----------|----------|
| AI/技术教程 | vector-illustration | blueprint, notion |
| 软件推荐 | notion | minimal-flat, vector |
| 系统架构 | blueprint | sci-fi, vector |
| 个人成长 | warm | watercolor, elegant |
| 数据分析 | editorial | scientific, blueprint |
| 设计/创意 | watercolor | playful, scene |
| 极简/效率 | minimal | elegant, notion |
| 复古/怀旧 | retro | vintage, pixel-art |
| 教育/教学 | sketch-notes | chalkboard, warm |

### By Tone (按语调)

| 语调 | 推荐风格 |
|------|----------|
| 专业严谨 | blueprint, scientific, elegant |
| 轻松亲切 | warm, playful, sketch |
| 现代简洁 | minimal, notion, flat |
| 创意艺术 | watercolor, fantasy-animation |
| 技术前沿 | sci-fi, blueprint, intuition-machine |

---

## Common Workflows (常见工作流)

### Workflow 1: 标准封面生成

```
1. 分析文章内容 → 识别主题和类型
2. 推荐Type和Style → 基于内容信号
3. 用户确认设置 → AskUserQuestion (可选)
4. 生成2张封面 → 不同构图变体
5. 输出完成 → 显示文件路径和描述
```

### Workflow 2: 使用偏好设置

```
1. 加载EXTEND.md → 读取preferred_style
2. 分析内容 → 仅确定Type
3. 直接生成 → 使用预设风格
4. 输出完成
```

### Workflow 3: 自定义风格

```
1. 分析内容 → Type和Style
2. 用户选择Other → 查看完整风格画廊
3. 精确选择风格 → 从完整列表
4. 生成封面
5. 保存偏好 → 更新EXTEND.md
```

---

## Integration with Other Skills (与其他技能集成)

### With article skill (创建文章)

```
1. /article → 创建公众号文章
2. article-cover-gen → 为文章生成封面
3. 输出目录 → 封面自动可用
```

### With md2wechat skill (格式转换)

```
1. 编写Markdown文章
2. article-cover-gen → 生成封面
3. md2wechat → 转换并上传
4. 封面图片 → 可在草稿中使用
```

### With baoyu-article-illustrator (文章配图)

```
1. baoyu-article-illustrator → 生成文章内插图
2. article-cover-gen → 生成封面
3. 统一风格 → 保持视觉一致性
```

---

## Troubleshooting (故障排除)

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 输出目录不存在 | 首次运行或路径错误 | 检查EXTEND.md配置，创建目录 |
| 生成失败 | API配置问题 | 检查image skill配置和API密钥 |
| 风格不匹配 | Type×Style不兼容 | 查看styles.md兼容性矩阵 |
| 文件已存在 | 同名文件冲突 | 自动添加时间戳或重命名 |
| 图片质量不理想 | Prompt不够详细 | 参考prompt-construction.md优化 |

---

## Tips & Best Practices (技巧与最佳实践)

### 封面设计建议

1. **视觉冲击**: 封面需要在feed中吸引注意
2. **文字精简**: 如果包含文字，仅标题或关键词
3. **风格一致**: 与文章内容风格匹配
4. **对比强烈**: 使用风格定义的调色板
5. **尺寸正确**: 确认16:9比例，1280x720像素

### Prompt优化

1. **具体描述**: 详细说明主视觉元素
2. **风格特征**: 引用风格的具体特征
3. **布局清晰**: 明确构图和元素位置
4. **色彩精确**: 使用风格的调色板颜色
5. **比例明确**: 始终包含16:9横向格式

### 工作流优化

1. **设置偏好**: 在EXTEND.md中保存常用风格
2. **批量生成**: 一次生成2张便于选择
3. **版本管理**: 保留多个版本供后续使用
4. **目录规范**: 固定输出目录便于管理
5. **风格统一**: 同系列文章使用相同风格
