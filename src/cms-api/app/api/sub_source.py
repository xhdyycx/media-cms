from blacksheep.server.controllers import APIController, json, post
from blacksheep.server.controllers import get
from blacksheep.server.authorization import auth
from app.db import get_db
from app.db.models.subsource import SubSource
from app.db.sub_op import SubSourceOp

class SubSourceController(APIController):
    
    def __init__(self):
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/subsource'
    @get('list')
    @auth('login')
    async def list(self, type: str = None, status: str = None):
        with get_db() as _var_var_0:
            _var_var_1 = SubSourceOp(_var_var_0)
            _var_var_2 = _var_var_1.list(type, status)
            _var_var_3 = []
            for _var_var_4 in _var_var_2:
                _var_var_3.append(_var_var_4.to_dict())
            return json({'code': 200, 'data': _var_var_3})
    @post('add')
    @auth('pro')
    async def add(self, payload: dict):
        payload = SubSource(**payload)
        with get_db() as _var_var_0:
            _var_var_1 = SubSourceOp(_var_var_0)
            _var_var_1.save(payload)
            return json({'code': 200, 'msg': '添加成功'})
    @post('update')
    @auth('pro')
    async def update(self, payload: dict):
        with get_db() as _var_var_0:
            _var_var_1 = SubSourceOp(_var_var_0)
            _var_var_1.update_sub(payload)
            return json({'code': 200, 'msg': '更新成功'})
    @post('delete')
    @auth('pro')
    async def delete(self, payload: dict):
        _var_var_5 = payload.get('ids')
        if not _var_var_5:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = SubSourceOp(_var_var_0)
            _var_var_1.delete_by_ids(_var_var_5)
            return json({'code': 200, 'msg': '删除成功'})
