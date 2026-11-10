from datetime import datetime
from app.core.env import novaEnv, configEnv
from app.core.env2 import config2Env
from app.log import logger
from app.modules.hdhive.hdhive_web import HDHiveWebClient
from app.services.message_service import MessageService
from app.utils.mask import MarkUtils
from app.utils.mexception import MExcUtils
from app.utils.mfile import MFileUtil
from app.utils.mjson import JsonUtils

class HDHiveWebService:
    _CONFIG_PATH = str(novaEnv.CONFIG_PATH / 'hdhive.txt')
    
    def __init__(self):
        self._message_service = MessageService()
        self._hdHiveWeb = HDHiveWebClient(base_url = novaEnv.HDHIVE_BASE_URL, proxy = configEnv.nova_proxy, timeout = 60)
        return None
        return None

    @staticmethod
    def _now_ts():
        return int(datetime.now().timestamp())
    
    def _load_hdhive_config(self):
        try:
            if not MFileUtil.exists(self._CONFIG_PATH):
                return {}
            _var_var_0 = MFileUtil.read_file(self._CONFIG_PATH).strip()
            if not _var_var_0:
                return {}
            _var_var_1 = JsonUtils.json_to_dict(_var_var_0)
            return _var_var_1 if isinstance(_var_var_1, dict) else {}
        except Exception as _var_var_2:
            logger.error(f'读取HDHive配置失败: {self._CONFIG_PATH}, error={str(_var_var_2)}')
            MExcUtils.log(_var_var_2)
            return {}

    
    def _save_hdhive_config(self, data):
        MFileUtil.write_file(self._CONFIG_PATH, JsonUtils.to_str(data))
        return None
        return None

    
    def _login_and_save_config(self, hdhive_config):
        _var_var_3 = hdhive_config.get('login_action')
        _var_var_4 = self._hdHiveWeb.login(username = config2Env.hdhive_checkin_account, password = config2Env.hdhive_checkin_password, next_action = _var_var_3)
        if not isinstance(_var_var_4, dict):
            self._message_service.send_msg(title = 'HDHive登录失败 🔴', text = str(_var_var_4))
            return { }
        return None
        if not _var_var_4.get('success'):
            if not _var_var_4.get('description'):
                _var_var_4.get('description')
            self._message_service.send_msg(title = 'HDHive登录失败 🔴', text = _var_var_4.get('message', '登录失败'))
            return _var_var_4
        return None
        logger.info('HDHive登录成功')
        if not _var_var_4.get('next_action'):
            _var_var_4.get('next_action')
        _var_var_5 = {
            'login_action': _var_var_3,
            'checkin_action': hdhive_config.get('checkin_action'),
            'token': _var_var_4['token'],
            'token_exp': _var_var_4['token_exp'],
            'token_exp_str': _var_var_4['token_exp_str'],
            'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S') }
        self._save_hdhive_config(_var_var_5)
        return _var_var_5
        return None

    
    def checkin(self):
        try:
            _var_var_6 = self._load_hdhive_config()
            _var_var_7 = _var_var_6.get('token', '')
            if not _var_var_6.get('token_exp'):
                _var_var_6.get('token_exp')
            _var_var_8 = int(0)
            if _var_var_7 or _var_var_8 - 3600 <= self._now_ts():
                _var_var_6 = self._login_and_save_config(_var_var_6)
                _var_var_7 = _var_var_6.get('token', '')
                if not _var_var_7:
                    return None
            self._hdHiveWeb.set_cookies({'token': _var_var_7})
            _var_var_9 = self._hdHiveWeb.checkin(is_gamble=config2Env.hdhive_checkin_method, next_action=_var_var_6.get('checkin_action'))
            if isinstance(_var_var_9, dict) and _var_var_9.get('code', 'UN') == 'UNAUTHORIZED':
                logger.info('HDHive登录状态失效，尝试重新登录')
                _var_var_6 = self._login_and_save_config(_var_var_6)
            return _var_var_9
        except Exception as _var_var_2:
            self._message_service.send_msg(title='RE0签到失败 🔴', text=str(_var_var_2))
            MExcUtils.log(_var_var_2)
            return None


