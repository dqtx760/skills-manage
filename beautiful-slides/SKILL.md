---
name: beautiful-slides
description: 使用 beautiful-html-templates 专业设计模板生成精美的 HTML 幻灯片。适合需要高质量、独特设计感的演示文稿。
---

# Beautiful Slides

使用 beautiful-html-templates 库中的专业设计模板生成 HTML 幻灯片。

## 模板列表

14 款精选模板可用：

| 模板 | 风格 | 适用场景 |
|------|------|----------|
| **Signal** | 深海军蓝 + 骨纸 + 哑光金 | 投资者 deck、董事会、咨询 |
| **Pin & Paper** | 黄纸 + 手写 Caveat + 安全针 | 研究报告、手工感 |
| **Mat** | 深鼠尾草 + 骨纸 + 焦橙 | 设计工作室、建筑 |
| **Grove** | 森林绿 + Playfair + 锈色 | 可持续、wellness、画廊 |
| **Coral** | 奶油 + 珊瑚 + Bebas Neue | 时尚、健身、杂志 |
| **Cartesian** | 暖中性 + Playfair | 学术、白皮书 |
| **Vellum** | 深蓝 + 暖黄斜体 Cormorant | 研究、学术 |
| **Soft Editorial** | 暖纸 + Cormorant Garamond | 品牌故事、优雅 |
| **Stencil & Tablet** | 骨纸 + 模板切割标题 | 考古、品牌 |
| **Monochrome** | 象牙账本纸 + 全黑字体 | 极简、正式 |
| **Pink Script** | 黑底 + 热粉 + 手写 | 夜店、奢华 |
| **Blue Professional** | 奶油 + 电光蓝 | B2B、专业 |
| **Broadside** | 深色 + 火焰橙 + 中英双语 | 品牌宣言 |
| **Biennale Yellow** | 太阳黄 + 靛蓝 + 氛围渐变 | 艺术、展览 |

## 工作流程

### Step 1: 收集需求

Ask (header: "Purpose"):
这个演示是做什么的？选项：
- 投资者 pitch
- 品牌宣言
- 研究报告
- 教学/教程
- 内部会议
- 其他

Ask (header: "Vibe"):
想要什么风格？选项：
- 正式专业
- 创意大胆
- 温暖手工
- 优雅文学
- 极简现代

### Step 2: 推荐模板

根据用户的 Purpose 和 Vibe，从 14 个模板中推荐 3 个最合适的候选。

列出每个候选模板：
- 模板名称
- 一句话风格描述
- 适用理由

### Step 3: 生成预览

1. 读取用户选中的模板：`templates/<slug>/template.html`
2. 替换占位内容为用户的实际标题/副标题
3. 保存预览到 `previews/<slug>.html`
4. 用 `open` 打开预览

### Step 4: 用户确认

Ask (header: "Choose"):
你更喜欢哪个模板？
- 模板 A: [名称]
- 模板 B: [名称]
- 模板 C: [名称]

### Step 5: 生成完整幻灯片

1. 读取选中模板的所有文件
2. 替换所有占位内容：
   - 标题、副标题
   - 正文内容
   - 图片
   - 页码
3. 根据内容需要添加/删除幻灯片
4. 合并所有资源为单个 HTML 文件

### Step 6: 交付

1. 用 `open` 打开生成的 HTML
2. 告诉用户：
   - 文件位置
   - 导航方式（方向键/空格/点击）
   - 如何自定义（修改 CSS 变量、替换图片）

## 模板位置

所有模板在 `templates/` 目录下，每个模板一个文件夹，包含：
- `template.html` - 主模板文件
- `*.css` - 样式文件
- `*.js` - 脚本文件
- 其他资源

## 设计规则

**保留（不要改）：**
- 字体和字体栈
- 颜色变量
- 布局网格
- 装饰元素

**替换（用户内容）：**
- 标题和正文
- 统计数据
- 图片
- 日期和署名
