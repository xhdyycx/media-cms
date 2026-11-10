from app.utils.mjson import JsonUtils

class AutoOrganizeConfig:
    MP_API_DOMAIN: str
    MP_API_TOKEN: str
    NEW_MEDIA_CID: str
    NEW_MEDIA_CID_PATH: str
    REDUNDANT_DATA_CID: str
    REDUNDANT_DATA_CID_PATH: str
    NEW_MEDIA_EXISTS_CID: str
    NEW_MEDIA_EXISTS_CID_PATH: str
    MOVIE_DIR_RENAME_RULE: str
    MOVIE_FILE_RENAME_RULE: str
    TV_DIR_RENAME_RULE: str
    TV_FILE_RENAME_RULE: str
    
    def __init__(self, config_json=None):
        if config_json is None:
            config_json = {}
        self.INCREMENT_SYNC_STATE = config_json.get('INCREMENT_SYNC_STATE')
        self.MONITOR_UPLOAD_STATE = config_json.get('MONITOR_UPLOAD_STATE')
        self.AUTO_ORGANIZE_STATE = config_json.get('AUTO_ORGANIZE_STATE')
        self.WECHAT_NOTIFY_STATE = config_json.get('WECHAT_NOTIFY_STATE')
        self.TG_NOTIFY_STATE = config_json.get('TG_NOTIFY_STATE')
class BasicConfig:
    COOKIE_FILE_PATH: str
    DEVICE_TYPE: str
    
    def __init__(self, config_json):
        if config_json is None:
            config_json = {}
        self.COOKIE_FILE_PATH = config_json.get('COOKIE_FILE_PATH')
        self.DEVICE_TYPE = config_json.get('DEVICE_TYPE')


class TmdbConfig:
    '''TMDB配置'''
    TMDB_API_DOMAIN: str
    TMDB_IMG_DOMAIN: str
    TMDB_API_KEY: str
    
    def __init__(self, config_json):
        if config_json is None:
            config_json = {}
        self.COOKIE_FILE_PATH = config_json.get('COOKIE_FILE_PATH')
        self.DEVICE_TYPE = config_json.get('DEVICE_TYPE')


class ServiceConfig:
    '''服务配置'''
    INCREMENT_SYNC_STATE: bool
    MONITOR_UPLOAD_STATE: bool
    AUTO_ORGANIZE_STATE: bool
    WECHAT_NOTIFY_STATE: bool
    TG_NOTIFY_STATE: bool
    
    def __init__(self, config_json):
        if config_json is None:
            config_json = {}
        self.COOKIE_FILE_PATH = config_json.get('COOKIE_FILE_PATH')
        self.DEVICE_TYPE = config_json.get('DEVICE_TYPE')


