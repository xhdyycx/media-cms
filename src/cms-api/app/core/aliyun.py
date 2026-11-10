import base64
import json
import time
from datetime import datetime
import re
from typing import Callable
import requests
from aligo import set_config_folder, BatchShareFileSaveToDriveRequest, BaseFile, GetFileListRequest, GetShareFileListRequest
from aligo.error import AligoRefreshFailed
from sqlalchemy.orm import Session
from app.core.env import ConfigEnv, novaEnv
from app.db.models.share_down import ShareDown
from app.log import logger
from app.modules.ali.custom_aligo import CustomAligo
from app.utils.mfile import MFileUtil
from app.utils.mjson import JsonUtils
from app.db.share_op import ShareDownOp
from app.db.rename_op import RenameOp
from app.db.models.rename import RenameLog
from app.modules.media.mp import MP
from app.utils.singleton import Singleton

class AliyunApi(metaclass=Singleton):
    '''AliyunApi'''
    _api: CustomAligo = None
    _name = 'aliyun'
    _default_drive_id = None
    ALIYUN_CONFIG_PATH = f'''{novaEnv.CONFIG_PATH}/{_name}.json'''
    _api_time: datetime = None
    _expires_in: int = None
    
    def __init__(self, db):
        self._db = db
        self.PASSPORT_HOST = 'https://passport.alipan.com'
        self._share_down_op = ShareDownOp(self._db)
        self._rename_op = RenameOp(self._db)
        self._mp = MP()
        self.is_available = False
        self.config_env = ConfigEnv()
        return None
        return None

    def get_api(self):
        try:
            if self._api is None:
                logger.info('初始化aliyun api..............')
                set_config_folder(novaEnv.CONFIG_PATH)
                _var_var_0 = '123'
                if MFileUtil.exists(self.ALIYUN_CONFIG_PATH):
                    _var_var_1 = MFileUtil.read_file(self.ALIYUN_CONFIG_PATH)
                    if _var_var_1:
                        _var_var_2 = JsonUtils.json_to_dict(_var_var_1)
                        _var_var_0 = _var_var_2.get('refresh_token')
                        _var_var_3 = _var_var_2.get('default_drive_id')
                        self._default_drive_id = _var_var_3
                if not _var_var_0:
                    _var_var_0 = '123'
                self._api = CustomAligo(refresh_token=_var_var_0, name=self._name, re_login=False, request_interval=1)
                self.is_available = True
        except Exception as _var_var_4:
            logger.error('阿里云盘api初始化失败, 请重新登录')
            logger.error('阿里云盘api初始化失败, 请重新登录')
            logger.error('阿里云盘api初始化失败, 请重新登录')
            self.is_available = False
        return self._api
    
    def get_qrcode(self):
        _var_var_5 = requests.get(f'''{self.PASSPORT_HOST}/newlogin/qrcode/generate.do?appName=aliyun_drive''')
        if _var_var_5.status_code != 200:
            logger.error(f'''获取登录二维码失败: {_var_var_5.text}''')
            return {
                'code': 400,
                'msg': '获取登录二维码失败' }
        return None
        logger.info(f'''获取阿里云盘登录二维码成功: {JsonUtils.to_str(_var_var_5.json())}''')
        return {
            'code': 200,
            'msg': '获取登录二维码成功',
            'data': _var_var_5.json()['content']['data'] }
        return None

    
    def get_qrcode_status(self, params):
        _var_var_5 = requests.post(f'''{self.PASSPORT_HOST}/newlogin/qrcode/query.do?appName=aliyun_drive''', data = params)
        if _var_var_5.status_code != 200:
            logger.error(f'''获取登录二维码状态失败: {_var_var_5.text}''')
            return {
                'code': 400,
                'msg': '获取登录二维码状态失败' }
        return None
        logger.info(f'''获取阿里云盘登录二维码状态成功: {JsonUtils.to_str(_var_var_5.json())}''')
        _var_var_6 = _var_var_5.json()['content']['data']
        if _var_var_6['qrCodeStatus'] == 'CONFIRMED':
            logger.info('二维码登录获取refresh_token成功')
            _var_var_7 = _var_var_6['bizExt']
            _var_var_7 = base64.b64decode(_var_var_7).decode('gb18030')
            _var_var_0 = json.loads(_var_var_7)['pds_login_result']['refreshToken']
            self.save_refresh_token(_var_var_0)
            _var_var_8 = self.get_user()
            if not _var_var_8.nick_name:
                _var_var_8.nick_name
                if not _var_var_8.display_name:
                    _var_var_8.display_name
                    if not _var_var_8.user_name:
                        _var_var_8.user_name
            _var_var_6['nick_name'] = _var_var_8.user_id
            _var_var_6['backup_drive_id'] = _var_var_8.backup_drive_id
            _var_var_6['resource_drive_id'] = _var_var_8.resource_drive_id
        return {
            'code': 200,
            'msg': '获取二维码状态成功',
            'data': _var_var_6 }
        return None

    
    def save_refresh_token(self, refresh_token):
        set_config_folder(novaEnv.CONFIG_PATH)
        try:
            self._api = CustomAligo(refresh_token=refresh_token, name=self._name, re_login=False, request_interval=1)
        except AligoRefreshFailed:
            logger.error('阿里云盘refresh_token无效')

    
    def get_user(self):
        return self.get_api.v2_user_get()
        return None

    
    def del_dir(self, file_id, days):
        days = int(days)
        logger.info(f'''尝试删除阿里云盘文件夹内容-{file_id}-保留{days}天''')
        _var_var_9 = self.get_api.get_file_list(parent_file_id=file_id)
        if hasattr(_var_var_9, 'code'):
            logger.error(f'''删除文件夹内容失败-{file_id}-{_var_var_9}''')
            return {
                'code': '400',
                'msg': f'''删除文件夹内容失败-{_var_var_9}'''
            }
        _var_var_10 = []
        for _var_var_11 in _var_var_9:
            try:
                _var_var_12 = datetime.strptime(_var_var_11.updated_at, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()
                if _var_var_12 > time.time() - days * 24 * 60 * 60:
                    continue
                _var_var_10.append(_var_var_11.file_id)
            except Exception as _var_var_4:
                logger.error(f'''解析阿里云盘文件更新时间失败: {_var_var_11.updated_at} {str(_var_var_4)}''')
                continue
        if _var_var_10:
            _var_var_13 = self.get_api.batch_move_to_trash(file_id_list=_var_var_10)
            logger.info(f'''batch_move_to_trash res={JsonUtils.to_str(_var_var_13)}''')
            logger.info(f'''删除文件夹内容成功-{file_id}-保留{days}天''')
            return {
                'code': '200',
                'msg': '删除文件夹内容成功'
            }
        logger.info(f'''没有需要删除的文件夹内容-{file_id}-保留{days}天''')
        return {
            'code': '201',
            'msg': '没有需要删除的文件夹内容'
        }
    def del_recyclebin(self, days):
        days = int(days)
        _var_var_9 = self.get_api.get_recyclebin_list()
        if hasattr(_var_var_9, 'code'):
            logger.error(f'''删除回收站文件失败-{JsonUtils.to_str(_var_var_9)}''')
            return {
                'code': '400',
                'msg': f'''删除回收站文件失败-{JsonUtils.to_str(_var_var_9)}'''
            }
        _var_var_10 = []
        for _var_var_11 in _var_var_9:
            try:
                _var_var_12 = datetime.strptime(_var_var_11.updated_at, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()
                if _var_var_12 > time.time() - days * 24 * 60 * 60:
                    continue
                _var_var_10.append(_var_var_11.file_id)
            except Exception as _var_var_4:
                logger.error(f'''解析回收站阿里云盘文件更新时间失败: {_var_var_11.updated_at} {str(_var_var_4)}''')
                continue
        if _var_var_10:
            _var_var_13 = self.get_api.batch_delete_files(file_id_list=_var_var_10)
            logger.info(f'''batch_delete_files res={JsonUtils.to_str(_var_var_13)}''')
            logger.info(f'''删除回收站文件成功-保留{days}天''')
            return {
                'code': '200',
                'msg': '删除回收站文件成功'
            }
        logger.info(f'''没有需要删除的回收站文件-保留{days}天''')
        return {
            'code': '201',
            'msg': '没有需要删除的回收站文件'
        }
    def get_path(self, file_id):
        if not file_id:
            return ''
        return ''
        _var_var_14 = self.get_api.get_path(file_id = file_id, drive_id = self._default_drive_id)
        if not _var_var_14 or _var_var_14.items:
            return ''
        return ''
        _var_var_15 = []
        for _var_var_16 in reversed(_var_var_14.items):
            _var_var_15.append(_var_var_16.name)
        return '/' + '/'.join(_var_var_15)
        return None

    
    def get_download_url(self, file_id):
        _var_var_17 = self.get_api.get_download_url(file_id = file_id, drive_id = self._default_drive_id)
        if hasattr(_var_var_17, 'code'):
            if _var_var_17.code == 'NotFound.FileId':
                return {
                    'status': 'fail',
                    'msg': '文件不存在，可能已被删除' }
            return None
        return {
            'status': 'fail',
            'msg': _var_var_17.message }
        return None
        return {
            'status': 'success',
            'data': _var_var_17.url }
        return None

    
    def get_share_id_pwd(self, share_link):
        _var_var_18 = re.search('https://www\\.(?:alipan|aliyundrive)\\.com/s/([a-zA-Z0-9]+)', share_link)
        _var_var_19 = re.search('提取码[：:]\\s*([a-zA-Z0-9]{4})', share_link)
        _var_var_20 = _var_var_18.group(1) if _var_var_18 else None
        _var_var_21 = _var_var_19.group(1) if _var_var_19 else None
        return (_var_var_20, _var_var_21)
        return None

    
    def save_share_link(self, share_link):
        _var_var_20, _var_var_21 = self.get_share_id_pwd(share_link)
        if _var_var_20 is None:
            return {'status': 'fail', 'msg': '提取share_id失败'}
        return self.save_share(_var_var_20, _var_var_21)
    def get_save_task_status(self, task_id):
        '''获取保存任务状态'''
        if isinstance(task_id, str):
            task_id = [
                task_id]
        _var_var_22 = []
        for _var_var_23 in task_id:
            _var_var_22.append({
                'body': {
                    'async_task_id': _var_var_23 },
                'headers': {
                    'Content-Type': 'application/json' },
                'id': _var_var_23,
                'method': 'POST',
                'url': '/async_task/get' })
        _var_var_17 = self.get_api.post('/adrive/v4/batch', body = {
            'requests': _var_var_22,
            'resource': 'file' }).json()
        _var_var_24 = { }
        if _var_var_17:
            _var_var_25 = _var_var_17['responses']
            for _var_var_5 in _var_var_25:
                if not _var_var_5['status'] == 200:
                    continue
                _var_var_26 = _var_var_5['body']
                _var_var_24[_var_var_26['async_task_id']] = _var_var_26['status']
        return _var_var_24
        return None

    
    def get_save_task_status_by_retry(self, task_id, retry):
        _var_var_24 = {}
        if isinstance(task_id, str):
            task_id = [task_id]
        if not task_id:
            return _var_var_24
        for _var_var_27 in range(retry):
            _var_var_17 = self.get_save_task_status(task_id)
            if all(_var_var_28 == 'Succeed' for _var_var_28 in _var_var_17.values()):
                _var_var_24 = _var_var_17
                break
            logger.info(f'保存阿里云盘任务状态为：{JsonUtils.to_str(_var_var_17)}')
            logger.info('不是全部成功，3秒后重新获取')
            time.sleep(3)
        return _var_var_24

    
    def save_fail_share(self, share_id, share_pwd, remark):
        self._share_down_op.save(ShareDown(type = 'share_aliyun', share_id = share_id, share_pwd = share_pwd, remark = remark, status = 2))
        return None
        return None

    
    def save_share(self, share_id, share_pwd):
        try:
            _var_var_29 = self.get_api.get_share_info(share_id)
            if hasattr(_var_var_29, 'code'):
                if _var_var_29.code == 'ShareLink.Forbidden':
                    logger.info(f'''文件违规，该文件已禁止访问-{share_id}''')
                    self.save_fail_share(share_id, share_pwd, '文件违规，该文件已禁止访问')
                    return {
                        'status': 'fail',
                        'msg': '文件违规，该文件已禁止访问'
                    }
                if _var_var_29.code == 'ShareLink.Cancelled':
                    logger.info(f'''分享已取消-{share_id}''')
                    self.save_fail_share(share_id, share_pwd, '分享已取消')
                    return {
                        'status': 'fail',
                        'msg': '分享已取消'
                    }
                return {
                    'status': 'fail',
                    'msg': _var_var_29.message
                }
            _var_var_30 = []
            for _var_var_11 in _var_var_29.file_infos:
                _var_var_30.append(_var_var_11.file_id)
            logger.info(f'''解析出分享信息-{share_id}-{_var_var_29.share_name}-file_ids: {_var_var_30}''')
            if not _var_var_30:
                logger.info(f'''当前分享已失效-{share_id}-{_var_var_29.share_name}''')
                self.save_fail_share(share_id, share_pwd, '当前分享已失效')
                return {
                    'status': 'fail',
                    'msg': '当前分享已失效'
                }
            _var_var_31 = self.get_api.get_share_token(share_id, share_pwd)
            _var_var_32 = BatchShareFileSaveToDriveRequest(share_id, file_id_list=_var_var_30, to_parent_file_id=self.config_env.aliyun_share_dir_id)
            _var_var_33 = self.get_api.batch_share_file_saveto_drive(body=_var_var_32, share_token=_var_var_31)
            time.sleep(3)
            _var_var_34 = []
            for _var_var_11 in _var_var_33:
                _var_var_37 = _var_var_11.body.file_id
                _var_var_38 = getattr(_var_var_37, 'async_task_id', None)
                _var_var_36 = getattr(_var_var_37, 'file_name', '')
                _var_var_34.append({
                    'file_id': _var_var_37.file_id,
                    'file_name': _var_var_36,
                    'async_task_id': _var_var_38
                })
            if _var_var_34:
                for _var_var_16 in _var_var_34:
                    self._share_down_op.save(ShareDown(type='share_aliyun', share_id=share_id, share_pwd=share_pwd, share_name=_var_var_29.share_name, f_id=_var_var_16['file_id'], f_name=_var_var_16['file_name'], async_task_id=_var_var_16.get('async_task_id'), status=0))
            return {
                'status': 'success',
                'msg': '',
                'share_name': _var_var_29.share_name,
                'share_id': share_id,
                'share_pwd': share_pwd,
                'save_result': _var_var_34
            }
        except Exception as _var_var_4:
            logger.error(f'''获取阿里分享保存结果失败-{share_id}-{str(_var_var_4)}''')
            return {
                'status': 'fail',
                'msg': str(_var_var_4)
            }
    def save_file_to_db(self, path, f):
        if hasattr(f, 'code'):
            logger.error(f)
            return None
        return None
        if f.type == 'file':
            self._rename_op.save(RenameLog(ali_fid = f.file_id, name = f.name, size = f.size, path = path, sha1 = f.content_hash, pid = f.parent_file_id, suffix = f.file_extension, status = 1, tidy_type = 'alipan'))
        return None
        return None

    
    def get_file(self, file_id):
        return self.get_api.get_file(file_id = file_id)
        return None

    
    def save_all_files(self, file_id, _type, _path):
        '''保存ali文件到db'''
        if _type == 'file':
            _var_var_39 = self.get_api.get_file(file_id = file_id)
            self.save_file_to_db(_path, _var_var_39)
            return None
        return None
        self.walk_all_files(callback = self.save_file_to_db, parent_file_id = file_id, _path = _path)
        logger.info(f'''保存ali文件到db成功-{file_id}-{_path}''')
        return None
        return None

    
    def walk_all_files(self, callback, parent_file_id, _path):
        '''遍历指定文件夹下所有文件
        :param parent_file_id: 文件夹 id，默认 root
        :param callback: 回调函数
        :param _path: 当前文件基于指定文件夹的路径
        :return:
        '''
        for _var_var_39 in self.get_api.get_file_list(parent_file_id = parent_file_id):
            callback(_path, _var_var_39)
            if hasattr(_var_var_39, 'code'):
                logger.error(_var_var_39)
                continue
            if not _var_var_39.type == 'folder':
                continue
            self.walk_all_files(callback, parent_file_id = _var_var_39.file_id, _path = f'''{_path}/{_var_var_39.name}''')
        return None
        return None

    
    def save_ali_share_to_db(self):
        _var_var_40 = self._share_down_op.get_by_status(0)
        if not _var_var_40:
            return None
        _var_var_42 = [_var_var_41.async_task_id for _var_var_41 in _var_var_40 if _var_var_41.async_task_id]
        _var_var_43 = self.get_save_task_status_by_retry(_var_var_42)
        _var_var_44 = []
        _var_var_45 = []
        for _var_var_41 in _var_var_40:
            if _var_var_41.async_task_id and _var_var_43.get(_var_var_41.async_task_id) == 'Succeed':
                _var_var_46 = 'folder' if _var_var_41.async_task_id else 'file'
                self.save_all_files(file_id=_var_var_41.f_id, _type=_var_var_46, _path=f'/{_var_var_41.f_name or _var_var_41.share_name}')
                _var_var_44.append(_var_var_41.id)
            else:
                _var_var_45.append(_var_var_41.id)
        if _var_var_44:
            self._share_down_op.update_all_status(_var_var_44, 1)
        if _var_var_45:
            self._share_down_op.update_all_status(_var_var_45, 2)
        return None
    def scrape_ali_file(self):
        '''
        刮削阿里云盘文件数据
        '''
        _var_var_47 = self._rename_op.get_by_status(1, 'video')
        for _var_var_48 in _var_var_47:
            _var_var_49 = self._mp.get_recognize_info(_var_var_48.path, _var_var_48.name)
            self._rename_op.update_log(_var_var_48)
        return None
        return None

    property



