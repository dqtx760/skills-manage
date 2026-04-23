---
name: image
description: 使用 ModelScope 通义千问 AI 生成图片。支持 /image 或 /gen-image 斜杠命令，以及自然语言描述如"生成一张...的图片"、"画一个..."。支持中文描述生成高质量图片，可自定义输出文件名和尺寸。
---

# ModelScope AI 图片生成

使用 ModelScope 通义千问 Z-Image-Turbo 模型生成高质量 AI 图片。

## 快速使用

### 斜杠命令（推荐）

直接在对话中使用以下斜杠命令：

```bash
/image <图片描述>
/gen-image <图片描述>
```

**使用示例：**
- `/image 一只金色的猫`
- `/gen-image 赛博朋克风格的未来城市，霓虹灯效果`
- `/image 可爱的卡通小熊，森林背景`

**带参数的命令：**
- `/image "描述" -o my_image.jpg`  # 指定输出文件名
- `/image "描述" -s 512x512`       # 指定图片尺寸

### 命令行直接调用

```bash
python3 scripts/generate_image.py "一只金色的猫"
```

## 工作流程

1. **解析请求**：从用户消息中提取图片描述（prompt）
2. **优化提示词**：根据描述优化英文 prompt
3. **调用 API**：使用 ModelScope 异步接口生成图片
4. **轮询结果**：每 5 秒检查一次任务状态
5. **保存图片**：下载并保存生成的图片

## 脚本参数

| 参数 | 说明 | 默认值 |
|-----|------|-------|
| `prompt` | 图片描述（必填） | - |
| `-m, --model` | 使用的模型 | `Tongyi-MAI/Z-Image-Turbo` |
| `-o, --output` | 输出文件路径 | `generated_image.jpg` |
| `-s, --size` | 图片尺寸 | `1024x1024` |

## 使用示例

### 基本用法
```bash
python3 scripts/generate_image.py "一只在草原上奔跑的狮子"
```

### 指定输出文件
```bash
python3 scripts/generate_image.py -o my_image.jpg "赛博朋克风格的未来城市"
```

### 指定图片尺寸
```bash
python3 scripts/generate_image.py -s 512x512 "可爱的卡通小熊"
```

## 提示词建议

### 优质 Prompt 特点
- **具体明确**：描述主体、环境、风格
- **细节丰富**：添加光影、色彩、构图信息
- **风格指定**：注明艺术风格（如"油画风格"、"写实摄影"）

### 示例 Prompt

| 场景 | Prompt |
|-----|--------|
| 动物 | "一只毛茸茸的金色猫咪，柔和的自然光，背景虚化，高清摄影" |
| 风景 | "壮丽的山峰日出，云雾缭绕，金色阳光洒满山谷，广角镜头" |
| 人物 | "年轻女性的肖像，微笑的表情，自然光，背景是城市天际线" |
| 抽象 | "流动的色彩，蓝色和紫色的渐变，梦幻般的质感，数字艺术" |
| 建筑 | "现代极简主义别墅，落地窗，周围是绿色花园，阳光明媚" |

## API 配置

脚本使用环境变量或配置文件设置 API Key：

```bash
export MODELSCOPE_API_KEY="ms-your-api-key-here"
```

或在脚本中直接设置（见 `scripts/config.py`）。

## 支持的模型

| 模型 ID | 特点 |
|---------|-----|
| `Tongyi-MAI/Z-Image-Turbo` | 快速生成，通用场景 |
| `Tongyi-MAI/Z-Image-Plus` | 高质量，细节丰富 |

## LoRA 支持

可以使用 LoRA 模型增强特定风格：

```python
# 单个 LoRA
"loras": "your-lora-repo-id"

# 多个 LoRA（权重和为 1.0）
"loras": {
    "lora-repo-id1": 0.6,
    "lora-repo-id2": 0.4
}
```

## 错误处理

| 错误 | 原因 | 解决方案 |
|-----|------|---------|
| API Key 无效 | 认证失败 | 检查环境变量或配置文件 |
| 任务超时 | 生成时间过长 | 增加轮询超时时间 |
| 生成失败 | Prompt 违规 | 调整描述内容 |

## 输出格式

生成的图片保存为 JPEG 格式，默认文件名：
- `generated_image.jpg`（单张）
- `generated_image_1.jpg`, `generated_image_2.jpg`（多张）

## 注意事项

⚠️ API 有速率限制，避免短时间内大量请求
⚠️ 生成时间约 5-30 秒，取决于服务器负载
⚠️ 请遵守内容使用政策，不得生成违规内容
