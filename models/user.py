# models/user.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120))
    likes = db.relationship('Like', backref='user', lazy=True)
    favorites = db.relationship('Favorite', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Like(db.Model):
    __tablename__ = 'likes'
    username = db.Column(db.String(80), db.ForeignKey('users.username'), primary_key=True)
    sushi_name = db.Column(db.String(50), primary_key=True)

    def __repr__(self):
        return f'<Like {self.username} - {self.sushi_name}>'

class Favorite(db.Model):
    __tablename__ = 'favorites'
    username = db.Column(db.String(80), db.ForeignKey('users.username'), primary_key=True)
    sushi_name = db.Column(db.String(50), primary_key=True)

    def __repr__(self):
        return f'<Favorite {self.username} - {self.sushi_name}>'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), db.ForeignKey('users.username'))
    sushi_name = db.Column(db.String(50))
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)  # 1-5星评分
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.id}>'