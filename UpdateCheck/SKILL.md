---
name: UpdateCheck
description: 检测 D:\project2026\fuwari\src\content\index.md 与下属 6 个文件夹（Zen/Xenia/AIHacks/Software/Technical/Workflow）的文件同步状态。当用户说"更新检查"、"同步索引"、"sync index"、"update index"、"检查 index.md 是否最新"时触发。用于发现新增或删除的笔记文件并自动更新 index.md。
---

# UpdateCheck — index.md 同步检查

扫描指定文件夹的 `.md` 文件，与 `index.md` 中各章节的链接列表对比，发现差异后自动更新。

## 操作流程

### 1. 扫描源文件夹

依次扫描以下文件夹（均为 `D:\project2026\fuwari\src\content\` 下的子目录）：

| 章节标题 | 源文件夹 | 相对路径前缀 |
|----------|---------|-------------|
| `### Zen` | `Zen/` | `Zen/` |
| `### Xenia` | `Xenia/` | `Xenia/` |
| `### AlHacks` | `posts/AIHacks/` | `posts/AIHacks/` |
| `### Software` | `posts/Software/` | `posts/Software/` |
| `### Technical` | `posts/Technical/` | `posts/Technical/` |
| `### Workflow` | `posts/Workflow/` | `posts/Workflow/` |

只统计 `.md` 文件，忽略子目录和其他类型。

### 2. 读取 index.md

读取 `D:\project2026\fuwari\src\content\index.md`，解析每个 `### 章节` 下的链接列表。链接格式为：
```
- [display name](relative/path/filename.md)
```

从链接中提取文件名，与磁盘文件对比。

### 3. 生成差异报告

对每个章节输出：

```
## Zen
  + 新增: file-a.md, file-b.md     ← 磁盘有但 index.md 没有
  - 删除: file-c.md                ← index.md 有但磁盘没有
  = 无变化
```

### 4. 更新 index.md

如果有差异，用磁盘文件的当前状态**完全重写该章节的链接列表**。规则：

- **保留** `### 章节标题` 行不变
- **保留** 标题和第一个链接之间的空行
- **保留** 章节之间的空行
- **重建** 该章节下的所有链接
- 显示名 = 文件名去掉 `.md` 后缀

**两种输出格式，按章节分组：**

| 章节 | 格式 | 示例 |
|------|------|------|
| Zen | 列表 | `- [显示名](Zen/xxx.md)` |
| Xenia | 列表 | `- [显示名](Xenia/xxx.md)` |
| AlHacks | 表格 | `| 日期 | 文件 |` |
| Software | 表格 | `| 日期 | 文件 |` |
| Technical | 表格 | `| 日期 | 文件 |` |
| Workflow | 表格 | `| 日期 | 文件 |` |

**列表格式（Zen / Xenia）：**
```
- [显示名](路径/filename.md)
```

**表格格式（AlHacks / Software / Technical / Workflow）：**
```
| 日期 | 文件 |
|------|------|
| YYYY/MM/DD | [显示名](路径/filename.md) |
| YYYY/MM/DD(2) | [显示名](路径/filename.md) |
```

- 表头固定为 `| 日期 | 文件 |` + `|------|------|`
- 日期列用 `yyyy/MM/dd` 格式（如 `2026/05/23`），取文件 `LastWriteTime`
- 同日多个文件时，第一个不加序号，后续依次加 `(2)` `(3)` `(4)` ...
- **按文件修改时间倒序排列（最新的在最前面）**

**URL 编码规则（使用 `[uri]::EscapeDataString`）：**
- 空格 → `%20`
- `+` → `%2B`
- `&` → `%26`
- 中文字符 → 按 URI 标准编码

**空文件夹处理：**
- 如果文件夹不存在或为空，保留章节标题，留一个空行，不生成任何链接

### 5. 汇总报告

更新完成后输出汇总：

```
✅ index.md 已更新:
  Zen: +1 新增, -1 删除
  AlHacks: +3 新增
  Software: 无变化
  Technical: -2 删除
  Workflow: 无变化
  Xenia: 无变化
```

## 实现方法

使用以下工具完成：

1. **PowerShell** 扫描文件夹并按时间倒序生成链接：

   **列表格式（Zen / Xenia）：**
   ```powershell
   $files = @(Get-ChildItem "D:\project2026\fuwari\src\content\<folder>" -File -Filter "*.md" | Sort-Object LastWriteTime -Descending)
   foreach ($f in $files) { $name = $f.BaseName; $encoded = [uri]::EscapeDataString($f.Name); "- [$name](<prefix>/$encoded)" }
   ```

   **表格格式（posts 子目录）：**
   ```powershell
   $files = @(Get-ChildItem "D:\project2026\fuwari\src\content\posts\<folder>" -File -Filter "*.md" | Sort-Object LastWriteTime -Descending)
   $prevDate = ""; $cnt = 0
   foreach ($f in $files) {
     $date = $f.LastWriteTime.ToString("yyyy/MM/dd")
     $encoded = [uri]::EscapeDataString($f.Name); $name = $f.BaseName
     if ($date -eq $prevDate) { $cnt++; $dateLabel = "$date($cnt)" }
     else { $cnt = 1; $prevDate = $date; $dateLabel = $date }
     "| $dateLabel | [$name](<prefix>/$encoded) |"
   }
   ```
   表头需手动添加：`| 日期 | 文件 |` + `|------|------|`

2. **Read** 工具读取 `D:\project2026\fuwari\src\content\index.md`

3. **Edit** 工具更新章节内容 —— 用 `old_string` 匹配完整的章节块（从 `### 标题` 到下一个 `###` 或文件末尾），`new_string` 替换为重建的链接列表

4. **编码**：用 PowerShell 的 `[uri]::EscapeDataString()` 生成正确编码的链接路径

## 注意事项

- 不要删除或修改 `###` 标题行
- 不要改变章节间的空行数量
- 不要修改 index.md 中不属于这 6 个章节的内容
- **Zen 和 Xenia 用列表格式，AlHacks/Software/Technical/Workflow 用表格格式**，不要混用
- 表格日期列只显示年月日 `yyyy/MM/dd`，不含时分秒
- 排序必须是**文件修改时间倒序**（最新的在最前面），不是字母序
- 只在有差异时才编辑文件
- 先报告再更新，让用户知道发生了什么
