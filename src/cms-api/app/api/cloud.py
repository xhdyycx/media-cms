from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, json, post
from blacksheep.server.controllers import get
from app.core.aliyun import AliyunApi
from app.core.emby_user import emby_user_util
from app.core.env import ConfigEnv
from app.core.m115 import M115
from app.core.m115v2 import M115v2
from app.core.m123 import M123
from app.core.obj_factory import ObjFactory
from app.core.task import save_ali_share_task, auto_tidy_task
from app.db import get_db
from app.db.account_op import Account115Op
from app.db.config_op import ConfigOp
from app.core.env import novaEnv
from app.db.models.account import Account115
from app.log import logger
from app.modules.wechat import WechatModule
from app.scheduler import Scheduler
from app.services.share_down import ShareDownService
from app.utils.ko_util import save_file
from app.utils.mjson import JsonUtils

class CloudController(APIController):
    
    def __init__(self):
        self._wx = WechatModule()
        self._aliyun_api = AliyunApi()
        self._CONFIG_ENV = ConfigEnv()
        return None
        return None

    @classmethod
    def route(cls):
        return '/api/cloud'
    @get('qrcode')
    @auth('login')
    async def login_qrcode(self, app: str = None):
        _var_var_0 = M115v2.login_qrcode_token(app)
        if not _var_var_0 or 'data' not in _var_var_0:
            logger.error(f'login_qrcode_token.resp={_var_var_0}')
            return json({'code': 400, 'msg': '获取二维码数据失败'})
        _var_var_0 = _var_var_0['data']
        return json({'code': 200, 'data': _var_var_0})
    @post('check_qrcode')
    @auth('login')
    async def check_qrcode(self, payload: dict):
        _var_var_0 = M115v2.login_qrcode_scan_status(payload.get('uid'), payload.get('time'), payload.get('sign'))
        if 1 == _var_var_0.get('state'):
            _var_var_0 = _var_var_0.get('data')
            if not _var_var_0:
                _var_var_0 = {'msg': '等待中...', 'status': 0}
        return json({'code': 200, 'data': _var_var_0})
    @post('bind_app')
    @auth('login')
    async def bind_app(self, payload: dict):
        _var_var_1 = payload.get('bind_type')
        _var_var_2 = payload.get('bind_id')
        _var_var_0 = M115v2.login_qrcode_scan_result(payload.get('uid'), payload.get('app'))
        if 1 != _var_var_0.get('state'):
            return json({'code': 400, 'msg': '登录失败，请重试'})
        _var_var_0 = _var_var_0.get('data')
        _var_var_3 = _var_var_0.get('cookie')
        _var_var_6 = '; '.join([f'{_var_var_4}={_var_var_5}' for _var_var_4, _var_var_5 in _var_var_3.items()]) if _var_var_3 else ''
        if not _var_var_3:
            return json({'code': 400, 'msg': '登录失败，请重试'})
        with get_db() as _var_var_7:
            if _var_var_1 and str(_var_var_1) == '3':
                _var_var_8 = Account115Op(_var_var_7)
                if _var_var_2:
                    logger.info(f'小号重新登录成功: {_var_var_0["user_name"]} {_var_var_0["user_id"]}')
                    _var_var_9 = _var_var_8.update_account({'id': int(_var_var_2), 'user_id': _var_var_0['user_id'], 'username': _var_var_0['user_name'], 'cookie_type': payload['app'], 'cookie': _var_var_6})
                    if not _var_var_9:
                        return json({'code': 404, 'msg': '小号不存在'})
                else:
                    logger.info(f'小号登录成功: {_var_var_0["user_name"]} {_var_var_0["user_id"]}')
                    _var_var_10 = Account115(type=3, user_id=_var_var_0['user_id'], username=_var_var_0['user_name'], status=1, cookie_type=payload['app'], cookie=_var_var_6)
                    _var_var_8.save(_var_var_10)
                emby_user_util.refresh_cache()
            else:
                _var_var_11 = ConfigOp(_var_var_7)
                _var_var_12 = _var_var_11.get_by_key('core')
                _var_var_13 = _var_var_12['basic']['COOKIE_FILE_PATH']
                save_file(_var_var_13, _var_var_6)
                logger.info(f'cookie已保存到: {_var_var_13}')
                _var_var_12['basic']['DEVICE_TYPE'] = payload['app']
                _var_var_11.update('core', _var_var_12)
                ObjFactory.refresh_instance(M115)
        return json({'code': 200, 'msg': '登录成功'})
    @get('get_full_path')
    @auth('login')
    async def get_full_path(self, cid: int):
        '''获取文件的完整路径'''
        _var_var_14 = ObjFactory.get_instance(M115)
        _var_var_0 = _var_var_14.fs_category_get_app(cid)
        if not _var_var_0 or 'paths' not in _var_var_0:
            return json({'code': 400, 'msg': '无效的cid或cookie已过期'})
        return json({'code': 200, 'data': _var_var_0})
    @get('get_full_path_by_id')
    @auth('login')
    async def get_full_path_by_id(self, type: str, id: int):
        '''获取文件的完整路径'''
        _var_var_15 = False
        _var_var_16 = ''
        if type == '123':
            _var_var_17 = ObjFactory.get_instance(M123)
            _var_var_15, _var_var_16 = _var_var_17.get_fid_path(id)
        if not _var_var_15 or not _var_var_16:
            return json({'code': 400, 'msg': '无效的id'})
        return json({'code': 200, 'data': {'full_path': _var_var_16}})
    @get('login_info')
    @auth('login')
    async def get_login_info(self, path: str = None, bind_id: int = None):
        '''获取登录信息
        '''
        if bind_id:
            with get_db() as _var_var_7:
                _var_var_8 = Account115Op(_var_var_7)
                _var_var_10 = _var_var_8.get(bind_id)
                if not _var_var_10:
                    return json({'code': 404, 'msg': '账号不存在'})
                _var_var_6 = _var_var_10.get('cookie')
                logger.info(f'bind_id={bind_id}, username={_var_var_10.get("username")}')
                if not _var_var_6:
                    return json({'code': 400, 'msg': '账号cookie为空'})
                logger.info(f'使用小号 {_var_var_10.get("id")} {_var_var_10.get("username")}')
                _var_var_14 = M115v2(cookies=_var_var_6)
        else:
            logger.info('使用主账号')
            _var_var_14 = ObjFactory.get_instance(M115)
        _var_var_0 = _var_var_14.login_info()
        if not _var_var_0 or not _var_var_0.get('state'):
            logger.error(f'login_info.resp={JsonUtils.to_str(_var_var_0)}')
            return json({'code': 400, 'msg': 'cookie已失效'})
        _var_var_18 = _var_var_0.get('data')
        if not _var_var_18:
            logger.error(f'login_info.resp={JsonUtils.to_str(_var_var_0)}')
            return json({'code': 400, 'msg': 'cookie已失效'})
        _var_var_19 = _var_var_18.get('sapce', {}).get('1')
        if not _var_var_19:
            logger.error(f'login_info.resp={JsonUtils.to_str(_var_var_0)}')
            return json({'code': 400, 'msg': '获取空间信息失败'})
        return json({'code': 200, 'data': {'user_name': _var_var_18.get('user_name'), 'size_used': _var_var_19.get('size_used'), 'size_total': _var_var_19.get('size_total')}})
    
    async def _handle_share_down(self, data):
        '''提取公共的分享下载处理逻辑'''
        pass

    @post('add_share_down')
    @auth('pro')
    async def add_share_down(self, data: dict):
        return await self._handle_share_down(data)
    @post('add_share_down_by_token')
    async def add_share_down_by_token(self, data: dict):
        _var_var_23 = data.get('token')
        if not _var_var_23:
            return json({'code': '400', 'message': 'token为空'})
        if _var_var_23 != novaEnv.NOVA_API_TOKEN:
            return json({'code': '400', 'message': 'token错误'})
        return await self._handle_share_down(data)
    @post('get_ali_path')
    @auth('pro')
    async def get_ali_path(self, params: dict):
        '''获取阿里文件的完整路径'''
        _var_var_24 = AliyunApi().get_path(params['ALIYUN_SHARE_DIR_ID'])
        if not _var_var_24:
            return json({'code': 400, 'msg': '请确认id是否正确；如果你填的是备份文件里的文件夹id，请换个备份文件外的文件夹id试试；反之，就填个备份文件里的文件夹id试试！'})
        return json({'code': 200, 'data': _var_var_24})
    @get('ali_qrcode')
    @auth('pro')
    async def ali_login_qrcode(self):
        return json(self._aliyun_api.get_qrcode())
    @post('ali_check_qrcode')
    @auth('pro')
    async def ali_check_qrcode(self, payload: dict):
        return json(self._aliyun_api.get_qrcode_status(payload))
