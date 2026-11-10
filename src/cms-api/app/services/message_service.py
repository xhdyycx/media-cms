from typing import Dict, List
from app.modules.tg.tg_bot import TGBot
from app.modules.wechat import WechatModule
from app.utils.singleton import Singleton

class MessageService(metaclass=Singleton):
    '''MessageService'''
    
    def __init__(self):
        self._wx = WechatModule()
        self._tg = TGBot()
        return None
        return None

    
    def _send_to_tg(self, title, text, image, userid, link, images, keyboards):
        return None

    def _send_to_wx(self, title, text, image, userid, link, images, keyboards):
        return None

    
    def send_msg(self, title, text, image, userid, link, images, source, keyboards):
        if not source:
            self._send_to_wx(title, text, image, userid, link, images, keyboards)
            self._send_to_tg(title, text, image, userid, link, images, keyboards)
            return None
        return None
        if source == 'wx':
            self._send_to_wx(title, text, image, userid, link, images)
        elif source == 'tg':
            self._send_to_tg(title, text, image, userid, link, images, keyboards)
        return None
        return None

    
    def register_commands(self, commands):
        self._wx.register_commands(commands)
        self._tg.register_commands(commands)
        return None
        return None


