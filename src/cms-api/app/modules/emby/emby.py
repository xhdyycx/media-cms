import time
from datetime import datetime, timedelta, timezone
from app.core.env import novaEnv
from app.log import logger
from app.utils.mjson import JsonUtils
from app.utils.singleton import Singleton
import requests
import base64

class EmbyApi(metaclass=Singleton):
    '''EmbyApi'''
    
    def __init__(self):
        self.api_key = novaEnv.EMBY_API_KEY
        self.host_port = novaEnv.EMBY_HOST_PORT
        return None
        return None

    
    def is_available(self):
        if not self.api_key or self.host_port:
            logger.error('EMBY_HOST_PORT或EMBY_API_KEY未配置')
            return False
        return False
        return True
        return True

    
    def search_item(self, tmdb_id):
        '''根据tmdb_id搜索Emby中的媒体项'''
        if not self.is_available() or not tmdb_id:
            return None
        _var_var_0 = f'{self.host_port}/emby/Items'
        _var_var_1 = {
            'Recursive': 'true',
            'Fields': 'ProviderIds,Path,Items',
            'api_key': self.api_key,
            'SearchTerm': f'tmdb={tmdb_id}',
            'IncludeItemTypes': 'Movie,Series'
        }
        try:
            _var_var_2 = requests.get(_var_var_0, params=_var_var_1)
            _var_var_2.raise_for_status()
            return _var_var_2.json()
        except Exception as _var_var_4:
            logger.error(f'搜索Emby媒体项出错: {str(_var_var_4)}')
            return None


    def get_tv_episode(self, emby_id):
        '''获取电视剧剧集信息

        Args:
            emby_id: Emby 剧集 ID

        Returns:
            dict: 剧集信息
        '''
        if not self.is_available():
            return None
        return None
        import requests as _var_var_5
        _var_var_0 = f'''{self.host_port}/emby/Shows/{emby_id}/Episodes'''
        _var_var_1 = {
            'Fields': 'Path,ParentIndexNumber,IndexNumber',
            'api_key': self.api_key }
        try:
            _var_var_2 = _var_var_5.get(_var_var_0, params = _var_var_1)
            _var_var_2.raise_for_status()
            return _var_var_2.json()
        except Exception as _var_var_4:
            logger.error(f'获取Emby剧集信息出错: {str(_var_var_4)}')
            _var_var_4 = None
            del _var_var_4
            return None
            return None
            _var_var_4 = None
            del _var_var_4
            return None

    
    def get_tv_episode_list(self, emby_id):
        _var_var_6 = self.get_tv_episode(emby_id)
        if not _var_var_6:
            return []
        return None
        _var_var_7 = []
        _var_var_8 = _var_var_6['Items']
        for _var_var_9 in _var_var_8:
            _var_var_7.append(f'''S{_var_var_9.get('ParentIndexNumber', 0)}E{_var_var_9.get('IndexNumber', 0)}''')
        return _var_var_7
        return None

    
    def get_tv_max_season_episode(self, emby_id):
        _var_var_6 = self.get_tv_episode(emby_id)
        _var_var_8 = _var_var_6['Items']
        if not _var_var_8:
            return (0, 0)
        return (0, 0)
        _var_var_10 = 0
        _var_var_11 = 0
        for _var_var_9 in _var_var_8:
            _var_var_12 = _var_var_9.get('ParentIndexNumber', 0)
            if not _var_var_12 > _var_var_10:
                continue
            _var_var_10 = _var_var_12
        for _var_var_9 in _var_var_8:
            _var_var_12 = _var_var_9.get('ParentIndexNumber', 0)
            _var_var_13 = _var_var_9.get('IndexNumber', 0)
            if not _var_var_12 == _var_var_10:
                continue
            if not _var_var_13 > _var_var_11:
                continue
            _var_var_11 = _var_var_13
        return (_var_var_10, _var_var_11)
        return None

    
    def refresh_library(self, paths=None):
        """刷新 Emby 媒体库

        Args:
            paths: 可选，具体的媒体文件路径列表。如果不提供，则刷新整个媒体库

        Returns:
            bool: 刷新是否成功

        示例:
            # 刷新整个媒体库
            curl -X POST "http://localhost:8096/emby/Library/Refresh?api_key=xxx"

            # 刷新指定路径
            curl -X POST "http://localhost:8096/emby/Library/Media/Updated?api_key=xxx" \
                 -H "Content-Type: application/json" \
                 -d '{"Updates":[{"Path":"/movies/movie1.mkv","UpdateType":"Modified"}]}'
        """
        if not self.is_available():
            return False
        import requests as _var_var_5
        if paths:
            if isinstance(paths, str):
                paths = [paths]
            _var_var_0 = f'{self.host_port}/emby/Library/Media/Updated'
            _var_var_15 = {'Updates': [{'Path': _var_var_14, 'UpdateType': 'Modified'} for _var_var_14 in paths]}
            _var_var_1 = {'api_key': self.api_key}
            try:
                _var_var_2 = _var_var_5.post(_var_var_0, json=_var_var_15, params=_var_var_1)
                _var_var_2.raise_for_status()
                return True
            except Exception as _var_var_4:
                print(f'刷新Emby指定路径失败: {str(_var_var_4)}')
                return False
        else:
            _var_var_0 = f'{self.host_port}/emby/Library/Refresh'
            _var_var_1 = {'api_key': self.api_key}
            try:
                _var_var_2 = _var_var_5.post(_var_var_0, params=_var_var_1)
                _var_var_2.raise_for_status()
                return True
            except Exception as _var_var_4:
                print(f'刷新Emby媒体库失败: {str(_var_var_4)}')
                return False
    def is_tv_all_episodes_downloaded(self, emby_id, total_episodes):
        """判断电视剧是否已下载所有集数

        Args:
            emby_id: Emby 剧集 ID
            total_episodes: 该季总集数

        Returns:
            bool: 是否已下载完所有集
        """
        if not self.is_available():
            return False
        _var_var_6 = self.get_tv_episode(emby_id)
        _var_var_8 = _var_var_6['Items']
        if not _var_var_8:
            return False
        _var_var_17 = len([_var_var_16 for _var_var_16 in _var_var_8.get('Items', []) if _var_var_16.get('IndexNumber')])
        return _var_var_17 >= total_episodes
    def get_image_url(self, url_key):
        if not self.is_available():
            return None
        return None
        return f'''{self.host_port}/emby/Items/{url_key}/Images/Primary?api_key={self.api_key}'''
        return None

    
    def get_libraries(self):
        '''获取所有媒体库信息'''
        try:
            _var_var_0 = f'{self.host}/emby/Library/SelectableMediaFolders'
            _var_var_1 = {'api_key': self.api_key}
            _var_var_2 = requests.get(_var_var_0, params=_var_var_1)
            _var_var_2.raise_for_status()
            return _var_var_2.json()
        except Exception as _var_var_4:
            logger.error(f'获取Emby媒体库列表失败: {str(_var_var_4)}')
            return []

    def _dummy_libraries(self):
        '''旧代码

        Returns:
            list: 媒体库列表，每个媒体库包含以下信息：
            [
                {
                    "Name": "电影",
                    "Id": "7",
                    "Locations": [
                        "/media/115/影视/101-动漫-大电影"
                    ]
                }
            ]
        '''
        if not self.is_available():
            return None
        try:
            _var_var_0 = f'''{self.host_port}/emby/Library/VirtualFolders'''
            _var_var_1 = {
                'api_key': self.api_key }
            _var_var_2 = requests.get(_var_var_0, params = _var_var_1)
            _var_var_2.raise_for_status()
            return _var_var_2.json()
        except Exception as _var_var_4:
            _var_var_4 = None
            logger.error(f'''获取Emby媒体库列表失败: {str(_var_var_4)}''')
            del _var_var_4
            return None

    @staticmethod
    def _format_emby_datetime(value):
        """将 Emby 时间转换为东八区时间。"""
        if value in (None, '', 0, '0'):
            return None
        try:
            if isinstance(value, (int, float)) or str(value).isdigit():
                _var_var_18 = float(value)
                if _var_var_18 >= 0x89F7FF5F7B58000:
                    _var_var_18 = (_var_var_18 - 0x89F7FF5F7B58000) / 10000000
                elif _var_var_18 >= 0xE8D4A51000:
                    _var_var_18 /= 1000
                _var_var_19 = datetime.fromtimestamp(_var_var_18, tz=timezone.utc)
            else:
                _var_var_19 = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
                if _var_var_19.tzinfo is None:
                    _var_var_19 = _var_var_19.replace(tzinfo=timezone.utc)
            _var_var_20 = timezone(timedelta(hours=8))
            return _var_var_19.astimezone(_var_var_20).strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError, OverflowError, OSError):
            logger.warning(f'无法解析 Emby 时间: {value}')
            return None
    
    def get_users(self, page, page_size, NameStartsWithOrGreater):
        '''分页查询 Emby 用户，并返回管理端需要的用户信息。'''
        if not self.is_available():
            return None
        try:
            _var_var_21 = (page - 1) * page_size
            _var_var_0 = f'''{self.host_port}/emby/Users/Query'''
            _var_var_1 = {
                'StartIndex': _var_var_21,
                'Limit': page_size,
                'api_key': self.api_key
            }
            if NameStartsWithOrGreater:
                _var_var_1['NameStartsWithOrGreater'] = NameStartsWithOrGreater
            _var_var_2 = requests.get(_var_var_0, params=_var_var_1)
            _var_var_2.raise_for_status()
            _var_var_22 = _var_var_2.json()
            _var_var_23 = []
            for _var_var_24 in _var_var_22.get('Items', []):
                _var_var_25 = {
                    'Id': _var_var_24.get('Id'),
                    'Name': _var_var_24.get('Name'),
                    'HasPassword': _var_var_24.get('HasPassword', False),
                    'HasConfiguredPassword': _var_var_24.get('HasConfiguredPassword', False),
                    'LastActivityDate': self._format_emby_datetime(_var_var_24.get('LastActivityDate')),
                    'LastLoginDate': self._format_emby_datetime(_var_var_24.get('LastLoginDate'))
                }
                _var_var_23.append(_var_var_25)
            return {
                'data': _var_var_23,
                'total': _var_var_22.get('TotalRecordCount', 0),
                'page': page,
                'page_size': page_size
            }
        except Exception as _var_var_4:
            logger.error(f'获取 Emby 用户列表失败: {str(_var_var_4)}')
            return None


