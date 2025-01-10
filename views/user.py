from flask import Blueprint, request, jsonify
from models.user import db, User

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': '用户名已存在'}), 400

    new_user = User(username=username, password=password)  # 直接存储密码
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': '注册成功'}), 200


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()  # 直接比较密码
    if user:
        return jsonify({'message': '登录成功'}), 200
    return jsonify({'message': '用户名或密码错误'}), 401