from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text  # 导入 text

# 初始化 Flask 应用和 SQLAlchemy
app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/sushi_db'  # 修改为你的数据库配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy
db = SQLAlchemy(app)


# 定义数据库模型
class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120))


class Like(db.Model):
    username = db.Column(db.String(80), db.ForeignKey('user.username'), primary_key=True)
    sushi_name = db.Column(db.String(50), primary_key=True)


class Favorite(db.Model):
    username = db.Column(db.String(80), db.ForeignKey('user.username'), primary_key=True)
    sushi_name = db.Column(db.String(50), primary_key=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), db.ForeignKey('user.username'))
    sushi_name = db.Column(db.String(50))
    content = db.Column(db.Text)
    score = db.Column(db.SmallInteger)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', backref=db.backref('comments', lazy=True))


# 检查数据库是否存在并删除
def check_and_create_db():
    with app.app_context():  # 显式进入应用上下文
        try:
            # 尝试连接并检查是否有数据库
            db.session.execute(text("SELECT 1 FROM information_schema.schemata WHERE schema_name = 'sushi_db'"))
            print("数据库 sushi_db 已存在，正在删除...")
            db.session.execute(text("DROP DATABASE sushi_db;"))
        except OperationalError:
            print("数据库 sushi_db 不存在，准备创建新的数据库...")

        # 创建新的数据库
        db.session.execute(text("CREATE DATABASE sushi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))
        db.session.execute(text("USE sushi_db;"))
        print("数据库 sushi_db 创建成功。")


# 创建表格并插入数据
def create_tables_and_insert_data():
    with app.app_context():  # 显式进入应用上下文
        db.create_all()  # 创建表格
        print("表格创建成功。")


# 主程序执行
if __name__ == '__main__':
    # 检查并创建数据库
    check_and_create_db()

    # 创建表格并插入测试数据
    create_tables_and_insert_data()

    print("脚本执行完成！")
