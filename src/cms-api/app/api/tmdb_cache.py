from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, get, json, post
from sqlalchemy.exc import IntegrityError
from app.db import get_db
from app.db.models.tmdb_cache import TmdbCache
from app.db.tmdb_cache_op import TmdbCacheOp
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.mjson import JsonUtils

class TmdbCacheController(APIController):
    
    def __init__(self):
        self.tmdbapi = TmdbApi()
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/tmdb_cache'
    @get('list')
    @auth('login')
    async def list(self, type: str = None, status: str = None, title: str = None, tmdb_id: str = None, page: int = 1, page_size: int = 10):
        with get_db() as _var_var_0:
            _var_var_1 = TmdbCacheOp(_var_var_0)
            _var_var_2 = _var_var_1.list_page(type, status, title, tmdb_id, page, page_size)
            _var_var_2['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json(_var_var_2)
    @get('get')
    @auth('login')
    async def get(self, id: int):
        with get_db() as _var_var_0:
            _var_var_1 = TmdbCacheOp(_var_var_0)
            _var_var_3 = _var_var_1.get(id)
            if not _var_var_3:
                return json({'code': 404, 'msg': '数据不存在'})
            return json({'code': 200, 'data': _var_var_3})
    @post('add')
    @auth('pro')
    async def add(self, payload: dict):
        _var_var_4 = payload.get('query_url')
        with get_db() as _var_var_0:
            _var_var_1 = TmdbCacheOp(_var_var_0)
            if _var_var_4 and _var_var_1.get_by_query_url(_var_var_4):
                return json({'code': 400, 'msg': '已存在，无需重复添加'})
            _var_var_5 = TmdbCache(**payload)
            try:
                _var_var_1.save(_var_var_5)
                return json({'code': 200, 'msg': '添加成功', 'data': _var_var_5.to_dict()})
            except IntegrityError:
                return json({'code': 400, 'msg': '已存在，无需重复添加'})
    @post('update')
    @auth('pro')
    async def update(self, payload: dict):
        if not payload.get('id'):
            return json({'code': 400, 'msg': 'id不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = TmdbCacheOp(_var_var_0)
            _var_var_6 = payload.get('query_response', '{}')
            _var_var_6 = JsonUtils.json_to_dict(_var_var_6)
            _var_var_7 = _var_var_6.get('title') or _var_var_6.get('name')
            if _var_var_7:
                payload['title'] = _var_var_7
            if _var_var_6.get('poster_path'):
                payload['poster_path'] = _var_var_6.get('poster_path')
            if _var_var_6.get('backdrop_path'):
                payload['backdrop_path'] = _var_var_6.get('backdrop_path')
            _var_var_8 = _var_var_1.update_cache(payload)
            if not _var_var_8:
                return json({'code': 404, 'msg': '数据不存在'})
            return json({'code': 200, 'msg': '更新成功'})
    @post('delete')
    @auth('pro')
    async def delete(self, payload: dict):
        _var_var_9 = payload.get('ids')
        if not _var_var_9:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = TmdbCacheOp(_var_var_0)
            _var_var_1.delete_by_ids(_var_var_9)
            return json({'code': 200, 'msg': '删除成功'})
