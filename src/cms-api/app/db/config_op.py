import os
from app.core.env import ConfigEnv
from app.db import DbOp
from app.db.models.cmsconfig import NovaConfig
from app.utils.mjson import JsonUtils

class ConfigOp(DbOp):
    _cache = { }
    
    def get_by_key(self, key):
        if key in self._cache:
            return self._cache[key]
        _var_var_0 = NovaConfig.get_by_key(self._db, key)
        if _var_var_0:
            _var_var_1 = JsonUtils.json_to_dict(_var_var_0.config_json)
            self._cache[key] = _var_var_1
            return _var_var_1
        if key == 'auto_organize':
            return {
                'CATEGORY_POLICY_URL': '/config/category.yaml',
                'NEW_MEDIA_CID': '',
                'NEW_MEDIA_CID_PATH': '',
                'REDUNDANT_DATA_CID': '',
                'REDUNDANT_DATA_CID_PATH': '',
                'NEW_MEDIA_EXISTS_CID': '',
                'NEW_MEDIA_EXISTS_CID_PATH': '',
                'RENAME_MEDIA_DIR_FORMAT': 1,
                'RENAME_MEDIA_VIDEO': 1,
                'NEW_MEDIA_FAILED_CID': '',
                'NEW_MEDIA_FAILED_CID_PATH': '' }
        if key == 'full_sync':
            return {
                'MEDIA_115_CID': '',
                'MEDIA_115_CID_PATH': '',
                'LOCAL_PATH': '/media',
                'VIDEO_SUFFIX': [],
                'IMAGE_SUFFIX': [],
                'MEDIA_DATA_SUFFIX': [] }
        if key == 'core':
            return {
                'basic': {
                    'COOKIE_FILE_PATH': '/config/115-cookies.txt',
                    'DEVICE_TYPE': 'ios' },
                'strm': {
                    'DIRECT_115_302_DOMAIN': 'http://172.17.0.1:9527',
                    'STRM_TYPE': 'pick_code_name',
                    'STRM_EXIST_IS_REBUILD': False },
                'tmdb': {
                    'TMDB_API_DOMAIN': 'https://api.tmdb.org',
                    'TMDB_IMG_DOMAIN': 'https://image.tmdb.org',
                    'TMDB_API_KEY': '' } }
        if key == 'incremental_sync':
            return {
                'SYNC_CRON': '*/20 8-23 * * *' }
        if key == 'monitor':
            return {
                'MONITOR_PATH': '' }
        return {}

    def get_all(self):
        _var_var_0 = { }
        _var_var_0.update(self.get_by_key('auto_organize'))
        _var_var_0.update(self.get_by_key('full_sync'))
        _var_var_0.update(self.get_by_key('core'))
        _var_var_0.update(self.get_by_key('incremental_sync'))
        _var_var_0.update(self.get_by_key('monitor'))
        return _var_var_0
        return None

    
    def init_env(self):
        _var_var_2 = NovaConfig.list(self._db)
        for _var_var_3 in _var_var_2:
            _var_var_1 = JsonUtils.json_to_dict(_var_var_3.config_json)
            
            def _var_var_4(key, value):
                if isinstance(value, dict):
                    for _var_var_7, _var_var_8 in value.items():
                        if _var_var_7 == 'HTTP_PROXY':
                            continue
                        os.environ[_var_var_7] = str(_var_var_8)
                elif key != 'HTTP_PROXY':
                    os.environ[key] = str(value)
                return None
                return None

            for _var_var_5, _var_var_6 in _var_var_1.items():
                _var_var_4(_var_var_5, _var_var_6)
        return None
        return None

    
    def update(self, key: str = '', config_json=None):
        if config_json is None:
            config_json = {}
        _var_var_0 = NovaConfig.get_by_key(self._db, key)
        if _var_var_0:
            _var_var_0.config_json = JsonUtils.to_str(config_json)
            _var_var_0.update(self._db, _var_var_0.to_dict())
        else:
            _var_var_0 = NovaConfig(key=key, config_json=JsonUtils.to_str(config_json))
            _var_var_0.create(self._db)
        if key in self._cache:
            del self._cache[key]
        self.init_env()
        ConfigEnv().refresh()

