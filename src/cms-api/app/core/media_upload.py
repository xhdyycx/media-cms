import queue
import threading
import time
import traceback
from _queue import Empty
from sqlalchemy.orm import Session
from app.core.obj_factory import ObjFactory
from app.core.m115 import M115
from app.db.clouddata_op import CloudDataOp
from app.db.models.clouddata import CloudData
from app.log import logger
from app.schemas.types import ActionEnum
from app.utils.ko_util import split_path, get_sha1, join_cloud_paths, get_suffix
from app.utils.mjson import JsonUtils
from app.utils.singleton import Singleton

class MediaImgUpload(metaclass=Singleton):
    '''MediaImgUpload'''
    
    def __init__(self, db):
        self.name = '媒体图片上传'
        self._db = db
        self._cloud_data_op = CloudDataOp(self._db)
        self.upload_queue_set = set()
        self.upload_queue = queue.Queue()
        self.upload_thread = threading.Thread(target = self.__process_upload)
        self.upload_thread.start()
        return None
        return None

    @property
    def _m115(self):
        return ObjFactory.get_instance(M115)
    
    def add(self, img):
        '''将文件信息添加到上传队列'''
        if img['p'] not in self.upload_queue_set:
            logger.info(f'''增加上传任务：{JsonUtils.to_str(img)}''')
            self.upload_queue.put(img)
            self.upload_queue_set.add(img['p'])
        return None
        return None

    
    def __process_upload(self):
        '''后台线程，持续处理上传队列中的文件'''
        while True:
            try:
                _var_var_0 = self.get_img()
                if not _var_var_0:
                    time.sleep(5)
                    continue
                self.upload_img_to_cloud(_var_var_0['p'], _var_var_0['t'])
                if _var_var_0['p'] in self.upload_queue_set:
                    self.upload_queue_set.remove(_var_var_0['p'])
            except Exception as _var_var_1:
                _var_var_2 = traceback.format_exc()
                logger.error(f"处理队列中的上传文件发生异常: {_var_var_1} \n" + str(_var_var_2))
                time.sleep(5)
    def get_img(self):
        try:
            return self.upload_queue.get(block=True, timeout=1)
        except Empty:
            return None

    
    def upload_img_to_cloud(self, local_path, stime):
        logger.debug(f'准备上传文件...{local_path}')
        _var_var_3 = int(time.time()) - stime
        if _var_var_3 < 10:
            logger.debug(f'暂停{10 - _var_var_3}s...')
            time.sleep(10 - _var_var_3)
        (_var_var_4, _var_var_5) = split_path(local_path)
        _var_var_6 = get_suffix(_var_var_5)
        _var_var_7 = self._cloud_data_op.get_by_local_path(_var_var_4, _var_var_5)
        if _var_var_7 and _var_var_7.sync_time + 5 >= stime:
            logger.debug(f'忽略文件...{local_path}')
            return None
        if _var_var_7:
            _var_var_8 = get_sha1(local_path)
            if _var_var_8 == _var_var_7.sha1:
                logger.info(f'相同sha1跳过...{local_path}')
                return None
            logger.info(f'开始上传文件-修改...{local_path}')
            self._m115.fs_delete(_var_var_7.fid)
            _var_var_9 = self._m115.upload_file(local_path, _var_var_5, _var_var_7.pid)['data']
            logger.info(f'上传响应={JsonUtils.to_str(_var_var_9)}')
            _var_var_10 = _var_var_9.get('id') or _var_var_9.get('file_id')
            if _var_var_10:
                _var_var_11 = CloudData(id=_var_var_7.id, fid=_var_var_10, f_modify_time=int(time.time()), pick_code=_var_var_9.get('pickcode') or _var_var_9.get('pick_code'), sha1=_var_var_9.get('filesha1') or _var_var_9.get('sha1'), size=_var_var_9.get('filesize') or _var_var_9.get('file_size'), pid=_var_var_7.pid, suffix=_var_var_6, action=ActionEnum.UPLOAD.name, status=1, desc='上传成功')
                self._cloud_data_op.update_by_id(_var_var_11)
            else:
                logger.info(f'上传文件-未获取到fid, 放弃删掉db数据...{local_path}')
                self._cloud_data_op.delete_cloud(_var_var_7)
                return None
        else:
            logger.info(f'开始上传文件-新增...{local_path}')
            (_var_var_12, _var_var_13) = split_path(_var_var_4)
            _var_var_7 = self._cloud_data_op.get_by_local_path(_var_var_12, _var_var_13)
            if not _var_var_7:
                logger.info(f'上传文件结束-父文件夹不存在（此日志可忽略）...{local_path}')
                return None
            _var_var_14 = self._m115.upload_file(local_path, _var_var_5, _var_var_7.fid)
            if not _var_var_14 or not _var_var_14.get('state'):
                logger.error(f'上传文件失败...{local_path}, resp={JsonUtils.to_str(_var_var_14)}')
                return None
            _var_var_9 = _var_var_14['data']
            logger.info(f'上传响应={JsonUtils.to_str(_var_var_9)}')
            _var_var_10 = _var_var_9.get('id') or _var_var_9.get('file_id')
            if _var_var_10:
                _var_var_11 = CloudData(**{'fid': _var_var_10, 'name': _var_var_5, 'f_modify_time': int(time.time()), 'pid': _var_var_7.fid, 'p_name': _var_var_7.name, 'full_y_path': join_cloud_paths(_var_var_7.full_y_path, _var_var_5), 'pick_code': _var_var_9.get('pickcode') or _var_var_9.get('pick_code'), 'sha1': _var_var_9.get('filesha1') or _var_var_9.get('sha1'), 'size': _var_var_9.get('filesize') or _var_var_9.get('file_size'), 'is_dir': 0, 'is_media_dir': 0, 'suffix': _var_var_6, 'local_name': _var_var_5, 'local_path': _var_var_4, 'action': ActionEnum.UPLOAD.name, 'status': 1, 'desc': '上传成功'})
                self._cloud_data_op.save(_var_var_11)
            else:
                logger.info(f'上传文件-未获取到fid, 放弃保存db数据（此日志可忽略）...{local_path}')

