import time
from blacksheep import Request, Response, json
from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, get, post
from app.core.env import novaEnv
from app.core.license import LicenseInfo
from app.db import get_db
from app.db.config_op import ConfigOp
from app.log import logger
from app.modules.emby.emby import EmbyApi
from app.services.emby_service import EmbyNotificationService
from app.utils.mjson import JsonUtils

class EmbyController(APIController):
    @classmethod
    def route(cls):
        return '/api/emby'
    
    def __init__(self):
        super().__init__()
        self.emby_api = EmbyApi()
    @get('/users')
    @auth('login')
    async def users(self, page: int = 1, page_size: int = 10, keyword: str = None) -> Response:
        if page < 1 or page_size < 1:
            return json({'code': 400, 'msg': 'page 和 page_size 必须大于 0'})
        _var_var_0 = self.emby_api.get_users(page, page_size, keyword)
        with get_db() as _var_var_1:
            _var_var_2 = 'emby_bind_115'
            _var_var_3 = ConfigOp(_var_var_1)
            _var_var_4 = _var_var_3.get_by_key(_var_var_2)
            _var_var_5 = _var_var_0['data']
            if _var_var_5:
                for _var_var_6 in _var_var_5:
                    _var_var_7 = _var_var_6.get('emby_id')
                    _var_var_8 = _var_var_4.get(_var_var_7, '')
                    if not _var_var_8:
                        continue
                    _var_var_9 = _var_var_8.split('#')
                    _var_var_6['bind_115_id'] = _var_var_9[0]
                    _var_var_6['bind_115_username'] = _var_var_9[1]
                    _var_var_6['bind_115_cid'] = _var_var_9[2]
        if _var_var_0 is None:
            return json({'code': 500, 'msg': '获取 Emby 用户列表失败'})
        return json({'code': 200, **_var_var_0})
    @post('/webhook')
    async def emby_webhook(self, request: Request) -> Response:
        try:
            _var_var_10 = request.query.get('token')
            if not _var_var_10:
                return json({'code': '400', 'message': 'token为空'})
            _var_var_10 = _var_var_10[0]
            if _var_var_10 != novaEnv.NOVA_API_TOKEN:
                return json({'code': '400', 'message': 'token错误'})
            if LicenseInfo().is_free():
                return json({'code': '400', 'message': '当前配置不支持此功能'})
            _var_var_5 = await request.json()
            with get_db() as _var_var_1:
                _var_var_11 = EmbyNotificationService(_var_var_1)
                _var_var_11.handle_notification(_var_var_5)
            return json({'status': 'success'})
        except Exception as _var_var_12:
            logger.info(f'处理 Emby Webhook 失败: {str(_var_var_12)}')
            return json({'status': 'error', 'message': str(_var_var_12)})
