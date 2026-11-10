from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, get, json, post
from app.core.emby_user import emby_user_util
from app.db import get_db
from app.db.account_op import Account115Op
from app.db.config_op import ConfigOp
from app.db.models.account import Account115
ACCOUNT_115_FIELDS = {
    'type',
    'cookie',
    'status',
    'user_id',
    'username',
    'cookie_type'}

class Account115Controller(APIController):
    @classmethod
    def route(cls):
        return '/api/account_115'
    @get('list')
    @auth('login')
    async def list(self, username: str = None, type: str = None, status: str = None, page: int = 1, page_size: int = 10):
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            _var_var_2 = _var_var_1.list_page(username, type, status, page, page_size)
            if _var_var_2 and _var_var_2.get('data'):
                for _var_var_3 in _var_var_2.get('data'):
                    if 'cookie' in _var_var_3:
                        del _var_var_3['cookie']
            return json(_var_var_2)
    @get('get')
    @auth('login')
    async def get(self, id: int):
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            _var_var_4 = _var_var_1.get(id)
            if not _var_var_4:
                return json({'code': 404, 'msg': '数据不存在'})
            return json({'code': 200, 'data': _var_var_4})
    @post('add')
    @auth('login')
    async def add(self, payload: dict):
        _var_var_5 = payload.get('username')
        if not _var_var_5:
            return json({'code': 400, 'msg': 'username不能为空'})
        _var_var_6 = self._filter_payload(payload)
        _var_var_6.setdefault('type', 2)
        _var_var_6.setdefault('status', 1)
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            if _var_var_1.get_by_username(_var_var_5):
                return json({'code': 400, 'msg': '账号已存在'})
            _var_var_3 = Account115(**_var_var_6)
            _var_var_1.save(_var_var_3)
            return json({'code': 200, 'msg': '添加成功', 'data': _var_var_3.to_dict()})
    @post('update')
    @auth('login')
    async def update(self, payload: dict):
        if not payload.get('id'):
            return json({'code': 400, 'msg': 'id不能为空'})
        _var_var_6 = self._filter_payload(payload)
        _var_var_6['id'] = payload['id']
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            _var_var_7 = _var_var_1.update_account(_var_var_6)
            if not _var_var_7:
                return json({'code': 404, 'msg': '数据不存在'})
            emby_user_util.refresh_cache()
            return json({'code': 200, 'msg': '更新成功'})
    @post('delete')
    @auth('login')
    async def delete(self, payload: dict):
        _var_var_8 = payload.get('ids')
        if not _var_var_8:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            _var_var_1.delete_by_ids(_var_var_8)
            emby_user_util.refresh_cache()
            return json({'code': 200, 'msg': '删除成功'})
    @post('bind_115_account')
    @auth('login')
    async def bind_115_account(self, payload: dict):
        _var_var_9 = payload['bind_id']
        _var_var_10 = payload.get('bind_username')
        _var_var_11 = payload['cid']
        _var_var_12 = payload['emby_id']
        with get_db() as _var_var_0:
            _var_var_13 = 'emby_bind_115'
            _var_var_14 = ConfigOp(_var_var_0)
            _var_var_15 = _var_var_14.get_by_key(_var_var_13)
            if _var_var_9 == 0:
                if _var_var_15 and _var_var_12 in _var_var_15:
                    del _var_var_15[_var_var_12]
                    _var_var_14.update(_var_var_13, _var_var_15)
                emby_user_util.refresh_cache()
                return json({'code': 200, 'msg': '解绑成功'})
            if _var_var_15:
                _var_var_15[_var_var_12] = f'{_var_var_9}#{_var_var_10}#{_var_var_11}'
            else:
                _var_var_15 = {_var_var_12: f'{_var_var_9}#{_var_var_10}#{_var_var_11}'}
            _var_var_14.update(_var_var_13, _var_var_15)
            emby_user_util.refresh_cache()
            return json({'code': 200, 'msg': '绑定成功'})
    @staticmethod
    def _filter_payload(payload: dict) -> dict:
        return {_var_var_13: _var_var_16 for _var_var_13, _var_var_16 in payload.items() if _var_var_13 in ACCOUNT_115_FIELDS}


