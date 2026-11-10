from pydantic import BaseModel
from app.core.m115v2 import M115v2
from app.db import get_db
from app.db.account_op import Account115Op
from app.db.config_op import ConfigOp

class EmbyBind(BaseModel):
    emby_id: str | int = None
    bind_id: str | int = None
    bind_username: str = None
    cid: str | None = None
    cookie: str = None


class EmbyUserUtils:
    EMBY_115_CACHE: dict[(str | int, EmbyBind)] = {}
    M115_CACHE: dict[(str | int, M115v2)] = {}
    
    def __init__(self):
        pass
    
    def refresh_cache(self):
        self.EMBY_115_CACHE.clear()
        self.M115_CACHE.clear()
        with get_db() as _var_var_0:
            _var_var_1 = Account115Op(_var_var_0)
            _var_var_2 = ConfigOp(_var_var_0)
            _var_var_3 = _var_var_2.get_by_key('emby_bind_115')
            if _var_var_3:
                for _var_var_4, _var_var_5 in _var_var_3.items():
                    (_var_var_6, _var_var_7, _var_var_8) = _var_var_5.split('#')
                    _var_var_9 = _var_var_1.get(_var_var_6)
                    if not _var_var_9:
                        continue
                    _var_var_10 = _var_var_9.get('cookie') if isinstance(_var_var_9, dict) else getattr(_var_var_9, 'cookie', None)
                    self.EMBY_115_CACHE[_var_var_4] = EmbyBind(emby_id=_var_var_4, bind_id=_var_var_6, bind_username=_var_var_7, cid=_var_var_8, cookie=_var_var_10)
                    self.M115_CACHE[_var_var_4] = M115v2(cookies=_var_var_10)
            _var_var_11 = _var_var_1.get_all(type=3, status=1)
            if _var_var_11:
                for _var_var_9 in _var_var_11:
                    cookie = _var_var_9.get('cookie') if isinstance(_var_var_9, dict) else getattr(_var_var_9, 'cookie', None)
                    item_id = _var_var_9.get('id') if isinstance(_var_var_9, dict) else getattr(_var_var_9, 'id', None)
                    self.M115_CACHE[str(item_id)] = M115v2(cookies=cookie)

    def get_cache(self, emby_id):
        if not emby_id:
            return None
        return self.EMBY_115_CACHE.get(emby_id)

    def get_cache_m115(self, emby_id):
        if not emby_id:
            return None
        if self.M115_CACHE.get(emby_id):
            return self.M115_CACHE.get(emby_id)
        if self.EMBY_115_CACHE.get(emby_id):
            _var_var_12 = M115v2(cookies=self.EMBY_115_CACHE.get(emby_id).cookie)
            self.M115_CACHE[emby_id] = _var_var_12
            return _var_var_12
        return None

emby_user_util = EmbyUserUtils()