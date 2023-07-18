from .blueprint import user
from .context import User as User
from flask import request

@user.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.get(username).password == password:
        return 