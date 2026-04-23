#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ModelScope AI 图片生成工具
使用通义千问 Z-Image-Turbo 模型生成图片

斜杠命令支持: /image <prompt> 或 /gen-image <prompt>
"""

import argparse
import time
import json
import sys
import os
from pathlib import Path

try:
    import requests
    from PIL import Image
    from io import BytesIO
except ImportError as e:
    print(f"错误: 缺少依赖库 - {e}")
    print("请安装: pip install requests pillow")
    sys.exit(1)

from config import (
    BASE_URL,
    API_KEY,
    DEFAULT_MODEL,
    POLL_INTERVAL,
    MAX_POLL_ATTEMPTS,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_OUTPUT_FILE,
)


def ensure_utf8_env():
    """确保环境支持中文输出"""
    if sys.platform == "win32":
        # Windows 系统设置 UTF-8 输出
        os.system('chcp 65001 >nul 2>&1')
        # 设置 stdout 编码
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')


# 初始化时设置编码
ensure_utf8_env()


def translate_to_english(prompt: str) -> str:
    """
    将中文 prompt 翻译为英文（ModelScope 模型对英文支持更好）
    这里简单返回原 prompt，实际使用时可以接入翻译 API
    """
    # 简单关键词映射
    keywords = {
        "猫": "cat",
        "狗": "dog",
        "风景": "landscape",
        "肖像": "portrait",
        "卡通": "cartoon",
        "写实": "realistic",
        "油画": "oil painting",
        "水彩": "watercolor",
    }

    result = prompt
    for cn, en in keywords.items():
        result = result.replace(cn, en)

    return result


def generate_image(
    prompt: str,
    model: str = DEFAULT_MODEL,
    output_path: str = "generated_image.jpg",
    size: str = "1920x1080",
    loras: dict = None,
) -> str:
    """
    生成图片

    Args:
        prompt: 图片描述
        model: 使用的模型
        output_path: 输出文件路径
        size: 图片尺寸
        loras: LoRA 配置

    Returns:
        生成的图片文件路径
    """
    common_headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # 构建请求数据
    request_data = {
        "model": model,
        "prompt": prompt,
        "size": size,
    }

    if loras:
        request_data["loras"] = loras

    # 发送异步请求
    print(f"正在生成图片: {prompt}")
    print(f"使用模型: {model}")

    response = requests.post(
        f"{BASE_URL}v1/images/generations",
        headers={**common_headers, "X-ModelScope-Async-Mode": "true"},
        data=json.dumps(request_data, ensure_ascii=False).encode("utf-8"),
    )

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"API 请求失败: {e}")
        print(f"响应: {response.text}")
        sys.exit(1)

    task_id = response.json().get("task_id")
    if not task_id:
        print("错误: 未获取到 task_id")
        sys.exit(1)

    print(f"任务 ID: {task_id}")
    print("等待生成...")

    # 轮询任务状态
    for attempt in range(MAX_POLL_ATTEMPTS):
        result = requests.get(
            f"{BASE_URL}v1/tasks/{task_id}",
            headers={**common_headers, "X-ModelScope-Task-Type": "image_generation"},
        )
        result.raise_for_status()
        data = result.json()

        task_status = data.get("task_status")

        if task_status == "SUCCEED":
            print("生成成功！正在下载...")

            image_urls = data.get("output_images", [])
            if not image_urls:
                print("错误: 未获取到图片 URL")
                sys.exit(1)

            # 下载第一张图片
            img_response = requests.get(image_urls[0])
            img_response.raise_for_status()

            image = Image.open(BytesIO(img_response.content))
            image.save(output_path)

            print(f"图片已保存至: {output_path}")
            return output_path

        elif task_status == "FAILED":
            error_msg = data.get("error", "未知错误")
            print(f"生成失败: {error_msg}")
            sys.exit(1)

        elif task_status == "RUNNING":
            print(f".", end="", flush=True)
            time.sleep(POLL_INTERVAL)

        else:
            print(f"未知状态: {task_status}")
            time.sleep(POLL_INTERVAL)

    print(f"\n超时: 任务在 {MAX_POLL_ATTEMPTS * POLL_INTERVAL} 秒内未完成")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="ModelScope AI 图片生成工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "一只金色的猫"
  %(prog)s -o my_image.jpg "赛博朋克城市"
  %(prog)s -s 512x512 "可爱的小熊"
        """,
    )

    parser.add_argument("prompt", help="图片描述")
    parser.add_argument(
        "-m",
        "--model",
        default=DEFAULT_MODEL,
        help="使用的模型 (默认: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help="输出文件名 (默认: %(default)s)",
    )
    parser.add_argument(
        "-s",
        "--size",
        default="1920x1080",
        help="图片尺寸 (默认: %(default)s)",
    )

    args = parser.parse_args()

    # 检测是否为绝对路径，如果是则直接使用，否则使用默认输出目录
    output_arg = Path(args.output)
    if output_arg.is_absolute():
        # 使用绝对路径
        output_path = output_arg
        # 确保父目录存在
        output_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        # 使用默认输出目录
        output_dir = Path(__file__).parent / DEFAULT_OUTPUT_DIR
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / args.output

    generate_image(
        prompt=args.prompt,
        model=args.model,
        output_path=str(output_path),
        size=args.size,
    )


if __name__ == "__main__":
    main()
