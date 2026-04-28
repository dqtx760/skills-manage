---
emoji: "🚀"
title: "AI 操控飞书"
subtitle: "飞书CLI教程分享"
---

# AI操控飞书，效率直接拉满！

发现一个超棒的工具，用AI就能帮你自动操控飞书，创建文档、整理知识库、发通知全都搞定 ✨

---

# 📦 安装配置教程

## 第1步 — 安装 CLI
```bash
# 安装
npm install -g @larksuite/cli

# 升级
npm update -g @larksuite/cli && npx skills add larksuite/cli -g -y

# 安装 CLI SKILL（必需）
npx skills add larksuite/cli -y -g
```

---

# ⚙️ 第2步 — 配置凭证

后台运行命令，会输出授权链接，浏览器打开完成配置即可

```bash
lark-cli config init --new
```

---

# 🔑 第3步 — 登录

同样后台运行，提取授权链接打开登录

```bash
lark-cli auth login --recommend
```

---

# ✅ 第4步 — 验证

```bash
lark-cli auth status
```

如果显示不正常，重新授权一次就好啦 🤗

---

# 🎯 AI能帮你做这些

✅ 创建教程文档，自动分章节  
✅ 生成系列教程大纲  
✅ 对比分析框架特性  
✅ 创建进度表、工具推荐表  
✅ 整理FAQ表格  
✅ 通知粉丝群、发问卷收集反馈  
✅ 创建知识空间，分类整理文档  
✅ 设置发布提醒，整理素材  

---

# 💡 使用场景举例

帮我创建一篇"Python爬虫入门教程"的文档，包含环境准备、基础语法、实战案例三个章节

生成一个"Vue3组合式API"系列教程的大纲，包含10个章节，从基础到进阶

通知我的粉丝群，本周将发布"Flutter跨平台开发"新教程

提醒我明天下午3点发布"TypeScript类型系统"教程

真的太方便了！创作效率提升N倍，赶紧试试吧 👇

---

# 🔗 开源地址

https://github.com/larksuite/cli

欢迎Star支持作者 ⭐

