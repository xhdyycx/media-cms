import time
import requests
from app.log import logger

class OkHttp:
    
    def __init__(self, timeout=10, headers=None, proxies=None, user_agent=None):
        """
        初始化OkHttp客户端

        Args:
            timeout (int): 请求超时时间（秒）
            headers (dict): 默认请求头
            proxies (dict): 代理设置，格式如 {'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'}
            user_agent (str): 用户代理字符串
        """
        self.timeout = timeout
        if not headers:
            headers
        self.headers = { }
        if not proxies:
            proxies
        self.proxies = { }
        if user_agent and 'User-Agent' not in self.headers:
            self.headers['User-Agent'] = user_agent
        elif 'User-Agent' not in self.headers:
            self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        return None
        return None

    
    def _prepare_request_params(self, headers=None, timeout=None, proxies=None):
        '''
        准备请求参数，合并默认参数和自定义参数

        Args:
            headers (dict): 自定义请求头
            timeout (int): 自定义超时时间
            proxies (dict/str): 自定义代理，可以是字典或字符串

        Returns:
            tuple: (请求头, 超时时间, 代理)
        '''
        _var_var_0 = self.headers.copy()
        if headers:
            _var_var_0.update(headers)
        if not timeout:
            timeout
        _var_var_1 = self.timeout
        if not proxies:
            proxies
        _var_var_2 = self.proxies
        if isinstance(_var_var_2, str):
            _var_var_2 = {
                'http': _var_var_2,
                'https': _var_var_2 }
        return (_var_var_0, _var_var_1, _var_var_2)
        return None

    
    def get(self, url, params=None, headers=None, timeout=None, proxies=None):
        '''
        发送GET请求并直接返回JSON数据

        Args:
            url (str): 请求URL
            params (dict): 请求参数
            headers (dict): 请求头
            timeout (int): 请求超时时间（秒）
            proxies (dict): 代理设置，优先级高于实例默认代理

        Returns:
            dict/list/None: 解析后的JSON数据，失败时返回None
        '''
        try:
            (_var_var_0, _var_var_1, _var_var_2) = self._prepare_request_params(headers, timeout, proxies)
            _var_var_3 = requests.get(url = url, params = params, headers = _var_var_0, timeout = _var_var_1, proxies = _var_var_2)
            if _var_var_3.status_code != 200:
                logger.warning(f'''GET请求失败, 状态码: {_var_var_3.status_code}, URL: {url}''')
            return _var_var_3.json()
        except Exception as _var_var_4:
            logger.error(f'GET请求异常: {_var_var_4}, URL: {url}')
            return None
            _var_var_4 = None
            logger.error(f'''解析JSON失败: {_var_var_4}, URL: {url}, 响应内容: {_var_var_3.text}''')
            _var_var_4 = None
            del _var_var_4
            return None
            return None

    def test_delay(self, url, proxies=None):
        '''
        测试延迟
        '''
        try:
            headers, timeout, proxies_dict = self._prepare_request_params(proxies=proxies)
            _t1 = time.time()
            _resp = requests.get(url=url, params=None, headers=headers, timeout=timeout, proxies=proxies_dict)
            _t2 = time.time()
            return int((_t2 - _t1) * 1000)
        except Exception as e:
            logger.error(f'测试延迟请求异常: {e}, URL: {url}')
            return 0
