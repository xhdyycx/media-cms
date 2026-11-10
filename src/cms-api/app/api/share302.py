from urllib.parse import unquote
from blacksheep import redirect, text, Request, json
from blacksheep.server.controllers import APIController, get, head
from cachetools import TTLCache
from p115client import P115OSError
from app.core.emby_user import emby_user_util
from app.core.m115 import M115
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.utils.mjson import JsonUtils
SHARE_URL_CACHE: TTLCache[(tuple, str)] = TTLCache(64, ttl = 60)

class Share302Controller(APIController):
    @classmethod
    def route(cls):
        return ''
    @get('/s/{share_code}')
    @head('/s/{share_code}')
    async def share_302(self, request: Request, share_code: str = ''):
        _var_var_0 = ObjFactory.get_instance(M115)
        if not (share_code := share_code.strip()):
            return text('share_code error', 404)
        _var_var_1 = share_code.split('.')
        if len(_var_var_1) > 1:
            share_code = _var_var_1[0]
        _var_var_2 = (request.get_first_header(b'User-agent') or b'').decode('latin-1')
        _var_var_3 = _var_var_2
        if _var_var_2 and 'lavf' in _var_var_2.lower():
            _var_var_3 = f'Emby-{_var_var_2}'
        _var_var_4 = (request.get_first_header(b'Range') or b'').decode('latin-1')
        _var_var_5 = request.original_client_ip
        _var_var_6 = request.url.query
        _var_var_7 = ''
        _var_var_8 = request.query.get('emby_user', [None])[0]
        _var_var_9 = request.query.get('source', [None])[0]
        if request.url.query:
            _var_var_7 = request.url.query.decode('utf-8')
            if _var_var_7.startswith('/'):
                _var_var_7 = _var_var_7[1:]
            if _var_var_7:
                _var_var_7 = unquote(_var_var_7)
                _var_var_7 = _var_var_7.replace(f'&emby_user={_var_var_8}&source={_var_var_9}', '')
        if _var_var_7:
            _var_var_7 = unquote(_var_var_7)
            _var_var_10 = f'{share_code} - {_var_var_7} - {_var_var_3} - {_var_var_5}'
        else:
            _var_var_10 = f'{share_code} - {_var_var_3} - {_var_var_5}'
        _var_var_11 = (share_code, _var_var_5, _var_var_2)
        _var_var_12 = SHARE_URL_CACHE.get(_var_var_11, '')
        if not _var_var_12:
            try:
                _var_var_13 = emby_user_util.get_cache_m115(_var_var_8)
                _var_var_14 = emby_user_util.get_cache(_var_var_8)
                if _var_var_13:
                    logger.info(f'使用小号播放分享 -> {_var_var_14.cid} {_var_var_14.bind_id} {_var_var_14.bind_username}')
                    _var_var_15 = await _var_var_13.share_download_video_url(share_code, {'user-agent': _var_var_2})
                else:
                    _var_var_15 = await _var_var_0.share_download_video_url(share_code, {'user-agent': _var_var_2})
                if _var_var_15 is None or not _var_var_15['state']:
                    logger.error(f'获取直连失败 - {_var_var_10}')
                    logger.error(f'{JsonUtils.to_str(_var_var_15)}')
                    return json('获取分享直连失败', 500)
                _var_var_12 = _var_var_15['data']['url']['url']
                SHARE_URL_CACHE[_var_var_11] = _var_var_12
                logger.info(f'获取分享直连成功 - {_var_var_10}')
            except P115OSError as _var_var_16:
                logger.error(f'获取分享直连失败 - P115OSError - {_var_var_10}')
                logger.exception(_var_var_16)
                return json(_var_var_16.args[1], 500)
            except (FileNotFoundError, IsADirectoryError) as _var_var_16:
                logger.error(f'获取分享直连失败 - 文件没找到-{_var_var_10}')
                logger.exception(_var_var_16)
                return json(_var_var_16.args[1], 404)
        else:
            logger.info(f'获取分享直连成功 - 缓存 - {_var_var_10}')
        return redirect(_var_var_12)
    head('/s/{share_code}')


