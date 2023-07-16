from flask import Blueprint

static_service = Blueprint('static_service', __name__, static_folder='../static')

@static_service.route('/')
def main():
    return static_service.send_static_file('index.html')

@static_service.route('/<path:path>')
def hello_world(path):
    print(path)
    return static_service.send_static_file(path)