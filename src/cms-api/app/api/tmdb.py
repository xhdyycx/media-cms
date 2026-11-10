from blacksheep.server.controllers import APIController, json, post, get
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.mexception import MExcUtils

class TmdbController(APIController):
    
    def __init__(self):
        self.tmdbapi = TmdbApi()
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/tmdb'
    @get('search_movie')
    async def search_movie(self, keyword: str = None, primary_release_year: str = None, page: int = 1):
        if not self.tmdbapi.is_available():
            return json({'code': 400, 'msg': 'TMDB API 不可用, 请检查tmdb配置'})
        try:
            _var_var_0 = self.tmdbapi.search_movie(keyword, primary_release_year, page)
            _var_var_1 = _var_var_0._json
            _var_var_1['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            MExcUtils.log(_var_var_2)
            return json({'code': 400, 'msg': 'tmdb配置不可用，或请求tmdb失败'})
    @get('search_tv')
    async def search_tv(self, keyword: str = None, primary_release_year: str = None, page: int = 1):
        if not self.tmdbapi.is_available():
            return json({'code': 400, 'msg': 'TMDB API 不可用, 请检查tmdb配置'})
        try:
            _var_var_0 = self.tmdbapi.search_tv(keyword, primary_release_year, page)
            _var_var_1 = _var_var_0._json
            _var_var_1['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            MExcUtils.log(_var_var_2)
            return json({'code': 400, 'msg': 'tmdb配置不可用，或请求tmdb失败'})
    @post('discover_tv')
    async def discover_tv(self, params: dict):
        if not self.tmdbapi.is_available():
            return json({'code': 400, 'msg': 'TMDB API 不可用, 请检查tmdb配置'})
        try:
            _var_var_0 = self.tmdbapi.discover_tv(params)
            _var_var_1 = _var_var_0._json
            _var_var_1['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            MExcUtils.log(_var_var_2)
            return json({'code': 400, 'msg': 'tmdb配置不可用，或请求tmdb失败'})
    @post('discover_movie')
    async def discover_movie(self, params: dict):
        if not self.tmdbapi.is_available():
            return json({'code': 400, 'msg': 'TMDB API 不可用, 请检查tmdb配置'})
        try:
            _var_var_0 = self.tmdbapi.discover_movie(params)
            _var_var_1 = _var_var_0._json
            _var_var_1['img_domain'] = self.tmdbapi.novaenv.tmdb_img_domain
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            MExcUtils.log(_var_var_2)
            return json({'code': 400, 'msg': 'tmdb配置不可用，或请求tmdb失败'})
