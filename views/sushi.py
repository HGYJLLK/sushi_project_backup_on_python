from flask import Blueprint, jsonify, request
from controllers.sushi import get_all_sushi, search_sushi

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
