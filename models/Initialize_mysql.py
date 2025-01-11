from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

# 初始化 Flask 应用和 SQLAlchemy
app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/'  # 修改为你的数据库配置
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
    try:
        # 尝试连接并检查是否有数据库
        db.engine.execute("SELECT 1 FROM information_schema.schemata WHERE schema_name = 'sushi_db'")
        print("数据库 sushi_db 已存在，正在删除...")
        db.engine.execute("DROP DATABASE sushi_db;")
    except OperationalError:
        print("数据库 sushi_db 不存在，准备创建新的数据库...")

    # 创建新的数据库
    db.engine.execute("CREATE DATABASE sushi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    db.engine.execute("USE sushi_db;")
    print("数据库 sushi_db 创建成功。")


# 创建表格并插入数据
def create_tables_and_insert_data():
    db.create_all()  # 创建表格
    print("表格创建成功。")

    # 插入一些测试数据
    user1 = User(username='user1', password='password123')
    user2 = User(username='user2', password='password456')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("用户数据插入成功。")

    like1 = Like(username='user1', sushi_name='Sushi1')
    like2 = Like(username='user2', sushi_name='Sushi2')
    db.session.add(like1)
    db.session.add(like2)
    db.session.commit()
    print("点赞数据插入成功。")

    favorite1 = Favorite(username='user1', sushi_name='Sushi2')
    favorite2 = Favorite(username='user2', sushi_name='Sushi1')
    db.session.add(favorite1)
    db.session.add(favorite2)
    db.session.commit()
    print("收藏数据插入成功。")

    comment1 = Comment(username='user1', sushi_name='Sushi1', content='Delicious!', score=5)
    comment2 = Comment(username='user2', sushi_name='Sushi2', content='Not bad.', score=4)
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.commit()
    print("评论数据插入成功。")


# 主程序执行
if __name__ == '__main__':
    # 检查并创建数据库
    check_and_create_db()

    # 创建表格并插入测试数据
    create_tables_and_insert_data()

    print("脚本执行完成！")
