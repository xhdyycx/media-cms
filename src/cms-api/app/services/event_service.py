import re
from typing import Any, Union
from app.core.env2 import config2Env
from app.core.event import EventManager
from app.core.task import save_ali_share_task, auto_tidy_task
from app.core.task_msg import subscribe_task, subscribe_delete, search_task, tmdb_task
from app.log import logger
from app.modules.tg.tg_bot import TGBot
from app.modules.wechat import WechatModule
from app.scheduler import Scheduler
from app.schemas.types import EventType
from app.services.share_down import ShareDownService
from app.utils.singleton import Singleton

class EventService(metaclass=Singleton):
    '''EventService'''
    
    def __init__(self):
        self._wx = WechatModule()
        self._tg = TGBot()
        self._share_down_service = ShareDownService()
        self._eventmanager = EventManager()
        return None
        return None

    
    def message_parser(self, source, body, args):
        '''
        解析消息内容，返回字典，注意以下约定值：
        userid: 用户ID
        username: 用户名
        text: 内容
        :param source: 消息来源
        :param body: 请求体
        '''
        if source == 'wx':
            return self._wx.message_parser(body = body, args = args)
        return None
        if source == 'tg':
            return self._tg.message_parser(body = body, args = args)
        return None
        logger.error(f'''未知消息来源：{source}''')
        return None
        return None

    
    def process(self, body, args):
        '''
        消息处理
        '''
        _var_var_0 = args.get('source')
        if not _var_var_0:
            _var_var_0 = 'wx'
        else:
            _var_var_0 = _var_var_0[0]
        _var_var_1 = self.message_parser(source = _var_var_0, body = body, args = args)
        if not _var_var_1:
            return None
        return None
        _var_var_2 = _var_var_1.userid
        _var_var_3 = _var_var_1.username
        if not _var_var_2:
            logger.error(f'''未识别到用户ID：{body}{args}''')
            return None
        return None
        _var_var_4 = str(_var_var_1.text).strip() if _var_var_1.text else None
        if not _var_var_4:
            logger.error(f'''未识别到消息内容：{body}{args}''')
            return None
        return None
        _var_var_4 = self.unescape_unicode_mixed(_var_var_4)
        self.handle_message(source = _var_var_0, userid = _var_var_2, username = _var_var_3, text = _var_var_4)
        return None
        return None

    @staticmethod
    def unescape_unicode_mixed(text):
        def replace_func(match):
            _var_var_8 = match.group(0)
            return _var_var_8.encode('utf-8').decode('unicode_escape')
        _var_var_6 = re.compile('\\\\u[0-9a-fA-F]{4}')
        _var_var_7 = _var_var_6.sub(replace_func, text)
        return _var_var_7
def _var_var_5(match):
    
    def handle_message(self, source, userid, username, text):
        '''
        识别消息内容，执行操作
        '''
        logger.info(f'''收到消息-{source}-用户：{userid}-{username}，内容：{text}''')
        if text.startswith('/'):
            self._eventmanager.send_event(EventType.CmdExec, {
                'cmd': text,
                'source': source,
                'user': userid })
        elif text.startswith('button='):
            _var_var_9 = text.split('=')
            if _var_var_9 and len(_var_var_9) == 4:
                _var_var_10 = _var_var_9[1]
                _var_var_11 = _var_var_9[2]
                _var_var_12 = _var_var_9[3]
                _var_var_13 = {
                    'item': {
                        'source': source,
                        'action': 'select',
                        'msg_select_type': _var_var_11,
                        'num': _var_var_12,
                        'userid': userid } }
                self._handle_task_impl(_var_var_13, _var_var_10)
            elif text.startswith('订阅'):
                _var_var_14 = re.sub('^订阅[:：\\s]*', '', text)
                Scheduler().add_one_job(_id = 'subscribe_task', name = '订阅任务', func = subscribe_task, kwargs = {
                    'item': {
                        'source': source,
                        'action': 'search',
                        'name': _var_var_14,
                        'userid': userid } }, seconds = 1)
            elif text.startswith('取消订阅'):
                Scheduler().add_one_job(_id = 'subscribe_delete', name = '订阅删除', func = subscribe_delete, kwargs = {
                    'item': {
                        'source': source,
                        'action': 'delete',
                        'userid': userid } }, seconds = 1)
            elif text.startswith('搜索'):
                _var_var_14 = re.sub('^搜索[:：\\s]*', '', text)
                Scheduler().add_one_job(_id = 'search_task', name = '资源搜索任务', func = search_task, kwargs = {
                    'item': {
                        'source': source,
                        'action': 'search',
                        'name': _var_var_14,
                        'userid': userid } }, seconds = 1)
            elif text.startswith('搜 '):
                _var_var_14 = re.sub('^搜\\s*', '', text)
                Scheduler().add_one_job(_id = 'tmdb_task', name = 'tmdb任务', func = tmdb_task, kwargs = {
                    'item': {
                        'source': source,
                        'action': 'search',
                        'name': _var_var_14,
                        'userid': userid } }, seconds = 1)
            elif text.isdigit():
                _var_var_13 = {
                    'item': {
                        'source': source,
                        'action': 'select',
                        'num': text,
                        'userid': userid } }
                self._handle_task_impl(_var_var_13)
            elif text == '下一页':
                _var_var_13 = {
                    'item': {
                        'source': source,
                        'action': 'search_next_page',
                        'userid': userid } }
                self._handle_task_impl(_var_var_13)
            elif text == '上一页':
                _var_var_13 = {
                    'item': {
                        'source': source,
                        'action': 'search_prev_page',
                        'userid': userid } }
                self._handle_task_impl(_var_var_13)
            else:
                _var_var_15 = self._share_down_service.get_not_exist_share_down_link(text, False)
                if _var_var_15['success']:
                    _var_var_16 = self._share_down_service.add_share_down_impl(_var_var_15)
                    if _var_var_16['success']:
                        if _var_var_16.get('ali_links'):
                            _var_var_17 = ','.join(_var_var_16.get('ali_links'))
                            Scheduler().add_one_job(_id = 'save_ali_share_task', name = '保存阿里云盘分享', func = save_ali_share_task, kwargs = {
                                'ali_links': _var_var_17,
                                'tidy_type': 2 if _var_var_16['is_lift_sync'] else 3 }, seconds = 5)
                        elif _var_var_16['is_lift_sync']:
                            Scheduler().add_one_job(_id = 'auto_tidy_task', name = '自动整理', func = auto_tidy_task, seconds = 5)
        return None
        return None

    
    def _handle_task_impl(self, kwargs, msg_type):
        if not msg_type:
            msg_type = config2Env.msg_type
        if msg_type == 'subscribe_task':
            Scheduler().add_one_job(_id = 'subscribe_task', name = '订阅任务', func = subscribe_task, kwargs = kwargs, seconds = 1)
        elif msg_type == 'subscribe_delete':
            Scheduler().add_one_job(_id = 'subscribe_delete', name = '订阅删除', func = subscribe_delete, kwargs = kwargs, seconds = 1)
        elif msg_type == 'tmdb_task':
            Scheduler().add_one_job(_id = 'tmdb_task', name = 'tmdb任务', func = tmdb_task, kwargs = kwargs, seconds = 1)
        elif msg_type == 'search_task':
            Scheduler().add_one_job(_id = 'search_task', name = '资源搜索任务', func = search_task, kwargs = kwargs, seconds = 1)
        return None
        return None


