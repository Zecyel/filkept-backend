from flask_sqlalchemy import SQLAlchemy
from .context import db

class User(db.Model):
    __bind_key__ = 'user'
    __tablename__ = 'user'

    userid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
