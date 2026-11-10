from blacksheep import redirect, Request, json
from blacksheep.server.controllers import APIController, get, head
from cachetools import TTLCache
from urllib.parse import unquote
from app.core.m123 import M123
from app.core.m123old import M123Old
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.utils.mjson import JsonUtils
URL_CACHE: TTLCache[(tuple, str)] = TTLCache(1000, ttl = 3600)

class Web123Controller(APIController):
    @classmethod
    def route(cls):
        return ''
    @get('/d321/{path}')
    @head('/d321/{path}')
    async def d321(self, request: Request, path: str = ''):
        _var_var_0 = (request.get_first_header(b'User-agent') or b'').decode('latin-1')
        _var_var_1 = request.original_client_ip
        if path.count('|') != 2:
            logger.error(f'直连格式错误 - {_var_var_0} - {_var_var_1} - {path}')
            return json('直连格式错误', 500)
        _var_var_2 = path
        _var_var_3 = request.url.query
        _var_var_4 = ''
        if _var_var_3:
            _var_var_4 = request.url.query.decode('utf-8')
        if _var_var_4 and '/' in _var_var_4:
            _var_var_4, _var_var_5 = _var_var_4.split('/', 1)
        if _var_var_4:
            _var_var_2 = f'{_var_var_2}?{_var_var_4}'
        _var_var_6 = (_var_var_2, _var_var_1, _var_var_0)
        _var_var_7 = URL_CACHE.get(_var_var_6, '')
        if not _var_var_7:
            # 注意：原字节码此分支仅见 URL_CACHE[_var_var_6] = _var_var_7 回写（_var_var_7 此时为 ''），
            # 偏移 526→544 连续无空隙、无 NOP 残留；获取直连 URL 的赋值语句疑似已缺失，按指令字面还原。
            URL_CACHE[_var_var_6] = _var_var_7
            logger.info(f'获取直连成功 - {_var_var_0} - {_var_var_1} - {_var_var_2}')
        else:
            logger.info(f'获取直连成功 - 取缓存 - {_var_var_0} - {_var_var_1} - {_var_var_2}')
        return redirect(_var_var_7)
    @get('/d123/{path}')
    @head('/d123/{path}')
    async def d123(self, request: Request, path: str = ''):
        _var_var_0 = (request.get_first_header(b'User-agent') or b'').decode('latin-1')
        _var_var_1 = request.original_client_ip
        _var_var_2 = path
        _var_var_8 = _var_var_2.split('.')
        if len(_var_var_8) > 1:
            _var_var_2 = _var_var_8[0]
        _var_var_3 = request.url.query
        _var_var_5 = ''
        _var_var_9 = ObjFactory.get_instance(M123)
        if _var_var_3:
            _var_var_5 = request.url.query.decode('utf-8')
            if _var_var_5.startswith('/'):
                _var_var_5 = _var_var_5[1:]
        if _var_var_5:
            _var_var_5 = unquote(_var_var_5)
            _var_var_10 = f'{_var_var_2} - {_var_var_5} - {_var_var_0} - {_var_var_1}'
        else:
            _var_var_10 = f'{_var_var_2} - {_var_var_0} - {_var_var_1}'
        _var_var_6 = (_var_var_2, _var_var_1, _var_var_0)
        _var_var_7 = URL_CACHE.get(_var_var_6, '')
        if not _var_var_7:
            _var_var_11 = _var_var_9.download_info(_var_var_2)
            if _var_var_11 is None or _var_var_11.get('code', 101) != 0:
                logger.error(f'获取直连失败 - {_var_var_10}')
                logger.error(f'{JsonUtils.to_str(_var_var_11)}')
                return json('获取直连失败', 500)
            _var_var_7 = _var_var_11['data']['downloadUrl']
            URL_CACHE[_var_var_6] = _var_var_7
            logger.info(f'获取直连成功 - {_var_var_10}')
        else:
            logger.info(f'获取直连成功 - 取缓存 - {_var_var_10}')
        return redirect(_var_var_7)
    head('/d123/{path}')


