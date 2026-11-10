import ast
import os
from pathlib import Path
from dotenv import load_dotenv
from app.utils.mjson import JsonUtils
from app.utils.singleton import Singleton
from version import APP_VERSION
load_dotenv('/config/config.env')

class NovaEnv(metaclass=Singleton):
    '''NovaEnv'''
    RUN_ENV = os.getenv('RUN_ENV', 'dev')
    APP_VERSION = os.getenv('APP_VERSION', APP_VERSION)
    DONATE_CODE = os.getenv('DONATE_CODE', '')
    NOVA_API_TOKEN: str = os.getenv('NOVA_API_TOKEN', 'cloud_media_sync')
    IS_HK_VPS: bool = os.getenv('IS_HK_VPS', '0') == '1'
    AUTO_TIDY_TYPE: bool = os.getenv('AUTO_TIDY_TYPE', '1')
    TZ: str = os.getenv('TZ', 'Asia/Shanghai')
    ROOT_PATH = Path(__file__).parents[2]
    LOG_PATH = '/logs'
    COVER_PATH = f'''{LOG_PATH}/cover'''
    LOG_FILE_PATH = f'''{LOG_PATH}/novamedia.log'''
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    CONFIG_PATH = Path('/config')
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    BINDING_115: str = os.getenv('BINDING_115')
    BINDING_123: str = os.getenv('BINDING_123')
    SQL_PATH = CONFIG_PATH / f'''cms-{RUN_ENV}.db'''
    DATABASE_SQL = os.getenv('DATABASE_SQL', f'''sqlite:///{SQL_PATH}''')
    IS_SQLITE = DATABASE_SQL.startswith('sqlite')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'novamedia-secret-key-2026')
    ADMIN_USERNAME: str = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD: str = os.getenv('ADMIN_PASSWORD', 'admin')
    EMBY_HOST_PORT: str = os.getenv('EMBY_HOST_PORT')
    EMBY_API_KEY: str = os.getenv('EMBY_API_KEY')
    MEDIA_IMG_NAMES = {
        'thumb',
        'banner',
        'fanart',
        'poster',
        'discart',
        'clearart',
        'clearlogo',
        'landscape'}
    CATEGORY_FILE_PATH = CONFIG_PATH / 'category.yaml'
    TIDY_FILE_PATH = CONFIG_PATH / 'tidy.yaml'
    DEMO_CATEGORY_FILE_PATH = 'demo/category.yaml' if RUN_ENV == 'dev' else '/novamedia/api/category.yaml'
    DEMO_TIDY_FILE_PATH = 'demo/tidy.yaml' if RUN_ENV == 'dev' else '/novamedia/api/tidy.yaml'
    SECRET_KEY = os.getenv('SECRET_KEY', 'FREE')
    IS_AUTHOR = SECRET_KEY == 'all_function_admin'
    WISH_ANSWER_USERNAME = os.getenv('WISH_ANSWER_USERNAME')
    P123_USERNAME = os.getenv('P123_USERNAME')
    P123_PASSWORD = os.getenv('P123_PASSWORD')
    IS_CREATE_MENU = os.getenv('IS_CREATE_MENU', 'YES') == 'YES'
    HDHIVE_API_KEY = os.getenv('HDHIVE_API_KEY', '')
    HDHIVE_BASE_URL = os.getenv('HDHIVE_BASE_URL', 'https://re0.me')

class ConfigEnv(metaclass=Singleton):
    '''ConfigEnv'''
    @property
    def use_115_open_api(self):
        return os.getenv('USE_OPEN_API', 'false').lower() == 'true'
    @property
    def m115_app_id(self):
        return os.getenv('M115_APP_ID', '')
    @property
    def direct_115_302_domain(self):
        return os.getenv('DIRECT_115_302_DOMAIN', 'http://172.17.0.1:9527')
    @property
    def strm_type(self):
        return os.getenv('STRM_TYPE', 'pick_code_name')
    @property
    def video_suffix(self):
        _var_var_0 = os.getenv('VIDEO_SUFFIX', "['mp4', 'mkv']")
        try:
            return ast.literal_eval(_var_var_0)
        except (ValueError, SyntaxError):
            return ['mp4', 'mkv']
    @property
    def wechat_status(self):
        return os.getenv('WECHAT_STATUS', 'false').lower() == 'true'
    @property
    def wechat_cor_pid(self):
        return os.getenv('WECHAT_COR_PID')
    @property
    def wechat_app_secret(self):
        return os.getenv('WECHAT_APP_SECRET')
    @property
    def wechat_app_id(self):
        return os.getenv('WECHAT_APP_ID')
    @property
    def wechat_proxy(self):
        return os.getenv('WECHAT_PROXY', 'https://qyapi.weixin.qq.com')
    @property
    def wechat_token(self):
        return os.getenv('WECHAT_TOKEN')
    @property
    def wechat_encoding_aes_key(self):
        return os.getenv('WECHAT_ENCODING_AES_KEY')
    @property
    def tg_bot_status(self):
        return os.getenv('TG_BOT_STATUS', 'false').lower() == 'true'
    @property
    def tg_bot_token(self):
        return os.getenv('TG_BOT_TOKEN')
    @property
    def tg_bot_chat_id(self):
        _var_var_1 = os.getenv('TG_BOT_CHAT_ID', '').split(',')
        if not _var_var_1:
            os.remove('TG_BOT_MASTER_CHAT_ID')
            return []
        os.environ['TG_BOT_MASTER_CHAT_ID'] = _var_var_1[0]
        return _var_var_1
    @property
    def tg_bot_master_chat_id(self):
        return os.getenv('TG_BOT_MASTER_CHAT_ID')
    @property
    def tmdb_api_key(self):
        return os.getenv('TMDB_API_KEY', '')
    @tmdb_api_key.setter
    def tmdb_api_key(self, key):
        if key:
            os.environ['TMDB_API_KEY'] = str(key)
    @property
    def tmdb_api_domain(self):
        _var_var_2 = os.getenv('TMDB_API_DOMAIN')
        return _var_var_2 if _var_var_2 else 'https://api.tmdb.org'
    @tmdb_api_domain.setter
    def tmdb_api_domain(self, domain):
        if domain:
            os.environ['TMDB_API_DOMAIN'] = str(domain)
    @property
    def tmdb_img_domain(self):
        _var_var_2 = os.getenv('TMDB_IMG_DOMAIN')
        return _var_var_2 if _var_var_2 else 'https://image.tmdb.org'
    @tmdb_img_domain.setter
    def tmdb_img_domain(self, domain):
        if domain:
            os.environ['TMDB_IMG_DOMAIN'] = str(domain)
    @property
    def tmdb_language(self):
        return os.getenv('TMDB_LANGUAGE', 'zh-CN')
    @property
    def is_zh_language(self):
        return self.tmdb_language == 'zh-CN'
    @property
    def sync_cron(self):
        _var_var_3 = os.getenv('SYNC_CRON')
        return _var_var_3 if _var_var_3 else '*/20 8-23 * * *'
    @property
    def api_wait_time(self):
        return float(os.getenv('API_WAIT_TIME', '1'))
    @property
    def sync_mode(self):
        return os.getenv('SYNC_MODE', 'normal')
    @property
    def sync_mode_is_fast(self):
        return os.getenv('SYNC_MODE', 'normal') == 'fast'
    @property
    def media_115_cid(self):
        return os.getenv('MEDIA_115_CID', '')
    @property
    def media_115_cid_path(self):
        return os.getenv('MEDIA_115_CID_PATH', '')
    @property
    def local_path(self):
        return os.getenv('LOCAL_PATH', '/media')
    @property
    def video_suffix(self):
        _var_var_0 = os.getenv('VIDEO_SUFFIX', "['mp4', 'mkv']")
        try:
            return ast.literal_eval(_var_var_0)
        except (ValueError, SyntaxError):
            return ['mp4', 'mkv']
    @property
    def image_suffix(self):
        try:
            return ast.literal_eval(os.getenv('IMAGE_SUFFIX', '[]'))
        except (ValueError, SyntaxError):
            return []
    @property
    def media_data_suffix(self):
        try:
            return ast.literal_eval(os.getenv('MEDIA_DATA_SUFFIX', '[]'))
        except (ValueError, SyntaxError):
            return []
    @property
    def media_min_size(self):
        _var_var_4 = os.getenv('MEDIA_MIN_SIZE', '0')
        try:
            return int(_var_var_4) * 1024 * 1024
        except ValueError:
            print('MEDIA_MIN_SIZE ERROR')
            return 0
    @property
    def image_download_threads(self):
        try:
            return int(os.getenv('IMG_DOWN_THREADS', 10))
        except ValueError:
            print('IMG_DOWN_THREADS ERROR')
            return 10
    @property
    def nova_proxy(self):
        return os.getenv('CMS_PROXY')
    @property
    def http_proxies(self):
        _var_var_5 = self.nova_proxy
        if _var_var_5:
            return {'http': _var_var_5, 'https': _var_var_5}
        return None
    @property
    def custom_regex_match(self):
        return os.getenv('CUSTOM_REGEX_MATCH')
    @property
    def new_media_cid(self):
        return os.getenv('NEW_MEDIA_CID')
    @property
    def new_media_cid_path(self):
        return os.getenv('NEW_MEDIA_CID_PATH')
    @property
    def redundant_data_cid(self):
        return os.getenv('REDUNDANT_DATA_CID')
    @property
    def redundant_data_cid_path(self):
        return os.getenv('REDUNDANT_DATA_CID_PATH')
    @property
    def new_media_exists_cid(self):
        return os.getenv('NEW_MEDIA_EXISTS_CID')
    @property
    def new_media_exists_cid_path(self):
        return os.getenv('NEW_MEDIA_EXISTS_CID_PATH')
    @property
    def movie_dir_rename_rule(self):
        return os.getenv('MOVIE_DIR_RENAME_RULE', '{first_letter}-{title}-{year}-[tmdb={tmdb_id}]')
    @property
    def movie_file_rename_rule(self):
        return os.getenv('MOVIE_FILE_RENAME_RULE', '{title}.{year}<.{resource_pix}><.{fps}><.{resource_version}><.{resource_source}><.{resource_type}><.{resource_effect}><.{video_encode}><.{audio_encode}><-{resource_team}>')
    @property
    def tv_dir_rename_rule(self):
        return os.getenv('TV_DIR_RENAME_RULE', '{first_letter}-{title}-{year}-[tmdb={tmdb_id}]')
    @property
    def tv_season_dir_rename_rule(self):
        return os.getenv('TV_SEASON_DIR_RENAME_RULE', 'Season {season_num:02d}')
    @property
    def tv_file_rename_rule(self):
        return os.getenv('TV_FILE_RENAME_RULE', '{title}.{year}.{season_episode}<.{resource_pix}><.{fps}><.{resource_version}><.{resource_source}><.{resource_type}><.{resource_effect}><.{video_encode}><.{audio_encode}><-{resource_team}>')
    @property
    def auto_min_size(self):
        _var_var_4 = os.getenv('AUTO_MIN_SIZE', '0')
        try:
            return int(_var_var_4) * 1024 * 1024
        except ValueError:
            print('AUTO_MIN_SIZE ERROR')
            return 0
    @property
    def auto_blacklist(self):
        _var_var_6 = os.getenv('AUTO_BLACKLIST')
        if _var_var_6:
            return _var_var_6.split('\n')
        return []
    @property
    def custom_words_replace(self):
        _var_var_6 = os.getenv('CUSTOM_WORDS_REPLACE')
        if _var_var_6:
            _var_var_7 = []
            _var_var_6 = _var_var_6.split('\n')
            for _var_var_8 in _var_var_6:
                if not _var_var_8:
                    continue
                if '=>' in _var_var_8:
                    _var_var_9 = _var_var_8.split('=>')
                    if len(_var_var_9) == 2:
                        _var_var_7.append({'old': _var_var_9[0].strip(), 'new': _var_var_9[1].strip()})
                    if len(_var_var_9) == 1:
                        _var_var_7.append({'old': _var_var_9[0].strip(), 'new': ''})
            return _var_var_7
        return []
    @property
    def custom_release_group(self):
        _var_var_6 = os.getenv('CUSTOM_RELEASE_GROUP')
        if _var_var_6:
            return _var_var_6.split('\n')
        return []
    @property
    def gpt_recognize_status(self):
        return os.getenv('GPT_RECOGNIZE_STATUS', 'disabled')
    @property
    def openai_base_url(self):
        return os.getenv('OPENAI_BASE_URL', 'https://api.siliconflow.cn/v1')
    @property
    def openai_model(self):
        return os.getenv('OPENAI_MODEL', 'deepseek-ai/DeepSeek-V2.5')
    @property
    def openai_api_key(self):
        return os.getenv('OPENAI_API_KEY')
    @property
    def share_down_dir_cid(self):
        return os.getenv('SHARE_DOWN_DIR_CID')
    @property
    def share_down_dir_path(self):
        return os.getenv('SHARE_DOWN_DIR_PATH')
    @property
    def auto_tidy_after_save(self):
        return os.getenv('AUTO_TIDY_AFTER_SAVE', 'YES').lower() == 'yes'
    @property
    def aliyun_share_dir_id(self):
        return os.getenv('ALIYUN_SHARE_DIR_ID')
    @property
    def aliyun_share_dir_name(self):
        return os.getenv('ALIYUN_SHARE_DIR_NAME')
    @property
    def aliyun_nick_name(self):
        return os.getenv('ALIYUN_NICK_NAME')
    @property
    def aliyun_to_115_dir_cid(self):
        return os.getenv('ALIYUN_TO_115_DIR_CID') or self.share_down_dir_cid
    @property
    def aliyun_to_115_dir_path(self):
        return os.getenv('ALIYUN_TO_115_DIR_PATH') or self.share_down_dir_path
    
    def refresh(self):
        os.environ['TMDB_CACHE_ENABLED'] = 'True'
        _var_var_5 = self.http_proxies
        if _var_var_5:
            os.environ['TMDB_PROXIES'] = str(_var_var_5)
        return None
        return None
    @property
    def emby_refresh_status(self):
        return os.getenv('EMBY_REFRESH_STATUS', 'false').lower() == 'true'
    @property
    def emby_path_replace_rule(self):
        return os.getenv('EMBY_PATH_REPLACE_RULE', '')
    @property
    def emby_path_style(self):
        return os.getenv('EMBY_PATH_STYLE', 'unix')
    @property
    def alist_url(self):
        return os.getenv('ALIST_URL', 'http://172.17.0.1:5244')
    @property
    def alist_token(self):
        return os.getenv('ALIST_TOKEN', '')
    @property
    def alist_sync_paths(self):
        try:
            return ast.literal_eval(os.getenv('ALIST_SYNC_PATHS', '[]'))
        except (ValueError, SyntaxError):
            print('ALIST_SYNC_PATHS ERROR')
            return []
    @property
    def alist_local_path(self):
        return os.getenv('ALIST_LOCAL_PATH', '/media/alist')
    @property
    def alist_video_suffix(self):
        return os.getenv('ALIST_VIDEO_SUFFIX', [])
    @property
    def alist_image_suffix(self):
        return os.getenv('ALIST_IMAGE_SUFFIX', [])
    @property
    def alist_media_data_suffix(self):
        return os.getenv('ALIST_MEDIA_DATA_SUFFIX', [])
    @property
    def alist_min_size(self):
        _var_var_4 = os.getenv('ALIST_MIN_SIZE', '0')
        try:
            return int(_var_var_4) * 1024 * 1024
        except ValueError:
            print('ALIST_MIN_SIZE ERROR')
            return 0
    @property
    def alist_api_interval(self):
        try:
            _var_var_10 = os.getenv('ALIST_API_INTERVAL')
            if _var_var_10:
                return float(_var_var_10)
            return None
        except ValueError:
            print('ALIST_API_INTERVAL ERROR')
            return 0
    @property
    def alist_download_threads(self):
        try:
            return int(os.getenv('ALIST_DOWNLOAD_THREADS', 5))
        except ValueError:
            print('ALIST_DOWNLOAD_THREADS ERROR')
            return 3
    @property
    def e_alist_sync_cron(self):
        return os.getenv('E_ALIST_SYNC_CRON')
    @property
    def share_115_code(self):
        return os.getenv('SHARE_115_CODE', '')
    @property
    def share_115_password(self):
        return os.getenv('SHARE_115_PASSWORD', '')
    @property
    def share_115_cid(self):
        return os.getenv('SHARE_115_CID', '0')
    @property
    def share_115_local_path(self):
        return os.getenv('SHARE_115_LOCAL_PATH', '/media/share')
    @property
    def share_115_video_suffix(self):
        return os.getenv('SHARE_115_VIDEO_SUFFIX', [])
    @property
    def share_115_image_suffix(self):
        return os.getenv('SHARE_115_IMAGE_SUFFIX', [])
    @property
    def share_115_media_data_suffix(self):
        return os.getenv('SHARE_115_MEDIA_DATA_SUFFIX', [])
    @property
    def share_115_min_size(self):
        _var_var_4 = os.getenv('SHARE_115_MIN_SIZE', '0')
        try:
            return int(_var_var_4) * 1024 * 1024
        except ValueError:
            print('SHARE_115_MIN_SIZE ERROR')
            return 0
    @property
    def share_115_api_interval(self):
        try:
            _var_var_11 = os.getenv('SHARE_115_API_INTERVAL')
            if _var_var_11:
                return float(_var_var_11)
            return None
        except ValueError:
            print('SHARE_115_API_INTERVAL ERROR')
            return 0
    @property
    def share_115_img_download_threads(self):
        try:
            return int(os.getenv('SHARE_115_IMG_DOWNLOAD_THREADS', 10))
        except ValueError:
            print('SHARE_115_IMG_DOWNLOAD_THREADS ERROR')
            return 10
    @property
    def e_115_dir_del_status(self):
        return os.getenv('E_115_DIR_DEL', 'disable').lower() == 'enable'
    @property
    def e_115_recycle_del_status(self):
        return os.getenv('E_115_RECYCLE_DEL', 'disable').lower() == 'enable'
    @property
    def e_aliyun_dir_del_status(self):
        return os.getenv('E_ALIYUN_DIR_DEL', 'disable').lower() == 'enable'
    @property
    def e_aliyun_recycle_del_status(self):
        return os.getenv('E_ALIYUN_RECYCLE_DEL', 'disable').lower() == 'enable'
    @property
    def e_alist_sync_status(self):
        return os.getenv('E_ALIST_SYNC', 'disable').lower() == 'enable'
    @property
    def e_115_dir_del_cron(self):
        return os.getenv('E_115_DIR_DEL_CRON')
    @property
    def e_115_dir_del_cid(self) -> list[str]:
        _var_var_12 = os.getenv('E_115_DIR_DEL_CID')
        if not _var_var_12:
            return []
        _var_var_12 = _var_var_12.split('\n')
        return [_var_var_13.strip() for _var_var_13 in _var_var_12 if _var_var_13.strip() and not _var_var_13.strip().startswith('#')]
    @property
    def e_115_dir_del_days(self):
        return int(os.getenv('E_115_DIR_DEL_DAYS', '0'))
    @property
    def e_115_recycle_del_cron(self):
        return os.getenv('E_115_RECYCLE_DEL_CRON')
    @property
    def e_115_recycle_del_days(self):
        return int(os.getenv('E_115_RECYCLE_DEL_DAYS', '0'))
    @property
    def e_115_recycle_del_account_ids(self):
        return ast.literal_eval(os.getenv('E_115_RECYCLE_DEL_ACCOUNT_IDS', '[0]'))
    @property
    def e_aliyun_dir_del_cron(self):
        return os.getenv('E_ALIYUN_DIR_DEL_CRON')
    @property
    def e_aliyun_dir_del_cid(self) -> list[str]:
        _var_var_12 = os.getenv('E_ALIYUN_DIR_DEL_CID')
        if not _var_var_12:
            return []
        _var_var_12 = _var_var_12.split('\n')
        return [_var_var_13.strip() for _var_var_13 in _var_var_12 if _var_var_13.strip() and not _var_var_13.strip().startswith('#')]
    @property
    def e_aliyun_dir_del_days(self):
        return int(os.getenv('E_ALIYUN_DIR_DEL_DAYS', '0'))
    @property
    def e_aliyun_recycle_del_cron(self):
        return os.getenv('E_ALIYUN_RECYCLE_DEL_CRON')
    @property
    def e_aliyun_recycle_del_days(self):
        return int(os.getenv('E_ALIYUN_RECYCLE_DEL_DAYS', '0'))
    @property
    def e_strm_replace_old(self):
        return os.getenv('E_STRM_REPLACE_OLD')
    @property
    def e_strm_replace_new(self):
        return os.getenv('E_STRM_REPLACE_NEW')
    @property
    def e_strm_replace_path(self):
        return os.getenv('E_STRM_REPLACE_PATH')
novaEnv = NovaEnv()
configEnv = ConfigEnv()

