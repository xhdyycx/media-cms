from datetime import datetime
from app.core.env2 import config2Env
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.modules.hdhive.hdhive_proxy import HDHiveProxyClient
from app.services.message_service import MessageService
from app.utils.mask import MarkUtils
from app.utils.mexception import MExcUtils
from app.utils.mjson import JsonUtils

class HdHiveService:
    
    def __init__(self):
        self.client = ObjFactory.get_instance(HDHiveProxyClient)
        self._message_service = MessageService()
        return None
        return None

    
    def checkin(self):
        try:
            _var_var_0 = '赌狗' if config2Env.hdhive_checkin_method else '正常'
            _var_var_1 = self.client.open_checkin(is_gambler = config2Env.hdhive_checkin_method)
            _var_var_2 = self.client.open_me()
            if not _var_var_2.get('code') != '200' or _var_var_2.get('success'):
                self._message_service.send_msg(title = 'RE0签到失败 🔴', text = f'''获取用户信息失败: {_var_var_2.get('message', '未知错误')}''')
                return None
            return None
            if not _var_var_2['data'].get('nickname'):
                _var_var_2['data'].get('nickname')
            _var_var_3 = _var_var_2['data']['username']
            _var_var_4 = f'''🧛账号：{MarkUtils.smart_mask(_var_var_3)}\n👊类型：{_var_var_0}签到'''
            if _var_var_2.get('success'):
                _var_var_4 = f'''{_var_var_4}\n💰积分：{_var_var_2['data']['points']}\n📦累计：{_var_var_2['data']['signin_days_total']} 天'''
            _var_var_4 = f'''{_var_var_4}\n🗓️时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'''
            if _var_var_1.get('success') and _var_var_1.get('data', { }).get('checked_in'):
                _var_var_4 = f'''{_var_var_4}\n📝结果：{_var_var_1.get('data', { }).get('message', '签到成功')}\n'''
                self._message_service.send_msg(title = 'RE0签到成功 🟢', text = _var_var_4)
                logger.info(f'''RE0签到成功: {JsonUtils.to_str(_var_var_1)}''')
            else:
                _var_var_4 = f'''{_var_var_4}\n📝原因：{_var_var_1.get('data', { }).get('message', '未知原因，请查看日志')}\n'''
                self._message_service.send_msg(title = 'RE0签到失败 🔴', text = _var_var_4)
                logger.error(f'''RE0签到失败: {JsonUtils.to_str(_var_var_1)}''')
        except Exception:
            _var_var_5 = None
            self._message_service.send_msg(title = 'RE0签到失败 🔴', text = str(_var_var_5))
            MExcUtils.log(_var_var_5)
            _var_var_5 = None
            del _var_var_5
            return None



