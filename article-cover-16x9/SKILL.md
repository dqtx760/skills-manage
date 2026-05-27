---
name: article-cover-16x9
description: 从文章或一段正文自动生成 16:9 封面图并保存到 D:\data\images\Article-illustrations。用户只要说"生成封面""做个封面""文章封面""博客封面""公众号封面""根据这篇文章出封面""cover image"，或提供文章/Markdown/文本并要求做封面时，就应该使用本 Skill。特别适合中文文章、博客文章、公众号文章、技术文章、观点文章的 1920×1080 横版封面。不要用于文章内多张配图，那种情况用 baoyu-article-illustrator；不要用于卡片海报排版，那种情况用 ljg-card。
---

# Article Cover 16:9

把用户提供的一段文章或一篇文章，提炼为一张 16:9 横版封面图，并保存到 D:\data\images\Article-illustrations。

核心目标：**少问问题，直接产出一张能用的 1920×1080 封面**。封面必须有明确视觉隐喻、电影感光影、强构图，并且给标题留出干净的中部左侧或中部右侧负空间。

## 输入

支持以下输入形式：

- 用户直接粘贴文章、段落、摘要、标题或选题。
- 用户提供本地文章路径，例如 `.md`、`.txt`、`.docx`、`.pdf`。能读取则读取全文；文件过长则读取标题、开头、结尾和关键小标题。
- 用户给出封面风格要求，例如“更赛博朋克”“极简”“像电影海报”“技术感”。

如果用户没有明确标题，自动提炼标题；如果用户已有标题，优先尊重原标题，但可以压缩到封面可读长度。

## 默认输出

- 图片尺寸：`1920x1080`
- 纵横比：`16:9`
- 默认保存位置：`D:\data\images\Article-illustrations\`
- 默认文件名：`cover-{slug}-{YYYYMMDD-HHMMSS}.png`
- 同时保存提示词记录：`cover-{slug}-{YYYYMMDD-HHMMSS}.prompt.md`

文件名 slug 用文章主题的 2-4 个英文或拼音/kebab-case 词，避免中文路径兼容问题。

## 工作流

### 1. 读取和提炼内容

快速完成以下判断，不要输出长篇分析：

1. 文章核心冲突或核心隐喻是什么。
2. 封面主标题：中文优先，少于 10 个汉字；英文少于 6 个词。
3. 封面副标题：一句短句，解释张力或收益，不超过 18 个汉字。
4. 视觉主体：一个能表达核心隐喻的具体画面，避免把抽象概念做成泛泛的科技背景。
5. 构图策略：二选一。
   - 视觉重心在右侧 2/3，左侧 1/3 留白放文字。
   - 视觉重心在左侧 2/3，右侧 1/3 留白放文字。

### 2. 简短确认文本

在生成前，向用户简短展示：

```markdown
主标题：[标题]
副标题：[副标题]
构图：[左侧留白/右侧留白]
```

如果用户明确说“直接生成”“不用确认”“按默认出图”，展示上述三行后直接继续生成，不再等待确认。

如果用户没有明确说跳过确认，但请求已经很明确，也可以只做一次轻量确认；不要进入复杂问卷。

### 3. 构造并保存完整图片提示词

在调用任何图片后端前，必须先把最终 prompt 保存到输出目录的 `.prompt.md` 文件。这个记录用于复现和二次修改。

Prompt 必须包含以下结构：

```text
Aspect Ratio: 16:9.
Resolution: 1920 × 1080.

Composition: [明确说明视觉重心在左/右侧 2/3，另一侧 1/3 是干净负空间，标题文字渲染在该区域。]

Subject: [基于文章核心隐喻的具体视觉画面。]

Text Rendering: Render the following text directly in the image, as part of the artwork (not overlay, not watermark):
- Main Title (主标题): "[主标题内容]" — placed in the negative space area, large size, bold, high contrast, clean sans-serif or serif font depending on style.
- Subtitle (副标题): "[副标题内容]" — placed below or beside the main title, smaller size, lower contrast but still readable.
The text must be rendered natively in the image, properly kerned, no distorted characters, no misspellings. Chinese characters must be correct and complete.

Style: cinematic lighting, high-detail material texture, editorial cover design, strong visual hierarchy, premium magazine cover aesthetic, 8k detail. The title text should look like it belongs to the cover design, not like a post-production overlay.

Prohibit: No extra random words, no logos, no watermarks, no UI screenshots, no decorative captions outside the specified title and subtitle. No text at the very top edge or very bottom edge — only in the designated negative space area.
```

中文文章可以让标题保持中文，但视觉描述尽量用英文表达，通常更利于图像模型理解。

### 4. 调用图片生成后端

沿用 `baoyu-article-illustrator` 的后端选择原则：优先使用当前环境可用的原生或已安装图片生成后端，不要用 SVG/HTML/Canvas 伪造位图。

**首选后端：GPT-Image-2**（apimart.ai，无水印，支持 16:9）。

调用方式：通过 Bash 执行 Python 脚本：

```bash
python "D:\data\images\Article-illustrations\gpt_image2_gen.py" "{final prompt}" "D:\data\images\Article-illustrations\cover-{slug}-{timestamp}.png" "16:9" "1k"
```

参数说明：

| 参数 | 值 | 说明 |
|------|-----|------|
| prompt | 完整提示词内容 | 从 Step 3 构造的最终 prompt |
| output | 输出目录绝对路径 | `.png` 格式，后续可转 JPG |
| size | `16:9` | 封面固定横版 |
| resolution | `1k` | 输出 ~1536×864 或 1672×941 |

脚本路径检测顺序：
1. `{output-dir}/gpt_image2_gen.py`（与输出同目录）
2. `D:\data\images\Article-illustrations\gpt_image2_gen.py`（默认位置）

如果 GPT-Image-2 脚本不可用，按以下降级顺序尝试：
- 用户在当前请求指定的其他后端
- 运行时原生图像工具（如 Codex imagegen）
- 已安装的其他非原生后端

降级时仍需保持约束：1920×1080、输出到 `D:\data\images\Article-illustrations\`、先保存 prompt 文件、生成位图文件。

如果没有任何可用图片后端，告诉用户缺少后端，并给出已保存的 prompt 文件路径。

### 5. 完成反馈

生成完成后，只输出必要信息：

```markdown
已生成封面：D:\data\images\Article-illustrations\cover-xxx.png
提示词记录：D:\data\images\Article-illustrations\cover-xxx.prompt.md
```

如果生成失败，保留 prompt 文件，并简短说明失败原因和下一步建议。

## 质量规则

- 标题空间必须在画面中部左侧或中部右侧，不能贴顶部或底部。
- 构图要主动创造负空间，而不是生成完再“假装能放字”。
- 不要做通用 AI 科技感背景；必须从文章里抽出具体隐喻。
- 标题短、有张力；副标题提供解释或补充。
- 画面优先像“文章封面/杂志封面/电影海报”，不是信息图，也不是 PPT 页。
- 只生成一张封面，除非用户明确要求多版。

## 修改请求

用户如果说"换个风格""标题不对""文字放右边""重新生成一版"，读取上一次的 `.prompt.md` 或沿用本轮上下文，只改用户指出的部分，然后保存新的 prompt 和图片到输出目录。不要覆盖旧文件。