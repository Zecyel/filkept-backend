from flask import Flask
from service import static_service

app = Flask(__name__)
app.static_folder = 'static'
app.register_blueprint(static_service)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 933)