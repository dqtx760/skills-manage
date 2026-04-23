"""
ModelScope API 配置
"""

# API 基础配置
BASE_URL = "https://api-inference.modelscope.cn/"
API_KEY = "ms-ac3397d3-a778-40a5-8085-bf27c9b0fceb"  # ModelScope Token

# 默认模型
DEFAULT_MODEL = "Tongyi-MAI/Z-Image-Turbo"

# 轮询配置
POLL_INTERVAL = 5  # 秒
MAX_POLL_ATTEMPTS = 60  # 最大轮询次数（5 分钟）

# 默认图片尺寸
DEFAULT_SIZE = "1024x1024"

# 默认输出目录
DEFAULT_OUTPUT_DIR = "../../output-images/image"  # 相对于 scripts 目录
DEFAULT_OUTPUT_FILE = "generated_image.jpg"
