import os
from app.utils.mjson import JsonUtils
from app.utils.singleton import Singleton

class Config2Env(metaclass=Singleton):
    '''Config2Env'''
    @property
    def def_http_proxies(self):
        _var_var_0 = os.getenv('HTTP_PROXY')
        if _var_var_0:
            return {'http': _var_var_0, 'https': _var_var_0}
    @property
    def m123_fid(self):
        return os.getenv('M123_FID', '')
    @property
    def m123_fid_path(self):
        return os.getenv('M123_FID_PATH', '')
    @property
    def m123_strm_path(self):
        return os.getenv('M123_STRM_PATH', '/media/123')
    @property
    def m123_video_suffix(self):
        return os.getenv('M123_VIDEO_SUFFIX', [])
    @property
    def m123_image_suffix(self):
        return os.getenv('M123_IMAGE_SUFFIX', [])
    @property
    def m123_media_data_suffix(self):
        return os.getenv('M123_MEDIA_DATA_SUFFIX', [])
    @property
    def m123_min_size(self):
        _var_var_1 = os.getenv('M123_MIN_SIZE', '0')
        try:
            return int(_var_var_1) * 1024 * 1024
        except ValueError:
            print('M123_MIN_SIZE ERROR')
            return 0
    @property
    def m123_download_threads(self):
        try:
            return int(os.getenv('M123_DOWNLOAD_THREADS', 3))
        except ValueError:
            print('M123_DOWNLOAD_THREADS ERROR')
            return 3
    @property
    def m123_sync_cron(self):
        return os.getenv('M123_SYNC_CRON')
    @property
    def m123_tidy_cron(self):
        return os.getenv('M123_TIDY_CRON')
    @property
    def m123_tidy_dir_id(self):
        return os.getenv('M123_TIDY_DIR_ID')
    @property
    def m123_tidy_dir_id_path(self):
        return os.getenv('M123_TIDY_DIR_ID_PATH')
    @property
    def m123_md5_repeat_id(self):
        return os.getenv('M123_MD5_REPEAT_ID', 18562666)
    @property
    def m123_md5_repeat_id_path(self):
        return os.getenv('M123_MD5_REPEAT_ID_PATH')
    @property
    def m123_redundant_data_id(self):
        return os.getenv('M123_REDUNDANT_DATA_ID')
    @property
    def m123_redundant_data_id_path(self):
        return os.getenv('M123_REDUNDANT_DATA_ID_PATH')
    @property
    def e_123_dir_del_cron(self):
        return os.getenv('E_123_DIR_DEL_CRON')
    @property
    def e_123_dir_del_cid(self):
        _var_var_2 = os.getenv('E_123_DIR_DEL_CID')
        if not _var_var_2:
            return []
        _var_var_2 = _var_var_2.split('\n')
        return [int(_var_var_3.strip()) for _var_var_3 in _var_var_2 if _var_var_3.strip() and not _var_var_3.strip().startswith('#')]
    @property
    def e_123_dir_del_days(self):
        return int(os.getenv('E_123_DIR_DEL_DAYS', '0'))
    @property
    def e_123_recycle_del_cron(self):
        return os.getenv('E_123_RECYCLE_DEL_CRON')
    @property
    def e_123_recycle_del_days(self):
        return int(os.getenv('E_123_RECYCLE_DEL_DAYS', '0'))
    @property
    def e_123_dir_del_status(self):
        return os.getenv('E_123_DIR_DEL', 'disable').lower() == 'enable'
    @property
    def e_123_recycle_del_status(self):
        return os.getenv('E_123_RECYCLE_DEL', 'disable').lower() == 'enable'
    @property
    def m115_copy_player(self):
        return os.getenv('M115_COPY_PLAYER', 'disable').lower() == 'enable'
    @property
    def m115_copy_player_cid(self):
        return int(os.getenv('M115_COPY_PLAYER_CID', '0'))
    @property
    def m115_copy_player_url_cache_time(self):
        return int(os.getenv('M115_COPY_PLAYER_URL_CACHE_TIME', '60'))
    @property
    def keep_suffix(self):
        return os.getenv('KEEP_SUFFIX', 'true').lower() == 'true'
    @property
    def image_download_strategy(self):
        return os.getenv('IMAGE_DOWNLOAD_STRATEGY', 'cdn')
    @property
    def e_cover_gen_status(self):
        return os.getenv('E_COVER_GEN', 'disable').lower() == 'enable'
    @property
    def e_cover_gen_cron(self):
        return os.getenv('E_COVER_GEN_CRON')
    @property
    def e_cover_gen_style(self):
        return os.getenv('E_COVER_GEN_STYLE', 'style-1')
    @property
    def e_cover_gen_blacklist(self) -> list[str]:
        _var_var_4 = os.getenv('E_COVER_GEN_BLACKLIST')
        if not _var_var_4:
            return []
        _var_var_4 = _var_var_4.split('\n')
        return [_var_var_5.strip() for _var_var_5 in _var_var_4 if _var_var_5.strip() and not _var_var_5.strip().startswith('#')]
    @property
    def e_cover_gen_select_rule(self):
        return os.getenv('E_COVER_GEN_SELECT_RULE', 'PremiereDate_Descending')
    @property
    def e_cover_gen_template_mapping(self):
        _var_var_6 = os.getenv('E_COVER_GEN_TEMPLATE_MAPPING', '')
        if not _var_var_6:
            return {}
        return JsonUtils.json_to_dict(_var_var_6)
    @property
    def msg_type(self):
        return os.getenv('MSG_TYPE', 'NON')
    @property
    def msg_select_type(self):
        return os.getenv('MSG_SELECT_TYPE', 'DEF')
    @property
    def hdhive_checkin_status(self):
        return os.getenv('E_HDHIVE_CHECKIN', 'disable').lower() == 'enable' and self.hdhive_checkin_cron
    @property
    def hdhive_checkin_cron(self):
        return os.getenv('E_HDHIVE_CHECKIN_CRON')
    @property
    def hdhive_checkin_method(self):
        return os.getenv('E_HDHIVE_CHECKIN_METHOD', 'daily') == 'bet'
    @property
    def hdhive_checkin_account(self):
        return os.getenv('E_HDHIVE_CHECKIN_ACCOUNT')
    @property
    def hdhive_checkin_password(self):
        return os.getenv('E_HDHIVE_CHECKIN_PASSWORD')
    @property
    def hdhive_resource_types(self):
        return os.getenv('hdhive_resource_types', ['115', 'aliPan', 'ed2k'])
    @property
    def hdhive_sort_by(self):
        _var_var_7 = os.getenv('hdhive_sort_by', 'unlock_points')
        if _var_var_7 not in ('unlock_points', 'updated_at'):
            _var_var_7 = 'unlock_points'
        return _var_var_7
    @property
    def hdhive_sort_order(self):
        return os.getenv('hdhive_sort_order', 'desc')

config2Env = Config2Env()

config2Env = Config2Env()
