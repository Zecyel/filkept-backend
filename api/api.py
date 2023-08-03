from dataclasses import dataclass
from json import dumps
from typing import Annotated, List, TypedDict, Dict

from flask import request
from .token import verify_token, parse_token

@dataclass
class ApiRule():
    method: Annotated[str, 'get', 'post']
    param: List[str]
    status: Dict[str, dict]
    token: Annotated[str, 'check', 'require', 'ignore']

class Api:

    @staticmethod
    def use(rule: ApiRule):
        # rule: like ['username', 'password']
        # method: 'get | 'post'
        def decorator(func):
            def wrapper() -> str:
                if rule.token == 'check':
                    token = request.headers.get('token')
                    if not verify_token(token):
                        return dumps({
                            'status': 'token_error',
                            'hint': '登陆信息已过期，请重新登录！',
                            'data': {}
                        })

                if rule.method == 'get':
                    kwargs = { k: request.args.get(k) for k in rule.param }
                if rule.method == 'post':
                    kwargs = { k: request.json.get(k) for k in rule.param }
                
                if rule.token == 'require':
                    token = request.headers.get('token')
                    kwargs = { 'token': parse_token(token), **kwargs}

                print(kwargs)
                ret = func(**kwargs)
                if isinstance(ret, tuple):  # return 'ok', {'token': '123'}
                    status = ret[0]; info = ret[1]
                else:   # return 'err'
                    status = ret; info = {}

                print(info)
                return dumps({**rule.status[status], 'data': info})
            
            wrapper.__name__ = func.__name__
            return wrapper

        return decorator
