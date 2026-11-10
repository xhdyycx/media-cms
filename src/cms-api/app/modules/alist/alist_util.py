import os
import time
from openlist import OpenlistClient
import shutil
from urllib.request import urlopen
from shutil import copyfileobj
from app.core.env import configEnv
from app.log import logger
from app.modules.emby.emby import EmbyApi
from app.services.message_service import MessageService
from app.utils.ko_util import convert_size
from app.utils.mutil import Mutil
from urllib.parse import quote
from app.utils.thread import ThreadUtil

class AlistUtil:
    
    def __init__(self):
        self.alist_url = configEnv.alist_url
        self.alist_token = configEnv.alist_token
        self.alist_client = OpenlistClient.from_auth(self.alist_token, self.alist_url)
        self.img_exts = configEnv.alist_image_suffix
        self.video_exts = configEnv.alist_video_suffix
        self.nfo_exts = configEnv.alist_media_data_suffix
        self.sub_exts = [
            'ass',
            'srt',
            'ssa',
            'sup']
        self.alist_api_interval = configEnv.alist_api_interval
        self.min_size = configEnv.alist_min_size
        self.min_size_mb = convert_size(self.min_size)
        self.down_thread = ThreadUtil(configEnv.alist_download_threads, configEnv.alist_download_threads)
        self.strm_count = 0
        self.nfo_count = 0
        self.root_path = ''
        self._emby_api = EmbyApi()
        self._message = MessageService()
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
        if self.nfo_count > 0:
            _var_var_4 = f'''{_var_var_4}\n图片字幕等：{self.nfo_count} 个'''
            _var_var_5 = True
        if _var_var_5:
            self._message.send_msg(title = '🌟alist同步结果🌟', text = _var_var_4.strip('\n'))
        self.strm_count = 0
        self.nfo_count = 0
        return None
        return None

    
    def sync_path_task(self, path, local_path, is_del, is_sync_sub):
        self.root_path = path
        self.sync_path(path, local_path, is_del, is_sync_sub)
        self.down_thread.wait_for_all_tasks()
        logger.info(f'''alist同步完成, path: {path}, 共生成{self.strm_count}个strm文件, {self.nfo_count}个nfo文件''')
        self.send_sync_result_msg()
        self.refresh_emby_library()
        return None
        return None

    
    def fs_list_page(self, path, page, per_page):
        _var_var_6 = {
            'path': path,
            'refresh': True,
            'page': page,
            'per_page': per_page }
        return self.alist_client.fs_list(payload = _var_var_6)
        return None

    
    def fs_list_all(self, path):
        _var_var_7 = 1
        _var_var_8 = 500
        _var_var_9 = []
        while True:
            _var_var_10 = self.fs_list_page(path, _var_var_7, _var_var_8)
            logger.info('获取alist文件列表, path: {}, page: {}, per_page: {}, res: {}'.format(path, _var_var_7, _var_var_8, _var_var_10))
            if _var_var_10['data'].get('per_page'):
                _var_var_8 = _var_var_10['data'].get('per_page')
            _var_var_9.extend(_var_var_10['data'].get('content', []))
            if _var_var_10['data']['total'] > _var_var_7 * _var_var_8:
                _var_var_7 += 1
            else:
                _var_var_10['data']['content'] = _var_var_9
                return _var_var_10

    
    def sync_path(self, path, local_path, is_del, is_sync_sub):
        logger.info(f'''开始同步文件夹: {path}''')
        if self.alist_api_interval:
            time.sleep(self.alist_api_interval)
        _var_var_11 = self.fs_list_all(path)
        if _var_var_11['code'] != 200:
            logger.error(f'''获取alist文件列表失败: {_var_var_11}''')
            return None
        return None
        if not _var_var_11.get('data', { }).get('content'):
            logger.info(f'''空文件夹: {path}''')
            return None
        return None
        self.sync_del(_var_var_11, Mutil.merge_paths(local_path, path), is_del)

    
    def sync_del(self, res, local_path, is_del):
        if not is_del:
            return None
        return None
        _var_var_13 = []
        for _var_var_12 in res['data']['content']:
            if _var_var_12['is_dir']:
                _var_var_13.append(_var_var_12['name'])
                continue
            _var_var_19 = _var_var_12['name'].split('.')[-1]
            if _var_var_19 in self.video_exts:
                _var_var_20 = Mutil.change_file_suffix(_var_var_12['name'], 'strm')
                _var_var_13.append(_var_var_20)
                continue
            if not _var_var_19 in self.sub_exts:
                continue
            _var_var_13.append(_var_var_12['name'])
        _var_var_21 = self.get_loacl_sync_files(local_path)
        for _var_var_22 in _var_var_21:
            if not _var_var_22['name'] not in _var_var_13:
                continue
            self.del_local_file(_var_var_22)
        return None
        return None

    
    def download_file(self, file):
        _var_var_2 = file['local_path']
        if not file['ext']:
            return None
        return None
        if file['ext'] in self.video_exts:
            _var_var_2 = Mutil.change_file_suffix(_var_var_2, 'strm')
            if not os.path.exists(_var_var_2):
                os.makedirs(os.path.dirname(_var_var_2), exist_ok = True)
                _var_var_23 = open(_var_var_2, 'w')
                _var_var_23.write(file['url'])
                logger.info(f'''strm生成成功: {_var_var_2}''')
                self.add_sync_path(os.path.dirname(_var_var_2))
            else:
                logger.info(f'''strm文件已存在，跳过生成: {_var_var_2}''')
        elif file['ext'] in self.img_exts and file['ext'] in self.nfo_exts or file['ext'] in self.sub_exts:
            if not os.path.exists(_var_var_2):
                os.makedirs(os.path.dirname(_var_var_2), exist_ok = True)
                with open(_var_var_2, 'wb') as _var_var_23:
                    _var_var_25 = urlopen(file['url'])
                    copyfileobj(_var_var_25, _var_var_23)
                logger.info(f'''下载文件成功: {_var_var_2}''')
            else:
                logger.info(f'''文件已存在，跳过下载: {_var_var_2}''')
        else:
            logger.info(f'''跳过{file['ext']}文件, name: {file['name']}''')
        return None
        
    def get_local_files(self, local_path):
        _var_var_26 = []
        if not os.path.exists(local_path):
            return _var_var_26
        return None
        _var_var_27 = os.scandir(local_path)
        for _var_var_28 in _var_var_27:
            _var_var_26.append({
                'name': _var_var_28.name,
                'is_dir': _var_var_28.is_dir(),
                'path': _var_var_28.path,
                'ext': os.path.splitext(_var_var_28.name)[1][1:] if _var_var_28.is_file() else '' })
        return _var_var_26

    
    def get_loacl_sync_files(self, local_path):
        _var_var_26 = []
        for _var_var_12 in self.get_local_files(local_path):
            if _var_var_12['is_dir']:
                _var_var_26.append(_var_var_12)
                continue
            if not _var_var_12['ext'] in ('strm',):
                continue
            _var_var_26.append(_var_var_12)
        return _var_var_26
        return None

    
    def del_local_file(self, file):
        try:
            if file['is_dir']:
                self.add_sync_path(file['path'])
                if os.path.exists(file['path']):
                    logger.info(f'''删除本地文件夹: {file['path']}''')
                    shutil.rmtree(file['path'])
                else:
                    logger.warning(f'''要删除的文件夹不存在: {file['path']}''')
            elif os.path.exists(file['path']):
                os.remove(file['path'])
                self.add_sync_path(os.path.dirname(file['path']))
                logger.info(f'''删除本地文件: {file['path']}''')
                if file['ext'] == 'strm':
                    _var_var_29 = Mutil.change_file_suffix(file['path'], 'nfo')
                    if os.path.exists(_var_var_29):
                        os.remove(_var_var_29)
                        self.add_sync_path(os.path.dirname(_var_var_29))
                        logger.info(f'''删除本地文件: {_var_var_29}''')
                    else:
                        logger.warning(f'''要删除的文件不存在: {file['path']}''')
        except Exception as e:
            logger.error(f'''删除文件失败: {file['path']}''')
            logger.error(f'''删除文件异常: {e}''')


if __name__ == '__main__':
    alist_util = AlistUtil()
    for file in alist_util.get_loacl_sync_files('/path/to/downloads'):
        print(file)

