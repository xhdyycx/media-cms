import os
import time
import shutil
from typing import Dict
from urllib.request import urlopen
from shutil import copyfileobj
from p115client import P115Client
from app.core.env import configEnv
from app.core.env2 import config2Env
from app.core.m115 import M115
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.modules.emby.emby import EmbyApi
from app.services.message_service import MessageService
from app.utils.ko_util import convert_size
from app.utils.mjson import JsonUtils
from app.utils.mutil import Mutil
from urllib.parse import quote
from app.utils.thread import ThreadUtil
IOS_UA = 'Mozilla/5.0 115disk/36.2.28 115Browser/36.2.28 115wangpan_android/36.2.28'

def get_ios_ua_app():
    '''
    获取 IOS 设备的 header（UA）和 APP
    '''
    return {
        'headers': {
            'user-agent': IOS_UA },
        'app': 'ios' }


def get_chrome_ua_app():
    '''
    获取 IOS 设备的 header（UA）和 APP
    '''
    return {
        'headers': {
            'user-agent': 'Mozilla/5.0 AppleWebKit/600 Safari/600 Chrome/124.0.0.0' },
        'app': 'chrome' }


class M115Util:
    
    def __init__(self):
        self._M115Util__client = P115Client(cookies = '')
        self.img_exts = configEnv.share_115_image_suffix
        self.video_exts = configEnv.share_115_video_suffix
        self.nfo_exts = configEnv.share_115_media_data_suffix
        self.sub_exts = [
            'ass',
            'srt',
            'ssa',
            'sup']
        self.api_interval = configEnv.share_115_api_interval
        self.min_size = configEnv.share_115_min_size
        self.min_size_mb = convert_size(self.min_size)
        self.domain = configEnv.direct_115_302_domain
        self.down_thread = ThreadUtil(configEnv.share_115_img_download_threads, configEnv.share_115_img_download_threads)
        self.strm_count = 0
        self.img_count = 0
        self.nfo_count = 0
        self._emby_api = EmbyApi()
        self._message = MessageService()
        self._m115 = ObjFactory.get_instance(M115)
        self._is_refresh_library = configEnv.emby_refresh_status
        self._sync_path_set = set()
        return None
        return None

    
    def add_sync_path(self, path):
        if self._is_refresh_library:
            self._sync_path_set.add(path)
        return None
        return None

    
    def refresh_emby_library(self):
        if not self._sync_path_set or self._is_refresh_library:
            self._sync_path_set.clear()
            logger.info('不刷新emby库')
            return None
        return None
        logger.info(f'''转换路径之前-{self._sync_path_set}''')
        _var_var_0 = list(set(self._sync_path_set))
        _var_var_1 = []
        for _var_var_2 in _var_var_0:
            if configEnv.emby_path_replace_rule:
                _var_var_3 = configEnv.emby_path_replace_rule.split('#')
                if len(_var_var_3) == 2:
                    _var_var_2 = _var_var_2.replace(_var_var_3[0], _var_var_3[1], 1)
            if configEnv.emby_path_style == 'windows':
                _var_var_2 = _var_var_2.replace('/', '\\')
            elif configEnv.emby_path_style == 'unix':
                _var_var_2 = _var_var_2.replace('\\', '/')
            _var_var_1.append(_var_var_2)
        logger.info(f'''转换路径之后-{_var_var_1}''')
        self._emby_api.refresh_libraries_by_paths(_var_var_1)
        self._sync_path_set.clear()
        return None
        return None

    
    def send_sync_result_msg(self):
        _var_var_4 = ''
        _var_var_5 = False
        if self.strm_count > 0:
            _var_var_4 = f'''{_var_var_4}\n视频STRM：{self.strm_count} 个'''
            _var_var_5 = True
        if self.img_count > 0:
            _var_var_4 = f'''{_var_var_4}\n媒体图片：{self.img_count} 个'''
            _var_var_5 = True
        if self.nfo_count > 0:
            _var_var_4 = f'''{_var_var_4}\n媒体数据：{self.nfo_count} 个'''
        if _var_var_5:
            self._message.send_msg(title = '🌟115分享同步结果🌟', text = _var_var_4.strip('\n'))
        self.strm_count = 0
        self.img_count = 0
        self.nfo_count = 0
        return None
        return None

    
    def sync_path_task(self, share_code, receive_code, cid, local_path):
        self.sync_path(share_code, receive_code, cid, local_path)
        self.down_thread.wait_for_all_tasks()
        logger.info(f'''115分享同步完成, local_path: {local_path}, 共生成{self.strm_count}个strm文件, {self.img_count}个图片, {self.nfo_count}个字幕、NFO''')
        self.send_sync_result_msg()
        self.refresh_emby_library()
        return None
        return None

    
    def sync_path(self, share_code, receive_code, cid: int | str = 0, local_path: str = '/media/share'):
        logger.info(f'开始同步cid: {cid} - {local_path}')
        if self.api_interval:
            time.sleep(self.api_interval)
        _var_var_6 = self._m115.share_snap(share_code, receive_code, cid)
        if not _var_var_6.get('state'):
            logger.error(f'获取115文件列表失败: {_var_var_6}')
            return
        _var_var_8 = [_var_var_7 for _var_var_7 in _var_var_6['data'] if _var_var_7.get('sha')]
        for _var_var_7 in _var_var_8:
            if int(_var_var_7['s']) < self.min_size and _var_var_7['ico'] in self.video_exts:
                logger.info(f'视频小于 {self.min_size_mb}, 不生成STRM: {_var_var_7["n"]}')
                continue
            _var_var_7['local_path'] = f'{local_path}/{_var_var_7["n"]}'
            _var_var_9 = f'{self.domain}/s/{share_code}_{receive_code}_{_var_var_7["fid"]}'
            if config2Env.keep_suffix:
                _var_var_9 = f'{_var_var_9}.{_var_var_7["ico"]}'
            if configEnv.strm_type == 'pick_code_name':
                _var_var_9 = f'{_var_var_9}?/{_var_var_7["n"]}'
            _var_var_7['url'] = _var_var_9
            if _var_var_7.get('u'):
                _var_var_7['u'] = _var_var_7['u'].replace('_100?', '_0?')
            if _var_var_7['ico'] in self.nfo_exts:
                _var_var_7['share_code'] = share_code
                _var_var_7['receive_code'] = receive_code
                self.download_nfo_file(_var_var_7)
                continue
            self.down_thread.submit(self.download_file, _var_var_7)
        _var_var_10 = [_var_var_7 for _var_var_7 in _var_var_6['data'] if not _var_var_7.get('sha')]
        for _var_var_11 in _var_var_10:
            _var_var_12 = f'{local_path}/{_var_var_11["n"]}'
            self.sync_path(share_code, receive_code, _var_var_11['cid'], _var_var_12)
    def download_nfo_file(self, file):
        try:
            _var_var_2 = file['local_path']
            if not os.path.exists(_var_var_2):
                self.nfo_count += 1
        except Exception as _var_var_13:
            logger.error(f'download_nfo_file异常: {_var_var_13}')
            return None

    
    def download_file(self, file):
        _var_var_2 = file['local_path']
        if not file['ico']:
            return None
        return None
        if file['ico'] in self.video_exts:
            _var_var_2 = Mutil.change_file_suffix(_var_var_2, 'strm')
            if not os.path.exists(_var_var_2):
                os.makedirs(os.path.dirname(_var_var_2), exist_ok = True)
                _var_var_14 = open(_var_var_2, 'w')
                _var_var_14.write(file['url'])
                logger.info(f'''strm生成成功: {_var_var_2}''')
                self.add_sync_path(os.path.dirname(_var_var_2))
            else:
                logger.info(f'''strm文件已存在，跳过生成: {_var_var_2}''')
        elif file['ico'] in self.img_exts:
            if not os.path.exists(_var_var_2):
                os.makedirs(os.path.dirname(_var_var_2), exist_ok = True)
                with open(_var_var_2, 'wb') as _var_var_14:
                    _var_var_15 = urlopen(file['u'])
                    copyfileobj(_var_var_15, _var_var_14)
                logger.info(f'''下载文件成功: {_var_var_2}''')
            else:
                logger.info(f'''文件已存在，跳过下载: {_var_var_2}''')
        else:
            logger.info(f'''跳过{file['ico']}文件, name: {file['n']}''')
        return None
        
    def share_snap(self, share_code, receive_code, cid: int | str = 0):
        _var_var_16 = 0
        _var_var_17 = 1150
        _var_var_18 = []
        _var_var_19 = {}
        while True:
            _var_var_20 = {
                'share_code': share_code,
                'receive_code': receive_code,
                'cid': cid,
                'offset': _var_var_16,
                'limit': 1150,
                'o': 'file_name',
            }
            _var_var_6 = self.__client.share_snap_app(_var_var_20, **get_chrome_ua_app())
            _var_var_19['state'] = _var_var_6['state']
            _var_var_19['error'] = _var_var_6.get('error')
            if not _var_var_6['state']:
                print(f'获取分享链接失败：{_var_var_6["error"]}')
                break
            _var_var_19['share_name'] = _var_var_6['data']['shareinfo']['share_title']
            _var_var_18 += _var_var_6['data']['list']
            if _var_var_6['data']['count'] <= _var_var_16 + _var_var_17:
                break
            _var_var_16 += _var_var_17
        _var_var_19['data'] = _var_var_18
        return _var_var_19
if __name__ == '__main__':
    m115_util = M115Util()
    m115_util.sync_path('swzeyz63nnw', 'h303', 0, '/media/share')

