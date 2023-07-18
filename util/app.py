from flask import Flask

from service import static_service
from service import user

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(static_service)
    app.register_blueprint(user)

    return app
