# Article Cover Generator - Detailed Workflow

## Step 1: Pre-check

### 1.0 Detect & Save Reference Images ⚠️ OPTIONAL

Check if user provided reference images for cover style.

| Input Type | Action |
|------------|--------|
| Image file path provided | Copy to `references/` subdirectory |
| Image in conversation | Ask user for file path |
| No reference | Use style system directly |

**如果用户提供了参考图**:
1. 复制到 `references/cover-ref.png`
2. 创建描述文件 `references/cover-ref.md`
3. 提取颜色和风格特征

### 1.1 Load Preferences (EXTEND.md) ⛔ BLOCKING

**CRITICAL**: 如果EXTEND.md不存在，必须先完成首次设置。

```bash
test -f .claude/skills/article-cover-gen/EXTEND.md && echo "project"
test -f "$HOME/.claude/skills/article-cover-gen/EXTEND.md" && echo "user"
```

| 结果 | 操作 |
|--------|--------|
| 找到 | 读取配置，显示摘要 → 继续 |
| 未找到 | ⛔ **阻塞**: 创建EXTEND.md配置文件 |

**支持的配置项**:
- 水印设置
- 偏好风格
- 自定义样式
- 输出目录
- 语言设置

---

## Step 2: Analyze Content

### 2.1 分析文章内容

| 分析项 | 描述 |
|----------|-------------|
| 主题 | 文章核心主题/关键词 |
| 类型 | 技术/教程/叙事/评论 |
| 用途 | 公众号封面/配图 |
| 推荐Type | 基于内容信号 |
| 推荐Style | 基于Type和内容 |

### 2.2 提取核心信息

- 文章标题
- 核心关键词 (2-4个)
- 主要观点/价值
- 目标受众

**CRITICAL**: 封面设计不需要详细文字，使用图标和视觉元素表达概念。

---

## Step 3: Confirm Settings ⚠️

**一次 AskUserQuestion 调用，最多3个问题。**

### Q1: Cover Type ⚠️ 必需

基于内容分析推荐:
- [推荐Type] (推荐)
- infographic / scene / flowchart / comparison / framework / timeline

### Q2: Visual Style ⚠️ 必需

如果EXTEND.md有 `preferred_style`:
- [自定义风格名 + 简短描述] (推荐)
- [其他兼容核心风格]
- Other (查看完整风格画廊)

**核心风格速览**:

| 核心风格 | 映射到 | 适合场景 |
|------------|---------|----------|
| `vector` | vector-illustration | 知识文章、教程、技术内容 |
| `minimal-flat` | notion | 通用、知识分享、SaaS |
| `sci-fi` | blueprint | AI、前沿技术、系统设计 |
| `hand-drawn` | sketch/warm | 轻松、反思、休闲内容 |
| `editorial` | editorial | 流程、数据、新闻 |

### Q3: Text Language ⚠️ 可选

当文章语言 ≠ EXTEND.md `language` 设置时:
- 文章语言 (匹配文章内容) (推荐)
- EXTEND.md语言 (用户通用偏好)

---

## Step 4: Generate Cover Prompts

### 4.1 创建Prompt 1 - 概念表现

保存为 `prompts/cover-{slug}-01.md`:

```yaml
---
cover_id: 01
type: [selected_type]
style: [selected_style]
aspect_ratio: "16:9"
size: "1280x720"
---

[Cover Prompt 1 - 概念表现]

Type: [type_description]
Layout: [cover composition]

FOCAL ELEMENT: [main visual element]
ATMOSPHERE: [mood, lighting]
COLORS: [from selected style palette]
STYLE: [style characteristics]

Text elements (minimal):
- [Article Title or Key Phrase] - Large, prominent position

COMPOSITION: [16:9 landscape layout]
- Background: [color/style]
- Main element: [position, size]
- Text: [position, hierarchy]
- Decorative: [minimal accents]

ASPECT: 16:9 horizontal, 1280x720px
```

### 4.2 创建Prompt 2 - 变体设计

保存为 `prompts/cover-{slug}-02.md`:

```yaml
---
cover_id: 02
type: [selected_type]
style: [selected_style]
aspect_ratio: "16:9"
size: "1280x720"
variation: true
---

[Cover Prompt 2 - 设计变体]

Type: [type_description] - Alternative composition
Layout: [different layout from Prompt 1]

VARIATION: [how this differs from Prompt 1]
- [Composition change]
- [Color emphasis shift]
- [Element arrangement]

[Rest of prompt structure follows Prompt 1...]

ASPECT: 16:9 horizontal, 1280x720px
```

### 4.3 Prompt模板结构

**通用封面Prompt结构**:
```
[Type] style 16:9 article cover

LAYOUT:
- Format: Horizontal 16:9
- Background: [style-based background]
- Main visual: [focal element]
- Text: [minimal, title only]

COLORS:
- [From selected style palette]

STYLE ELEMENTS:
- [From style characteristics]

TEXT:
- Main: "[Article Title or Key Phrase]"
- Position: [centered/top/bottom]
- Size: Large, prominent

COMPOSITION:
- Clean, balanced layout
- Generous white space
- Main element: [position and treatment]

ASPECT: 16:9 horizontal (1280x720)
```

---

## Step 5: Generate Images

### 5.1 选择生成方法

**检测环境并选择合适的方法**:

| 环境 | 方法 | 命令 |
|------------|----------|----------|
| **Claude Code** | 使用 `/image` skill | `/image "<prompt>" -o <path> -s 1280x720` |
| **Claudian/Obsidian** | 使用Python脚本 | `python D:\zhishiku\.claude\skills\image\scripts\generate_image.py "<prompt>" -o <path> -s 1280x720` |
| **Other/CMD** | 使用Python脚本 | `python <image-skill-path>/scripts/generate_image.py "<prompt>" -o <path> -s 1280x720` |

**Image skill位置**: `D:\zhishiku\.claude\skills\image\`
**脚本路径**: `image/scripts/generate_image.py`

### 5.2 生成封面

**输出目录**: `D:\zhishiku\5️⃣输出\image\cover\`

**Claude Code环境**:
```bash
# 封面 1
/image "<prompt_1>" -o "D:/zhishiku/5️⃣输出/image/cover/{topic}-01.png" -s 1280x720

# 封面 2
/image "<prompt_2>" -o "D:/zhishiku/5️⃣输出/image/cover/{topic}-02.png" -s 1280x720
```

**Claudian/Obsidian/Other环境**:
```bash
cd D:\zhishiku\.claude\skills\image

# 封面 1
python scripts/generate_image.py "<prompt_1>" -o "D:/zhishiku/5️⃣输出/image/cover/{topic}-01.png" -s 1280x720

# 封面 2
python scripts/generate_image.py "<prompt_2>" -o "D:/zhishiku/5️⃣输出/image/cover/{topic}-02.png" -s 1280x720
```

**生成步骤**:
1. 检查输出目录存在，不存在则创建
2. 对每张封面:
   - 如果文件存在，重命名为备份
   - 生成图片
   - 报告进度 "Generated X/2 - 已保存到 D:/zhishiku/5️⃣输出/image/cover/"
3. 失败时重试一次，然后记录并继续

### 5.3 添加水印 (如果启用)

如果EXTEND.md中启用水印，添加到prompt:
```
Include a subtle watermark "[content]" positioned at [position] with approximately [opacity*100]% visibility.
```

---

## Step 6: Finalize

### 6.1 输出摘要

```
Cover Generation Complete!

Topic: [article topic/title]
Type: [type] | Style: [style]
Location: D:\zhishiku\5️⃣输出\image\cover\
Images: 2/2 generated

Files:
- {topic}-01.png → [description - Concept focus]
- {topic}-02.png → [description - Variation design]

Aspect Ratio: 16:9 (1280x720)
```

### 6.2 文件管理

| 操作 | 说明 |
|--------|--------|
| 重命名 | 用户可自定义文件名 |
| 备份 | 覆盖前自动备份原文件 |
| 删除 | 删除不需要的版本 |

---

## Step 7: Integration with Article (Optional)

### 7.1 更新文章封面

如果文章需要引用封面:
```markdown
![封面](D:/zhishiku/5️⃣输出/image/cover/{topic}-01.png)
```

### 7.2 PicList 上传 (可选)

如果用户使用PicList图床:
1. 图片已保存到固定目录
2. PicList自动检测并上传
3. 上传后替换本地路径为图床URL

---

## Troubleshooting

| 问题 | 解决方案 |
|------|---------|
| 输出目录不存在 | 创建目录或检查EXTEND.md配置 |
| 生成失败 | 检查image skill配置和API密钥 |
| 风格不匹配 | 查看styles.md选择兼容风格 |
| 尺寸问题 | 确认aspect_ratio和size参数 |
