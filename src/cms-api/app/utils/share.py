# File: share.py (Cleaned & Decompiled)
import re
from app.log import logger

class ShareUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_hdhive_link(_url):
        _var_var_0 = re.findall(r'https://hdhive\.com/resource/115/[0-9a-fA-F]{32}(?![0-9a-fA-F])', _url)
        if _var_var_0:
            return set(_var_var_0)
        return []

    @staticmethod
    def get_share_down_link(_url):
        _var_var_1 = {'success': False, 'share_links': [], 'magnet_links': [], 'ali_links': [], 'ed2k_links': []}
        if not _url:
            return _var_var_1
        _var_var_2 = re.findall(r'https://(?:115|anxia|115cdn)\.com/s/[a-zA-Z0-9]+\?password=[a-zA-Z0-9]{4}', _url)
        _var_var_3 = re.findall(r'magnet:\?xt=urn:btih:(?:[0-9a-fA-F]{40}|[0-9a-zA-Z]{32})', _url)
        _var_var_4 = re.findall(r'https://(?:www\.)?(?:aliyundrive|alipan)\.com/s/[a-zA-Z0-9]+', _url)
        _var_var_5 = re.findall(r'ed2k://\|file\|.*\|.*\|.*\|', _url)
        if _var_var_2:
            logger.info(f'解析出115分享: {_var_var_2}')
            _var_var_1['success'] = True
            _var_var_1['share_links'] = set(_var_var_2)
        if _var_var_5:
            logger.info(f'解析出ed2k链接: {_var_var_5}')
            _var_var_1['success'] = True
            _var_var_1['ed2k_links'] = set(_var_var_5)
        if _var_var_3:
            logger.info(f'解析出磁力链接: {_var_var_3}')
            _var_var_1['success'] = True
            _var_var_1['magnet_links'] = set(_var_var_3)
        if _var_var_4:
            logger.info(f'解析出阿里云盘分享: {_var_var_4}')
            _var_var_1['success'] = True
            _var_var_1['ali_links'] = set(_var_var_4)
        return _var_var_1