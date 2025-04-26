from flask import Blueprint, request, jsonify
from models.user import db
from models.admin import Admin

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "用户名和密码不能为空"}), 400

        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.password == password:
            # 更新最后登录时间
            admin.last_login = db.func.now()
            db.session.commit()

            return (
                jsonify(
                    {
                        "message": "登录成功",
                        "data": {
                            "username": admin.username,
                        },
                    }
                ),
                200,
            )

        return jsonify({"message": "用户名或密码错误"}), 401
    except Exception as e:
        return jsonify({"message": f"登录失败: {str(e)}"}), 500


@admin_bp.route("/add", methods=["POST"])
def add_admin():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "用户名和密码不能为空"}), 400

        if Admin.query.filter_by(username=username).first():
            return jsonify({"message": "管理员用户名已存在"}), 400

        new_admin = Admin(username=username, password=password)
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({"message": "添加管理员成功"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"添加失败: {str(e)}"}), 500
