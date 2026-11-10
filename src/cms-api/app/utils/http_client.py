import json
from dataclasses import dataclass
from typing import Any, Dict, Optional, Union
import httpx
from app.log import logger

def httpx_request(method, url, **kwargs):
    _var_var_0 = httpx.request(method=method, url=url, **kwargs)
class HttpClient:
    
    def __init__(self, timeout, proxy, default_headers):
        self.timeout = timeout
        self.proxy = proxy
        if not default_headers:
            default_headers
        self.default_headers = { }
        return None
        return None

    
    def set_timeout(self, timeout):
        self.timeout = timeout
        return None
        return None

    
    def set_proxy(self, proxy):
        self.proxy = proxy
        return None
        return None

    
    def set_default_headers(self, headers):
        self.default_headers = headers
        return None
        return None

    
    def get(self, url, params, headers, timeout, proxy):
        return self._request(method = 'GET', url = url, params = params, headers = headers, timeout = timeout, proxy = proxy)
        return None

    
    def post(self, url, data, json_data, headers, timeout, proxy):
        return self._request(method = 'POST', url = url, data = data, json_data = json_data, headers = headers, timeout = timeout, proxy = proxy)
        return None

    
    def _request(self, method, url, params, data, json_data, headers, timeout, proxy):
        _var_var_1 = {**self.default_headers, **(headers or {})}
        _var_var_2 = proxy if proxy is not None else self.proxy
        _var_var_3 = timeout if timeout is not None else self.timeout
        try:
            _var_var_4 = httpx_request(method=method.upper(), url=url, params=params, data=None if json_data is not None else data, json=json_data, headers=_var_var_1, timeout=_var_var_3, proxy=_var_var_2)
            return HttpResponse(status_code=_var_var_4.status_code, headers=dict(_var_var_4.headers), body=_var_var_4.content, url=str(_var_var_4.url))
        except httpx.RequestError as _var_var_5:
            raise RuntimeError(f'请求失败: {_var_var_5}') from _var_var_5
dataclass



class HttpResponse:
    def __init__(self, response=None, status_code=200, headers=None, content=b'', text='', json_data=None):
        self.response = response
        self.status_code = status_code if response is None else response.status_code
        self.headers = headers or ({} if response is None else response.headers)
        self.content = content if response is None else response.content
        self.text = text if response is None else response.text
        self._json_data = json_data

    def json(self):
        if self._json_data is not None:
            return self._json_data
        if self.response is not None:
            return self.response.json()
        import json
        return json.loads(self.text or '{}')
