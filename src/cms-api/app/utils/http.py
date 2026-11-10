from typing import Union, Any, Optional
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
import requests
import urllib3
from requests import Session, Response
from urllib3.exceptions import InsecureRequestWarning
from app.log import logger
urllib3.disable_warnings(InsecureRequestWarning)

class RequestUtils:
    _headers: dict = None
    _cookies: Union[(str, dict)] = None
    _proxies: dict = None
    _timeout: int = 20
    _session: Session = None
    
    def __init__(self, headers, ua, cookies, proxies, session, timeout, referer, content_type, accept_type):
        if not content_type:
            content_type = 'application/x-www-form-urlencoded; charset=UTF-8'
        if headers:
            self._headers = headers
        else:
            self._headers = {
                'User-Agent': ua,
                'Content-Type': content_type,
                'Accept': accept_type,
                'referer': referer }
        if cookies:
            if isinstance(cookies, str):
                self._cookies = self.cookie_parse(cookies)
            else:
                self._cookies = cookies
        if proxies:
            self._proxies = proxies
        if session:
            self._session = session
        if timeout:
            self._timeout = timeout
        return None
        return None

    
    def request(self, method: str, url: str, raise_exception: bool = False, **kwargs) -> Optional[Response]:
        '''
        发起HTTP请求
        :param method: HTTP方法，如 get, post, put 等
        :param url: 请求的URL
        :param raise_exception: 是否在发生异常时抛出异常，否则默认拦截异常返回None
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: HTTP响应对象
        :raises: requests.exceptions.RequestException 仅raise_exception为True时会抛出
        '''
        if self._session is None:
            request_func = requests.request
        else:
            request_func = self._session.request
        kwargs.setdefault('headers', self._headers)
        kwargs.setdefault('cookies', self._cookies)
        kwargs.setdefault('proxies', self._proxies)
        kwargs.setdefault('timeout', self._timeout)
        kwargs.setdefault('verify', False)
        kwargs.setdefault('stream', False)
        try:
            return request_func(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logger.debug(f'请求失败: {e}')
            if raise_exception:
                raise
            return None
    def get(self, url: str, params: dict = None, **kwargs) -> Optional[str]:
        '''
        发送GET请求
        :param url: 请求的URL
        :param params: 请求的参数
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: 响应的内容，若发生RequestException则返回None
        '''
        res = self.request(method='get', url=url, params=params, **kwargs)
        return str(res.content, 'utf-8') if res else None
    def post(self, url: str, data: Any = None, json: dict = None, **kwargs) -> Optional[Response]:
        '''
        发送POST请求
        :param url: 请求的URL
        :param data: 请求的数据
        :param json: 请求的JSON数据
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: HTTP响应对象，若发生RequestException则返回None
        '''
        if json is None:
            json = {}
        return self.request(method='post', url=url, data=data, json=json, **kwargs)
    def put(self, url: str, data: Any = None, **kwargs) -> Optional[Response]:
        '''
        发送PUT请求
        :param url: 请求的URL
        :param data: 请求的数据
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: HTTP响应对象，若发生RequestException则返回None
        '''
        return self.request(method='put', url=url, data=data, **kwargs)
    def get_res(self, url: str, params: dict = None, data: Any = None, json: dict = None, allow_redirects: bool = True, raise_exception: bool = False, **kwargs) -> Optional[Response]:
        '''
        发送GET请求并返回响应对象
        :param url: 请求的URL
        :param params: 请求的参数
        :param data: 请求的数据
        :param json: 请求的JSON数据
        :param allow_redirects: 是否允许重定向
        :param raise_exception: 是否在发生异常时抛出异常，否则默认拦截异常返回None
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: HTTP响应对象，若发生RequestException则返回None
        :raises: requests.exceptions.RequestException 仅raise_exception为True时会抛出
        '''
        return self.request(method='get', url=url, params=params, data=data, json=json, allow_redirects=allow_redirects, raise_exception=raise_exception, **kwargs)
    def post_res(self, url: str, data: Any = None, params: dict = None, allow_redirects: bool = True, files: Any = None, json: dict = None, raise_exception: bool = False, **kwargs) -> Optional[Response]:
        '''
        发送POST请求并返回响应对象
        :param url: 请求的URL
        :param data: 请求的数据
        :param params: 请求的参数
        :param allow_redirects: 是否允许重定向
        :param files: 请求的文件
        :param json: 请求的JSON数据
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :param raise_exception: 是否在发生异常时抛出异常，否则默认拦截异常返回None
        :return: HTTP响应对象，若发生RequestException则返回None
        :raises: requests.exceptions.RequestException 仅raise_exception为True时会抛出
        '''
        return self.request(method='post', url=url, data=data, params=params, allow_redirects=allow_redirects, files=files, json=json, raise_exception=raise_exception, **kwargs)
    def put_res(self, url: str, data: Any = None, params: dict = None, allow_redirects: bool = True, files: Any = None, json: dict = None, raise_exception: bool = False, **kwargs) -> Optional[Response]:
        '''
        发送PUT请求并返回响应对象
        :param url: 请求的URL
        :param data: 请求的数据
        :param params: 请求的参数
        :param allow_redirects: 是否允许重定向
        :param files: 请求的文件
        :param json: 请求的JSON数据
        :param raise_exception: 是否在发生异常时抛出异常，否则默认拦截异常返回None
        :param kwargs: 其他请求参数，如headers, cookies, proxies等
        :return: HTTP响应对象，若发生RequestException则返回None
        :raises: requests.exceptions.RequestException 仅raise_exception为True时会抛出
        '''
        return self.request(method='put', url=url, data=data, params=params, allow_redirects=allow_redirects, files=files, json=json, raise_exception=raise_exception, **kwargs)
    @staticmethod
    def cookie_parse(cookies_str: str, array: bool = False) -> Union[list, dict]:
        '''
        解析cookie，转化为字典或者数组
        :param cookies_str: cookie字符串
        :param array: 是否转化为数组
        :return: 字典或者数组
        '''
        if not cookies_str:
            return {}
        cookies = {}
        cookies_array = cookies_str.split(';')
        for cookies_item in cookies_array:
            cookies_item_array = cookies_item.split('=')
            if len(cookies_item_array) > 1:
                cookies[cookies_item_array[0].strip()] = cookies_item_array[1].strip()
        if array:
            return [{'name': key, 'value': value} for key, value in cookies.items()]
        return cookies
    @staticmethod
    def standardize_base_url(host):
        '''
        标准化提供的主机地址，确保它以http://或https://开头，并且以斜杠(/)结尾
        :param host: 提供的主机地址字符串
        :return: 标准化后的主机地址字符串
        '''
        if not host:
            return host
        if not host.endswith('/'):
            host += '/'
        if not host.startswith('http://') and not host.startswith('https://'):
            host = 'http://' + host
        return host

    @staticmethod
    def adapt_request_url(host, endpoint):
        '''
        基于传入的host，适配请求的URL，确保每个请求的URL是完整的，用于在发送请求前自动处理和修正请求的URL。
        :param host: 主机头
        :param endpoint: 端点
        :return: 完整的请求URL字符串
        '''
        if not host and not endpoint:
            return None
        if endpoint.startswith(('http://', 'https://')):
            return endpoint
        host = RequestUtils.standardize_base_url(host)
        return urljoin(host, endpoint) if host else endpoint
    @staticmethod
    def combine_url(host: str, path: Optional[str] = None, query: Optional[dict] = None) -> Optional[str]:
        '''
        使用给定的主机头、路径和查询参数组合生成完整的URL。
        :param host: str, 主机头，例如 https://example.com
        :param path: Optional[str], 包含路径和可能已经包含的查询参数的端点，例如 /path/to/resource?current=1
        :param query: Optional[dict], 可选，额外的查询参数，例如 {"key": "value"}
        :return: str, 完整的请求URL字符串
        '''
        try:
            if path is None:
                path = '/'
            host = RequestUtils.standardize_base_url(host)
            url = urljoin(host, path)
            parsed_url = urlparse(url)
            query_dict = parse_qs(parsed_url.query)
            if query:
                for key, value in query.items():
                    query_dict[key] = value
            query_str = urlencode(query_dict, doseq=True)
            new_parsed_url = parsed_url._replace(query=query_str)
            new_url = urlunparse(new_parsed_url)
            return str(new_url)
        except Exception as e:
            logger.debug(f'Error combining URL: {e}')
            return None


