from flask import Blueprint, request, jsonify
from models.user import db
from models.admin import Admin
from models.user import User, Comment, Like, Favorite
from controllers.sushi import add_sushi, update_sushi, delete_sushi, get_all_sushi
import os
from werkzeug.utils import secure_filename
import shutil
import json

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


# 用户管理API
@admin_bp.route("/users", methods=["GET"])
def get_users():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        users = User.query.paginate(page=page, per_page=per_page)

        return (
            jsonify(
                {
                    "message": "获取用户列表成功",
                    "data": {
                        "users": [{"username": user.username} for user in users.items],
                        "total": users.total,
                        "pages": users.pages,
                        "current_page": page,
                    },
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({"message": f"获取用户列表失败: {str(e)}"}), 500


@admin_bp.route("/users/<username>", methods=["DELETE"])
def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "用户不存在"}), 404

        # 删除关联的点赞、收藏和评论
        Like.query.filter_by(username=username).delete()
        Favorite.query.filter_by(username=username).delete()
        Comment.query.filter_by(username=username).delete()

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "删除用户成功"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"删除用户失败: {str(e)}"}), 500


@admin_bp.route("/users/<username>", methods=["PUT"])
def update_user(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "用户不存在"}), 404

        data = request.get_json()
        new_password = data.get("password")

        if new_password:
            user.password = new_password
            db.session.commit()
            return jsonify({"message": "更新用户成功"}), 200
        else:
            return jsonify({"message": "没有提供更新数据"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"更新用户失败: {str(e)}"}), 500


# 评论管理API
@admin_bp.route("/comments", methods=["GET"])
def get_comments():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        comments = Comment.query.order_by(Comment.created_at.desc()).paginate(
            page=page, per_page=per_page
        )

        return (
            jsonify(
                {
                    "message": "获取评论列表成功",
                    "data": {
                        "comments": [
                            {
                                "id": comment.id,
                                "username": comment.username,
                                "sushi_name": comment.sushi_name,
                                "content": comment.content,
                                "score": comment.score,
                                "created_at": comment.created_at.strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                ),
                            }
                            for comment in comments.items
                        ],
                        "total": comments.total,
                        "pages": comments.pages,
                        "current_page": page,
                    },
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({"message": f"获取评论列表失败: {str(e)}"}), 500


@admin_bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    try:
        comment = Comment.query.get(comment_id)
        if not comment:
            return jsonify({"message": "评论不存在"}), 404

        db.session.delete(comment)
        db.session.commit()

        return jsonify({"message": "删除评论成功"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"删除评论失败: {str(e)}"}), 500


@admin_bp.route("/sushi", methods=["GET"])
def admin_get_sushi_list():
    try:
        # 获取所有寿司
        sushi_list = get_all_sushi()

        return jsonify({"message": "获取寿司列表成功", "data": sushi_list}), 200
    except Exception as e:
        return jsonify({"message": f"获取寿司列表失败: {str(e)}"}), 500


@admin_bp.route("/sushi", methods=["POST"])
def admin_add_sushi():
    try:
        data = request.get_json()
        name = data.get("name")
        image_filename = data.get("image")
        price = data.get("price")
        details = data.get("details")

        if not all([name, image_filename, price, details]):
            return jsonify({"message": "所有字段都必须填写"}), 400

        success, message = add_sushi(name, image_filename, price, details)

        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"message": message}), 400
    except Exception as e:
        return jsonify({"message": f"添加寿司失败: {str(e)}"}), 500


@admin_bp.route("/sushi/<name>", methods=["PUT"])
def admin_update_sushi(name):
    try:
        data = request.get_json()
        image_filename = data.get("image")
        price = data.get("price")
        details = data.get("details")

        if not all([image_filename, price, details]):
            return jsonify({"message": "所有字段都必须填写"}), 400

        success, message = update_sushi(name, image_filename, price, details)

        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"message": message}), 404
    except Exception as e:
        return jsonify({"message": f"更新寿司失败: {str(e)}"}), 500


@admin_bp.route("/sushi/<name>", methods=["DELETE"])
def admin_delete_sushi(name):
    try:
        success, message = delete_sushi(name)
        return jsonify({"message": message}), 200
    except Exception as e:
        return jsonify({"message": f"删除寿司失败: {str(e)}"}), 500
