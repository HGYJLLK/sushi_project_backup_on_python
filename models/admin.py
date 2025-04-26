from models.user import db
from datetime import datetime


class Admin(db.Model):
    __tablename__ = "admins"
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Admin {self.username}>"
