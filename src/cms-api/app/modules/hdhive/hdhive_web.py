import json
import base64
import re
from typing import Any, Dict, Optional, Union
from urllib.parse import urljoin
from datetime import datetime, timezone, timedelta
from app.utils.http_client import HttpClient, HttpResponse
from app.utils.mjson import JsonUtils

class HDHiveWebClient:
    '''HDHive 网页端会话封装，适用于基于浏览器登录态的请求。'''
    DEFAULT_BASE_URL = 'https://re0.me'
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    DEFAULT_LOGIN_ACTION = '602b5a3af7ab2e93be6a14001ca83c1be491ccecea'
    DEFAULT_SIGN_ACTION = '402b7e1f30165a6ded288e0043f2dbb11db4a998a1'
    CST = timezone(timedelta(hours = 8))
    @staticmethod
    def _normalize_proxy(proxy):
        if not proxy:
            return None
        if isinstance(proxy, str):
            return proxy
        return proxy.get('https') or proxy.get('http')
    
    def __init__(self, base_url, proxy, timeout, user_agent):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self._cookies = { }
        self._default_headers = {
            'user-agent': user_agent,
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache' }
        self.client = HttpClient(timeout = timeout, proxy = self._normalize_proxy(proxy), default_headers = self._default_headers)
        return None
        return None

    @staticmethod
    def _cookie_string_to_dict(cookie):
        _var_var_0 = {}
        for _var_var_1 in cookie.split(';'):
            if '=' not in _var_var_1:
                continue
            _var_var_2, _var_var_3 = _var_var_1.split('=', 1)
            _var_var_0[_var_var_2.strip()] = _var_var_3.strip()
        return _var_var_0
if '=' not in _var_var_1:
    
    def set_cookies(self, cookies):
        _var_var_4 = self._cookie_string_to_dict(cookies) if isinstance(cookies, str) else cookies
        self._cookies.update(_var_var_4)
        return None
        return None

    
    def update_headers(self, headers):
        self._default_headers.update(headers)
        self.client.set_default_headers(self._default_headers)
        return None
        return None

    
    def build_url(self, path):
        return urljoin(f'''{self.base_url}/''', path.lstrip('/'))
        return None

    
    def _build_cookie_header(self) -> Optional[str]:
        if not self._cookies:
            return None
        return '; '.join(f'{_var_var_2}={_var_var_3}' for _var_var_2, _var_var_3 in self._cookies.items())
        # None('; '.join)
        return None

    @staticmethod
    def _extract_cookie_pairs(set_cookie_header):
        if not set_cookie_header:
            return {}
        _var_var_5 = {}
        for _var_var_6 in set_cookie_header.split(','):
            _var_var_7 = _var_var_6.strip().split(';', 1)[0].strip()
            if '=' not in _var_var_7:
                continue
            _var_var_2, _var_var_3 = _var_var_7.split('=', 1)
            if _var_var_2.lower() in {'path', 'domain', 'secure', 'expires', 'httponly', 'samesite', 'max-age'}:
                continue
            _var_var_5[_var_var_2.strip()] = _var_var_3.strip()
        return _var_var_5

    @staticmethod
    def _decode_jwt_part(part):
        _var_var_8 = '=' * (-len(part) % 4)
        _var_var_9 = base64.urlsafe_b64decode(part + _var_var_8)
        return json.loads(_var_var_9.decode('utf-8'))
    
    def decode_jwt(self, token):
        if not token:
            return {}
        _var_var_10 = token.split('.')
        if len(_var_var_10) != 3:
            return {'raw': token, 'error': 'invalid jwt format'}
        try:
            _var_var_11 = self._decode_jwt_part(_var_var_10[0])
            _var_var_12 = self._decode_jwt_part(_var_var_10[1])
            _var_var_14 = _var_var_12.get('exp')
            _var_var_15 = _var_var_12.get('nbf')
            _var_var_16 = _var_var_12.get('iat')
            return {
                'header': _var_var_11,
                'payload': _var_var_12,
                'exp': _var_var_14,
                'nbf': _var_var_15,
                'iat': _var_var_16
            }
        except Exception as _var_var_7:
            return {'raw': token, 'error': str(_var_var_7)}


