import base64
from pathlib import Path

from flask import Blueprint, jsonify, request

from controllers.sushi import get_all_sushi, search_sushi, SUSHI_DETAILS, SUSHI_DATA

sushi_bp = Blueprint('sushi', __name__)


@sushi_bp.route('/', methods=['GET'])
def get_sushi_list():
    try:
        sushi_list = get_all_sushi()
        return jsonify({
            'status': 'success',
            'data': sushi_list
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


# 添加 get_image_base64 函数的实现
def get_image_base64(image_path):
    """将图片转换为 Base64 编码"""
    try:
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode()
            # 获取文件扩展名
            file_extension = Path(image_path).suffix.lower()
            # 根据扩展名选择正确的 MIME 类型
            mime_types = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif'
            }
            mime_type = mime_types.get(file_extension, 'image/jpeg')
            return f"data:{mime_type};base64,{encoded_image}"
    except Exception as e:
        print(f"Error reading image: {str(e)}")
        return None


@sushi_bp.route('/search', methods=['GET'])
def search():
    try:
        keyword = request.args.get('keyword', '')
        if not keyword:
            return jsonify({
                'status': 'error',
                'message': '请提供搜索关键词'
            }), 400

        results = search_sushi(keyword)
        return jsonify({
            'status': 'success',
            'data': results
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


"""
    "金枪鱼寿司": {
        "name_en": "Tuna Sushi",
        "description": "精选金枪鱼生鱼片，肉质紧实，味道鲜美",
        "steps": [
            "准备寿司醋和米饭",
            "准备金枪鱼生鱼片",
            "将寿司醋拌入米饭",
            "把金枪鱼片盖在米饭上"
        ]
    }
"""


@sushi_bp.route("/detail", methods=['GET'])
def get_sushi_detail():
    try:
        sushi_name = request.args.get('sushi_name', '')
        # 检查寿司是否存在
        sushi_detail = SUSHI_DETAILS.get(sushi_name)
        if not sushi_detail:
            return jsonify({
                'status': 'error',
                'message': f'未找到寿司 {sushi_name} 的详情'
            }), 404

        # 获取寿司图片
        # 从 SUSHI_DATA 中找到对应的图片路径
        sushi = next((s for s in SUSHI_DATA if s.name == sushi_name), None)
        if not sushi:
            raise Exception("找不到寿司图片")

        image_base64 = get_image_base64(sushi.image)
        if not image_base64:
            raise Exception("无法加载图片")

        # 使用列表来构建 Markdown 内容
        md_parts = [
            f"# {sushi_name}",
            "",  # 空行
            f"![{sushi_name}]({image_base64})",
            "",  # 空行
            f"{sushi_detail['description']}",  # 描述
            "",  # 空行
            "## 制作步骤"
        ]

        # 添加制作步骤
        for i, step in enumerate(sushi_detail['steps'], 1):
            md_parts.append(f"***步骤 {i} :*** {step}")

        # 用换行符连接所有部分
        content = "\n".join(md_parts)

        return jsonify({
            'status': 'success',
            'data': {
                'content': content
            }
        })

    except Exception as e:
        print(f"Error: {str(e)}")  # 添加日志便于调试
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
