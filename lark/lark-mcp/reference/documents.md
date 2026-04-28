# 文档操作

## 核心规则

```yaml
# 搜索文档必须使用用户身份
useUAT: true

# 参数名注意
docx_builtin_search: search_key  # 不是 query
wiki_v1_node_search: query       # 不是 search_key
```

## 搜索文档

```yaml
工具: mcp__lark-mcp__docx_builtin_search
data:
  search_key: "关键词"
  count: 20
useUAT: true
```

响应：
```json
{
  "docs_entities": [
    {
      "docs_token": "doxcnxxxxxx",
      "title": "文档标题",
      "docs_type": "docx"
    }
  ]
}
```

## 获取文档内容

```yaml
工具: mcp__lark-mcp__docx_v1_document_rawContent
path:
  document_id: "doxcnxxxxxx"
params:
  lang: 0  # 0=中文, 1=英文
useUAT: true
```

## 导入 Markdown

```yaml
工具: mcp__lark-mcp__docx_builtin_import
data:
  markdown: "# 标题\n\n正文内容..."
  file_name: "文档.md"
useUAT: true
```

返回文档 URL 和 token。

## 批量更新文档块

```yaml
工具: mcp__lark-mcp__docx_v1_documents_blocks_batch_update
path:
  document_id: "doxcnxxxxxx"  # 文档ID，从URL中获取
data:
  requests:
    - update_text_elements:
        elements:
          - text_run:
              content: "新的文本内容"
              text_element_style:
                bold: false
useUAT: true
```

**功能**：批量更新文档中块的富文本内容，可以用来编辑已有文档。

**获取 document_id**：从文档URL `https://xxx.feishu.cn/docx/doxcnxxxxxx` 中获取 `doxcnxxxxxx` 部分。

**说明**：这是飞书OpenAPI原生接口，支持多种更新操作：
- `update_text_elements`: 更新文本元素内容
- `update_text_style`: 更新文本样式
- `update_table_property`: 更新表格属性
- `insert_blocks`: 插入块
- `delete_blocks`: 删除块

## docs_types 可选值

| 类型 | 说明 |
|------|------|
| `docx` | 新版文档 |
| `doc` | 旧版文档 |
| `sheet` | 电子表格 |
| `bitable` | 多维表格 |
| `mindnote` | 思维导图 |
| `file` | 云空间文件 |

## 从 URL 获取 document_id

```
https://xxx.feishu.cn/docx/doxcnxxxxxx
                          ↑ document_id
```

## 常见错误

| 错误 | 解决 |
|------|------|
| User access token not configured | 配置 OAuth |
| permission denied | 使用 `useUAT: true` |
| document not found | 检查 document_id |

## 工作流：导入并分享

```yaml
# 1. 导入 Markdown
工具: mcp__lark-mcp__docx_builtin_import
data:
  markdown: "# 报告\n\n内容..."

# 2. 添加权限（使用返回的 token）
工具: mcp__lark-mcp__drive_v1_permissionMember_create
path:
  token: "返回的token"
params:
  type: "docx"
data:
  member_type: "email"
  member_id: "user@example.com"
  perm: "view"
```
