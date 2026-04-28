# Prompt Construction - Article Cover

## Cover Prompt Format

封面prompt文件使用YAML frontmatter + 内容:

```yaml
---
cover_id: 01
type: infographic
style: blueprint
aspect_ratio: "16:9"
size: "1280x720"
variation: false
references:                    # 仅当references/目录中文件存在时
  - ref_id: 01
    filename: 01-ref-style.png
    usage: style              # direct | style | palette
---

[Type-specific template content below...]
```

**⚠️ CRITICAL - 何时包含 `references` 字段**:

| 情况 | 操作 |
|-----------|--------|
| 参考图保存到 `references/` | 在frontmatter中包含 ✓ |
| 风格口头提取（无文件） | 不在frontmatter中包含，改为追加到prompt正文 |

**参考图使用类型** (仅当文件存在):

| 使用 | 描述 | 生成操作 |
|-------|-------------|-------------------|
| `direct` | 主要视觉参考 | 传递给 `--ref` 参数 |
| `style` | 仅风格特征 | 在prompt文本中描述风格 |
| `palette` | 调色板提取 | 在prompt中包含颜色 |

---

## Default Composition Requirements (默认构图要求)

**应用到所有封面prompt**:

| 要求 | 描述 |
|-------------|-------------|
| **干净构图** | 简单布局，无视觉杂乱 |
| **留白充足** | 充裕的边距和呼吸空间 |
| **简洁背景** | 纯色或微妙渐变，避免复杂纹理 |
| **居中或内容导向** | 主视觉元素居中或按内容需求定位 |
| **突出核心信息** | 留白引导注意力到关键信息 |

**添加到所有封面prompt**:
> Clean composition with generous white space. Simple or no background. Main elements centered or positioned by content needs. 16:9 horizontal aspect ratio optimized for article covers.

---

## Text in Covers (封面文字)

封面文字设计原则:

| 元素 | 指导原则 |
|---------|-----------|
| **大小** | 大而突出，立即可读 |
| **风格** | 手写字体增加温暖感 |
| **内容** | 简洁关键词和核心概念 |
| **语言** | 匹配文章语言 |
| **位置** | 居中或底部，避免遮挡主视觉 |

**添加到有文字的封面prompt**:
> Text should be large and prominent with clear typography. Keep minimal - article title or key phrase only. Position to avoid obscuring main visual element.

**封面文字建议**:
- 仅包含文章标题或核心关键词
- 避免长段落或详细说明
- 使用简洁有力的短语
- 考虑中英文双语效果

---

## Cover Prompt Principles (封面Prompt原则)

优秀封面prompt必须包含:

1. **构图结构优先**: 描述布局、区域、流向
2. **核心元素**: 主体视觉元素描述
3. **色彩方案**: 风格定义的调色板
4. **风格特征**: 线条处理、纹理、情绪
5. **宽高比**: 16:9横向格式
6. **尺寸**: 1280x720像素

---

## Type-Specific Cover Templates (类型特定封面模板)

### Infographic Cover

```yaml
---
cover_id: 01
type: infographic
style: vector-illustration
aspect_ratio: "16:9"
---

[Article Title] - Infographic Cover

LAYOUT: Horizontal 16:9, infographic style

FOCAL ELEMENT: [main icon/illustration representing topic]
BACKGROUND: Cream off-white (#F5F0E6) with subtle texture

COLORS (from vector-illustration palette):
- Background: Cream Off-White (#F5F0E6)
- Primary accent: Coral Red (#E07A5F)
- Secondary: Mint Green (#81B29A)
- Highlights: Mustard Yellow (#F2CC8F)
- Outlines: Deep Charcoal (#2D2D2D)

STYLE ELEMENTS:
- Flat vector illustration with clean black outlines
- Geometric simplification
- Playful decorative elements (dots, stars, simple shapes)
- Retro soft colors, no gradients

TEXT (if included):
- Main: "[Article Title or Key Phrase]"
- Position: Centered or lower third
- Style: Large, bold, clear typography
- Color: Black or primary accent

COMPOSITION:
- Clean horizontal layout optimized for 16:9
- Generous white space around main element
- Centered focal point
- Minimal decorative accents

ASPECT: 16:9 horizontal (1280x720px)
```

### Scene Cover

```yaml
---
cover_id: 01
type: scene
style: warm
aspect_ratio: "16:9"
---

[Article Title] - Atmospheric Scene Cover

LAYOUT: Horizontal 16:9, scene style

FOCAL POINT: [main subject/scene element]
ATMOSPHERE: [lighting, mood description]
MOOD: [emotion to convey]
COLOR TEMPERATURE: Warm/Golden hour

COLORS (from warm palette):
- Background: Cream (#FFFAF0) or Soft Peach (#FED7AA)
- Primary: Warm Orange (#ED8936)
- Secondary: Golden Yellow (#F6AD55)
- Accents: Terracotta (#C05621), Deep Brown (#744210)

STYLE ELEMENTS:
- Soft rounded shapes and friendly aesthetics
- Golden hour lighting effects
- Gentle gradients with warmth
- Soft shadows without harsh edges
- Hand-drawn quality touches

TEXT (if included):
- Main: "[Article Title]"
- Position: Lower third or overlaid on subtle area
- Style: Warm, approachable typography

ASPECT: 16:9 horizontal (1280x720px)
```

### Blueprint Cover

```yaml
---
cover_id: 01
type: infographic
style: blueprint
aspect_ratio: "16:9"
---

[Article Title] - Technical Blueprint Cover

LAYOUT: Horizontal 16:9, technical schematic

FOCAL ELEMENT: [technical diagram/system representation]
BACKGROUND: Blue (#1E3A5F) with grid pattern

COLORS (from blueprint palette):
- Background: Deep Blue (#1E3A5F)
- Grid lines: Light Blue (#4A7BA7)
- Elements: White (#FFFFFF) or Cyan (#64B5F6)
- Accents: Orange (#FF9800) for highlights

STYLE ELEMENTS:
- Technical precision, schematic lines
- Grid-based layout
- Monospace labels, technical aesthetic
- Clean geometric shapes
- High contrast for readability

TEXT (if included):
- Main: "[Article Title]"
- Style: Monospace or technical sans-serif
- Color: White or cyan for visibility

ASPECT: 16:9 horizontal (1280x720px)
```

### Minimal Cover

```yaml
---
cover_id: 01
type: infographic
style: minimal
aspect_ratio: "16:9"
---

[Article Title] - Minimal Cover

LAYOUT: Horizontal 16:9, ultra-minimal

FOCAL ELEMENT: [single simple geometric representation]
BACKGROUND: Pure White (#FFFFFF) or Off-White (#FAFAFA)

COLORS (from minimal palette):
- Background: White (#FFFFFF)
- Primary: Pure Black (#000000)
- Accent: [Single content-derived color, sparing use]

STYLE ELEMENTS:
- Single focal element per cover
- Maximum negative space
- Thin, precise lines
- Simple geometric forms
- Subtle shadows if any
- Clean, uncluttered compositions

TEXT (if included):
- Main: "[Article Title]"
- Style: Clean, bold sans-serif
- Position: Centered or bottom-aligned
- Color: Black

ASPECT: 16:9 horizontal (1280x720px)
```

---

## Variation Prompts (变体Prompt)

第二张封面应该是第一张的设计变体:

```yaml
---
cover_id: 02
type: [same as 01]
style: [same as 01]
aspect_ratio: "16:9"
variation: true
---

[Article Title] - Alternative Design

VARIATION from Cover 01:
- [Composition change: e.g., from centered to split layout]
- [Color emphasis: e.g., different accent color dominance]
- [Element rearrangement: e.g., different focal treatment]
- [Alternative perspective or angle]

[Rest follows the base template structure...]

ASPECT: 16:9 horizontal (1280x720px)
```

**变体策略**:

| 方面 | 变体选项 |
|------|----------|
| 构图 | 居中 → 左右分割 / 顶部偏重 / 全幅背景 |
| 色彩 | 主色调变化 / 对比色强调 |
| 元素 | 不同图标表现 / 抽象程度变化 |
| 文字位置 | 居中 → 底部 / 顶部 / 覆盖 |

---

## What to Avoid (需要避免的)

- 模糊描述 ("a nice cover image")
- 过度复杂的设计 ("include everything related to topic")
- 过多文字细节
- 通用装饰元素
- 忽略16:9比例要求
- 与风格定义不匹配的颜色/元素

---

## Watermark Integration (水印集成)

如果EXTEND.md中启用水印，追加到prompt:

```
Include a subtle watermark "[content]" positioned at [position] with approximately [opacity*100]% visibility. Watermark should not interfere with main visual elements.
```

---

## Cover-Specific Enhancements (封面专用增强)

### 添加视觉冲击力

```
VISUAL IMPACT:
- Strong focal point that stands out in a feed
- High contrast for visibility at small sizes
- Bold color choices from style palette
- Clear visual hierarchy
```

### 优化社交媒体显示

```
SOCIAL MEDIA OPTIMIZATION:
- Clear and readable at small sizes (thumbnail preview)
- Strong visual hook for scrolling feed
- Minimal text that remains legible when compressed
- Avoid thin details that may blur at small sizes
```

---

## Example Complete Cover Prompt

```yaml
---
cover_id: 01
type: infographic
style: vector-illustration
aspect_ratio: "16:9"
size: "1280x720"
---

AI工具全攻略 - Vector Illustration Cover

LAYOUT: Horizontal 16:9, infographic style with centered focal element

FOCAL ELEMENT: Stylized AI brain/chip icon combining organic and tech elements
BACKGROUND: Cream off-white (#F5F0E6) with subtle paper texture

COLORS (from vector-illustration palette):
- Background: Cream Off-White (#F5F0E6)
- Outlines: Deep Charcoal (#2D2D2D)
- Primary accent: Coral Red (#E07A5F) for main shapes
- Secondary: Mint Green (#81B29A) for supporting elements
- Highlights: Mustard Yellow (#F2CC8F) for energy
- Touches: Burnt Orange (#D4764A), Rock Blue (#577590)

STYLE ELEMENTS:
- Flat vector illustration with uniform black outlines
- Geometric simplification - circuits as clean lines, neurons as dots
- Retro toy model aesthetic, cute and approachable
- No gradients or 3D effects
- Playful accents: small stars, plus signs, simple geometric shapes
- Closed outlines like coloring book style

TEXT:
- Main: "AI工具全攻略"
- Position: Lower third, centered
- Style: Bold sans-serif, large and clear
- Color: Black (#1A1A1A)

COMPOSITION:
- Clean horizontal 16:9 layout
- Main AI icon centered in upper two-thirds
- Generous white space around focal element
- Text centered in lower third
- Minimal decorative accents (dots, plus signs) for energy

VISUAL IMPACT:
- Strong focal point that stands out in feed
- High contrast between coral/mint elements and cream background
- Bold, approachable aesthetic
- Clear at small sizes for thumbnail preview

ASPECT: 16:9 horizontal (1280x720px)
```
