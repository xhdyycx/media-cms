import os
import shutil
from app.core.con_storage import StorageApi
from app.core.m123 import M123
from app.core.obj_factory import ObjFactory
from app.log import logger
from app.types.con_file import ConFile
from app.utils.ko_util import convert_size
from app.utils.mjson import JsonUtils
from app.utils.mtime import TimeUtils
from app.utils.mutil import Mutil
from app.utils.thread import ThreadUtil

class CommonSync(StorageApi):
    
    def __init__(self, storage_type, video_ext, img_ext, nfo_ext, min_size, down_threads):
        super().__init__()
        self.storage_type = storage_type
        self.img_ext = img_ext
        self.video_ext = video_ext
        self.nfo_ext = nfo_ext
        self.min_size = min_size
        self.min_size_mb = convert_size(min_size)
        self.down_thread = ThreadUtil(down_threads, 1000)
        self.strm_count = 0
        self.img_count = 0
        self.nfo_count = 0

    @property
    def _m123(self):
        return ObjFactory.get_instance(M123)
    
    def sync_path_task(self, fid, path, local_path, is_del, is_sync_sub):
        (_var_var_0, _var_var_1) = self.fs_file_info(fid, path, local_path)
        if not _var_var_0:
            return None
        return None
        self.sync_path(_var_var_1, is_del, is_sync_sub)
        logger.info(f'''{self.storage_type}同步完成, path: {path}, 共生成{self.strm_count}个strm文件, {self.nfo_count}个图片字幕等文件''')
        self.send_sync_result_msg()
        self.refresh_emby_library()
        return None
        return None

    
    def fs_file_info(self, fid, path, local_path):
        if self.storage_type == '123':
            _var_var_2 = self._m123.open_fs_detail(fid)
            if _var_var_2['code'] != 0:
                logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_2)}''')
                return (False, None)
            return (False, None)
            _var_var_3 = _var_var_2['data']
            _var_var_4 = '根目录'
            _var_var_5 = _var_var_3['parentFileID']
            _var_var_6 = ''
            while _var_var_5 != 0:
                _var_var_7 = self._m123.open_fs_detail(_var_var_5)
                if _var_var_7['code'] != 0:
                    logger.error(f'''获取123文件列表失败-{JsonUtils.to_str(_var_var_7)}''')
                    break
                else:
                    _var_var_8 = _var_var_7['data']['filename']
                    if _var_var_7['data']['fileID'] == _var_var_3['parentFileID']:
                        _var_var_4 = _var_var_8
                    _var_var_6 = f'''/{_var_var_8}{_var_var_6}'''
                    _var_var_5 = _var_var_7['data']['parentFileID']
            _var_var_9 = Mutil.merge_paths(local_path, _var_var_6).rstrip('/')
            _var_var_6 = f'''{_var_var_6}/{_var_var_3['filename']}'''
            _var_var_10 = ConFile(is_dir = 1, fid = fid, pid = _var_var_3['parentFileID'], name = _var_var_3['filename'], p_name = _var_var_4, full_y_path = _var_var_6, local_path = _var_var_9, local_name = _var_var_3['filename'], f_modify_time = _var_var_3['createAt'], sync_time = TimeUtils.get_current_time_str(), status = 'success')
            return (True, _var_var_10)
        return None
        return (False, None)
        return (False, None)

    
    def sync_path(self, dir_info, is_del, is_sync_sub):
        _var_var_11 = dir_info.fid
        logger.info(f'''开始同步{self.storage_type}文件夹: {_var_var_11} {dir_info.full_y_path}''')
        (_var_var_0, _var_var_12, _var_var_13) = self.fs_list({
            'fid': _var_var_11 })
        if not _var_var_0:
            return None
        return None
        _var_var_14 = Mutil.merge_paths(dir_info.local_path, dir_info.local_name)
        self.sync_delete(_var_var_11, _var_var_12, _var_var_13)
        _var_var_15 = []
        _var_var_16 = [
            dir_info]
        for _var_var_17 in _var_var_12:
            if int(_var_var_17.size) < self.min_size and _var_var_17.ext in self.video_ext:
                logger.info(f'''视频小于 {self.min_size_mb}, 不同步: {_var_var_17.name}''')
                continue
            _var_var_17.p_name = dir_info.name
            _var_var_17.full_y_path = f'''{dir_info.full_y_path}/{_var_var_17.name}'''
            _var_var_17.local_path = _var_var_14
            _var_var_15.append((self.download_file, (_var_var_17,)))
        if _var_var_15:
            _var_var_16.extend(self.down_thread.submit_batch_async_and_wait_results(_var_var_15))
        self.save_to_db(_var_var_16)
        if is_sync_sub and _var_var_13:
            for _var_var_18 in _var_var_13:
                _var_var_18.p_name = dir_info.name
                _var_var_18.full_y_path = f'''{dir_info.full_y_path}/{_var_var_18.name}'''
                _var_var_18.local_path = _var_var_14
                _var_var_18.local_name = _var_var_18.name
                _var_var_18.sync_time = TimeUtils.get_current_time_str()
                _var_var_18.status = 'success'
                self.sync_path(_var_var_18, is_del, is_sync_sub)
        return None
        return None

    
    def sync_del(self, file_list, dir_list, local_path, is_del):
        if not is_del:
            return None
        return None
        _var_var_19 = []
        for _var_var_18 in dir_list:
            _var_var_19.append(_var_var_18.name)
        for _var_var_17 in file_list:
            if _var_var_17.ext in self.video_ext:
                _var_var_20 = Mutil.change_file_suffix(_var_var_17.name, 'strm')
                _var_var_19.append(_var_var_20)
                continue
            _var_var_19.append(_var_var_17.name)
        _var_var_21 = self.get_local_sync_files(local_path)
        for _var_var_22 in _var_var_21:
            if not _var_var_22['name'] not in _var_var_19:
                continue
            self.del_local_file(_var_var_22)
        return None
        return None

    
    def get_local_files(self, local_path):
        _var_var_23 = []
        if not os.path.exists(local_path):
            return _var_var_23
        return None
        _var_var_24 = os.scandir(local_path)
        for _var_var_25 in _var_var_24:
            _var_var_23.append({
                'name': _var_var_25.name,
                'is_dir': _var_var_25.is_dir(),
                'path': _var_var_25.path,
                'ext': os.path.splitext(_var_var_25.name)[1][1:] if _var_var_25.is_file() else '' })
        return _var_var_23

    
    def get_local_sync_files(self, local_path):
        _var_var_23 = []
        for _var_var_17 in self.get_local_files(local_path):
            if _var_var_17['is_dir']:
                _var_var_23.append(_var_var_17)
                continue
            if not _var_var_17['ext'] in ('strm',):
                continue
            _var_var_23.append(_var_var_17)
        return _var_var_23
        return None

    
    def del_local_file(self, _file):
        try:
            if _file['is_dir']:
                self.add_sync_path(_file['path'])
                if os.path.exists(_file['path']):
                    logger.info(f'''删除本地文件夹: {_file['path']}''')
                    shutil.rmtree(_file['path'])
                else:
                    logger.warning(f'''要删除的文件夹不存在: {_file['path']}''')
            elif os.path.exists(_file['path']):
                os.remove(_file['path'])
                self.add_sync_path(os.path.dirname(_file['path']))
                logger.info(f'''删除本地文件: {_file['path']}''')
                if _file['ext'] == 'strm':
                    _var_var_26 = Mutil.change_file_suffix(_file['path'], 'nfo')
                    if os.path.exists(_var_var_26):
                        os.remove(_var_var_26)
                        self.add_sync_path(os.path.dirname(_var_var_26))
                        logger.info(f'''删除本地文件: {_var_var_26}''')
                    else:
                        logger.warning(f'''要删除的文件不存在: {_file['path']}''')
        except Exception as _var_var_27:
            logger.error(f'''删除本地文件失败: {_file['path']}''')
            logger.error(f'''删除本地文件异常: {_var_var_27}''')

if __name__ == '__main__':
    commonSync = CommonSync()

