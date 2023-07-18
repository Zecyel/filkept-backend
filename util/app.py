from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import bind_database

from service import static_service
from service import user

app = None
db = None

def create_app(name: str) -> Flask:
    global app
    app = Flask(__name__)
    bind_database(app)
    init_app(app)

    app.static_folder = 'static'
    app.register_blueprint(static_service)
    app.register_blueprint(user)

    return app

def init_app(app: Flask) -> None:
    global db
    db = SQLAlchemy(app)