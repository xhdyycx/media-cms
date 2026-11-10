import json
import html
import re
import threading
import time
from threading import Event
from typing import Optional, List, Dict, Any, Tuple
import telebot
from telebot import apihelper, types
from app.core.env import configEnv
from app.core.license import LicenseInfo
from app.log import logger
from app.schemas import CommonMessage, MessageChannel
from app.utils.common import retry
from app.utils.mhttp import HttpClient
from app.utils.mjson import JsonUtils
from app.utils.mlist import MListUtils
from app.utils.share import ShareUtil
from app.utils.singleton import Singleton

class TGBot(metaclass=Singleton):
    '''TGBot'''
    _ds_url = 'http://127.0.0.1:9528/api/wx/message?source=tg'
    _event = Event()
    _bot: telebot.TeleBot = None
    _html_tag_re = re.compile('(<[^<>]*>)')
    _html_tag_name_re = re.compile('^<\\s*/?\\s*([a-zA-Z][\\w-]*)')
    _void_html_tags = {
        'br',
        'hr',
        'img',
        'link',
        'meta',
        'input'}
    
    def __init__(self):
        self._polling_thread = None
        self.init_bot()
        return None
        return None

    
    def init_bot(self):
        try:
            if not configEnv.tg_bot_status or not configEnv.tg_bot_token or not configEnv.tg_bot_chat_id:
                logger.info(f'TGBot不可用-status={configEnv.tg_bot_status}，tg_bot_token={configEnv.tg_bot_token}，tg_bot_chat_id={configEnv.tg_bot_chat_id}')
                return
            if configEnv.http_proxies:
                apihelper.proxy = configEnv.http_proxies
            self._bot = telebot.TeleBot(configEnv.tg_bot_token, parse_mode='HTML')
            
            def run_polling():
                try:
                    self._bot.infinity_polling(long_polling_timeout=30, logger_level=None)
                except Exception as _var_var_11:
                    logger.error(f'TG机器人异常：{str(_var_var_11)}')
            
            self._polling_thread = threading.Thread(target=run_polling, daemon=True)
            self._polling_thread.start()
            logger.info('TG机器人启动成功')
        except Exception as _var_var_5:
            logger.exception(_var_var_5)
            logger.error('TG机器人初始化失败')

    def stop_bot(self):
        if self._bot:
            self._bot.stop_polling()
            self._polling_thread.join()
            logger.info('TG机器人消息接收服务已停止.')
        return None
        return None

    
    def is_enable(self):
        if configEnv.tg_bot_status:
            configEnv.tg_bot_status
        return self._bot is not None
        return None

    @staticmethod
    def _escape_html(text: str) -> str:
        """
        Telegram HTML 特殊字符转义
        """
        return html.escape(text or '', quote=False)
    @classmethod
    @classmethod
    def _update_html_tag_stack(cls, tag: str, tag_stack: List[Tuple[str, str]]) -> None:
        """
        记录 HTML 标签状态，长文本分段时用于补齐跨段标签。
        """
        _var_var_12 = tag.strip()
        if _var_var_12.startswith('<!--') or _var_var_12.startswith('<!'):
            return
        _var_var_13 = cls._html_tag_name_re.match(_var_var_12)
        if not _var_var_13:
            return
        _var_var_14 = _var_var_13.group(1).lower()
        if _var_var_12.startswith('</'):
            for _var_var_15 in range(len(tag_stack) - 1, -1, -1):
                if tag_stack[_var_var_15][0] == _var_var_14:
                    del tag_stack[_var_var_15:]
                    break
            return
        if _var_var_12.endswith('/>') or _var_var_14 in cls._void_html_tags:
            return
        tag_stack.append((_var_var_14, _var_var_12))

    @staticmethod
    def _find_html_text_split(text: str, limit: int) -> int:
        """
        在纯文本中查找分隔点，尽量避免切开 HTML entity。
        """
        if limit >= len(text):
            return len(text)
        _var_var_16 = max(text.rfind('\n', 0, limit), text.rfind(' ', 0, limit), text.rfind('\t', 0, limit))
        if _var_var_16 > 0:
            return _var_var_16 + 1
        _var_var_16 = limit
        _var_var_17 = text.rfind('&', 0, _var_var_16)
        _var_var_18 = text.rfind(';', 0, _var_var_16)
        if _var_var_17 > _var_var_18:
            _var_var_19 = text.find(';', _var_var_17 + 1)
            if _var_var_19 != -1:
                if _var_var_17 > 0:
                    _var_var_16 = _var_var_17
                elif _var_var_19 + 1 <= limit:
                    _var_var_16 = _var_var_19 + 1
        return max(1, _var_var_16)

    @classmethod
    def _split_html_text(cls, text: str, chars_per_string: int = 4096) -> List[str]:
        """
        Telegram HTML 文本分段，避免切开标签，并保证每段里的跨段标签闭合。
        """
        if not text:
            return []
        _var_var_20 = []
        _var_var_24 = []
        _var_var_26 = 0
        _var_var_25 = False
        _var_var_27 = []

        def _var_var_21(stack: List[Tuple[str, str]]) -> str:  # code name: closing_tags
            return ''.join((f'</{_var_var_14}>' for _var_var_14, _var_var_34 in reversed(stack)))

        def _var_var_23(stack: List[Tuple[str, str]]) -> str:  # code name: opening_tags
            return ''.join((_var_var_35 for _var_var_34, _var_var_35 in stack))

        def _var_var_22() -> None:  # code name: flush
            if not _var_var_25:
                _var_var_33 = _var_var_23(_var_var_27)
                _var_var_24 = [_var_var_33] if _var_var_33 else []
                _var_var_26 = len(_var_var_33)
                return
            _var_var_20.append(''.join(_var_var_24) + _var_var_21(_var_var_27))
            _var_var_33 = _var_var_23(_var_var_27)
            _var_var_24 = [_var_var_33] if _var_var_33 else []
            _var_var_26 = len(_var_var_33)
            _var_var_25 = False

        def _var_var_28(value: str) -> None:  # code name: append_plain_text
            _var_var_36 = value
            while _var_var_36:
                _var_var_37 = len(_var_var_21(_var_var_27))
                _var_var_38 = chars_per_string - _var_var_26 - _var_var_37
                if _var_var_38 <= 0:
                    _var_var_22()
                    continue
                if len(_var_var_36) <= _var_var_38:
                    _var_var_24.append(_var_var_36)
                    _var_var_26 += len(_var_var_36)
                    _var_var_25 = True
                    break
                _var_var_16 = cls._find_html_text_split(_var_var_36, _var_var_38)
                _var_var_24.append(_var_var_36[:_var_var_16])
                _var_var_26 += _var_var_16
                _var_var_25 = True
                _var_var_36 = _var_var_36[_var_var_16:]
                _var_var_22()
                if _var_var_36:
                    continue
        _var_var_30 = [(_var_var_29) for _var_var_29 in cls._html_tag_re.split(text) if _var_var_29]
        for _var_var_29 in _var_var_30:
            if cls._html_tag_re.fullmatch(_var_var_29):
                _var_var_31 = list(_var_var_27)
                cls._update_html_tag_stack(_var_var_29, _var_var_31)
                _var_var_32 = _var_var_26 + len(_var_var_29) + len(_var_var_21(_var_var_31))
                if _var_var_25 and _var_var_32 > chars_per_string:
                    _var_var_22()
                if not _var_var_25:
                    cls._update_html_tag_stack(_var_var_29, _var_var_27)
                    _var_var_33 = _var_var_23(_var_var_27)
                    _var_var_24 = [_var_var_33] if _var_var_33 else []
                    _var_var_26 = len(_var_var_33)
                    continue
                _var_var_24.append(_var_var_29)
                _var_var_26 += len(_var_var_29)
                cls._update_html_tag_stack(_var_var_29, _var_var_27)
            else:
                _var_var_28(_var_var_29)
        if _var_var_25:
            _var_var_20.append(''.join(_var_var_24) + _var_var_21(_var_var_27))
        return _var_var_20

    def register_commands(self, commands):
        '''
        注册菜单命令
        '''
        if not self._bot:
            return
        if not commands:
            return
        try:
            self._bot.delete_my_commands()
            cmd_list = [
                telebot.types.BotCommand(k[1:], str(v.get('description')))
                for k, v in commands.items()
            ]
            self._bot.set_my_commands(commands=cmd_list)
        except Exception as _var_var_5:
            logger.error('TGBot设置菜单失败')
            logger.exception(_var_var_5)
