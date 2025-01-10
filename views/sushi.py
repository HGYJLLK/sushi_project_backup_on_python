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
def get_content():
    try:
        content = (
            "# 寿司介绍\n" +
            "\n" +
            "![寿司图片](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEBLAEsAAD/4QB+RXhpZgAASUkqAAgAAAAEAA4BAgAiAAAAPgAAAJiCAgAGAAAAYAAAABoBBQABAAAAZgAAABsBBQABAAAAbgAAAAAAAABCZWVmIFN1Y2hpIE5pZ2lyaSBvbiBhIGJsYWNrIHBsYXRlTWFudUhLLAEAAAEAAAAsAQAAAQAAAP...)\n" +
            "\n" +
            "***Vue :*** [Vue3 官网](https://cn.vuejs.org/)\n" +
            "***CSDN :*** [CSDN 官网](https://www.csdn.net/)\n" +
            "\n" +
            "## 寿司种类\n" +
            "\n" +
            "***牛肉寿司 :*** [寿司制作教程](https://www.runoob.com/cooking/sushi-tutorial.html)\n" + 
            "***金枪鱼寿司 :*** [寿司历史介绍](https://www.history-of-sushi.net)\n" +
            "\n" +
            "## 制作方法\n" +
            "\n" +
            "***步骤一 :*** 准备寿司醋和米饭\n" +
            "***步骤二 :*** 准备生鱼片\n" +
            "***步骤三 :*** 将食材卷起即可"
        )

        return jsonify({
            'status': 'success',
            'data': {
                'content': content
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500