[Skills-Link](https://github.com/shanliuling/skills-link) 让所有 AI 编程工具共享同一个 Skills 文件夹。

## 一图读懂

```
┌─────────────────────────────────────────────────────────────────────┐
│                         本地电脑                                    │
│                                                                     │
│   .qwen/skills ──┐                                                 │
│   .claude/skills ──┤     ┌──────────────────┐                       │
│   .codex/skills ──┤     │  .skillshub      │◀─── 软链接           │
│   .trae/skills ───┼────▶│  (D:\project2026 │                       │
│   ...            │     │   \skills-manage)│                       │
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

配置文件在 `C:\Users\Administrator\config.yaml`，确保 masterDir 指向软链接：

```yaml
masterDir: C:\Users\Administrator\.skillshub
```

### 添加 Skills 两步走

1. **导入**：运行 `skills-link`，扫描中央仓库，发现新 skills
2. **创建链接**：运行 `skills-link`，选择"创建链接"，各 Agent 才能看到

### 推送到 GitHub

```bash
# 方式1：双击运行
D:\project2026\skills-manage\push.bat

# 方式2：命令行
cd C:\Users\Administrator\.skillshub
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

## 常见问题

### Q1：安装 skill 后其他 Agent 看不到？

需要两步：
1. 运行 `skills-link` → 选择"导入"
2. 运行 `skills-link` → 选择"创建链接"

### Q2：删除 skill 怎么操作？

1. 删除 `.skillshub` 里的内容
2. 执行 `push.bat` 推送

**注意**：不要从 Agent 目录删除，只删了链接，源文件还在。

### Q3：另一台电脑怎么同步？

```bash
# 1. 克隆仓库
git clone https://github.com/dqtx760/skills-manage C:\Users\Administrator\.skillshub

# 2. 创建链接
skills-link
```

## 详细文档

更完整的使用说明：[一款让41+AI工具共享Skills的神器](../AIHacks/skills-link.md)

---

**有问题？扫码加微信**

![weix2.webp](https://gitee.com/da-qiang-classmate/typora/raw/master/image/weix2.webp)
