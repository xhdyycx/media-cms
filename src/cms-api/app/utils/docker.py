import re
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, Optional
import requests
from app.log import logger

class DockerHubAPI:
    '''通过 Docker Registry V2 API 获取 Docker Hub 镜像信息。'''
    AUTH_URL = 'https://auth.docker.io/token'
    REGISTRY_URL = 'https://registry-1.docker.io'
    MANIFEST_ACCEPT = ', '.join(('application/vnd.oci.image.index.v1+json', 'application/vnd.docker.distribution.manifest.list.v2+json', 'application/vnd.oci.image.manifest.v1+json', 'application/vnd.docker.distribution.manifest.v2+json'))
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'cloud-media-sync/version-check' })
        return None
        return None

    @staticmethod
    def _normalize_proxies(proxies):
        if isinstance(proxies, str):
            return {'http': proxies, 'https': proxies}
        return proxies
    
    def _get_token(self, image, proxies):
        _var_var_0 = self.session.get(self.AUTH_URL, params = {
            'service': 'registry.docker.io',
            'scope': f'''repository:{image}:pull''' }, proxies = self._normalize_proxies(proxies), timeout = 10)
        _var_var_0.raise_for_status()
        _var_var_1 = _var_var_0.json()
        if not _var_var_1.get('token'):
            _var_var_1.get('token')
        _var_var_2 = _var_var_1.get('access_token')
        if not _var_var_2:
            raise ValueError('Docker Registry 认证响应中缺少 token')
        return _var_var_2
        return None

    @staticmethod
    def _tag_sort_key(tag: str):
        """让数字版本按版本号倒序排列，而不是按字符串排列。"""
        _var_var_3 = re.fullmatch('v?(\\d+(?:\\.\\d+)*)', tag)
        _var_var_4 = tuple(int(_var_var_5) for _var_var_5 in _var_var_3.group(1).split('.')) if _var_var_3 else ()
        return (tag == 'latest', bool(_var_var_3), _var_var_4, tag)
        return (tag == 'latest', bool(_var_var_3), _var_var_4, tag)
        # None(tuple)
        return None
    
    def get_repository_tags(self, namespace: str, repository: str, proxies=None) -> Dict[str, Any]:
        """获取仓库标签，并转换为旧接口兼容的 ``results`` 结构。"""
        _var_var_6 = f'{namespace}/{repository}'
        try:
            _var_var_2 = self._get_token(_var_var_6, proxies)
            _var_var_0 = self.session.get(f'{self.REGISTRY_URL}/v2/{_var_var_6}/tags/list', headers={'Authorization': f'Bearer {_var_var_2}'}, proxies=self._normalize_proxies(proxies), timeout=10)
            _var_var_0.raise_for_status()
            _var_var_7 = _var_var_0.json().get('tags') or []
            _var_var_7.sort(key=self._tag_sort_key, reverse=True)
            return {'results': [{'name': _var_var_8} for _var_var_8 in _var_var_7]}
        except Exception as _var_var_9:
            logger.warning(f'获取仓库标签失败: {_var_var_9}')
            return {}
    def _get_manifest_info(self, image, tag, proxies):
        '''读取标签对应的镜像摘要及镜像配置中的创建时间。'''
        _var_var_2 = self._get_token(image, proxies)
        _var_var_10 = {
            'Authorization': f'''Bearer {_var_var_2}''',
            'Accept': self.MANIFEST_ACCEPT }
        _var_var_11 = self._normalize_proxies(proxies)
        _var_var_12 = f'''{self.REGISTRY_URL}/v2/{image}/manifests/{tag}'''
        _var_var_0 = self.session.get(_var_var_12, headers = _var_var_10, proxies = _var_var_11, timeout = 10)
        _var_var_0.raise_for_status()
        _var_var_13 = _var_var_0.headers.get('Docker-Content-Digest', '')
        _var_var_14 = _var_var_0.json()
        if not _var_var_14.get('manifests'):
            _var_var_14.get('manifests')
        _var_var_15 = []
        if _var_var_15:
            _var_var_16 = _var_var_15[0]
            _var_var_0 = self.session.get(f'{self.REGISTRY_URL}/v2/{image}/manifests/{_var_var_16["digest"]}', headers=_var_var_10, proxies=_var_var_11, timeout=10)
            _var_var_0.raise_for_status()
            _var_var_14 = _var_var_0.json()
        _var_var_17 = ''
        if not _var_var_14.get('config'):
            _var_var_14.get('config')
        _var_var_18 = { }.get('digest')
        if _var_var_18:
            _var_var_0 = self.session.get(f'''{self.REGISTRY_URL}/v2/{image}/blobs/{_var_var_18}''', headers = {
                'Authorization': f'''Bearer {_var_var_2}''' }, proxies = _var_var_11, timeout = 10)
            _var_var_0.raise_for_status()
            _var_var_17 = _var_var_0.json().get('created', '')
        return {
            'digest': _var_var_13,
            'created': _var_var_17 }
        # None(next)
        return None

    @staticmethod
    def _format_created_at(created):
        if not created:
            return ''
        _var_var_20 = created.replace('Z', '+00:00')
        return datetime.fromisoformat(_var_var_20).astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
    @staticmethod
    def get_cms_version(proxies=None):
        try:
            api = DockerHubAPI()
            namespace = 'imaliang'
            repository = 'cloud-media-sync'
            tags_data = api.get_repository_tags(namespace, repository, proxies)
            tag_name = next((item.get('name') for item in tags_data.get('results', []) if item.get('name') and item.get('name') != 'latest'), None)
            if not tag_name:
                logger.warning('Docker Registry 未返回可用的 novamedia 版本标签')
                return ''
            image = f"{namespace}/{repository}"
            manifest_info = api._get_manifest_info(image, tag_name, proxies)
            return {
                'tag_name': tag_name,
                'last_updated': api._format_created_at(manifest_info.get('created', '')),
                'digest': manifest_info.get('digest', '')
            }
        except Exception as e:
            logger.warning(f'获取 novamedia 最新版本号失败（不影响正常使用）: {e}')
            return ''
