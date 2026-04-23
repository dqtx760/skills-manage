# ModelScope AI 图片生成 Skill

使用 ModelScope 通义千问 Z-Image-Turbo 模型生成高质量 AI 图片的 Claude Skill。

## 功能特点

- 支持中文描述生成图片
- 异步任务处理，自动轮询结果
- 可自定义输出路径和图片尺寸
- 支持 LoRA 模型增强

## 安装依赖

```bash
pip install requests pillow
```

## 配置 API Key

编辑 `scripts/config.py`，设置你的 ModelScope API Key：

```python
API_KEY = "ms-your-api-key-here"
```

或使用环境变量：

```bash
export MODELSCOPE_API_KEY="ms-your-api-key-here"
```

## 使用方法

### 斜杠命令（推荐）

在 Claude Code 对话中直接使用：

```bash
/image 一只金色的猫
/gen-image 赛博朋克城市
/image 可爱的卡通小熊 -o bear.jpg
```

**支持的命令：**
- `/image <描述>` - 生成图片
- `/gen-image <描述>` - 同上

**可选参数：**
- `-o, --output` - 指定输出文件名
- `-s, --size` - 指定图片尺寸

### 命令行使用

```bash
# 基本用法
python3 scripts/generate_image.py "一只金色的猫"

# 指定输出文件
python3 scripts/generate_image.py -o my_image.jpg "赛博朋克城市"

# 指定图片尺寸
python3 scripts/generate_image.py -s 512x512 "可爱的小熊"
```

## 目录结构

```
modelscope-image-gen/
├── SKILL.md           # Skill 定义文件
├── README.md          # 说明文档
├── modelscope-image-gen.skill  # Skill 配置
└── scripts/
    ├── config.py      # API 配置
    └── generate_image.py  # 生成脚本
```

## 注意事项

- API 有速率限制，请合理使用
- 生成时间约 5-30 秒
- 请遵守内容使用政策

## 参考链接

- [ModelScope 官方文档](https://modelscope.cn/docs)
- [通义千问图片生成](https://modelscope.cn/models/Tongyi-MAI/Z-Image-Turbo)
