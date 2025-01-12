from flask import Blueprint, request, jsonify
from models.user import db, User
from werkzeug.security import generate_password_hash, check_password_hash  # 添加密码哈希功能

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

        # 使用werkzeug提供的密码哈希功能
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

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

        if user and check_password_hash(user.password, password):
            return jsonify({
                'message': '登录成功',
                'data': {
                    'username': user.username,
                    # 可以添加其他需要返回的用户信息
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