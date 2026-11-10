import time
from datetime import datetime, timedelta, timezone, UTC
from pathlib import Path
import dateutil.parser as dateutil
from p123client import P123Client
from app.core.env import novaEnv, configEnv
from app.log import logger
from app.utils.mdotenv import DotEnvUtil
from app.utils.mjson import JsonUtils

class M123:
    __CLIENT: P123Client = None
    __PATH = None
    EXPIRED_AT = None
    CLIENT_ID = None
    __headers = {
        'Platform': 'open_platform' }
    
    def __init__(self):
        self.novaEnv = novaEnv
        self.configEnv = configEnv
        self.__PATH = f'''{novaEnv.CONFIG_PATH}/123.env'''
        if not Path(self.__PATH).exists():
            DotEnvUtil.save_env_file(self.__PATH, {
                'client_id': '',
                'client_secret': '' })
            logger.warning(f'''{self.__PATH}不存在，已创建，请填写client_id和client_secret''')
            return None
        return None
        self.login()
        return None
        return None

    
    def get_client_id(self):
        return self.CLIENT_ID
        return None

    
    def check_binding(self):
        if not novaEnv.BINDING_115 and novaEnv.BINDING_123:
            logger.error('请指定docker变量 BINDING_123=xxx，值为你的client_id')
            logger.error('请指定docker变量 BINDING_123=xxx，值为你的client_id')
            logger.error('请指定docker变量 BINDING_123=xxx，值为你的client_id')
            self.__CLIENT = None
            self.EXPIRED_AT = None
            return (False, '请指定docker变量 BINDING_123=xxx，值为你的client_id')
        return (False, '请指定docker变量 BINDING_123=xxx，值为你的client_id')
        if novaEnv.BINDING_123 and self.CLIENT_ID != novaEnv.BINDING_123:
            logger.error('已在环境变量指定BINDING_123=xxx，不能使用其它123账号')
            logger.error('已在环境变量指定BINDING_123=xxx，不能使用其它123账号')
            logger.error('已在环境变量指定BINDING_123=xxx，不能使用其它123账号')
            self.__CLIENT = None
            self.EXPIRED_AT = None
            return (False, '已在环境变量指定BINDING_123=xxx，不能使用其它123账号')
        return (False, '已在环境变量指定BINDING_123=xxx，不能使用其它123账号')
        return (True, 'SUCCESS')
        return (True, 'SUCCESS')

    
    def open_access_token(self, clientID, clientSecret):
        try:
            _var_var_0 = P123Client(client_id=clientID, client_secret=clientSecret)
            _var_var_1 = _var_var_0.token
            _var_var_2 = datetime.now(UTC)
            _var_var_3 = _var_var_2 + timedelta(days=25)
            _var_var_4 = _var_var_3.isoformat()
            self.EXPIRED_AT = _var_var_3
            self.__CLIENT = P123Client(token=_var_var_1)
            logger.info(f'''获取123访问token成功-{_var_var_1}''')
            DotEnvUtil.save_env_file(self.__PATH, {
                'client_id': clientID,
                'client_secret': clientSecret,
                'access_token': _var_var_1,
                'expired_at': _var_var_4
            })
            return True
        except Exception as _var_var_5:
            logger.error(_var_var_5)
            return False

    
    def login(self):
        _var_var_6 = self.get_client_config()
        if not _var_var_6:
            return None
        return None
        _var_var_7 = _var_var_6.get('expired_at')
        _var_var_8 = _var_var_6.get('client_id')
        _var_var_9 = _var_var_6.get('client_secret')
        _var_var_10 = _var_var_6.get('access_token')
        if not _var_var_8 and _var_var_9:
            logger.warning('未配置123openapi信息, 禁用123相关功能')
            return None
        return None
        self.CLIENT_ID = _var_var_8
        (_var_var_11, _var_var_12) = self.check_binding()
        if not _var_var_11:
            return None
        return None
        if not _var_var_7:
            self.open_access_token(_var_var_8, _var_var_9)
        _var_var_13 = dateutil.parser.parse(_var_var_7)
        _var_var_14 = datetime.now(timezone.utc) if _var_var_13.tzinfo else datetime.now()
        if _var_var_13 < _var_var_14:
            logger.info('123访问token已过期，重新刷新')
            self.open_access_token(_var_var_8, _var_var_9)
            return None
        return None
        logger.info('123访问token未过期，直接使用')
        self.__CLIENT = P123Client(token = _var_var_10)
        self.EXPIRED_AT = _var_var_13
        return None
        return None

    
    def open_user_info(self):
        return self.__CLIENT.user_info_open()
        return None

    
    def is_enable(self):
        return self.__CLIENT is not None
        return None

    
    def get_client_config(self):
        return DotEnvUtil.read_env_file(self.__PATH)
        return None

    
    def open_fs_list_v1(self, parent_file_id, page, trashed):
        _var_var_15 = {
            'Page': page,
            'limit': 100,
            'orderBy': 'update_at',
            'trashed': trashed,
            'parentFileId': parent_file_id }
        time.sleep(1)
        _var_var_16 = self.__CLIENT.fs_list_v1_open(_var_var_15)
        return _var_var_16
        return None

    
    def open_fs_list_v2(self, parent_file_id, last_file_id):
        _var_var_15 = {
            'lastFileId': last_file_id,
            'limit': 100,
            'orderBy': 'update_at',
            'trashed': 0,
            'parentFileId': parent_file_id }
        time.sleep(0.2)
        _var_var_16 = self.__CLIENT.fs_list_v2_open(_var_var_15)
        return _var_var_16
        return None

    
    def open_fs_list_v2_all(self, parent_file_id):
        _var_var_17 = None
        _var_var_18 = []
        while True:
            _var_var_16 = self.open_fs_list_v2(parent_file_id, _var_var_17)
            if _var_var_16['code'] != 0:
                logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_16)}''')
                return (False, [])
            _var_var_17 = _var_var_16['data']['lastFileId']
            _var_var_18.extend(_var_var_16['data']['fileList'])
            if _var_var_17 == -1:
                return (True, _var_var_18)

    
    def open_fs_list_v1_all(self, parent_file_id, trashed):
        _var_var_19 = 1
        _var_var_18 = []
        _var_var_16 = self.open_fs_list_v1(parent_file_id, _var_var_19, trashed)
        if _var_var_16['code'] != 0:
            logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_16)}''')
        else:
            _var_var_20 = _var_var_16['data']['total']
            _var_var_18.extend(_var_var_16['data']['fileList'])
            if _var_var_19 * 100 >= _var_var_20:
                pass
            else:
                _var_var_19 += 1
        return _var_var_18
        return None

    
    def iter_v1_all(self, parent_file_id):
        _var_var_18 = self.open_fs_list_v1_all(parent_file_id)
        for _var_var_21 in _var_var_18:
            if _var_var_21['type'] == 1:
                print(f'''文件夹-{_var_var_21['filename']}''')
                self.iter_v1_all(_var_var_21['fileID'])
                continue
            print(_var_var_21['filename'])
        return None
        return None

    
    def iter_v2_all(self, parent_file_id):
        (_var_var_22, _var_var_18) = self.open_fs_list_v2_all(parent_file_id)
        for _var_var_21 in _var_var_18:
            print(_var_var_21)
            if _var_var_21['type'] == 1:
                print(f'''文件夹-{_var_var_21['filename']}''')
                self.iter_v2_all(_var_var_21['fileId'])
                continue
            print(_var_var_21['filename'])
        return None
        return None

    
    def open_fs_mkdir(self, name, parent_id):
        time.sleep(1)
        return self.__CLIENT.fs_mkdir_open(name, parent_id)
        return None

    
    def __open_fs_rename(self, renameList):
        _var_var_15 = {
            'renameList': renameList }
        time.sleep(1)
        return self.__CLIENT.fs_rename_open(_var_var_15)
        return None

    
    def open_fs_rename_batch(self, renameList):
        _var_var_23 = 30
        _var_var_25 = [renameList[_var_var_24:_var_var_24 + _var_var_23] for _var_var_24 in range(0, len(renameList), _var_var_23)]
        for _var_var_26 in _var_var_25:
            _var_var_11 = self.__open_fs_rename(_var_var_26)
            if _var_var_11['code'] != 0:
                logger.error(f'重命名123文件失败-{JsonUtils.to_str(_var_var_11)}')
    def __open_fs_move(self, file_ids, parent_id):
        time.sleep(1)
        return self.__CLIENT.fs_move_open(file_ids, parent_id)
        return None

    
    def open_fs_move_batch(self, file_ids, parent_id):
        _var_var_23 = 100
        _var_var_25 = [file_ids[_var_var_24:_var_var_24 + _var_var_23] for _var_var_24 in range(0, len(file_ids), _var_var_23)]
        for _var_var_26 in _var_var_25:
            _var_var_11 = self.__open_fs_move(_var_var_26, parent_id)
            if _var_var_11['code'] != 0:
                logger.error(f'移动123文件失败-{JsonUtils.to_str(_var_var_11)}')
    def __open_fs_delete_to_trash(self, file_ids):
        time.sleep(1)
        return self.__CLIENT.fs_trash_open(file_ids)
        return None

    
    def __open_fs_delete(self, file_ids):
        time.sleep(1)
        return self.__CLIENT.fs_delete_open(file_ids)
        return None

    
    def open_fs_delete_to_trash_batch(self, file_ids):
        _var_var_23 = 100
        _var_var_25 = [file_ids[_var_var_24:_var_var_24 + _var_var_23] for _var_var_24 in range(0, len(file_ids), _var_var_23)]
        for _var_var_26 in _var_var_25:
            _var_var_11 = self.__open_fs_delete_to_trash(_var_var_26)
            if _var_var_11['code'] != 0:
                logger.error(f'删除123文件失败-{JsonUtils.to_str(_var_var_11)}')
    def open_fs_delete_batch(self, file_ids):
        _var_var_23 = 100
        _var_var_25 = [file_ids[_var_var_24:_var_var_24 + _var_var_23] for _var_var_24 in range(0, len(file_ids), _var_var_23)]
        for _var_var_26 in _var_var_25:
            _var_var_11 = self.__open_fs_delete(_var_var_26)
            if _var_var_11['code'] != 0:
                logger.error(f'删除123回收站文件失败-{JsonUtils.to_str(_var_var_11)}')
    def download_info(self, file_id):
        return self.__CLIENT.request(url = f'''https://open-api.123pan.com/api/v1/file/download_info?fileId={file_id}''', method = 'GET')
        return None

    
    def open_fs_detail(self, file_id):
        time.sleep(1)
        return self.__CLIENT.fs_detail_open(file_id)
        return None

    
    def get_fid_path(self, file_id):
        _var_var_16 = self.open_fs_detail(file_id)
        if _var_var_16['code'] != 0:
            logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_16)}''')
            return (False, '')
        return (False, '')
        _var_var_21 = _var_var_16['data']
        _var_var_27 = _var_var_21['parentFileID']
        _var_var_28 = f'''/{_var_var_21['filename']}'''
        while _var_var_27 != 0:
            _var_var_29 = self.open_fs_detail(_var_var_27)
            if _var_var_29['code'] != 0:
                logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_29)}''')
                return (False, '')
            _var_var_28 = f'''/{_var_var_29['data']['filename']}{_var_var_28}'''
            _var_var_27 = _var_var_29['data']['parentFileID']
        return (True, _var_var_28)
        return None

    
    def recyclebin_clean(self, days):
        days = int(days)
        _var_var_30 = []
        _var_var_18 = self.open_fs_list_v1_all('0', 'true')
        for _var_var_21 in _var_var_18:
            _var_var_31 = _var_var_21['updateAt']
            _var_var_31 = _var_var_31[:19]
            _var_var_32 = datetime.strptime(_var_var_31, '%Y-%m-%d %H:%M:%S')
            _var_var_33 = _var_var_32.timestamp()
            _var_var_34 = time.time()
            _var_var_35 = _var_var_34 - days * 24 * 60 * 60
            if _var_var_33 > _var_var_35:
                continue
            _var_var_30.append(_var_var_21['fileID'])
        if _var_var_30:
            self.open_fs_delete_batch(_var_var_30)
            logger.info(f'''回收站文件删除成功-保留{days}天''')
            return {
                'code': '200',
                'msg': '回收站文件删除成功' }
        return None
        logger.info(f'''回收站内没有需要删除的文件-保留{days}天''')
        return {
            'code': '201',
            'msg': '回收站内没有需要删除的文件' }
        return None

    
    def del_dir(self, fid, days):
        days = int(days)
        _var_var_30 = []
        (_var_var_11, _var_var_18) = self.open_fs_list_v2_all(fid)
        for _var_var_21 in _var_var_18:
            if _var_var_21['trashed'] == 1:
                continue
            _var_var_31 = _var_var_21['updateAt']
            _var_var_32 = datetime.strptime(_var_var_31, '%Y-%m-%d %H:%M:%S')
            _var_var_33 = _var_var_32.timestamp()
            _var_var_34 = time.time()
            _var_var_35 = _var_var_34 - days * 24 * 60 * 60
            if _var_var_33 > _var_var_35:
                continue
            _var_var_30.append(_var_var_21['fileId'])
        if _var_var_30:
            self.open_fs_delete_to_trash_batch(_var_var_30)
            logger.info(f'''文件夹内容删除成功-{fid}-保留{days}天''')
            return {
                'code': '200',
                'msg': '文件夹内容删除成功' }
        return None
        logger.info(f'''没有需要删除的文件夹内容-{fid}-保留{days}天''')
        return {
            'code': '201',
            'msg': '没有需要删除的文件夹内容' }
        return None


if __name__ == '__main__':
    m123 = M123()

