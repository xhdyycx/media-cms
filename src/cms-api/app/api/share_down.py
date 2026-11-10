from blacksheep.server.controllers import APIController, json, post
from blacksheep.server.controllers import get
from blacksheep.server.authorization import auth
from app.db import get_db
from app.db.share_op import ShareDownOp

class ShareDownController(APIController):
    
    def __init__(self):
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/share_down'
    @get('list')
    @auth('pro')
    async def list(self, type: str = None, status: str = None, page: int = 1, page_size: int = 10):
        with get_db() as _var_var_0:
            _var_var_1 = ShareDownOp(_var_var_0)
            return _var_var_1.list_page(type, status, page, page_size)
    @post('delete')
    @auth('pro')
    async def delete(self, payload: dict):
        _var_var_2 = payload.get('ids')
        if not _var_var_2:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = ShareDownOp(_var_var_0)
            _var_var_1.delete_by_ids(_var_var_2)
            return json({'code': 200, 'msg': '删除成功'})
