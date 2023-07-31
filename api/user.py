from .api import ApiRule

Login = ApiRule(
    method = 'post',
    param = ['username', 'password'],
    status = {
        'ok': {
            'status': 'success',
            'hint': '登录成功！'
        },
        'err': {
            'status': 'error',
            'hint': '用户名或密码错误'
        }
    },
    token = 'ignore'
)

Register = ApiRule(
    method = 'post',
    param = ['username', 'password'],
    status = {
        'ok': {
            'status': 'success',
            'hint': '注册成功！'
        },
        'repl': {
            'status': 'error',
            'hint': '用户名重复'
        }
    },
    token = 'ignore'
)

UserRule = {
    'Login': Login,
    'Register': Register
}