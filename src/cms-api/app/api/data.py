from blacksheep.server.controllers import APIController, json, post
from blacksheep.server.authorization import auth
from app.core.env import novaEnv
from app.core.media_sync import MediaSync
from app.db import get_db
from app.db.clouddata_op import CloudDataOp

class CloudDataController(APIController):
    
    def __init__(self):
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/data'
    @post('list')
    @auth('login')
    async def list(self, params: dict):
        with get_db() as _var_var_0:
            _var_var_1 = CloudDataOp(_var_var_0)
            return _var_var_1.list_dict_page(params)
    @post('delete')
    @auth('login')
    async def delete(self, payload: dict):
        _var_var_2 = payload.get('ids')
        if not _var_var_2:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_3 = MediaSync(_var_var_0)
            _var_var_3.delete_file_by_ids(_var_var_2)
            return json({'code': 200, 'msg': '删除成功'})
    @post('truncate')
    @auth('login')
    async def truncate(self, payload: dict):
        if payload.get('NOVA_API_TOKEN', '') != novaEnv.NOVA_API_TOKEN:
            return json({'code': '400', 'msg': 'NOVA_API_TOKEN 错误'})
        with get_db() as _var_var_0:
            _var_var_1 = CloudDataOp(_var_var_0)
            _var_var_1.truncate()
            return json({'code': 200, 'msg': '清空成功'})
