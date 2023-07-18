from .blueprint import user
from .context import ORM, Api, Rule
from flask import request

UserRule = Rule['User']
UserORM = ORM['User']

@user.route('/login', methods = ['POST'])
@Api.use(UserRule['Login'])
def login(username, password):
    if UserORM.login(username, password):
        return 'ok', { 'token': '123' }
    else:
        return 'err'