from datetime import datetime

import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Article(db.Model):
    __tablename__ = "articles"

    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
