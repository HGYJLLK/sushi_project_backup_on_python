from flask import Blueprint, request, jsonify
from models.user import db, User

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': '用户名和密码不能为空'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'message': '用户名已存在'}), 400

        # 直接存储原始密码
        new_user = User(username=username, password=password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': '注册成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'注册失败: {str(e)}'}), 500

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': '用户名和密码不能为空'}), 400

        user = User.query.filter_by(username=username).first()

        # 直接比较原始密码
        if user and user.password == password:
            return jsonify({
                'message': '登录成功',
                'data': {
                    'username': user.username,
                }
            }), 200

        return jsonify({'message': '用户名或密码错误'}), 401
    except Exception as e:
        return jsonify({'message': f'登录失败: {str(e)}'}), 500

@user_bp.route('/status', methods=['POST'])
def check_status():
    try:
        data = request.get_json()
        username = data.get('username')

        if not username:
            return jsonify({'message': '用户名不能为空'}), 400

        user_exists = User.query.filter_by(username=username).first() is not None

        return jsonify({
            'message': '查询成功',
            'data': {
                'exists': user_exists,
                'username': username if user_exists else None
            }
        }), 200
    except Exception as e:
        return jsonify({'message': f'查询失败: {str(e)}'}), 500