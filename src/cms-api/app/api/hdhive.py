from blacksheep import json
from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, post, get
from app.core.env import novaEnv, configEnv
from app.core.obj_factory import ObjFactory
from app.modules.hdhive.hdhive_proxy import HDHiveProxyClient

class HdHiveController(APIController):
    @classmethod
    def route(cls):
        return '/api/hdhive'
    @post('/auth_url')
    @auth('login')
    async def auth_url(self, params: dict):
        _var_var_0 = str(params.get('redirect_uri', '')).strip()
        if not _var_var_0:
            return json({'code': 400, 'msg': 'redirect_uri 不能为空'})
        _var_var_1 = ObjFactory.get_instance(HDHiveProxyClient)
        _var_var_2 = _var_var_1.build_authorize_url(params.get('redirect_uri'))
        return json({'code': 200, 'data': {'authorize_url': _var_var_2}})
    @get('/info')
    @auth('login')
    async def info(self):
        _var_var_1 = ObjFactory.get_instance(HDHiveProxyClient)
        _var_var_3 = _var_var_1.open_me()
        if _var_var_3['code'] != '200' or not _var_var_3['success']:
            return json({'code': 400, 'message': _var_var_3['message']})
        return json({'code': 200, 'data': _var_var_3['data'], 'message': '获取用户信息成功'})
    @post('/auth')
    @auth('login')
    async def auth(self, params: dict):
        try:
            _var_var_1 = ObjFactory.get_instance(HDHiveProxyClient)
            _var_var_1.open_oauth_token(code=params['code'])
            return json({'code': 200, 'msg': '授权成功'})
        except Exception as _var_var_4:
            return json({'code': 400, 'msg': f'{str(_var_var_4)}'})
