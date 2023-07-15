from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def hello_world(path):
    print(path)
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 933)