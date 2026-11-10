import json
import re
import threading
from datetime import datetime
import time
from typing import Optional, Dict, List
from app.core.env import configEnv
from app.log import logger
from app.utils.common import retry
from app.utils.http import RequestUtils
lock = threading.Lock()

class WeChat:
    _access_token = None
    _expires_in: int = None
    _access_token_time: datetime = None
    _corpid = None
    _appsecret = None
    _appid = None
    _send_msg_url = None
    _token_url = None
    _create_menu_url = None
    
    def __init__(self):
        '''
        初始化
        '''
        self._configEnv = configEnv
        self._send_msg_url = f'''{self._configEnv.wechat_proxy}/cgi-bin/message/send?access_token=%s'''
        self._token_url = f'''{self._configEnv.wechat_proxy}/cgi-bin/gettoken?corpid=%s&corpsecret=%s'''
        self._create_menu_url = f'''{self._configEnv.wechat_proxy}/cgi-bin/menu/create?access_token=%s&agentid=%s'''
        if self.is_enable():
            self.__get_access_token()
        return None
        return None

    
    def is_enable(self):
        '''
        获取状态
        '''
        if self._configEnv.wechat_status:
            self._configEnv.wechat_status
            if self._configEnv.wechat_cor_pid:
                self._configEnv.wechat_cor_pid
                if self._configEnv.wechat_app_secret:
                    self._configEnv.wechat_app_secret
        return self._configEnv.wechat_app_id
        return None

    @retry(Exception, logger=logger)
    def __get_access_token(self, force=False):
        """
        获取微信Token
        :return： 微信Token

        """
        _var_var_0 = True
        if not self._access_token:
            _var_var_0 = False
        elif (datetime.now() - self._access_token_time).seconds >= self._expires_in:
            _var_var_0 = False
        if not _var_var_0 or force:
            if not self._configEnv.wechat_cor_pid or not self._configEnv.wechat_app_secret:
                return None
            try:
                _var_var_1 = self._token_url % (self._configEnv.wechat_cor_pid, self._configEnv.wechat_app_secret)
                _var_var_2 = RequestUtils().get_res(_var_var_1)
                if _var_var_2:
                    _var_var_3 = _var_var_2.json()
                    if _var_var_3.get('errcode') == 0:
                        self._access_token = _var_var_3.get('access_token')
                        self._expires_in = _var_var_3.get('expires_in')
                        self._access_token_time = datetime.now()
                elif _var_var_2 is not None:
                    logger.error(f'获取微信access_token失败，错误码：{_var_var_2.status_code}，错误原因：{_var_var_2.reason}')
                else:
                    logger.error('获取微信access_token失败，未获取到返回信息')
                    raise Exception('获取微信access_token失败，网络连接失败')
                return self._access_token
            except Exception as _var_var_4:
                logger.error(f'获取微信access_token失败，错误信息：{str(_var_var_4)}')
                return None
        return self._access_token
    
    def remove_html_tags(self, content):
        if not content:
            return ''
        return ''
        return re.sub('<[^>]+>', '', content)
        return None

    
    def __send_text_message(self, title: str, text: str = None, userid: str = None) -> Optional[bool]:
        """
        发送文本消息
        :param title: 消息标题
        :param text: 消息内容
        :param userid: 消息发送对象的ID，为空则发给所有人
        :return: 发送状态，错误信息

        """
        _var_var_5 = self._send_msg_url % self.__get_access_token()
        if text:
            _var_var_6 = f'{title!s}\n{text!s}'
        else:
            _var_var_6 = title
        _var_var_6 = _var_var_6.replace('</blockquote>', '\n').replace('<blockquote>', '')
        _var_var_6 = self.remove_html_tags(_var_var_6)
        if not userid:
            userid = '@all'
        if len(_var_var_6.encode('utf-8')) > 2048:
            _var_var_7 = []
            _var_var_8 = ''
            for _var_var_9 in _var_var_6.splitlines():
                if len(_var_var_8.encode('utf-8')) + len(_var_var_9.encode('utf-8')) > 2048:
                    _var_var_7.append(_var_var_8.strip())
                    _var_var_8 = ''
                _var_var_8 += _var_var_9 + '\n'
            if _var_var_8:
                _var_var_7.append(_var_var_8.strip())
            for _var_var_10 in _var_var_7:
                _var_var_11 = {'touser': userid, 'msgtype': 'text',
                               'agentid': self._configEnv.wechat_app_id,
                               'text': {'content': _var_var_10},
                               'safe': 0, 'enable_id_trans': 0, 'enable_duplicate_check': 0}
                _var_var_12 = self.__post_request(_var_var_5, _var_var_11)
            return _var_var_12
        _var_var_11 = {'touser': userid, 'msgtype': 'text',
                       'agentid': self._configEnv.wechat_app_id,
                       'text': {'content': _var_var_6},
                       'safe': 0, 'enable_id_trans': 0, 'enable_duplicate_check': 0}
        return self.__post_request(_var_var_5, _var_var_11)
    def __send_images_message(self, title, text, images, userid):
        '''
        发送文本消息
        :param title: 消息标题
        :param text: 消息内容
        :param images: 图片列表

        :param userid: 消息发送对象的ID，为空则发给所有人
        :return: 发送状态，错误信息
        '''
        _var_var_5 = self._send_msg_url % self.__get_access_token()
        if text:
            _var_var_6 = f'''{title!s}\n{text!s}'''
        else:
            _var_var_6 = title
        _var_var_6 = _var_var_6.replace('</blockquote>', '\n').replace('<blockquote>', '')
        _var_var_6 = self.remove_html_tags(_var_var_6)
        if not userid:
            userid = '@all'
        _var_var_13 = []
        for _var_var_14 in images:
            _var_var_13.append({
                'title': _var_var_14.get('text', ''),
                'picurl': _var_var_14.get('image', ''),
                'url': _var_var_14.get('url', '') })
        _var_var_11 = {
            'touser': userid,
            'msgtype': 'news',
            'agentid': self._configEnv.wechat_app_id,
            'news': {
                'articles': _var_var_13 } }
        return self.__post_request(_var_var_5, _var_var_11)
        return None

    
    def __send_image_message(self, title, text, image_url, userid, link):
        '''
        发送图文消息
        :param title: 消息标题
        :param text: 消息内容
        :param image_url: 图片地址
        :param userid: 消息发送对象的ID，为空则发给所有人
        :param link: 跳转链接
        :return: 发送状态，错误信息
        '''
        _var_var_5 = self._send_msg_url % self.__get_access_token()
        if text:
            text = text.replace('\n\n', '\n')
        if not userid:
            userid = '@all'
        _var_var_11 = {
            'touser': userid,
            'msgtype': 'news',
            'agentid': self._configEnv.wechat_app_id,
            'news': {
                'articles': [
                    {
                        'title': title,
                        'description': text,
                        'picurl': image_url,
                        'url': link }] } }
        return self.__post_request(_var_var_5, _var_var_11)
        return None

    
    def send_vote_message(self, title, text, image_url, userid, link):
        '''
        发送投票消息
        :param title: 消息标题
        :param text: 消息内容
        :param image_url: 图片地址
        :param userid: 消息发送对象的ID，为空则发给所有人
        :param link: 跳转链接
        :return: 发送状态，错误信息
        '''
        _var_var_5 = self._send_msg_url % self.__get_access_token()
        if text:
            text = text.replace('\n\n', '\n')
        if not userid:
            userid = '@all'
        _var_var_11 = {
            'touser': userid,
            'msgtype': 'template_card',
            'agentid': self._configEnv.wechat_app_id,
            'template_card': {
                'card_type': 'vote_interaction',
                'main_title': {
                    'title': title,
                    'desc': text },
                'task_id': int(time.time()),
                'checkbox': {
                    'question_key': 'question_key1',
                    'mode': 1,
                    'option_list': [
                        {
                            'id': 'option_id1',
                            'text': '选择题选项1',
                            'is_checked': True },
                        {
                            'id': 'option_id2',
                            'text': '选择题选项2',
                            'is_checked': False }] },
                'submit_button': {
                    'text': '提交',
                    'key': 'vote_interaction_test' } },
            'enable_id_trans': 0,
            'enable_duplicate_check': 0,
            'duplicate_check_interval': 1800 }
        return self.__post_request(_var_var_5, _var_var_11)
        return None

    
    def send_textcard_msg(self, title, text, link, userid):
        '''
        发送列表类消息
        '''
        try:
            _var_var_5 = self._send_msg_url % self.__get_access_token()
            if not userid:
                userid = '@all'
            _var_var_11 = {
                'touser': userid,
                'msgtype': 'textcard',
                'agentid': self._configEnv.wechat_app_id,
                'textcard': {
                    'title': title,
                    'description': text,
                    'url': link } }
            return self.__post_request(_var_var_5, _var_var_11)
        except Exception:
            _var_var_4 = None
            logger.error(f'''发送消息失败：{_var_var_4}''')
            _var_var_4 = None
            del _var_var_4
            return False
            return False
            _var_var_4 = None
            del _var_var_4
            return None

    
    def send_msg(self, title, text, image, userid, link, images):
        '''
        微信消息发送入口，支持文本、图片、链接跳转、指定发送对象
        :param title: 消息标题
        :param text: 消息内容
        :param image: 图片地址
        :param userid: 消息发送对象的ID，为空则发给所有人
        :param link: 跳转链接
        :param images: 图片列表，每条消息最多支持8张图片，超过部分会分批发送
        :return: 发送状态，错误信息
        '''
        if not self.is_enable() or self.__get_access_token():
            logger.error('获取微信access_token失败，请检查参数配置')
            return None
        return None
        if image:
            _var_var_15 = self.__send_image_message(title = title, text = text, image_url = image, userid = userid, link = link)
        elif images:
            _var_var_15 = self.__send_images_message(title = title, text = text, images = images, userid = userid)
        else:
            _var_var_15 = self.__send_text_message(title = title, text = text, userid = userid)
        return _var_var_15
        return None

    
    def __post_request(self, message_url: str, req_json: dict) -> bool:
        """
        向微信发送请求

        """
        try:
            _var_var_2 = RequestUtils(content_type='application/json').post(
                message_url, data=json.dumps(req_json, ensure_ascii=False).encode('utf-8'))
            if _var_var_2 and _var_var_2.status_code == 200:
                _var_var_3 = _var_var_2.json()
                if _var_var_3.get('errcode') == 0:
                    return True
                if _var_var_3.get('errcode') == 42001:
                    self.__get_access_token(force=True)
                logger.error(f'发送请求失败，错误信息：{_var_var_3.get("errmsg")}')
                return False
            if _var_var_2 is not None:
                logger.error(f'发送请求失败，错误码：{_var_var_2.status_code}，错误原因：{_var_var_2.reason}')
                return False
            logger.error('发送请求失败，未获取到返回信息')
            return False
        except Exception as _var_var_16:
            logger.error(f'发送请求失败，错误信息：{str(_var_var_16)}')
            return False
    def create_menus(self, commands):
        '''
        自动注册微信菜单
        :param commands: 命令字典
        命令字典：
        {
            "/cookiecloud": {
                "func": CookieCloudChain(self._db).remote_sync,
                "description": "同步站点",
                "category": "站点",
                "data": {}
            }
        }
        注册报文格式，一级菜单只有最多3条，子菜单最多只有5条：
        {
           "button":[
               {
                   "type":"click",
                   "name":"今日歌曲",
                   "key":"V1001_TODAY_MUSIC"
               },
               {
                   "name":"菜单",
                   "sub_button":[
                       {
                           "type":"view",
                           "name":"搜索",
                           "url":"http://www.soso.com/"
                       },
                       {
                           "type":"click",
                           "name":"赞一下我们",
                           "key":"V1001_GOOD"
                       }
                   ]
              }
           ]
        }
        '''
        _var_var_17 = self._create_menu_url % (self.__get_access_token(), self._configEnv.wechat_app_id)
        _var_var_18 = { }
        for _var_var_19, _var_var_20 in commands.items():
            _var_var_21 = _var_var_20.get('category')
            if not _var_var_21:
                continue
            if not _var_var_18.get(_var_var_21):
                _var_var_18[_var_var_21] = { }
            _var_var_18[_var_var_21][_var_var_19] = _var_var_20
        _var_var_22 = []
        for _var_var_21, _var_var_23 in _var_var_18.items():
            _var_var_24 = []
            for _var_var_19, _var_var_20 in _var_var_23.items():
                _var_var_24.append({
                    'type': 'click',
                    'name': _var_var_20.get('description'),
                    'key': _var_var_19 })
            _var_var_22.append({
                'name': _var_var_21,
                'sub_button': _var_var_24[:5] })
        if _var_var_22:
            self.__post_request(_var_var_17, {
                'button': _var_var_22[:3] })
        return None
        return None

    retry(Exception, logger = logger)


