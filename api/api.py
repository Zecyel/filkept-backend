from dataclasses import dataclass
from json import dumps
from typing import Annotated, List, TypedDict, Dict

from flask import request

@dataclass
class ApiRule():
    method: Annotated[str, 'get', 'post']
    param: List[str]
    status: Dict[str, object]

class Api:

    @staticmethod
    def use(rule: ApiRule):

        print('Entered Api.use')
        # rule: like ['username', 'password']
        # method: 'get | 'post'
        def decorator(func):

            def wrapped_func() -> str:
                
                if rule.method == 'get':
                    kwargs = { k: request.args.get(k) for k in rule.param }
                if rule.method == 'post':
                    kwargs = { k: request.form.get(k) for k in rule.param }
                    
                ret = func(**kwargs)
                if isinstance(ret, tuple):  # return 'ok', {'token': '123'}
                    status = ret[0]; info = [1]
                else:   # return 'err'
                    status = ret; info = {}
                return dumps({**info, **rule.status[status]})

            return wrapped_func

        return decorator
