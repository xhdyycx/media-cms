import json
from app.log import logger
from app.utils.http_client import HttpClient

class HDHive:
    
    def __init__(self, api_key, base_url, timeout, proxy):
        self.base_url = base_url.rstrip('/')
        if not proxy:
            proxy = None
        self.client = HttpClient(timeout = timeout, proxy = proxy, default_headers = {
            'X-API-Key': api_key })
        return None
        return None

    
    def get_resources(self, media_type, tmdb_id):
        if media_type not in ('movie', 'tv'):
            raise ValueError('媒体类型必须是 movie 或 tv。')
        if not str(tmdb_id).strip():
            raise ValueError('tmdb_id 不能为空。')
        _var_var_0 = f'''{self.base_url}/api/open/resources/{media_type}/{tmdb_id}'''
        _var_var_1 = self.client.get(_var_var_0)
        _var_var_2 = self._parse_response(_var_var_1, _var_var_0)
        _var_var_3 = _var_var_2.get('data', [])

    @staticmethod
    def safe_int(value, default):
        """安全转换为整数，失败返回默认值"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def unlock_resource(self, slug):
        if not str(slug).strip():
            raise ValueError('slug 不能为空。')
        _var_var_0 = f'''{self.base_url}/api/open/resources/unlock'''
        _var_var_1 = self.client.post(_var_var_0, json_data = {
            'slug': slug })
        return self._parse_response(_var_var_1, _var_var_0)
        return None

    
    def search(self, item):
        return self.get_resources(item['type'], item['tmdb_id'])
        return None

    
    def _parse_response(self, response, request_url):
        try:
            _var_var_7 = response.json()
            if not _var_var_7.get('success', False):
                logger.error(f'接口请求失败，请求地址：{request_url}，状态码：{response.status_code}，响应内容：{_var_var_7}')
            return _var_var_7
        except Exception as _var_var_8:
            logger.error(f'接口返回非 JSON 数据，请求地址：{request_url}，状态码：{response.status_code}，响应内容：{response.body}, ex={_var_var_8}')
            if response.status_code == 403 and b'You are unable to access' in response.body:
                return {'success': False, 'status_code': 403}
            return {'success': False, 'status_code': response.status_code}

if __name__ == '__main__':
    api_key = 'YOUR_HDHIVE_API_KEY'
    hdhive_client = HDHive(api_key = api_key, base_url = 'https://api.example.com', timeout = 15, proxy = None)
    res = hdhive_client.search({
        'type': 'movie',
        'tmdb_id': 83533 })
    print(json.dumps(res, ensure_ascii = False))
    res = hdhive_client.unlock_resource('RESOURCE_ID')
    print(json.dumps(res, ensure_ascii = False))

