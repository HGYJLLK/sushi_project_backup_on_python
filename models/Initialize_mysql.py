from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import pymysql

# 数据库配置
DB_USER = 'root'
DB_PASSWORD = '123qweQWE!'
DB_HOST = 'localhost'
DB_NAME = 'sushi_db'

# 初始化 Flask 应用
app = Flask(__name__)


# 创建一个函数来初始化数据库连接
def init_db():
    # 首先连接到 MySQL 服务器（不指定具体数据库）
    root_engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/')

    try:
        # 检查数据库是否存在
        with root_engine.connect() as conn:
            # 先尝试删除已存在的数据库
            conn.execute(text(f"DROP DATABASE IF EXISTS {DB_NAME}"))
            conn.commit()

            # 创建新数据库
            conn.execute(text(f"CREATE DATABASE {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
            conn.commit()
            print(f"数据库 {DB_NAME} 创建成功。")
    except Exception as e:
        print(f"创建数据库时出错: {str(e)}")
        raise
    finally:
        root_engine.dispose()


# 初始化数据库
init_db()

# 配置实际的应用数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
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

# 管理员模型
class Admin(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime)


def create_tables():
    with app.app_context():
        try:
            db.create_all()
            print("表格创建成功。")
        except Exception as e:
            print(f"创建表格时出错: {str(e)}")
            raise


# 主程序执行
if __name__ == '__main__':
    try:
        # 创建表格
        create_tables()
        print("脚本执行完成！")
    except Exception as e:
        print(f"程序执行出错: {str(e)}")