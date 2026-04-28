[Skills-Link](https://github.com/shanliuling/skills-link) 让所有 AI 编程工具共享同一个 Skills 文件夹。

## 一图读懂

```
┌─────────────────────────────────────────────────────────────────────┐
│                         本地电脑                                    │
│                                                                     │
│   .qwen/skills ──┐                                                 │
│   .claude/skills ──┤     ┌──────────────────┐                       │
│   .codex/skills ──┤     │  AISkills        │◀─── 软链接           │
│   .trae/skills ───┼────▶│  (C:\Users\      │                       │
│   ...            │     │  Administrator\   │                       │
│                   │     │   \AISkills)     │                       │
│                   │     └──────────────────┘                       │
│                              │                                      │
│                              ▼ GitHub                              │
│                   https://github.com/dqtx760/skills-manage         │
└─────────────────────────────────────────────────────────────────────┘
```

**一句话解释**：所有 AI 工具的 Skills 目录都指向同一个地方，修改一次，所有工具都生效。

## 快速开始

### 安装

```bash
npm install -g skills-link
```

### 初始化

```bash
skills-link setup
```

配置文件在 `C:\Users\Administrator\Desktop\config.yaml`，确保 masterDir 指向中央仓库：

```yaml
masterDir: C:\Users\Administrator\AISkills
```

### 添加 Skills 两步走

1. **导入**：运行 `skills-link`，扫描中央仓库，发现新 skills
2. **创建链接**：运行 `skills-link`，选择"创建链接"，各 Agent 才能看到

### 推送到 GitHub

```bash
# 方式1：双击运行
C:\Users\Administrator\AISkills\push.bat

# 方式2：命令行
cd C:\Users\Administrator\AISkills
git add . && git commit -m "更新" && git push
```

## 支持的 Agent（41+ 个）

| 分类 | 包含的 Agent |
|------|-------------|
| 主流 IDE/工具 | Claude Code, Cursor, Windsurf, Cline, Trae, Trae CN, Gemini CLI, Roo Code |
| 国内工具 | Qwen Code, Kimi Code CLI, Kiro CLI, Junie, iFlow CLI |
| 海外工具 | GitHub Copilot, Continue, Replit, Goose, OpenCode, OpenHands |
| 其他 | AdaL, Amp, Antigravity, Augment, CodeBuddy, Codex, Command Code, Cortex Code, Crush, Droid, Kilo Code, Kode, MCPJam, Mistral Vibe, Mux, Neovate, OpenClaw, Pi, Pochi, Qoder, Zencoder |

## 核心命令

| 命令 | 作用 |
|------|------|
| `skills-link` | 交互式菜单 |
| `skills-link list` | 查看已安装的 Skills |
| `skills-link health` | 检查软链接状态 |
| `skills-link sync` | 推送到 GitHub |

## Skills 分类

| 分类 | Skills |
|------|--------|
| **内容创作/** | 5 个 (ai-writing-assistant, article-review, content-rewriting-2601, x-mastery-mentor, 爆款文案生成器) |
| **前端UI设计/** | 5 个 (awesome-design-md, frontend-design, skill-site-generator, ui-ux-pro-max-skill, website-audit) |
| **生图/** | 3 个 (article-cover-gen, baoyu-article-illustrator, ljg-card) |
| **网络搜索/** | 3 个 (agent-reach, web-access, web-scraper) |
| **ppt生成/** | 4 个 (frontend-slides, guizang-ppt-skill, huashu-design, ian-handdrawn-ppt) |
| **lark/** | 21 个飞书相关 (lark-approval, lark-base, lark-calendar, lark-contact, lark-doc, lark-drive, lark-event, lark-im, lark-mail, lark-mcp, lark-minutes, lark-openapi-explorer, lark-shared, lark-sheets, lark-skill-maker, lark-task, lark-vc, lark-whiteboard, lark-wiki, lark-workflow-meeting-summary, lark-workflow-standup-report) |
| **mem/** | 5 个记忆相关 (mem-file-scan, mem-monthly, mem-query, mem-record, mem-weekly) |
| **obsidian/** | 5 个 Obsidian 相关 (excalidraw-diagram, mermaid-visualizer, obsidian-bases, obsidian-canvas-creator, obsidian-markdown) |
| **prompt/** | 5 个提示词相关 (prompt-analyzer, prompt-extractor, prompt-generator, prompt-master, prompt-xray) |
| **person-skill/** | 16 个人物技能 (elon-musk-skill, feynman-skill, guizang-ppt-skill, ilya-sutskever-skill, karpathy-skill, mrbeast-skill, munger-skill, naval-skill, nuwa-skill, paul-graham-skill, steve-jobs-skill, taleb-skill, trump-skill, x-mentor-skill, yourself-skill, zhang-yiming-skill, zhangxuefeng-skill) |
| **perspective/** | 14 个人物视角 (andrej-karpathy-perspective, elon-musk-perspective, feynman-perspective, ilya-sutskever-perspective, mrbeast-perspective, munger-perspective, naval-perspective, paul-graham-perspective, steve-jobs-perspective, sun-yuchen-perspective, taleb-perspective, trump-perspective, zhang-yiming-perspective, zhangxuefeng-perspective) |
| **content/** | 2 个内容相关 (content-digest, content-topic-generator) |
| **design/** | 2 个设计相关 (canvas-design, design-master) |
| **web/** | 2 个网页相关 (web-article-translator, web-artifacts-builder) |
| **topic/** | 4 个主题相关 (topic-agent, topic-collector, topic-generator, topic-reviewer) |
| **redbook/** | 4 个小红书相关 (Auto-Redbook-Skills, png-xiaohongshu, xiaohongshu-cli, xiaohongshu-converter) |
| **office/** | 3 个文档相关 (docx, pdf, xlsx) |
| **frontend/** | 2 个前端相关 (frontend-design, frontend-slides) |
| **media/** | 3 个媒体相关 (text-to-speech, video-master, youtube-transcript-cn) |

**提示**：Agent 调用 Skills 时直接使用 skill 名称，无需关心所在分类目录。

## 常见问题

### Q1：安装 skill 后其他 Agent 看不到？

需要两步：
1. 运行 `skills-link` → 选择"导入"
2. 运行 `skills-link` → 选择"创建链接"

### Q2：删除 skill 怎么操作？

1. 删除 `AISkills` 里的内容
2. 执行 `push.bat` 推送

**注意**：不要从 Agent 目录删除，只删了链接，源文件还在。

### Q3：另一台电脑怎么同步？

```bash
# 1. 克隆仓库
git clone https://github.com/dqtx760/skills-manage C:\Users\Administrator\AISkills

# 2. 创建链接
skills-link
```

## 详细文档

更完整的使用说明：[一款让41+AI工具共享Skills的神器](../AIHacks/skills-link.md)

---

**有问题？扫码加微信**

![weix2.webp](https://gitee.com/da-qiang-classmate/typora/raw/master/image/weix2.webp)
