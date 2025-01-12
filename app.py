from flask import Flask, send_from_directory
from flask_cors import CORS
from models.user import db
from views.user import user_bp
from views.sushi import sushi_bp
from views.sushi_interaction import sushi_interaction_bp
import os

app = Flask(__name__)
CORS(app)


# 保持原有的图片路由
@app.route('/controllers/sushi_img/<path:filename>')
def serve_sushi_image(filename):
    return send_from_directory('controllers/sushi_img', filename)


# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/sushi_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

# 初始化数据库
db.init_app(app)

# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/api/auth')
app.register_blueprint(sushi_bp, url_prefix='/api/sushi')  # 原有的寿司路由
app.register_blueprint(sushi_interaction_bp, url_prefix='/api/sushi/actions')  # 新的交互功能

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 确保数据库表已创建
    app.run(debug=True, port=5001)
