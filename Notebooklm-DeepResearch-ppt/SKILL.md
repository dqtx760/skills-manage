---
name: Notebooklm-DeepResearch-ppt
description: |
  使用 NotebookLM 对指定主题进行 Web 深度研究，导出引用文献全文为 Markdown，
  并生成中文 3D 风格演示文稿（PPT）到桌面。
  触发词：深度研究、Deep Research、notebooklm 研究、研究 PPT、生成研究幻灯片。
  用户说"帮我研究 XXX 做个 PPT"、"对 XXX 做深度研究"、"notebooklm 研究一下 XXX"时触发。
version: 1.0.0
---

# NotebookLM 深度研究 + PPT 生成

## 触发条件

- 用户输入「/Notebooklm-DeepResearch-ppt <研究主题>」
- 用户说「帮我深度研究 XXX 做个 PPT」
- 用户说「对 XXX 做 deep research，生成演示文稿」

## 前置条件

- 已安装 `notebooklm-py`（`pip install notebooklm-py`）
- 已完成 NotebookLM 登录（`python -m notebooklm login`，浏览器登录 Google 后按回车）
- 如登录过期，先执行 `python -m notebooklm login`，再继续

## 执行流程

### Step 1：登录验证

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm list
```

- 如果报 `Authentication expired`，提示用户执行 `python -m notebooklm login` 并等待完成
- 如果正常列出笔记本，继续 Step 2

### Step 2：创建笔记本

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm create "<研究主题> 深度研究"
```

记录返回的 notebook ID。

### Step 3：设置当前笔记本

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm use <notebook_id>
```

### Step 4：启动深度研究

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm source add-research "<研究主题> comprehensive analysis, comparison, features, pricing, user experience, pros and cons"
```

### Step 5：等待研究完成并导入信源

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm research wait --import-all
```

注意：可能因超时自动重试，最终会显示 `Imported N sources`。

### Step 6：列出信源，选取唯一信源

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm source list
```

研究导入可能产生重复信源（同一页面多次出现）。从每个唯一标题中选取一个 ID（优先选最早创建的）。

### Step 7：导出引用文献全文

为每个唯一信源执行：

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm source fulltext <source_id>
```

将全文保存为 Markdown 文件：

- **目录**：`01-输入/Notebooklm/<研究主题>/`
- **文件名**：用信源标题命名，去掉特殊字符，如 `Claude Code Pricing 2026.md`
- **格式**：

```markdown
# <信源标题>

<全文内容>
```

目录不存在则自动创建。

### Step 8：生成中文演示文稿

使用 3D 风格提示词生成 Slide Deck：

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm generate slide-deck "<3D风格提示词，见下方>"
```

**3D 风格 PPT 提示词模板**：

```
创建一份中文演示文稿，基于笔记本中的所有信源内容，全面分析 <研究主题>。

要求：
1. 使用简体中文
2. 内容全面：概述、核心功能/特点、对比分析、使用场景、优缺点、推荐建议
3. 数据驱动：引用信源中的具体数据和案例
4. 结构清晰：封面 → 目录 → 各章节 → 总结

视觉风格要求：
你是一位专家级UI UX演示设计师，请生成高保真、未来科技感的16比9演示文稿幻灯片。
全局视觉语言：融合Apple Keynote极简主义、现代SaaS产品设计和玻璃拟态风格。
配色：深邃虚空黑基底，霓虹紫、电光蓝、柔和珊瑚橙、青色作为高光点缀。
排版：Bento便当盒网格系统，磨砂玻璃材质容器，巨大内部留白。
3D元素：礼物质感3D物体作为视觉锚点，抛光金属、幻彩亚克力、透明玻璃材质。
字体：干净无衬线字体，高对比度。
渲染质量：虚幻引擎5渲染，8k分辨率，超细节纹理。
```

### Step 9：等待生成并下载

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm artifact wait <artifact_id> --timeout 600
```

下载到桌面：

```bash
PYTHONIOENCODING=utf-8 python -m notebooklm download slide-deck --artifact <artifact_id> --format pptx "C:/Users/Administrator/Desktop/<研究主题> 研究报告.pptx"
```

### Step 10：汇报结果

向用户展示：

1. NotebookLM 笔记本链接
2. 导出的文献清单（文件名 + 来源 URL）
3. PPT 文件路径和大小

## 输出目录结构

```
01-输入/Notebooklm/
└── <研究主题>/
    ├── 信源1.md
    ├── 信源2.md
    └── ...

桌面/
└── <研究主题> 研究报告.pptx
```

## 注意事项

- 所有 notebooklm-py 命令必须加 `PYTHONIOENCODING=utf-8` 前缀（Windows GBK 编码兼容）
- `research wait --import-all` 可能超时重试，耐心等待直到显示 `Imported N sources`
- `artifact wait` 超时后用 `artifact poll` 检查状态，可多次重试
- 重复信源需要去重：同一标题只保留一个 ID
- 如用户未指定主题，先询问研究方向
- 每个步骤完成后向用户汇报进度
