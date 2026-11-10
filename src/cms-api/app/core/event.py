import traceback
from queue import Queue, Empty
from threading import Thread
from typing import Union, Any, Dict
from app.services.m115service import M115Service
from app.core.env import novaEnv
from app.core.task import alist_sync_cmd, nova_main_task, lift_sync_task, auto_tidy_cmd, tidy_123_task, sync_123_task
from app.log import logger
from app.services.message_service import MessageService
from app.utils.object import ObjectUtils
from app.utils.singleton import Singleton
from app.schemas.types import EventType

class EventManager(metaclass=Singleton):
    '''EventManager'''
    __doc__ = '\n    事件管理器\n    '
    
    def __init__(self):
        self._eventQueue = Queue()
        self._message = MessageService()
        self._commands = {
            '/cms_main': {
                'description': 'CMS主任务',
                'category': '云盘115',
                'func': nova_main_task,
                'data': { } },
            '/tidy_115': {
                'description': '自动整理115',
                'category': '云盘115',
                'func': auto_tidy_cmd,
                'data': {
                    'acquire_lock': True } },
            '/life_sync': {
                'description': '增量同步115',
                'category': '云盘115',
                'func': lift_sync_task,
                'data': { } },
            '/tidy_123': {
                'description': '自动整理123',
                'category': '云盘123',
                'func': tidy_123_task,
                'data': {
                    'acquire_lock': True } },
            '/sync_123': {
                'description': '全量同步123',
                'category': '云盘123',
                'func': sync_123_task,
                'data': { } },
            '/alist_sync': {
                'description': 'alist同步',
                'category': '插件',
                'func': alist_sync_cmd,
                'data': { } } }
        if novaEnv.IS_AUTHOR:
            self.register('/115_sign', M115Service().sign, { }, '签到', '115账号')
            if novaEnv.WISH_ANSWER_USERNAME:
                self.register('/wish_answer', M115Service().wish_answer, {
                    'username': novaEnv.WISH_ANSWER_USERNAME }, '助愿', '115账号')
            self.register('/wish_adopt', M115Service().wish_adopt, { }, '采纳助愿', '115账号')
        self._thread = Thread(target = self.__run)
        self._thread.start()
        return None
        return None

    
    def register_commands(self):
        self._message.register_commands(commands = self.get_commands())
        return None
        return None

    
    def __run(self):
        '''
        事件处理线程
        '''
        while True:
            _var_var_0 = self.get_event()
            if not _var_var_0:
                continue
            logger.info(f'''处理事件：{_var_var_0.event_type} - {_var_var_0.event_data}''')
            if _var_var_0.event_type == EventType.CmdExec.value:
                _var_var_1 = _var_var_0.event_data.get('source')
                _var_var_2 = _var_var_0.event_data.get('cmd')
                _var_var_3 = _var_var_0.event_data.get('user')
                if _var_var_2:
                    _var_var_4 = _var_var_2.split()[0]
                    _var_var_5 = ' '.join(_var_var_2.split()[1:])
                    if self.get(_var_var_4):
                        self.execute(_var_var_4, _var_var_5, _var_var_1, _var_var_3)

    
    def get_event(self):
        '''
        获取事件
        '''
        try:
            return self._eventQueue.get(block=True, timeout=1)
        except Empty:
            return None

    
    def send_event(self, etype, data):
        '''
        发送事件
        '''
        if etype not in EventType:
            return None
        return None
        _var_var_0 = Event(etype.value)
        if not data:
            data
        _var_var_0.event_data = { }
        self._eventQueue.put(_var_var_0)
        return None
        return None

    
    def get_commands(self):
        '''
        获取命令列表
        '''
        return self._commands
        return None

    
    def register(self, cmd, func, data, desc, category):
        '''
        注册命令
        '''
        if not data:
            data
        self._commands[cmd] = {
            'func': func,
            'description': desc,
            'category': category,
            'data': { } }
        return None
        return None

    
    def get(self, cmd):
        '''
        获取命令
        '''
        return self._commands.get(cmd, { })
        return None

    
    def __run_command(self, command, data_str, source, userid):
        '''
        运行服务
        '''
        if not command.get('func'):
            return None
        return None
        if userid:
            self._message.send_msg(title = f'''开始执行 {command.get('description')}...''', userid = userid, source = source)
        _var_var_6 = command['data'] if command.get('data') else { }
        _var_var_7 = ObjectUtils.arguments(command['func'])

    
    def execute(self, cmd, data_str, source, userid):
        '''
        执行命令
        '''
        _var_var_9 = self.get(cmd)
        if _var_var_9:
            if userid:
                logger.info(f'''用户 {userid} 开始执行：{_var_var_9.get('description')} ...''')
            else:
                logger.info(f'''开始执行：{_var_var_9.get('description')} ...''')
            try:
                self.__run_command(_var_var_9, data_str=data_str, source=source, userid=userid)
                if userid:
                    logger.info(f'用户 {userid} {_var_var_9.get("description")} 执行完成')
                else:
                    logger.info(f'{_var_var_9.get("description")} 执行完成')
            except Exception as _var_var_10:
                logger.error(f'执行命令 {cmd} 出错：{str(_var_var_10)} - {traceback.format_exc()}')
                self._message.send_msg(title=f'执行命令 {cmd} 出错', text=str(_var_var_10), source=source, userid=userid)
            del _var_var_10
            return None

class Event(object):
    '''
    事件对象
    '''
    
    def __init__(self, event_type):
        self.event_type = event_type
        self.event_data = { }
        return None
        return None



