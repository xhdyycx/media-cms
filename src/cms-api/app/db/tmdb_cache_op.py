from app.db import DbOp
from app.db.models.tmdb_cache import TmdbCache

class TmdbCacheOp(DbOp):
    @staticmethod
    def _to_int(value, default=None):
        if value is None or value == '':
            return default
        return int(value)
    
    def save(self, cache):
        cache.create(self._db)
        return None
        return None

    
    def get(self, rid):
        _var_var_0 = TmdbCache.get(self._db, rid)
        return _var_var_0.to_dict() if _var_var_0 else None
        return None

    
    def get_by_query_url(self, query_url):
        _var_var_0 = TmdbCache.get_by_query_url(self._db, query_url)
        return _var_var_0.to_dict() if _var_var_0 else None
        return None

    
    def get_tmdb_cache(self, type, tmdb_id, season_num):
        season_num = self._to_int(season_num)
        _var_var_0 = TmdbCache.get_tmdb_cache(self._db, type, tmdb_id, season_num)
        return _var_var_0.to_dict() if _var_var_0 else None
        return None

    
    def update_cache(self, cache):
        _var_var_1 = TmdbCache.get(self._db, cache['id'])
        if _var_var_1:
            _var_var_1.update(self._db, cache)
        return _var_var_1
        return None

    
    def delete_by_ids(self, ids):
        TmdbCache.delete_by_ids(self._db, ids)
        return None
        return None

    
    def list_page(self, type: str = None, status: int = None, title: str = None, tmdb_id: str = None, page: int = 1, page_size: int = 10):
        status = self._to_int(status)
        page = self._to_int(page, 1)
        page_size = self._to_int(page_size, 10)
        _var_var_2 = TmdbCache.list_page(self._db, type, status, title, tmdb_id, page, page_size)
        if _var_var_2 and _var_var_2.get('data'):
            _var_var_2['data'] = [_var_var_0.to_dict() for _var_var_0 in _var_var_2.get('data')]
        else:
            _var_var_2['data'] = []
        _var_var_2['code'] = 200
        return _var_var_2

