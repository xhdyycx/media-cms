import xml.dom.minidom as xml
from typing import Optional, Union, List, Tuple, Any, Dict
from app.core.env import novaEnv, configEnv
from app.log import logger
from app.modules.wechat.WXBizMsgCrypt3 import WXBizMsgCrypt
from app.modules.wechat.wechat import WeChat
from app.schemas import MessageChannel
from app.schemas.message import CommonMessage
from app.utils.dom import DomUtils
from app.utils.singleton import Singleton

class WechatModule(metaclass=Singleton):
    '''WechatModule'''
    
    def __init__(self):
        self._configEnv = configEnv
        self._wechat = WeChat()

    
    def message_parser(self, body, args):
        try:
            _var_var_0 = args.get('msg_signature', [''])[0]
            _var_var_1 = args.get('timestamp', [''])[0]
            _var_var_2 = args.get('nonce', [''])[0]
            if not _var_var_0 or not _var_var_1 or not _var_var_2:
                logger.error(f'微信请求参数错误：{args}')
                return None
            _var_var_3 = WXBizMsgCrypt(sToken = self._configEnv.wechat_token, sEncodingAESKey = self._configEnv.wechat_encoding_aes_key, sReceiveId = self._configEnv.wechat_cor_pid)
            if not body:
                logger.error('微信请求数据为空')
                return None
            (_var_var_4, _var_var_5) = _var_var_3.DecryptMsg(sPostData = body, sMsgSignature = _var_var_0, sTimeStamp = _var_var_1, sNonce = _var_var_2)
            if _var_var_4 != 0:
                logger.error(f'解密微信消息失败 {_var_var_4}')
                return None
            _var_var_6 = xml.dom.minidom.parseString(_var_var_5.decode('UTF-8'))
            _var_var_7 = _var_var_6.documentElement
            _var_var_8 = DomUtils.tag_value(_var_var_7, 'MsgType')
            _var_var_9 = DomUtils.tag_value(_var_var_7, 'Event')
            _var_var_10 = DomUtils.tag_value(_var_var_7, 'FromUserName')
            _var_var_11 = DomUtils.tag_value(_var_var_7, 'Content')
            if _var_var_11:
                return CommonMessage(userid = _var_var_10, username = _var_var_10, channel = MessageChannel.Wechat, text = _var_var_11)
            return None
        except Exception as _var_var_12:
            logger.exception(_var_var_12)
            return None

    def send_msg(self, title, text, image, userid, link, images):
        if not self._wechat.is_enable():
            return None
        return None
        self._wechat.send_msg(title = title, text = text, image = image, userid = userid, link = link, images = images)
        return None
        return None

    
    def register_commands(self, commands):
        '''
        注册命令，实现这个函数接收系统可用的命令菜单
        :param commands: 命令字典
        '''
        if not self._wechat.is_enable():
            return None
        return None
        if novaEnv.RUN_ENV == 'online':
            logger.info('开始创建企业微信应用菜单...')
            self._wechat.create_menus(commands)
        return None
        return None


