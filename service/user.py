from api import Rule
from api.api import Api
from api.token import generate_token
from database.orm import ORM
from flask import Blueprint

user = Blueprint('User', __name__, url_prefix = '/user')

UserRule = Rule['User']
UserORM = ORM['User']

@user.route('/login', methods = ['POST'])
@Api.use(UserRule['Login'])
def login(username, password):
    if UserORM.login(username, password):
        return 'ok', { 'token':  generate_token({
            'username': username
        }) }
    else:
        return 'err'
    
@user.route('/register', methods = ['POST'])
@Api.use(UserRule['Register'])
def register(username, password):
    if UserORM.register(username, password):
        return 'ok'
    else:
        return 'repl'