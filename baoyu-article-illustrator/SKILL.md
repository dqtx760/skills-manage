---
name: baoyu-article-illustrator
description: Analyzes article structure, identifies positions requiring visual aids, generates illustrations with Type × Style two-dimension approach. Use when user asks to "illustrate article", "add images", "generate images for article", or "为文章配图".
---

# Article Illustrator

Analyze articles, identify illustration positions, generate images with Type × Style consistency.

## Two Dimensions

| Dimension | Controls | Examples |
|-----------|----------|----------|
| **Type** | Information structure | infographic, scene, flowchart, comparison, framework, timeline |
| **Style** | Visual aesthetics | notion, warm, minimal, blueprint, watercolor, elegant |

Combine freely: `--type infographic --style blueprint`

## Types

| Type | Best For |
|------|----------|
| `infographic` | Data, metrics, technical |
| `scene` | Narratives, emotional |
| `flowchart` | Processes, workflows |
| `comparison` | Side-by-side, options |
| `framework` | Models, architecture |
| `timeline` | History, evolution |

## Styles

See [references/styles.md](references/styles.md) for Core Styles, full gallery, and Type × Style compatibility.

## Workflow

```
- [ ] Step 1: Pre-check (EXTEND.md, references, config)
- [ ] Step 2: Analyze content
- [ ] Step 3: Confirm settings (AskUserQuestion)
- [ ] Step 4: Generate images
- [ ] Step 5: Finalize
```

### Step 1: Pre-check

**1.5 Load Preferences (EXTEND.md) ⛔ BLOCKING**

```bash
test -f .claude/skills/baoyu-article-illustrator/EXTEND.md && echo "project"
test -f "$HOME/.claude/skills/baoyu-article-illustrator/EXTEND.md" && echo "user"
```

| Result | Action |
|--------|--------|
| Found | Read, parse, display summary |
| Not found | ⛔ Run [first-time-setup](references/config/first-time-setup.md) |

Full procedures: [references/workflow.md](references/workflow.md#step-1-pre-check)

### Step 2: Analyze

| Analysis | Output |
|----------|--------|
| Content type | Technical / Tutorial / Methodology / Narrative |
| Purpose | information / visualization / imagination |
| Core arguments | 2-5 main points |
| Positions | Where illustrations add value |

**CRITICAL**: Metaphors → visualize underlying concept, NOT literal image.

Full procedures: [references/workflow.md](references/workflow.md#step-2-setup--analyze)

### Step 3: Confirm Settings ⚠️

**ONE AskUserQuestion, max 4 Qs. Q1-Q3 REQUIRED.**

| Q | Options |
|---|---------|
| **Q1: Type** | [Recommended], infographic, scene, flowchart, comparison, framework, timeline, mixed |
| **Q2: Density** | minimal (1-2), balanced (3-5), per-section (Recommended), rich (6+) |
| **Q3: Style** | [Recommended], minimal-flat, sci-fi, hand-drawn, editorial, scene, Other |
| Q4: Language | When article language ≠ EXTEND.md setting |

Full procedures: [references/workflow.md](references/workflow.md#step-3-confirm-settings-)

### Step 4: Generate Images

1. Create prompts per [references/prompt-construction.md](references/prompt-construction.md)
2. **Detect available image generation method**:
   - **Method A (Claude Code)**: Use `/image` skill directly
   - **Method B (Other environments)**: Use Python script directly
3. Process references (`direct`/`style`/`palette`)
4. Apply watermark if EXTEND.md enabled
5. Generate sequentially
6. Retry once on failure

**Method A - Claude Code (with `/image` skill)**:
```bash
/image "<prompt>" -o illustrations/{topic}/01-{type}-{slug}.png
```

**Method B - Direct Python call (universal)**:
```bash
cd D:\zhishiku\.claude\skills\image
python scripts/generate_image.py "<prompt>" -o "../output/{filename}"
# Then move/copy to illustrations/{topic}/
```

**Image skill location**: `D:\zhishiku\.claude\skills\image\`
**Script**: `scripts/generate_image.py`

Full procedures: [references/workflow.md](references/workflow.md#step-4-generate-images)

### Step 5: Finalize

Insert `![description](path/NN-{type}-{slug}.png)` after paragraphs.

```
Article Illustration Complete!
Article: [path] | Type: [type] | Density: [level] | Style: [style]
Images: X/N generated
```

### Step 6: Upload to PicList (Optional)

**For Obsidian users with PicList plugin** - 图片已生成到固定目录 `D:\data\images\image`

**User workflow**:
1. 图片自动保存到 `D:\data\images\image`
2. 在 Obsidian 中手动插入图片路径
3. PicList 自动监控并上传该目录
4. 上传后自动替换本地路径为图床 URL

**16:9 横图配置**: 在 EXTEND.md 中设置 `aspect_ratio: "16:9"`

Full procedures: [references/workflow.md](references/workflow.md#step-7-upload-to-piclist-optional)

**For 16:9 format preference**: Add to prompt `16:9 aspect ratio`

Full procedures: [references/workflow.md](references/workflow.md#step-7-upload-to-piclist-optional)

## Output Directory

```
illustrations/{topic-slug}/
├── source-{slug}.{ext}
├── references/           # if provided
├── prompts/
└── NN-{type}-{slug}.png
```

**Slug**: 2-4 words, kebab-case. **Conflict**: append `-YYYYMMDD-HHMMSS`.

## Modification

| Action | Steps |
|--------|-------|
| Edit | Update prompt → Regenerate → Update reference |
| Add | Position → Prompt → Generate → Insert |
| Delete | Delete files → Remove reference |

## Local Environment Configuration

**Image Generation Backend**: `image` skill (ModelScope 通义千问 API)

| Component | Path | Status |
|-----------|-------|--------|
| Image skill | `D:\zhishiku\.claude\skills\image\` | Configured |
| API Config | `image/scripts/config.py` | API Key set |
| Python Script | `image/scripts/generate_image.py` | Available |

### Environment-Specific Usage

| Environment | Method | Command |
|------------|----------|----------|
| **Claude Code** | `/image` skill | `/image "<prompt>" -o <path>` |
| **Claudian/Obsidian** | Python script | `python D:\zhishiku\.claude\skills\image\scripts\generate_image.py "<prompt>" -o <path>` |
| **Other** | Python script | `python <image-skill-path>/scripts/generate_image.py "<prompt>" -o <path>` |

**Note**: In non-Claude Code environments, always use the Python script directly instead of slash commands.

## References

| File | Content |
|------|---------|
| [references/workflow.md](references/workflow.md) | Detailed procedures |
| [references/usage.md](references/usage.md) | Command syntax |
| [references/styles.md](references/styles.md) | Style gallery |
| [references/prompt-construction.md](references/prompt-construction.md) | Prompt templates |
| [references/config/first-time-setup.md](references/config/first-time-setup.md) | First-time setup |
