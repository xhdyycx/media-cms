from blacksheep.server.responses import json
from blacksheep.server.controllers import APIController, post
from app.core.auth import create_access_token
from app.core.env import NovaEnv
from app.core.license import LicenseInfo
from app.db import get_db
from app.db.user_op import UserOp

class AuthController(APIController):
    
    def __init__(self):
        self._CMS_ENV = NovaEnv()
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/auth'
    @post('login')
    async def login(self, credentials: dict):
        _var_var_0 = credentials.get('username')
        _var_var_1 = credentials.get('password')
        if not _var_var_0 or not _var_var_1:
            return json({'code': 400, 'msg': '用户名和密码不能为空'})
        with get_db() as _var_var_2:
            _var_var_3 = UserOp(_var_var_2)
            _var_var_4 = _var_var_3.login(_var_var_0, _var_var_1)
            if not _var_var_4:
                return json({'code': 400, 'msg': '用户名或密码错误'})
            _var_var_5 = create_access_token({'username': _var_var_0, 'id': _var_var_4.id})
            _var_var_6 = LicenseInfo().get_type()
            return json({'code': 200, 'data': {'version': f'{self._CMS_ENV.APP_VERSION} - {_var_var_6}', 'permission': _var_var_6, 'token': _var_var_5, 'id': _var_var_4.id, 'username': _var_var_4.username}})
