from flask import Flask
from flask_cors import CORS

from service import static_service
from service import user
from service import ebook

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(static_service)
    app.register_blueprint(user)
    app.register_blueprint(ebook)

    CORS(app, resources={'*': {"origins": "*"}})

    return app
