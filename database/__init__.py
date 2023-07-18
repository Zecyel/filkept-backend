from flask import Flask

def bind_database(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database/data/user.db'
    app.config["SQLALCHEMY_BINDS"] = {
        'user': 'sqlite:///database/data/user.db'
    }