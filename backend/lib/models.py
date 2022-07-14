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


class Credit(db.Model):
    __tablename__ = "credits"

    credit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    credit_owner_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    credit_value = db.Column(db.SmallInteger, nullable=False, default=10)


class Win(db.Model):
    __tablename__ = "wins"

    win_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    winner_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    won_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class Loss(db.Model):
    __tablename__ = "losses"

    loss_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loser_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    lost_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
