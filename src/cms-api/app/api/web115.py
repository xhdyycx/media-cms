# File: web115.py (Cleaned & Decompiled)
from urllib.parse import unquote, parse_qs
from blacksheep import Request, Response, json, redirect, text
from blacksheep.server.controllers import APIController, get, head
from cachetools import TTLCache
from app.core.emby_user import emby_user_util
from app.core.env2 import config2Env
from app.core.m115 import M115
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.utils.mjson import JsonUtils

URL_CACHE: TTLCache[(tuple, str)] = TTLCache(500, ttl=10)
PICK_CODE_CACHE: TTLCache[(tuple, str)] = TTLCache(1000, ttl=3600)
DEVICE_CACHE: TTLCache[(str, dict)] = TTLCache(1000, ttl=3600)

class Web302Controller(APIController):

    @classmethod
    def route(cls):
        return ''

    @get('/d/{pick_code}')
    @head('/d/{pick_code}')
    async def index(self, request: Request, pick_code: str):
        """处理 115 云盘文件下载请求，并返回 302 重定向。"""
        _var_var_0 = pick_code.split('.')
        if len(_var_var_0) > 1:
            pick_code = _var_var_0[0]
        _var_var_1 = ''
        _var_var_2 = request.query.get('emby_user', [None])[0]
        _var_var_3 = request.query.get('source', [None])[0]
        if request.url.query:
            _var_var_1 = request.url.query.decode('utf-8')
            if _var_var_1.startswith('/'):
                _var_var_1 = _var_var_1[1:]
            if _var_var_1:
                _var_var_1 = unquote(_var_var_1)
                _var_var_1 = _var_var_1.replace(f'&emby_user={_var_var_2}&source={_var_var_3}', '')
        _var_var_4 = (request.get_first_header(b'User-agent') or b'').decode('latin-1')
        _var_var_5 = request.original_client_ip
        _var_var_6 = (pick_code, _var_var_4, _var_var_5, _var_var_2)
        _var_var_7 = URL_CACHE.get(_var_var_6)
        if _var_var_7:
            _var_var_8 = self.build_log(_var_var_3, _var_var_4, pick_code, _var_var_1, _var_var_5)
            logger.info(f'使用缓存直连 - {_var_var_8}')
            return redirect(_var_var_7)
        _var_var_9 = ObjFactory.get_instance(M115)
        _var_var_10 = {'user-agent': _var_var_4}
        _var_var_11 = emby_user_util.get_cache_m115(_var_var_2)
        _var_var_12 = emby_user_util.get_cache(_var_var_2)
        _var_var_13 = False
        if _var_var_11:
            _var_var_13 = True
            logger.info(f'使用小号播放 -> {_var_var_12.cid} {_var_var_12.bind_id} {_var_var_12.bind_username}')
        try:
            _var_var_8 = self.build_log(_var_var_3, _var_var_4, pick_code, _var_var_1, _var_var_5, _var_var_13)
            if not _var_var_13:
                _var_var_14 = bool(_var_var_4 and 'lavf' in _var_var_4.lower())
                _var_var_15 = config2Env.m115_copy_player and config2Env.m115_copy_player_cid
                if not _var_var_1:
                    logger.error('复制播放【strm直连格式】必须使用【pick_code_name】')
                    _var_var_15 = False
                if _var_var_15 and not _var_var_14:
                    _var_var_16 = DEVICE_CACHE.get(pick_code, {})
                    _var_var_17 = f'{_var_var_2}{_var_var_4}{_var_var_5}'
                    if not _var_var_16:
                        _var_var_18 = pick_code
                    else:
                        _var_var_18 = _var_var_16.get(_var_var_17)
                    if not _var_var_18:
                        _var_var_18 = _var_var_9.get_copy_pick_code(_var_var_9.to_id(pick_code), config2Env.m115_copy_player_cid, _var_var_1)
                        if _var_var_18:
                            logger.info(f'复制成功- {pick_code} -> {_var_var_18}')
                        else:
                            logger.error('复制失败，直接获取原文件直连')
                            _var_var_18 = pick_code
                    logger.info(f'复制播放- {pick_code} -> {_var_var_18}')
                    pick_code = _var_var_18
                    _var_var_16[_var_var_17] = _var_var_18
                    DEVICE_CACHE[pick_code] = _var_var_16
                _var_var_19 = _var_var_9.download_url_app(pick_code, _var_var_10)
                _var_var_20 = self.get_url(_var_var_19, _var_var_8)
                URL_CACHE[_var_var_6] = _var_var_20
                return redirect(_var_var_20)
            _var_var_21 = 'Mozilla/5.0 115disk/36.2.28 115Browser/36.2.28 115wangpan_android/36.2.28'
            _var_var_22 = {'user-agent': _var_var_21}
            _var_var_19 = _var_var_9.download_url_chrome(pick_code, _var_var_22)
            _var_var_23 = _var_var_9.to_id(pick_code)
            _var_var_24 = self.get_url_chrome(_var_var_19, _var_var_8, _var_var_23)
            _var_var_20 = _var_var_24['url']['url']
            URL_CACHE[_var_var_6] = _var_var_20
            _var_var_25 = _var_var_24['file_size']
            _var_var_26 = _var_var_24['sha1']
            _var_var_1 = _var_var_24['file_name']
            _var_var_27 = (pick_code, _var_var_25, _var_var_26, _var_var_12.cid)
            _var_var_28 = PICK_CODE_CACHE.get(_var_var_27)
            if _var_var_28:
                logger.info(f'使用缓存秒传 - {pick_code} -> {_var_var_28}')
                _var_var_29 = _var_var_28
            else:
                _var_var_30 = _var_var_11.seconds_upload_file(_var_var_1, _var_var_25, _var_var_26, _var_var_20, _var_var_12.cid, ua=_var_var_21)
                _var_var_29 = _var_var_30.get('pick_code')
                if _var_var_30['success']:
                    PICK_CODE_CACHE[_var_var_27] = _var_var_29
                elif _var_var_30.get('statuscode', 0) == 10014:
                    logger.error(f'秒传失败 - 你填的cid= {_var_var_12.cid} 不是小号 {_var_var_12.bind_username} 的')
                    return json({'error': '秒传失败'}, 500)
                else:
                    logger.error(f'秒传失败 - {pick_code}')
                    return json({'error': '秒传失败'}, 500)
            _var_var_19 = _var_var_11.download_url_app(_var_var_29, _var_var_10)
            _var_var_20 = self.get_url(_var_var_19, _var_var_8)
            URL_CACHE[_var_var_6] = _var_var_20
            return redirect(_var_var_20)
        except Exception as _var_var_31:
            logger.exception(_var_var_31)
            return json({'error': '获取下载链接失败'}, 500)

    @staticmethod
    def build_log(source, user_agent, pick_code, name, remote_addr, is_seconds_upload=False):
        _var_var_14 = bool(user_agent and 'lavf' in user_agent.lower())
        _var_var_32 = user_agent
        if _var_var_14:
            _var_var_32 = f'Emby的请求-{user_agent}'
        if name:
            _var_var_33 = f'{pick_code} - {name} - {_var_var_32} - {remote_addr}'
        else:
            _var_var_33 = f'{pick_code} - {_var_var_32} - {remote_addr}'
        if is_seconds_upload:
            _var_var_33 = f'小号 - {_var_var_33}'
        if source:
            _var_var_33 = f'【9096】{_var_var_33}'
        return _var_var_33

    @staticmethod
    def get_url(url_res, log_tag):
        if not url_res or url_res.get('state'):
            logger.error(f'获取直连失败 - {log_tag}')
            raise ValueError(JsonUtils.to_str(url_res))
        _var_var_20 = url_res.get('data', {}).get('url', '')
        if not _var_var_20:
            raise ValueError(JsonUtils.to_str(url_res))
        logger.info(f'获取直连成功 - {log_tag}')
        return _var_var_20

    @staticmethod
    def get_url_chrome(url_res, log_tag, fid):
        if not url_res or url_res.get('state'):
            logger.error(f'获取直连失败 - {log_tag}')
            raise ValueError(JsonUtils.to_str(url_res))
        _var_var_24 = url_res['data'][str(fid)]
        _var_var_20 = _var_var_24['url']['url']
        if not _var_var_20:
            raise ValueError(JsonUtils.to_str(url_res))
        logger.info(f'获取直连成功 - {log_tag}')
        return _var_var_24