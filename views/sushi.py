from flask import Blueprint, jsonify, request
from controllers.sushi import get_all_sushi, search_sushi
import base64
from pathlib import Path

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


@sushi_bp.route("/content", methods=['GET'])
def get_content():  # 移除 async 因为 Flask 不支持原生 async
    try:
        # 读取图片文件并转换为 Base64
        image_path = Path("../controllers/sushi_img/beef_sushi.jpg")
        if not image_path.exists():
            return jsonify({
                'status': 'error',
                'message': '图片文件不存在'
            }), 404

        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        # 在 Markdown 文本中嵌入 Base64 图片
        markdown_text = f"""
        # 你的标题

        这是一些文本内容

        ![embedded image](data:image/png;base64,{encoded_image})

        更多的文本内容
        """

        return jsonify({
            'status': 'success',
            'data': {
                'text': markdown_text
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
