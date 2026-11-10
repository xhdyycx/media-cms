import json
import os
import time
from sqlalchemy.orm import Session
from app.core.env import ConfigEnv, configEnv
from app.core.env2 import config2Env
from app.core.obj_factory import ObjFactory
from app.core.media_monitor import MediaImgMonitor
from app.db.clouddata_op import CloudDataOp
from app.db.config_op import ConfigOp
from app.db.models.clouddata import CloudData
from app.db.rename_op import RenameOp
from app.db.share_op import ShareDownOp
from app.db.sub_op import SubMediaOp, SubSourceOp
from app.modules.emby.emby import EmbyApi
from app.modules.tmdb.tmdbapi import TmdbApi
from app.services.message_service import MessageService
from app.utils.ko_util import del_path, join_local_paths, change_file_suffix, get_thumb_name, rename, create_strm_file, join_cloud_paths, convert_size
from app.schemas.types import ActionEnum, StatusEnum
from app.log import logger
from app.core.m115 import M115
from app.db.liftlist_op import LiftListOp
from app.utils.mjson import JsonUtils
from app.utils.thread import ThreadUtil
from app.utils.mutil import Mutil
from app.utils.wrapper import exception_ignore, log_exec_time

class MediaSync:
    '''
    媒体库同步类
    '''
    
    def __init__(self, db, is_refresh_library):
        self._db = db
        self._CONFIG_ENV = ConfigEnv()
        self._lift_list_op = LiftListOp(self._db)
        self._cloud_data_op = CloudDataOp(self._db)
        self._rename_op = RenameOp(self._db)
        self._config_op = ConfigOp(self._db)
        self._share_down_op = ShareDownOp(self._db)
        self._sub_media_op = SubMediaOp(self._db)
        self._sub_source_op = SubSourceOp(self._db)
        self._sync_path_set = set()
        self._is_refresh_library = is_refresh_library
        self._msg_strm_count = 0
        self._msg_img_success_count = 0
        self._msg_img_fail_count = 0
        self._msg_nfo_success_count = 0
        self._msg_nfo_fail_count = 0
        self._batch_size = 1000
        self._batch_items = []
        self._batch_dir_items = { }
        self._MediaSync__CONFIG = self._config_op.get_all()
        self._MediaSync__VIDEO_SUFFIX = self._MediaSync__CONFIG.get('VIDEO_SUFFIX', [
            'mp4',
            'mkv'])
        self._MediaSync__IMAGE_SUFFIX = self._MediaSync__CONFIG.get('IMAGE_SUFFIX', [])
        self._MediaSync__MEDIA_DATA_SUFFIX = self._MediaSync__CONFIG.get('MEDIA_DATA_SUFFIX', [])
        self._media_img_monitor = MediaImgMonitor()
        logger.info(f'''图片下载线程数: {configEnv.image_download_threads}''')
        self._MediaSync__img_down_thread = ThreadUtil(configEnv.image_download_threads, configEnv.image_download_threads)
        self._message = MessageService()
        self._tmdbapi = TmdbApi()
        self._emby_api = EmbyApi()
        self._media_min_size = configEnv.media_min_size
        self._media_min_size_mb = convert_size(self._media_min_size)
        self._MediaSync__MUSIC_SUFFIX = [
            'aac',
            'aiff',
            'amr',
            'ape',
            'au',
            'flac',
            'm4a',
            'mid',
            'midi',
            'mp3',
            'ogg',
            'wav',
            'wma',
            'dff',
            'dsd']
        return None
        return None

    @property
    def _m115(self):
        return ObjFactory.get_instance(M115)
    
    def add_sync_path(self, path):
        if self._is_refresh_library:
            self._sync_path_set.add(path)
        return None
        return None

    
    def collect_impl(self, item):
        self._lift_list_op.add(item)
        return None
        return None

    
    def lift_sync_to_db(self):
        _var_var_0 = self._lift_list_op.get_max_lid()
        self._m115.life_behavior_sync(_var_var_0, self.collect_impl)
        logger.info('同步115生活事件到db-执行完成')
        return None
        return None

    
    def lift_db_sync_to_local(self):
        _var_var_1 = self._lift_list_op.get_all()
        _var_var_2 = False
        if _var_var_1 and len(_var_var_1) > 0:
            self._media_img_monitor.stop()
            _var_var_2 = True
        for _var_var_3 in _var_var_1:
            _var_var_4 = json.loads(_var_var_3.item_json)
            _var_var_5 = _var_var_4['behavior_type']
            logger.info(f'''增量同步-{_var_var_5}-{_var_var_3.id}-lid={_var_var_3.lid}''')
            if _var_var_5 == 'upload_file':
                _var_var_5
                self.__process_upload_file(_var_var_4)
            elif _var_var_1 == 'upload_image_file':
                _var_var_1
                self.__process_upload_file(_var_var_4)
            elif _var_var_1 == 'receive_files':
                _var_var_1
                self.__process_receive_files(_var_var_4)
            elif _var_var_1 == 'copy_folder':
                _var_var_1
                self.__process_copy_folder(_var_var_4)
            elif _var_var_1 == 'copy_file':
                _var_var_1
                self.__process_copy_file(_var_var_4)
            elif _var_var_1 == 'new_folder':
                _var_var_1
                self.__process_new_folder(_var_var_4)
            elif _var_var_1 == 'delete_file':
                _var_var_1
                self.__process_delete_file(_var_var_4)
            elif _var_var_1 == 'folder_rename':
                _var_var_1
                self.__process_folder_rename(_var_var_4)
            elif _var_var_1 == 'rename_file':
                _var_var_1
                self.__process_rename_file(_var_var_4)
            elif _var_var_1 == 'move_file':
                _var_var_1
                self.__process_move_file(_var_var_4)
            elif _var_var_1 == 'move_image_file':
                self.__process_move_file(_var_var_4)
            else:
                logger.info(f'''跳过该类型的同步-{_var_var_5}-item={_var_var_3.item_json}''')
            _var_var_3.update(self._db, {
                'status': StatusEnum.SUCCESS.value })
        if _var_var_2:
            self._media_img_monitor.start(self._MediaSync__CONFIG.get('MONITOR_PATH'))
        logger.info('同步db中的115生活事件到本地-执行完成')
        return None
        return None

    def __process_delete_file(self, item):
        item_db = self._cloud_data_op.get_by_fid(item['file_id'])
        if item_db is None:
            return
        self._MediaSync__process_delete_file_impl(item_db)
    
    def __process_delete_file_impl(self, item_db):
        self.delete_local_file(item_db)
        self._cloud_data_op.delete_by_fid(item_db)
        logger.info(f'''文件删除-执行成功-{item_db.name}''')
        return None
        return None

    
    def delete_file_by_ids(self, ids):
        _var_var_6 = self._cloud_data_op.get_by_ids(ids)
        for _var_var_7 in _var_var_6:
            self.__process_delete_file_impl(_var_var_7)
        return None
        return None

    
    def delete_local_file(self, item_db):
        self.add_sync_path(item_db.local_path)
        if item_db.is_dir:
            if del_path(join_local_paths(item_db.local_path, item_db.name)):
                logger.info(f'''删除本地文件夹-成功-{item_db.name}''')
            return None
        if item_db.suffix in self._MediaSync__VIDEO_SUFFIX:
            _var_var_8 = join_local_paths(item_db.local_path, item_db.name)
            _var_var_9 = change_file_suffix(_var_var_8, 'strm')
            _var_var_10 = change_file_suffix(_var_var_8, 'nfo')
            _var_var_11 = get_thumb_name(_var_var_8)
            if del_path(_var_var_9):
                logger.info(f'''删除本地strm-成功-{_var_var_9}''')
            if del_path(_var_var_10):
                logger.info(f'''删除本地nfo-成功-{_var_var_10}''')
            if del_path(_var_var_11):
                logger.info(f'''删除本地缩略图-成功-{_var_var_11}''')
            elif del_path(join_local_paths(item_db.local_path, item_db.name)):
                logger.info(f'''删除本地{item_db.suffix}-成功-{item_db.local_path}''')
        return None
        return None

    def __process_folder_rename(self, item):
        item_db = self._cloud_data_op.get_by_fid(item['file_id'])
        if item_db is None:
            return
        update_time = int(item['update_time'])
        if update_time <= item_db.f_modify_time:
            return
        item_db.f_modify_time = update_time
        old_name = item_db.name
        new_name = item['file_name']
        if item['file_name'] != old_name:
            rename(join_local_paths(item_db.local_path, old_name), join_local_paths(item_db.local_path, new_name))
            logger.info(f'文件夹重命名-执行重命名-{old_name}->{new_name}')
            self.add_sync_path(item_db.local_path)
        else:
            logger.info(f'文件夹重命名-无需同步-{old_name}->{new_name}')
            return
        logger.info(f'文件夹重命名-删除旧记录-{old_name}->{new_name}')
        self._cloud_data_op.delete_by_fid(item_db)
        parent_db = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not parent_db:
            logger.info(f"文件夹重命名-结束-非监控文件夹-{item['parent_id']}-{item.get('parent_name')}")
            return
        folder_db = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=parent_db.fid, p_name=parent_db.name, pick_code=item['pick_code'], is_dir=1, status=1)
        logger.info(f'文件夹重命名-同步新名称-{old_name}->{new_name}')
        self.sync_folder_to_local(folder_db, parent_db)
    def __process_rename_file(self, item):
        item_db = self._cloud_data_op.get_by_fid(item['file_id'])
        if item_db is None:
            return
        update_time = int(item['update_time'])
        if update_time <= item_db.f_modify_time:
            return
        item_db.f_modify_time = update_time
        old_name = item_db.name
        new_name = item['file_name']
        if item['file_name'] == old_name:
            logger.info(f'文件重命名-无需同步-{old_name}->{new_name}')
            return
        logger.info(f'文件重命名-删除旧记录-{old_name}->{new_name}')
        self.delete_local_file(item_db)
        self._cloud_data_op.delete_cloud(item_db)
        parent_db = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not parent_db:
            logger.info(f"文件重命名-结束-非监控文件夹-{item['parent_id']}-{item.get('parent_name')}")
            return
        file_db = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=item['parent_id'], p_name=parent_db.name, full_y_path=join_cloud_paths(parent_db.full_y_path, item['file_name']), pick_code=item['pick_code'], sha1=item['sha1'], size=item['file_size'], suffix=item['ico'], is_dir=0, status=1)
        if item.get('thumb_l'):
            file_db.thumb = item['thumb_l'].replace('_100?', '_0?')
        thumb = item.get('thumb')
        if thumb and thumb.startswith('?'):
            file_db.thumb = f"""https://imgjump.115.com{thumb}&size=0&sha1={item.get('sha1', '')}"""
        logger.info(f'文件重命名-同步新名称-{old_name}->{new_name}')
        self.sync_file_to_local(file_db, parent_db)
    def __process_copy_folder(self, item):
        _var_var_15 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_15 or item['sha1']:
            logger.info(f'文件夹复制-结束-移动到非监控文件夹-{item["parent_id"]}-{item.get("parent_name")}')
            return
        _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=_var_var_15.fid, p_name=_var_var_15.name, pick_code=item['pick_code'], is_dir=1, status=1)
        self.sync_folder_to_local(_var_var_16, _var_var_15)
    def __process_copy_file(self, item):
        _var_var_15 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_15:
            return
        logger.info(f'文件复制-执行同步-{item["file_name"]}')
        _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=item['parent_id'], p_name=_var_var_15.name, full_y_path=join_cloud_paths(_var_var_15.full_y_path, item['file_name']), pick_code=item['pick_code'], sha1=item['sha1'], size=item['file_size'], suffix=item['ico'], is_dir=0, status=1)
        if item.get('thumb_l'):
            _var_var_16.thumb = item['thumb_l'].replace('_100?', '_0?')
        _var_var_11 = item.get('thumb')
        if _var_var_11 and _var_var_11.startswith('?'):
            _var_var_16.thumb = f'https://imgjump.115.com{_var_var_11}&size=0&sha1={item.get("sha1", "")}'
        self.sync_file_to_local(_var_var_16, _var_var_15)
    def __process_receive_files(self, item):
        _var_var_17 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_17:
            logger.info(f'文件接收-结束-非监控文件夹-{item["parent_id"]}-{item.get("parent_name")}')
            return
        _var_var_4 = self._cloud_data_op.get_by_fid(item['file_id'])
        if _var_var_4:
            logger.info('文件接收-结束-重复同步')
            return
        logger.info(f'文件接收-执行同步-{item["file_name"]}')
        _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=item['parent_id'], p_name=_var_var_17.name, full_y_path=join_cloud_paths(_var_var_17.full_y_path, item['file_name']), pick_code=item['pick_code'], status=1)
        if item['sha1']:
            _var_var_16.sha1 = item['sha1']
            _var_var_16.size = item['file_size']
            _var_var_16.suffix = item['ico']
            _var_var_16.is_dir = 0
            if item.get('thumb_l'):
                _var_var_16.thumb = item['thumb_l'].replace('_100?', '_0?')
            self.sync_file_to_local(_var_var_16, _var_var_17)
        else:
            _var_var_16.is_dir = 1
            self.sync_folder_to_local(_var_var_16, _var_var_17)
    def __process_new_folder(self, item):
        _var_var_15 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_15:
            logger.info(f'文件夹创建-结束-非监控文件夹-{item["parent_id"]}-{item.get("parent_name")}')
            return
        _var_var_18 = self._cloud_data_op.get_by_fid(item['file_id'])
        if _var_var_18:
            logger.info(f'文件夹创建-结束-无需重复创建-{item["file_id"]}-{item.get("file_name")}')
            return
        _var_var_19 = join_local_paths(_var_var_15.local_path, _var_var_15.name, item['file_name'])
        os.makedirs(_var_var_19, exist_ok=True)
        _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=_var_var_15.fid, p_name=_var_var_15.name, full_y_path=join_cloud_paths(_var_var_15.full_y_path, item['file_name']), pick_code=item['pick_code'], local_path=join_local_paths(_var_var_15.local_path, _var_var_15.name), local_name=item['file_name'], action=ActionEnum.DIR.name, is_dir=1, status=1)
        self._cloud_data_op.save(_var_var_16)
        logger.info(f'文件夹创建-成功-{item["file_id"]}-{_var_var_19}')
    def __process_move_file(self, item):
        _var_var_4 = self._cloud_data_op.get_by_fid(item['file_id'])
        _var_var_20 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_20 and not _var_var_4:
            return
        if _var_var_4:
            logger.info(f'文件移动-删除旧的-{item["file_name"]}')
            self.__process_delete_file_impl(_var_var_4)
        if _var_var_20:
            logger.info(f'文件移动-执行同步-{item["file_name"]}')
            _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=item['parent_id'], p_name=_var_var_20.name, full_y_path=join_cloud_paths(_var_var_20.full_y_path, item['file_name']), pick_code=item['pick_code'], status=1)
            if item['sha1']:
                _var_var_16.sha1 = item['sha1']
                _var_var_16.size = item['file_size']
                _var_var_16.suffix = item['ico']
                _var_var_16.is_dir = 0
                if item.get('thumb_l'):
                    _var_var_16.thumb = item['thumb_l'].replace('_100?', '_0?')
                self.sync_file_to_local(_var_var_16, _var_var_20)
            else:
                _var_var_16.is_dir = 1
                self.sync_folder_to_local(_var_var_16, _var_var_20)
    def __process_upload_file(self, item):
        _var_var_15 = self._cloud_data_op.get_by_fid(item['parent_id'])
        if not _var_var_15:
            return
        logger.info(f'文件上传-执行同步-{item["file_name"]}')
        _var_var_16 = CloudData(fid=item['file_id'], name=item['file_name'], f_modify_time=item['update_time'], pid=item['parent_id'], p_name=_var_var_15.name, full_y_path=join_cloud_paths(_var_var_15.full_y_path, item['file_name']), pick_code=item['pick_code'], sha1=item['sha1'], size=item['file_size'], suffix=item['ico'], is_dir=0, status=1)
        if not item['sha1']:
            _var_var_16.is_dir = 1
        if item.get('thumb_l'):
            _var_var_16.thumb = item['thumb_l'].replace('_100?', '_0?')
        if _var_var_16.is_dir:
            self.sync_folder_to_local(_var_var_16, _var_var_15)
        else:
            self.sync_file_to_local(_var_var_16, _var_var_15)
    
    def sync_file_to_local(self, ycd, folder_item):
        suffix = ycd.suffix
        folder_local_path = join_local_paths(folder_item.local_path, folder_item.name)
        local_name = ycd.name
        item_db = self._cloud_data_op.get_by_fid(ycd.fid)
        if item_db and item_db.name != ycd.name:
            self.delete_local_file(item_db)
        if suffix in self._MediaSync__VIDEO_SUFFIX:
            action = ActionEnum.STRM.name
            local_name = change_file_suffix(local_name, 'strm')
            local_path = join_local_paths(folder_local_path, local_name)
            if suffix not in self._MediaSync__MUSIC_SUFFIX and int(ycd.size) < self._media_min_size:
                logger.info(f'视频小于{self._media_min_size_mb}，跳过同步-{ycd.name}')
                return
            if self._MediaSync__CONFIG['strm']['STRM_EXIST_IS_REBUILD'] or not os.path.exists(local_path):
                create_strm_file(local_path, self.build_direct(ycd.pick_code, ycd.name, ycd.suffix, ycd.sha1, ycd.size))
                self.add_sync_path(folder_local_path)
                self._msg_strm_count += 1
                logger.info(f'strm文件创建-成功-{ycd.name}')
            else:
                logger.info(f'strm文件创建-跳过-已存在-{ycd.name}')
        elif suffix in self._MediaSync__IMAGE_SUFFIX or suffix in self._MediaSync__MEDIA_DATA_SUFFIX:
            action = ActionEnum.DOWN.name
            local_path = join_local_paths(folder_local_path, local_name)
            try:
                if (item_db is None and not os.path.exists(local_path)) or (item_db and int(ycd.f_modify_time) > int(item_db.sync_time)) or (os.path.exists(local_path) and os.path.getsize(local_path) < 1024):
                    if ycd.thumb:
                        action = ActionEnum.IMG.name
                        if config2Env.image_download_strategy == 'cdn':
                            self._MediaSync__img_down_thread.submit(Mutil.download_file_v2, ycd.thumb, local_path)
                            logger.info(f'提交图片下载任务成功：{local_path}')
                        else:
                            self._m115.download_pick_code(ycd.pick_code, local_path)
                            logger.info(f'下载{suffix}文件成功-{ycd.name}')
                    else:
                        self._m115.download_pick_code(ycd.pick_code, local_path)
                        logger.info(f'下载{suffix}文件成功-{ycd.name}')
                    if suffix in self._MediaSync__IMAGE_SUFFIX:
                        self._msg_img_success_count += 1
                    else:
                        self._msg_nfo_success_count += 1
                else:
                    logger.info(f'跳过已同步的文件-{ycd.name}')
            except Exception as e:
                logger.exception(e)
                if item_db:
                    self._cloud_data_op.delete_cloud(item_db)
                    logger.info(f'删掉下载异常的数据-{ycd.name}')
        else:
            logger.info(f'跳过{suffix}后缀的文件-{ycd.name}')
            return
        if not item_db:
            ycd.local_name = local_name
            ycd.local_path = folder_local_path
            ycd.action = action
            ycd.desc = '同步成功'
            self._cloud_data_op.save(ycd)
        else:
            item_db.fid = ycd.fid
            item_db.name = ycd.name
            item_db.f_modify_time = ycd.f_modify_time
            item_db.full_y_path = ycd.full_y_path
            item_db.thumb = ycd.thumb
            item_db.local_name = local_name
            item_db.local_path = folder_local_path
            item_db.action = action
            item_db.desc = '同步成功'
            self._cloud_data_op.update_cloud(item_db)
    def sync_folder_to_local(self, ycd, folder_item):
        item_db = self._cloud_data_op.get_by_fid(ycd.fid)
        if not ycd.local_path and folder_item:
            ycd.local_path = join_local_paths(folder_item.local_path, folder_item.name)
        if not ycd.full_y_path and folder_item:
            ycd.full_y_path = join_cloud_paths(folder_item.full_y_path, ycd.name)
        if item_db is None:
            ycd.action = ActionEnum.SYNC.name
            ycd.desc = '创建文件夹成功'
            ycd.local_name = ycd.name
            ycd = self._cloud_data_op.save(ycd)
            logger.info(f'保存文件夹成功-{ycd.name}')
        else:
            item_db.name = ycd.name
            item_db.f_modify_time = ycd.f_modify_time
            item_db.pid = ycd.pid
            item_db.p_name = ycd.p_name
            if not ycd.full_y_path:
                item_db.full_y_path = ycd.full_y_path
            if not ycd.local_path:
                item_db.local_path = ycd.local_path
            item_db.action = ActionEnum.SYNC.name
            item_db.desc = '同步文件夹成功'
            ycd = self._cloud_data_op.update_cloud(item_db)
        for sub_item in self.fs_115_files(ycd.fid):
            if sub_item.is_dir:
                self.sync_folder_to_local(sub_item, ycd)
            else:
                self.sync_file_to_local(sub_item, ycd)
    def fs_115_files(self, cid):
        _var_var_29 = 1150
        _var_var_30 = {
            'offset': 0,
            'limit': _var_var_29,
            'cid': cid }
        _var_var_31 = []
        _var_var_32 = 0
        while _var_var_32 < 1:
            try:
                _var_var_33 = self._m115.fs_files_app(_var_var_30, self._MediaSync__CONFIG['basic'].get('API_WAIT_TIME'))
                if len(_var_var_33['paths']) == 1:
                    logger.error(f'''获取文件夹内容失败，当前文件夹已删除，cid={cid}''')
                    return []
            except Exception as _var_var_26:
                logger.error('接口列表请求异常')
                logger.exception(_var_var_26)
                _var_var_32 += 1
                continue
            _var_var_34 = ''
            for _var_var_7 in _var_var_33['paths']:
                if _var_var_7['fid'] == 0 or _var_var_7['name'] == '根目录':
                    continue
                _var_var_34 = f'''{_var_var_34}/{_var_var_7['name']}'''
            for _var_var_7 in _var_var_33['data']:
                if _var_var_7['is_dir']:
                    _var_var_35 = CloudData(fid=_var_var_7['fid'], name=_var_var_7['name'], f_modify_time=_var_var_7['update_time'], pid=_var_var_7['pid'], p_name=_var_var_7['p_name'], full_y_path=_var_var_34 + '/' + _var_var_7['name'], pick_code=_var_var_7['pick_code'], is_dir=1)
                else:
                    _var_var_35 = CloudData(fid=_var_var_7['fid'], name=_var_var_7['name'], f_modify_time=_var_var_7['update_time'], pid=_var_var_7['pid'], p_name=_var_var_7['p_name'], full_y_path=_var_var_34 + '/' + _var_var_7['name'], pick_code=_var_var_7['pick_code'], sha1=_var_var_7['sha1'], size=_var_var_7['size'], thumb=_var_var_7['thumb'], is_dir=0, suffix=_var_var_7['ico'])
                _var_var_31.append(_var_var_35)
            if _var_var_33['offset'] + _var_var_33['limit'] >= _var_var_33['count']:
                break
            _var_var_30['offset'] += _var_var_29
        return _var_var_31

    def full_sync(self, cid, local_path):
        self._media_img_monitor.stop()
        _var_var_16 = self.get_root_folder(cid, local_path)
        if not _var_var_16:
            return
        self.sync_folder_to_local(_var_var_16, _var_var_16)
        self.__img_down_thread.wait_for_all_tasks()
        self._media_img_monitor.start(self.__CONFIG.get('MONITOR_PATH'))
        self.send_sync_result_msg()
    def fast_sync(self, cid, local_path, sync_type):
        self._media_img_monitor.stop()
        self.fast_sync_folder_to_local_kk(cid, local_path, sync_type)
        self.__img_down_thread.wait_for_all_tasks()
        self._media_img_monitor.start(self.__CONFIG.get('MONITOR_PATH'))
        self.send_sync_result_msg()
    
    def save_video(self, cid, local_path, item):
        _var_var_36 = False
        if item['ico'] not in self._MediaSync__MUSIC_SUFFIX and int(item['size']) < self._media_min_size:
            logger.info(f'''视频小于{self._media_min_size_mb}，跳过同步-{item['name']}''')
            return None
        if item['ico'] not in self._MediaSync__VIDEO_SUFFIX:
            logger.info(f'''非媒体文件后缀{item['ico']}，跳过同步-{item['name']}''')
            return None
        for _var_var_37 in item['ancestors']:
            if _var_var_37['id'] == item['id']:
                continue
            if _var_var_37['id'] == int(cid):
                _var_var_36 = True
            if _var_var_37['id'] in self._batch_dir_items:
                continue
            _var_var_37['is_add'] = _var_var_36
            _var_var_37['local_path'] = Mutil.get_dirname(Mutil.merge_paths(local_path, _var_var_37['path']))
            _var_var_37['local_name'] = _var_var_37['name']
            _var_var_37['status'] = 1
            self._batch_dir_items[_var_var_37['id']] = _var_var_37
        if self._MediaSync__CONFIG['strm']['STRM_EXIST_IS_REBUILD'] or not Mutil.is_exists(Mutil.merge_paths(item['local_path'], item['local_name'])):
            Mutil.create_strm_file(item['local_path'], item['local_name'], self.build_direct(item['pick_code'] or item['pickcode'], item['name'], item['ico'], item['sha1'], item['size']))
            self.add_sync_path(item['local_path'])
            self._msg_strm_count += 1
            logger.info(f'''strm文件创建-成功-{item['local_name']}''')
        self._batch_items.append(item)
        if len(self._batch_items) >= self._batch_size:
            self._cloud_data_op.bulk_insert_file(self._batch_items)
            self._batch_items.clear()
        if len(self._batch_dir_items) >= self._batch_size:
            self._cloud_data_op.bulk_insert_dir(self._batch_dir_items)
            self._batch_dir_items.clear()
        return None
        return None

    
    def save_file(self, cid, item):
        if item.get('action', ActionEnum.UNKNOWN.name) == ActionEnum.STRM.name:
            if self._MediaSync__CONFIG['strm']['STRM_EXIST_IS_REBUILD'] or not Mutil.is_exists(Mutil.merge_paths(item['local_path'], item['local_name'])):
                Mutil.create_strm_file(item['local_path'], item['local_name'], self.build_direct(item.get('pick_code') or item.get('pickcode'), item['name'], item['ico'], item['sha1'], item['size']))
                self.add_sync_path(item['local_path'])
                self._msg_strm_count += 1
                logger.info(f'''strm文件创建-成功-{item['local_name']}''')
        self._batch_items.append(item)
        if len(self._batch_items) >= self._batch_size:
            self._cloud_data_op.bulk_insert_file(self._batch_items)
            self._batch_items.clear()
        return None

    
    def fast_sync_folder_to_local_kk(self, cid, local_path, sync_type):
        _var_var_39 = []
        _var_var_40 = []
        _var_var_41 = []
        if 'video' in sync_type:
            _var_var_39 = self._MediaSync__VIDEO_SUFFIX
        if 'media_data' in sync_type and configEnv.media_data_suffix:
            _var_var_41 = self._MediaSync__MEDIA_DATA_SUFFIX
        if 'image' in sync_type and configEnv.image_suffix:
            _var_var_40 = self._MediaSync__IMAGE_SUFFIX
        self._m115.iter_files_with_path_kk(cid, _var_var_39, _var_var_40, _var_var_41, local_path, self.save_file)
        self._cloud_data_op.bulk_insert_file(self._batch_items)
        self._batch_items.clear()
        if 'image' in sync_type and configEnv.image_suffix:
            if config2Env.image_download_strategy == 'cdn':
                logger.info('图片下载策略为CDN...')
                self.down_img()
            else:
                logger.info('图片下载策略为接口下载...')
                self.down_nfo(ActionEnum.IMG.name)
        if 'media_data' in sync_type and configEnv.media_data_suffix:
            self.down_nfo()
        return None
        return None

    
    def down_img(self):
        _var_var_42 = 1000
        while True:
            _var_var_43 = []
            logger.info('开始下载图片文件...')
            _var_var_44 = self._cloud_data_op.list_page({
                'page': 1,
                'page_size': _var_var_42,
                'action': ActionEnum.IMG.name,
                'status': 0 })
            if _var_var_44['total'] == 0 or not _var_var_44['data']:
                break
            for _var_var_7 in _var_var_44['data']:
                _var_var_45 = _var_var_7.thumb
                _var_var_46 = _var_var_45.split('&t=')[1].split('&')[0]
                _var_var_47 = int(time.time() + 300)
                if int(_var_var_46) < _var_var_47:
                    logger.info(f'''图片CDN已过期-{_var_var_7.name}''')
                    _var_var_7.status = 2
                    _var_var_7.desc = '图片CDN已过期'
                    _var_var_43.append(_var_var_7)
                    logger.info(f'''图片CDN已过期-{_var_var_7.name}''')
                    self._msg_img_fail_count += 1
                    continue
                _var_var_48 = self._cloud_data_op.get_by_fid(_var_var_7.pid)
                if not _var_var_48:
                    _var_var_7.status = 3
                    _var_var_7.desc = '父文件夹不存在'
                    _var_var_43.append(_var_var_7)
                    logger.info(f'''父文件夹不存在-{_var_var_7.name}''')
                    self._msg_img_fail_count += 1
                    continue
                _var_var_49 = Mutil.merge_paths(_var_var_48.local_path, _var_var_48.local_name)
                _var_var_25 = Mutil.merge_paths(_var_var_49, _var_var_7.name)
                if self._MediaSync__CONFIG['strm']['STRM_EXIST_IS_REBUILD'] or not Mutil.is_exists(_var_var_25) or os.path.getsize(_var_var_25) < 1024:
                    self._MediaSync__img_down_thread.submit(Mutil.download_file_v2, _var_var_45, _var_var_25)
                    self._msg_img_success_count += 1
                    logger.info(f'''提交图片下载任务成功：{_var_var_25}''')
                _var_var_7.status = 1
                _var_var_7.p_name = _var_var_48.name
                _var_var_7.full_y_path = Mutil.merge_paths(_var_var_48.full_y_path, _var_var_7.name)
                _var_var_7.local_path = _var_var_49
                _var_var_7.local_name = _var_var_7.name
                _var_var_43.append(_var_var_7)
            self._cloud_data_op.bulk_update_cloud(_var_var_43)
            if int(_var_var_44['total']) <= _var_var_42:
                break
        logger.info(f'''媒体图片同步完成，成功：{self._msg_img_success_count}，失败：{self._msg_img_fail_count}''')
        return None

    
    def down_nfo(self, action):
        _var_var_42 = 1000
        while True:
            logger.info('开始下载...')
            _var_var_44 = self._cloud_data_op.list_page({
                'page': 1,
                'page_size': _var_var_42,
                'action': action,
                'status': 0 })
            if _var_var_44['total'] == 0 or not _var_var_44['data']:
                break
            for _var_var_7 in _var_var_44['data']:
                _var_var_48 = self._cloud_data_op.get_by_fid(_var_var_7.pid)
                if not _var_var_48:
                    _var_var_7.status = 3
                    _var_var_7.desc = '父文件夹不存在'
                    self._cloud_data_op.update_data(_var_var_7)
                    logger.info(f'''父文件夹不存在-{_var_var_7.name}''')
                    self._msg_nfo_fail_count += 1
                    continue
                _var_var_49 = Mutil.merge_paths(_var_var_48.local_path, _var_var_48.local_name)
                _var_var_25 = Mutil.merge_paths(_var_var_49, _var_var_7.name)
                if self._MediaSync__CONFIG['strm']['STRM_EXIST_IS_REBUILD'] or not Mutil.is_exists(_var_var_25) or os.path.getsize(_var_var_25) < 1024:
                    self._m115.download_pick_code(_var_var_7.pick_code, _var_var_25)
                    self._msg_nfo_success_count += 1
                    logger.info(f'''下载{_var_var_7.suffix}文件成功：{_var_var_25}''')
                _var_var_7.status = 1
                _var_var_7.p_name = _var_var_48.name
                _var_var_7.full_y_path = Mutil.merge_paths(_var_var_48.full_y_path, _var_var_7.name)
                _var_var_7.local_path = _var_var_49
                _var_var_7.local_name = _var_var_7.name
                self._cloud_data_op.update_data(_var_var_7)
            if int(_var_var_44['total']) <= _var_var_42:
                break
        logger.info(f'''媒体数据同步完成，成功：{self._msg_nfo_success_count}，失败：{self._msg_nfo_fail_count}''')
        return None

    
    def get_root_folder(self, cid, local_path):
        _var_var_16 = self._cloud_data_op.get_by_fid(cid)
        if _var_var_16:
            return _var_var_16
        _var_var_30 = {
            'offset': 0,
            'limit': 1,
            'cid': cid }
        try:
            _var_var_33 = self._m115.fs_files_app(_var_var_30, self._MediaSync__CONFIG['basic'].get('API_WAIT_TIME'))
            if len(_var_var_33['paths']) == 1:
                logger.error(f'''获取文件夹信息失败，请检查文件夹ID是否正确 - {cid}''')
                return None
        except Exception as _var_var_26:
            logger.error('接口列表请求异常')
            logger.exception(_var_var_26)
            return None
        _var_var_34 = ''
        for _var_var_7 in _var_var_33['paths']:
            if _var_var_7['fid'] == 0 or _var_var_7['name'] == '根目录':
                continue
            _var_var_34 = f'''{_var_var_34}/{_var_var_7['name']}'''
        _var_var_16 = CloudData(fid = _var_var_33['paths'][-1]['fid'], name = _var_var_33['paths'][-1]['name'], f_modify_time = int(time.time()), pid = _var_var_33['paths'][-2]['fid'], p_name = _var_var_33['paths'][-2]['name'], full_y_path = _var_var_34, local_path = Mutil.get_dirname(Mutil.merge_paths(local_path, _var_var_34)), is_dir = 1, status = 1)
        return _var_var_16

    
    def get_root_folder_old(self, cid, local_path):
        _var_var_16 = self._cloud_data_op.get_by_fid(cid)
        if _var_var_16:
            return _var_var_16
        _var_var_7 = self._m115.fs_category_get(cid)
        if _var_var_7['sha1'] != '':
            return None
        _var_var_34 = ''
        for _var_var_50 in _var_var_7['paths']:
            if _var_var_50['file_name'] == '根目录' or _var_var_50['file_id'] == 0:
                continue
            _var_var_34 = f'''{_var_var_34}/{_var_var_50['file_name']}'''
        _var_var_51 = _var_var_7['paths'][-1]['file_id']
        _var_var_52 = _var_var_7['paths'][-1]['file_name']
        _var_var_16 = CloudData(fid = cid, name = _var_var_7['file_name'], f_modify_time = _var_var_7['utime'], pid = _var_var_51, p_name = _var_var_52, pick_code = _var_var_7['pick_code'], full_y_path = _var_var_34 + '/' + _var_var_7['file_name'], local_path = local_path, is_dir = 1, status = 1)
        return _var_var_16
        return None

    
    def build_direct(self, pick_code, name, suffix, sha1, size):
        _var_var_45 = f'''{self._MediaSync__CONFIG['strm'].get('DIRECT_115_302_DOMAIN', 'http://172.17.0.1:9527')}/d/{pick_code}'''
        if config2Env.keep_suffix:
            _var_var_45 = f'''{_var_var_45}.{suffix}'''
        if self._MediaSync__CONFIG['strm']['STRM_TYPE'] == 'pick_code_name':
            _var_var_45 = f'''{_var_var_45}?/{name}'''
        return _var_var_45
        return None

    
    def refresh_emby_library(self):
        if not self._sync_path_set or configEnv.emby_refresh_status:
            self._sync_path_set.clear()
            return None
        logger.info(f'''转换路径之前-{self._sync_path_set}''')
        _var_var_53 = list(set(self._sync_path_set))
        _var_var_54 = []
        for _var_var_38 in _var_var_53:
            if configEnv.emby_path_replace_rule:
                _var_var_55 = configEnv.emby_path_replace_rule.split('#')
                if len(_var_var_55) == 2:
                    _var_var_38 = _var_var_38.replace(_var_var_55[0], _var_var_55[1], 1)
            if configEnv.emby_path_style == 'windows':
                _var_var_38 = _var_var_38.replace('/', '\\')
            elif configEnv.emby_path_style == 'unix':
                _var_var_38 = _var_var_38.replace('\\', '/')
            _var_var_54.append(_var_var_38)
        logger.info(f'''转换路径之后-{_var_var_54}''')
        self._emby_api.refresh_libraries_by_paths(_var_var_54)
        self._sync_path_set.clear()
        return None
        return None

    
    def send_sync_result_msg(self):
        _var_var_56 = ''
        _var_var_57 = False
        if self._msg_strm_count > 0:
            _var_var_56 = f'''{_var_var_56}\n视频STRM：{self._msg_strm_count} 个'''
            _var_var_57 = True
        if self._msg_img_success_count > 0:
            _var_var_56 = f'''{_var_var_56}\n媒体图片：{self._msg_img_success_count} 个'''
            _var_var_57 = True
        if self._msg_nfo_success_count > 0:
            _var_var_56 = f'''{_var_var_56}\n媒体数据：{self._msg_nfo_success_count} 个'''
            _var_var_57 = True
        if _var_var_57:
            self._message.send_msg(title = '🌟CMS同步结果🌟', text = _var_var_56.strip('\n'))
        self._msg_strm_count = 0
        self._msg_img_success_count = 0
        self._msg_img_fail_count = 0
        self._msg_nfo_success_count = 0
        self._msg_nfo_fail_count = 0
        return None
        return None

