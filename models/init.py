from flask_sqlalchemy import SQLAlchemy

# 创建一个全局的数据库实例
db = SQLAlchemy()

# 导入所有模型


# 初始化数据库的函数
def init_db(app):
    db.init_app(app)

    # 在应用上下文中创建所有表
    with app.app_context():
        db.create_all()