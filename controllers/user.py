from models.user import User, db


def create_user(username, password):
    try:
        user = User()
        user.username = username
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return True, "注册成功"
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return True, user
    return False, None
