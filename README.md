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
| Qwen Code   | C:\Users\Administrator.qwen\skills    |
| Claude Code | C:\Users\Administrator.claude\skills  |
| Codex       | C:\Users\Administrator.codex\skills   |
| Trae        | C:\Users\Administrator.trae\skills    |
| Trae CN     | C:\Users\Administrator.trae-cn\skills |
| Gemini CLI  | C:\Users\Administrator.gemini\skills  |
| iFlow CLI   | C:\Users\Administrator.iflow\skills   |

## 详细文档

更完整的使用说明：[点此查看](https://www.dqtx.cc/posts/aihacks/skills-link/)

---

**有问题？扫码加微信**

![weix2.webp](https://gitee.com/da-qiang-classmate/typora/raw/master/image/weix2.webp)
