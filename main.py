from flask import redirect
from util import create_app

app = create_app()

@app.route('/')
def index_page():
    return redirect('/static')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 933)