# AISkills - AI Skills 中央仓库

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
npm i -g skills-link
```

### 初始化

```bash
skills-link
```

配置文件，确保 masterDir 指向中央仓库：

```yaml
C:\Users\Administrator\AISkills\config.yaml
```

### 推送到 GitHub

```bash
skills-link sync
```

## Agent Skills 目录

> 以下目录中的 skills 都是指向中央仓储的符号链接

| Agent       | Skills 目录                           |
| ----------- | ------------------------------------- |
| Claude Code | `C:\Users\Administrator\.claude\skills`  |
| Qwen Code   | `C:\Users\Administrator\.qwen\skills`    |
| Codex       | `C:\Users\Administrator\.codex\skills`   |
| Trae        | `C:\Users\Administrator\.trae\skills`    |
| Trae CN     | `C:\Users\Administrator\.trae-cn\skills` |
| Gemini CLI  | `C:\Users\Administrator\.gemini\skills`  |
| iFlow CLI   | `C:\Users\Administrator\.iflow\skills`   |

---

## Skills 总览（共 56 个）

调用方式：`/skill-name` 斜杠命令，或自然语言触发（见"触发方式"列）。

### PPT / 幻灯片

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/frontend-slides` | zarazhangrui | 从零创建或转换 PPT 为动画丰富的 HTML 幻灯片 | "做个PPT"、"转成网页幻灯片"、"presentation" |
| `/guizang-ppt-skill` | op7418 | 电子杂志 × 电子墨水风格横向翻页 PPT（单 HTML） | "杂志风PPT"、"horizontal swipe deck"、"editorial magazine" |
| `/huashu-design` | alchaincyf | 花叔Design：HTML 高保真原型、交互Demo、动画、设计评审 | "做原型"、"交互原型"、"HTML演示"、"app原型" |
| `/ian-handdrawn-ppt` | helloianneo | 手绘风技术文章/PPT 页面图片 | "手绘风PPT"、"课件"、"手绘配图" |

### 前端 / UI 设计

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/frontend-design` | anthropics | 去"AI味"，统一排版，生成高质量前端界面 | "做个网页"、"landing page"、"设计一个UI" |
| `/impeccable` | pbakaus | 前端设计全栈优化：UX评审、视觉层级、动效、排版、无障碍 | "优化设计"、"review UI"、"排版"、"调色"、"polish" |
| `/awesome-design-md` | VoltAgent | 复刻大厂 UI 设计参考库 | 查阅式 skill，提供设计灵感 |
| `/website-audit` | MarcinKilarski | 网站审计：可访问性、性能、SEO 分析 | "审计网站"、"website audit" |

### 写作 / 内容创作

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/ai-writing-assistant` | — | 社交媒体写作助手，6种结构化写作方法 | "帮我写文案"、"社交媒体内容" |
| `/content-rewriting-2601` | — | 内容改写/扩写，分层风格、人性化叙事 | "改写这篇文章"、"扩写"、"润色" |
| `/TopTier Creator` | — | 爆款文案生成器，公众号/短视频/朋友圈全场景 | "爆款文案"、"写个爆款" |
| `/wewrite` | oaker-io | 微信公众号全流程：热点→选题→框架→写作→排版→推草稿箱 | "公众号"、"推文"、"写一篇公众号" |
| `/writing-assistant-skill` | Ceeon | 自媒体写作交互助手，选题到发布全流程 | "写文章"、"检查草稿"、"诊断数据" |
| `/talk-normal` | hexiecs | 去 AI 味：精简冗余、去除套话，保留信息量 | "去掉AI味"、"说人话"、"精简" |

### 文章配图 / 视觉卡片

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/baoyu-article-illustrator` | JimLiu | 文章配图：分析结构、自动生成插图 | "为文章配图"、"illustrate article" |
| `/ljg-card` | lijigang | 内容铸造：6种视觉卡片模板（长图/信息图/漫画/白板等） | "铸"、"做成图"、"做成卡片"、"sketchnote"、"漫画" |
| `/image` | — | 通义千问 AI 生图 | "/image"、"生成一张...的图片"、"画一个..." |

### 图表 / 可视化

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/excalidraw-diagram` | — | 生成 Excalidraw 流程图/思维导图（支持动画模式） | "画图"、"流程图"、"思维导图"、"Excalidraw" |
| `/mermaid-visualizer` | — | 文本转 Mermaid 专业图表 | "画个图"、"可视化"、"mermaid" |

### Obsidian

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/obsidian-bases` | kepano | 创建/编辑 Obsidian Bases 数据库视图 | ".base文件"、"数据库视图"、"Bases" |
| `/obsidian-canvas-creator` | — | 文本转 Obsidian Canvas 思维导图/自由画布 | "Canvas"、"思维导图"、"画布" |
| `/axton-obsidian-visual-skills` | axtonliu | Obsidian 可视化工具集合 | 查阅式 skill |

### 网络 / 搜索

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/web-access` | eze-is | 联网操作总入口：搜索、抓取、登录操作、社交平台 | "搜索"、"看下这个网页"、"抓取小红书" |
| `/web-scraper` | — | 网页转 Markdown，提取文章内容 | "抓取网页"、"提取文章"、"fetch URL" |
| `/agent-reach` | Panniantong | 跨14个平台搜索：X、Reddit、YouTube、GitHub、小红书、抖音等 | "搜一下"、"跨平台搜索"、"search X" |

### 大佬思维框架（Perspective 系列）

| Skill | 说明 |
|-------|------|
| `/paul-graham-perspective` | Paul Graham（YC 创始人）：200+ essays 蒸馏 |
| `/steve-jobs-perspective` | Steve Jobs：产品哲学、极简主义 |
| `/elon-musk-perspective` | 马斯克：第一性原理、5个心智模型 |
| `/naval-perspective` | Naval Ravikant：财富、幸福、杠杆思维 |
| `/munger-perspective` | 查理·芒格：多元思维模型 |
| `/taleb-perspective` | 塔勒布：反脆弱、黑天鹅 |
| `/feynman-perspective` | 费曼：学习法、物理学思维 |
| `/andrej-karpathy-perspective` | Karpathy：AI/深度学习视角 |
| `/ilya-sutskever-perspective` | Ilya Sutskever：AGI 前沿思考 |
| `/mrbeast-perspective` | MrBeast：内容创造操作系统 |
| `/trump-perspective` | 特朗普：行为逻辑与决策模式 |
| `/sun-yuchen-perspective` | 孙宇晨：6维度行为逻辑蒸馏 |
| `/zhang-yiming-perspective` | 张一鸣：字节跳动方法论 |
| `/zhangxuefeng-perspective` | 张雪峰：教育/职业规划视角 |

> 用法：`/paul-graham-perspective 你怎么看创业？` 或 "用芒格的思维分析这个问题"

### Skill 管理

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/skill-creator` | anthropics | 创建、编辑、优化 skill | "创建一个skill"、"帮我做个skill" |
| `/skill-site-generator` | eze-is | 为 skill 生成官网并部署 | "给skill做个官网"、"landing page" |
| `/find-skills` | vercel-labs | 发现和推荐可安装的 skill | "有什么skill可以..."、"找一个能做X的skill" |
| `/nuwa-skill` | alchaincyf | 女娲造人：输入人名→深度调研→生成人物 Skill | "造skill"、"蒸馏XX" |

### 项目规划 / 执行

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/planning-with-files-zh` | OthmanAdi | Manus 风格文件规划：task_plan.md / findings.md / progress.md | "帮我规划"、"拆解项目"、"制定计划" |
| `/make-plan` | — | 创建分阶段实施计划 | "做个计划"、"plan this feature" |
| `/do` | — | 执行分阶段计划（配合 make-plan） | "执行这个计划"、"run the plan" |
| `/pathfinder` | — | 代码库架构映射、发现重复、统一架构 | "审计架构"、"find the ideal path" |
| `/advisory-board` | Backtthefuture | 私董会：12位顶级思想家决策智囊团 | "开私董会"、"请智囊团"、"帮我决策" |

### 记忆 / 学习

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/claude-mem` | thedotmack | 跨会话持久化记忆 | "记住这个"、"上次我们做了什么" |
| `/mem-search` | — | 搜索跨会话记忆数据库 | "我们之前怎么解决的？"、"did we already solve this?" |
| `/knowledge-agent` | — | 从记忆构建知识库 | "建一个知识库"、"整理我们的经验" |
| `/self-improving-agent` | peterskoett | 自动纠错记录：从错误中学习 | 自动触发（出错/纠正时记录） |

### AI 协作

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/ai-pair` | axtonliu | 多 Agent 协调：一个创建，两个评审（Codex + Gemini） | "多模型协作"、"AI pair" |

### 社交媒体

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/x-mastery-mentor` | alchaincyf | X/Twitter 运营导师：6位顶级创作者方法论 + 算法分析 | "X运营"、"Twitter策略"、"涨粉" |

### 开发工具

| Skill | 来源 | 说明 | 触发方式 |
|-------|------|------|----------|
| `/smart-explore` | — | tree-sitter AST 结构化代码搜索，省 token | "看看代码结构"、"找某个函数" |
| `/version-bump` | — | 自动语义化版本发布：npm publish + git tag + changelog | "发个版本"、"release" |
| `/timeline-report` | — | 从记忆生成项目开发历程报告 | "项目时间线"、"development journey" |

---

## 调用方式总结

| 方式 | 示例 |
|------|------|
| **斜杠命令** | `/ljg-card`、`/huashu-design`、`/image 画一只猫` |
| **自然语言** | "帮我做个PPT"、"生成一张图"、"去掉AI味"、"用芒格思维分析" |

大部分 skill 都支持自然语言触发，系统会根据 SKILL.md 中的 description 自动匹配。

## 详细文档

更完整的使用说明：[点此查看](https://www.dqtx.cc/posts/aihacks/skills-link/)
