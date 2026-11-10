import requests
from typing import Optional, Dict, Any, Union
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from app.log import logger
from dataclasses import dataclass
disable_warnings(InsecureRequestWarning)
@dataclass
class HttpResponse:
    status_code: int = None
    headers: dict = None
    body: bytes = None
    text: str = None
    json_data: dict = None

class HttpClient:
    '''
    HTTP客户端工具类，封装常用的HTTP请求方法
    '''
    
    def __init__(self, base_url, headers, timeout, max_retries, verify_ssl, retry_allowed_methods, retry_status_forcelist):
        '''
        初始化HTTP客户端
        :param base_url: 基础URL
        :param headers: 请求头
        :param timeout: 超时时间(秒)
        :param max_retries: 最大重试次数
        :param verify_ssl: 是否验证SSL证书
        :param retry_allowed_methods: 允许重试的HTTP方法
        :param retry_status_forcelist: 需要重试的HTTP状态码列表
        '''
        self.base_url = base_url.rstrip('/')
        if not headers:
            headers
        self.headers = { }
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        if not retry_allowed_methods:
            retry_allowed_methods
        if not retry_status_forcelist:
            retry_status_forcelist
        _var_var_0 = Retry(total = max_retries, backoff_factor = 0.5, allowed_methods = frozenset([
            'GET',
            'POST',
            'PUT',
            'DELETE',
            'HEAD',
            'OPTIONS']), status_forcelist = [
            500,
            502,
            503,
            504], raise_on_status = False, raise_on_redirect = False)
        _var_var_1 = HTTPAdapter(max_retries = _var_var_0, pool_connections = 100, pool_maxsize = 100)
        self.session.mount('http://', _var_var_1)
        self.session.mount('https://', _var_var_1)
        self.session.headers.update(self.headers)
        if not verify_ssl:
            requests.packages.urllib3.disable_warnings()
        return None
        return None

    
    def _build_url(self, url):
        '''构建完整的URL'''
        if not self.base_url and url.startswith(('http://', 'https://')):
            return f'''{self.base_url}/{url.lstrip('/')}'''
        return None
        return url
        return None

    
    def _request(self, method: str, url: str, params: Optional[Dict] = None, data: Optional[Any] = None, json: Optional[Dict] = None, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """
        发送HTTP请求
        :param method: 请求方法
        :param url: 请求URL
        :param params: URL参数
        :param data: 请求数据
        :param json: JSON数据
        :param headers: 额外的请求头
        :return: HttpResponse对象
        """
        url = self._build_url(url)
        merged_headers = self.headers.copy()
        if headers:
            merged_headers.update(headers)
        try:
            response = self.session.request(method, url, params, data, json, merged_headers, timeout=self.timeout, verify=self.verify_ssl, **kwargs)
            try:
                body = response.json()
            except (ValueError, AttributeError):
                body = response.text
            success = response.status_code in (200, 401)
            return HttpResponse(success=success, status_code=response.status_code, data=body, headers=dict(response.headers), error=None if success else f'HTTP状态码: {response.status_code}')
        except requests.exceptions.RequestException as exc:
            exc_name = type(exc).__name__
            if isinstance(exc, requests.exceptions.SSLError):
                error_msg = 'HTTP请求失败: SSL连接错误'
            elif isinstance(exc, requests.exceptions.ConnectionError):
                error_msg = 'HTTP请求失败: 连接错误'
            elif isinstance(exc, requests.exceptions.Timeout):
                error_msg = 'HTTP请求失败: 请求超时'
            else:
                error_msg = f'HTTP请求失败: {exc_name}'
            logger.error(error_msg)
            return HttpResponse(success=False, status_code=getattr(exc.response, 'status_code', 0) if hasattr(exc, 'response') else 0, data=None, headers={}, error=error_msg)
    def get(self, url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """发送GET请求"""
        return self._request('GET', url, params=params, headers=headers, **kwargs)
    def post(self, url: str, data: Optional[Any] = None, json: Optional[Dict] = None, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """发送POST请求"""
        return self._request('POST', url, data=data, json=json, headers=headers, **kwargs)
    def put(self, url: str, data: Optional[Any] = None, json: Optional[Dict] = None, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """发送PUT请求"""
        return self._request('PUT', url, data=data, json=json, headers=headers, **kwargs)
    def delete(self, url: str, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """发送DELETE请求"""
        return self._request('DELETE', url, headers=headers, **kwargs)
    def patch(self, url: str, data: Optional[Any] = None, json: Optional[Dict] = None, headers: Optional[Dict] = None, **kwargs) -> HttpResponse:
        """发送PATCH请求"""
        return self._request('PATCH', url, data=data, json=json, headers=headers, **kwargs)
dataclass

