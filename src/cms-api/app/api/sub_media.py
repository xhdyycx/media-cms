from blacksheep.server.controllers import APIController, json, post
from blacksheep.server.controllers import get
from blacksheep.server.authorization import auth
from app.db import get_db
from app.db.models.submedia import SubMedia
from app.db.sub_op import SubMediaOp
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.mjson import JsonUtils

class SubMediaController(APIController):
    
    def __init__(self):
        self.tmdbapi = TmdbApi()
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/submedia'
    @get('list')
    @auth('login')
    async def list(self, type: str = None, status: str = None, page: int = 1, page_size: int = 10):
        with get_db() as _var_var_0:
            _var_var_1 = SubMediaOp(_var_var_0)
            _var_var_2 = _var_var_1.list_page(type, status, page, page_size)
            _var_var_2['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json(_var_var_2)
    @post('add')
    @auth('pro')
    async def add(self, payload: dict):
        payload = SubMedia(**payload)
        with get_db() as _var_var_0:
            _var_var_1 = SubMediaOp(_var_var_0)
            if payload.type == 'tv':
                _var_var_3 = self.tmdbapi.get_tv_season_list(payload.tmdb_id)
                _var_var_4, _var_var_5 = self.tmdbapi.get_tv_max_season_episode(_var_var_3)
                payload.season_info = JsonUtils.to_str(_var_var_3)
                payload.max_season = _var_var_4
                payload.max_season_episodes = _var_var_5
            return json(_var_var_1.save(payload))
    @post('update')
    @auth('pro')
    async def update(self, payload: dict):
        with get_db() as _var_var_0:
            _var_var_1 = SubMediaOp(_var_var_0)
            _var_var_1.update_sub(payload)
            return json({'code': 200, 'msg': '更新成功'})
    @post('delete')
    @auth('pro')
    async def delete(self, payload: dict):
        _var_var_6 = payload.get('ids')
        if not _var_var_6:
            return json({'code': 400, 'msg': 'ids不能为空'})
        with get_db() as _var_var_0:
            _var_var_1 = SubMediaOp(_var_var_0)
            _var_var_1.delete_by_ids(_var_var_6)
            return json({'code': 200, 'msg': '删除成功'})
