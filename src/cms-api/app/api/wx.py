# File: wx.py (Cleaned & Decompiled)
from typing import Any
from blacksheep import Request, text
from blacksheep.server.controllers import APIController, post, get
from app import schemas
from app.core.env import configEnv
from app.log import logger
from app.modules.wechat import WXBizMsgCrypt
from app.services.event_service import EventService

class WxController(APIController):

    @classmethod
    def route(cls):
        return '/api/wx'

    @post('message')
    async def user_message(self, request: Request):
        """
        用户消息响应
        """
        _var_var_0 = await request.text()
        _var_var_1 = request.query
        EventService().process(_var_var_0, _var_var_1)
        logger.info('处理消息成功...')
        return schemas.Response(success=True)

    @get('message')
    def msg_verify(self, echostr: str = None, msg_signature: str = None, timestamp: str = None, nonce: str = None):
        """
        微信验证响应
        """
        logger.info(f"收到wx验证请求: echostr={echostr}, msg_signature={msg_signature}, timestamp={timestamp}, nonce={nonce}")
        return wechat_verify(echostr, msg_signature, timestamp, nonce)

def wechat_verify(echostr, msg_signature, timestamp, nonce):
    """
    微信验证响应
    """
    try:
        _var_var_2 = WXBizMsgCrypt(sToken=configEnv.wechat_token, sEncodingAESKey=configEnv.wechat_encoding_aes_key, sReceiveId=configEnv.wechat_cor_pid)
        _var_var_4, _var_var_5 = _var_var_2.VerifyURL(sMsgSignature=msg_signature, sTimeStamp=timestamp, sNonce=nonce, sEchoStr=echostr)
        logger.info(f"ret={_var_var_4}, sEchoStr={_var_var_5}")
        if _var_var_4 != 0:
            logger.error('微信请求验证失败 VerifyURL ret: %s' % str(_var_var_4))
        return text(_var_var_5.decode('utf-8'))
    except Exception as _var_var_3:
        logger.error(f"微信请求验证失败: {str(_var_var_3)}")
        return str(_var_var_3)