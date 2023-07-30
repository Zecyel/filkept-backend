from flask import Flask
from flask_cors import CORS

from service import static_service
from service import user

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(static_service)
    app.register_blueprint(user)

    CORS(app, resources={'*': {"origins": "*"}})

    return app
