from flask import Blueprint

static_service = Blueprint('static_service', __name__, static_folder='../static', url_prefix = '/static')

@static_service.route('/')
def main():
    print('Entered')
    return static_service.send_static_file('index.html')

@static_service.route('/assets/<path:path>')    # I don't know why but it has to be like this
def fetch_asset_file(path):
    return static_service.send_static_file('assets/' + path)