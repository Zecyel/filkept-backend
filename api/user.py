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
    }
    token = 'ignore'
)

UserRule = {
    'Login': Login
}