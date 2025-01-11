# views/sushi_interaction.py
from flask import Blueprint, request, jsonify
from models.user import db, Like, Favorite, Comment

sushi_interaction_bp = Blueprint('sushi_interaction', __name__)


@sushi_interaction_bp.route('/status/<sushi_name>', methods=['GET'])
def get_sushi_status(sushi_name):
    """获取寿司的统计信息（点赞数、评论数等）"""
    username = request.args.get('username')

    likes_count = Like.query.filter_by(sushi_name=sushi_name).count()
    comments_count = Comment.query.filter_by(sushi_name=sushi_name).count()

    # 计算平均分
    comments = Comment.query.filter_by(sushi_name=sushi_name).all()
    avg_score = sum(c.score for c in comments) / len(comments) if comments else 0

    user_status = {}
    if username:
        user_status = {
            'has_liked': Like.query.filter_by(username=username, sushi_name=sushi_name).first() is not None,
            'has_favorited': Favorite.query.filter_by(username=username, sushi_name=sushi_name).first() is not None
        }

    return jsonify({
        'likes_count': likes_count,
        'comments_count': comments_count,
        'average_score': round(avg_score, 1),
        'user_status': user_status
    }), 200


@sushi_interaction_bp.route('/like', methods=['POST'])
def like_sushi():
    data = request.get_json()
    username = data.get('username')
    sushi_name = data.get('sushi_name')

    if not all([username, sushi_name]):
        return jsonify({'message': '缺少必要参数'}), 400

    existing_like = Like.query.filter_by(
        username=username,
        sushi_name=sushi_name
    ).first()

    if existing_like:
        return jsonify({'message': '已经点赞过了'}), 400

    new_like = Like(username=username, sushi_name=sushi_name)
    db.session.add(new_like)

    try:
        db.session.commit()
        return jsonify({'message': '点赞成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '点赞失败'}), 500


@sushi_interaction_bp.route('/unlike', methods=['POST'])
def unlike_sushi():
    data = request.get_json()
    username = data.get('username')
    sushi_name = data.get('sushi_name')

    if not all([username, sushi_name]):
        return jsonify({'message': '缺少必要参数'}), 400

    like = Like.query.filter_by(
        username=username,
        sushi_name=sushi_name
    ).first()

    if not like:
        return jsonify({'message': '还没有点赞'}), 400

    db.session.delete(like)

    try:
        db.session.commit()
        return jsonify({'message': '取消点赞成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '取消点赞失败'}), 500


@sushi_interaction_bp.route('/favorite', methods=['POST'])
def favorite_sushi():
    data = request.get_json()
    username = data.get('username')
    sushi_name = data.get('sushi_name')

    if not all([username, sushi_name]):
        return jsonify({'message': '缺少必要参数'}), 400

    existing_favorite = Favorite.query.filter_by(
        username=username,
        sushi_name=sushi_name
    ).first()

    if existing_favorite:
        return jsonify({'message': '已经收藏过了'}), 400

    new_favorite = Favorite(username=username, sushi_name=sushi_name)
    db.session.add(new_favorite)

    try:
        db.session.commit()
        return jsonify({'message': '收藏成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '收藏失败'}), 500


@sushi_interaction_bp.route('/unfavorite', methods=['POST'])
def unfavorite_sushi():
    data = request.get_json()
    username = data.get('username')
    sushi_name = data.get('sushi_name')

    if not all([username, sushi_name]):
        return jsonify({'message': '缺少必要参数'}), 400

    favorite = Favorite.query.filter_by(
        username=username,
        sushi_name=sushi_name
    ).first()

    if not favorite:
        return jsonify({'message': '还没有收藏'}), 400

    db.session.delete(favorite)

    try:
        db.session.commit()
        return jsonify({'message': '取消收藏成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '取消收藏失败'}), 500


@sushi_interaction_bp.route('/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    username = data.get('username')
    sushi_name = data.get('sushi_name')
    content = data.get('content')
    score = data.get('score')

    if not all([username, sushi_name, content, score]):
        return jsonify({'message': '缺少必要参数'}), 400

    if not 1 <= score <= 5:
        return jsonify({'message': '评分必须在1-5之间'}), 400

    new_comment = Comment(
        username=username,
        sushi_name=sushi_name,
        content=content,
        score=score
    )
    db.session.add(new_comment)

    try:
        db.session.commit()
        return jsonify({'message': '评论成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '评论失败'}), 500


@sushi_interaction_bp.route('/comments/<sushi_name>', methods=['GET'])
def get_comments(sushi_name):
    comments = Comment.query.filter_by(sushi_name=sushi_name).order_by(Comment.created_at.desc()).all()
    return jsonify({
        'comments': [{
            'id': c.id,
            'username': c.username,
            'content': c.content,
            'score': c.score,
            'created_at': c.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for c in comments]
    }), 200


@sushi_interaction_bp.route('/user/likes/<username>', methods=['GET'])
def get_user_likes(username):
    likes = Like.query.filter_by(username=username).all()
    return jsonify({
        'likes': [l.sushi_name for l in likes]
    }), 200


@sushi_interaction_bp.route('/user/favorites/<username>', methods=['GET'])
def get_user_favorites(username):
    favorites = Favorite.query.filter_by(username=username).all()
    return jsonify({
        'favorites': [f.sushi_name for f in favorites]
    }), 200