
[Skills-Link](https://github.com/shanliuling/skills-link/blob/main/README.zh.md)让所有 AI 编程工具共享同一个 skills 文件夹的工具。通过符号链接机制，新增或编辑一个 skill，所有 41+ 个 AI 应用立即可见。

## 工作原理
```
  Claude Code ──┐
  Cursor ───────┤
  Windsurf ─────┤
  Cline ────────┼──▶  ~/AISkills/  ◀──▶  GitHub
  Gemini CLI ───┤        ▲
  Trae ─────────┤        │
  Roo Code ─────┘   Master 目录
                    (唯一数据源)
```

每个应用的 `~/.xxx/skills` 变成指向同一个 Master 目录的符号链接。新增或编辑一个 skill，所有应用立即可见。

## 支持的 Agent（41+ 个）

| 分类 | 包含的 Agent |
|------|-------------|
| 主流 IDE/工具 | Claude Code, Cursor, Windsurf, Cline, Trae, Trae CN, Gemini CLI, Roo Code |
| 国内工具 | Qwen Code, Kimi Code CLI, Kiro CLI, Junie, iFlow CLI |
| 海外工具 | GitHub Copilot, Continue, Replit, Goose, OpenCode, OpenHands |
| 其他 | AdaL, Amp, Antigravity, Augment, CodeBuddy, Codex, Command Code, Cortex Code, Crush, Droid, Kilo Code, Kode, MCPJam, Mistral Vibe, Mux, Neovate, OpenClaw, Pi, Pochi, Qoder, Zencoder |

另有 `universal` 通用回退，适用于未列出的 agent。


## 安装

```bash
npm i -g skills-link
```

## 核心命令

- `skills-link`：交互式启动 — 导入、链接、同步
- `skills-link list`：列出本地 skills
- `skills-link sync`：提交并推送到 GitHub
- `skills-link watch`：文件变更时自动同步
- `skills-link health`：检查符号链接状态

## 我的 Skills 架构

### 中央仓储（Master 目录）

> 所有 Agent 的 skills 目录都通过符号链接指向这里

**`C:\Users\Administrator\.skillshub\`** ←→ **GitHub 仓库**

- 本地路径：`C:\Users\Administrator\.skillshub\`（符号链接 → GitHub 仓库）
- GitHub：`https://github.com/dqtx760/skills-manage`

**现在中央仓储就是 GitHub 仓库，给任何 Agent 安装 skill 都会同步到这里！**

### Agent Skills 目录映射

> 以下目录中的 skills 都是指向中央仓储的符号链接

| Agent          | Skills 目录                                  |
| -------------- | ------------------------------------------ |
| Qwen Code      | C:\Users\Administrator\.qwen\skills        |
| Claude Code    | C:\Users\Administrator\.claude\skills      |
| Codex          | C:\Users\Administrator\.codex\skills       |
| Trae           | C:\Users\Administrator\.trae\skills        |
| Trae CN        | C:\Users\Administrator\.trae-cn\skills     |
| Gemini CLI     | C:\Users\Administrator\.gemini\skills      |
| Roo Code       | C:\Users\Administrator\.roo\skills         |
| Continue       | C:\Users\Administrator\.continue\skills    |
| OpenHands      | C:\Users\Administrator\.openhands\skills   |
| Kiro CLI       | C:\Users\Administrator\.kiro\skills        |
| Junie          | C:\Users\Administrator\.junie\skills       |
| Kilo Code CLI  | C:\Users\Administrator\.kilocode\skills    |
| Kode           | C:\Users\Administrator\.kode\skills        |
| Zencoder       | C:\Users\Administrator\.zencoder\skills    |
| Neovate        | C:\Users\Administrator\.neovate\skills     |
| Mux            | C:\Users\Administrator\.mux\skills         |
| Pochi          | C:\Users\Administrator\.pochi\skills       |
| CodeBuddy      | C:\Users\Administrator\.codebuddy\skills   |
| Command Code   | C:\Users\Administrator\.commandcode\skills |
| Augment        | C:\Users\Administrator\.augment\skills     |
| IBM Bob        | C:\Users\Administrator\.bob\skills         |
| MCPJam         | C:\Users\Administrator\.mcpjam\skills      |
| iFlow CLI      | C:\Users\Administrator\.iflow\skills       |
| Universal (通用) | C:\Users\Administrator\.agents\skills      |

### 现有 Skills（共 67 个）

> 📋 详细 Skill 列表和使用说明：[快捷键&命令/可用Skill](../快捷键&命令/可用Skill.md)


### GitHub 仓库

**https://github.com/dqtx760/skills-manage**

> 注意：更新仓库后，可使用 `skills-link sync` 同步到本地

### .gitignore 说明

以下文件/目录已排除，不会推送到 GitHub：

- `output/`：生成的图片、视频等输出文件
- `output-images/`：图片生成输出目录
- `__pycache__/`：Python 缓存文件
- `*.pyc`：Python 编译文件
- `.claude/settings.local.json`：本地配置文件（可能含敏感信息）

> 注意：`image/scripts/config.py` 中包含明文 API KEY，建议改为环境变量方式

### 推送脚本

> 双击 `push.bat` 即可一键推送到 GitHub

脚本位置：
```
D:\project2026\skills-manage\push.bat
```

功能：
- 自动 add 所有文件
- 输入提交信息（可直接回车使用默认信息）
- 自动推送到 GitHub

### 注意事项

**删除 Skill**：
- 正确做法：删除中央仓储 `.skillshub\xxx-skill` 里的内容，然后 `push.bat` 推送
- 删除后，所有 Agent 的 skills 目录里的软链接自动失效（文件消失）
- ⚠️ 不要只从某个 Agent 目录删除，那样只删了链接，源文件还在

## 关于作者
大强同学---Build in Public 践行者，数字生产力玩家。

| 平台         | 链接                                                                                                                                                                                                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 官网         | [dqtx.cc](https://www.dqtx.cc/)、[cv.dqtx.cc](https://cv.dqtx.cc/)                                                                                                                                                                                                        |
| 𝕏 Twitter | [@qdtx760](https://x.com/dqtx760)                                                                                                                                                                                                                                        |
| Bilibili   | [大强同学_](https://space.bilibili.com/491358682/upload/video)                                                                                                                                                                                                               |
| YouTube    | [Derek Zhao](https://www.youtube.com/@dqtx760/videos)                                                                                                                                                                                                                    |
| 小红书        | [大强同学](https://www.xiaohongshu.com/user/profile/5ce0d3a7000000001202e31b?xsec_token=YBBIYOqFwg1n9igsF09ObGwd0ulMEur6mgk7llsXBpS_M=&xsec_source=app_share&xhsshare=CopyLink&appuid=5ce0d3a7000000001202e31b&apptime=1751276165&share_id=94cac1806524407ea7a7f0f960f41b38) |
| 公众号        | 微信搜「大强同学」或扫码关注 ↓                                                                                                                                                                                                                                                         |
![](https://gitee.com/da-qiang-classmate/typora/raw/master/image/weix2.webp)
