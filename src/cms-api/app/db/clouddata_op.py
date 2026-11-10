import time
from datetime import datetime
import pytz
from app.core.env import novaEnv
from app.db import DbOp
from app.db.models.clouddata import CloudData
from app.log import logger
from app.schemas.types import ActionEnum
from app.utils.ko_util import is_media_dir

class CloudDataOp(DbOp):
    '''
    云盘数据操作
    '''
    
    def get_media_dir(self, pageNum, pageSize):
        return CloudData.get_media_dir(self._db, pageNum, pageSize)
        return None

    
    def get_by_fid(self, fid):
        return CloudData.get_by_fid(self._db, fid)
        return None

    
    def get_by_pid(self, pid):
        return CloudData.get_by_pid(self._db, pid)
        return None

    
    def get_video_by_pid(self, pid):
        return CloudData.get_video_by_pid(self._db, pid)
        return None

    
    def get_by_sha1(self, sha1):
        return CloudData.get_by_sha1(self._db, sha1)
        return None

    
    def get_by_pick_code(self, pick_code):
        return CloudData.get_by_pick_code(self._db, pick_code)
        return None

    
    def save(self, ycd):
        ycd.sync_time = int(time.time())
        if ycd.is_dir == 1 and is_media_dir(ycd.name):
            ycd.is_media_dir = 1
        ycd.create(self._db)
        return ycd
        return None

    
    def bulk_insert_file(self, items):
        if not items:
            return
        data_list = []
        sync_time = int(time.time())
        tz = pytz.timezone(novaEnv.TZ)
        time_str = datetime.fromtimestamp(sync_time, tz=tz).strftime('%Y-%m-%d %H:%M:%S')
        for item in items:
            is_dir = 0
            if item.get('is_dir'):
                is_dir = 1
            if is_dir == 1:
                logger.info(f'开始保存云盘文件夹, name={item["name"]}')
            else:
                logger.info(f'开始保存云盘文件, name={item["name"]}')
            pick_code = item.get('pickcode') or item.get('pick_code')
            path = item.get('path', '')
            dir_name = ''
            if path:
                dir_name = path.split('/')[-2]
                if not dir_name:
                    dir_name = '/'
            else:
                dir_name = item.get('dir_name', '')
            cd = CloudData(**{
                'fid': item['id'],
                'name': item['name'],
                'f_modify_time': item.get('utime') or sync_time,
                'pid': item['parent_id'],
                'p_name': dir_name,
                'full_y_path': path,
                'pick_code': pick_code,
                'sha1': item.get('sha1', ''),
                'size': item.get('size', ''),
                'suffix': item.get('ico', ''),
                'thumb': item.get('thumb', ''),
                'sync_time': sync_time,
                'is_dir': is_dir,
                'local_path': item.get('local_path', ''),
                'local_name': item.get('local_name', ''),
                'action': item.get('action', ActionEnum.UNKNOWN.name),
                'create_time': time_str,
                'last_update_time': time_str,
                'is_media_dir': 1 if is_media_dir(item['name']) else 0,
                'status': item.get('status', 0),
            })
            data_list.append(cd.to_dict())
        if len(data_list) > 0:
            CloudData.bulk_insert_file(self._db, data_list)
    def bulk_insert_dir(self, items):
        data_list = []
        sync_time = int(time.time())
        tz = pytz.timezone(novaEnv.TZ)
        time_str = datetime.fromtimestamp(sync_time, tz=tz).strftime('%Y-%m-%d %H:%M:%S')
        for fid in items.keys():
            item = items[fid]
            if not item['is_add']:
                continue
            cd = CloudData(**{
                'fid': item['id'],
                'name': item['name'],
                'f_modify_time': sync_time,
                'pid': item['parent_id'],
                'p_name': item['parent_name'],
                'full_y_path': item.get('path', ''),
                'sync_time': sync_time,
                'size': 0,
                'is_dir': 1,
                'local_path': item.get('local_path', ''),
                'local_name': item.get('local_name', ''),
                'action': ActionEnum.DIR.name,
                'create_time': time_str,
                'last_update_time': time_str,
                'is_media_dir': 1 if is_media_dir(item['name']) else 0,
                'status': item.get('status', 0),
            })
            data_list.append(cd.to_dict())
        if len(data_list) > 0:
            CloudData.bulk_insert_dir(self._db, data_list)
    def bulk_insert_dir_v2(self, items):
        data_list = []
        sync_time = int(time.time())
        tz = pytz.timezone(novaEnv.TZ)
        time_str = datetime.fromtimestamp(sync_time, tz=tz).strftime('%Y-%m-%d %H:%M:%S')
        for fid in items.keys():
            item = items[fid]
            if not item['is_add']:
                continue
            cd = CloudData(**{
                'fid': item['id'],
                'name': item['name'],
                'f_modify_time': sync_time,
                'pid': item['parent_id'],
                'p_name': item['parent_name'],
                'full_y_path': item.get('path', ''),
                'sync_time': sync_time,
                'size': 0,
                'is_dir': 1,
                'local_path': item.get('local_path', ''),
                'local_name': item.get('local_name', ''),
                'action': ActionEnum.DIR.name,
                'create_time': time_str,
                'last_update_time': time_str,
                'is_media_dir': 1 if is_media_dir(item['name']) else 0,
                'status': item.get('status', 0),
            })
            data_list.append(cd.to_dict())
        if len(data_list) > 0:
            CloudData.bulk_insert_dir(self._db, data_list)
    def delete_cloud(self, db_cd):
        CloudData.delete_cloud(self._db, db_cd)
        return None
        return None

    
    def delete_by_fid(self, db_cd):
        _var_var_11 = CloudData.get_dirs_by_pid(self._db, db_cd.fid)
        if _var_var_11:
            for _var_var_12 in _var_var_11:
                self.delete_by_fid(_var_var_12)
        CloudData.delete_by_pid(self._db, db_cd.fid)
        self.delete_cloud(db_cd)
        return None
        return None

    
    def update_cloud(self, db_cd):
        db_cd.sync_time = int(time.time())
        db_cd.update(self._db, db_cd.to_dict())
        return db_cd
        return None

    
    def update_data(self, db_cd):
        db_cd.update(self._db, db_cd.to_dict())
        return db_cd
        return None

    
    def update_by_id(self, db_cd):
        db_cd.sync_time = int(time.time())
        CloudData.get(self._db, db_cd.id).update(self._db, db_cd.to_dict())
        return None
        return None

    
    def get_by_pid_and_name(self, pid, name):
        return CloudData.get_by_pid_and_name(self._db, pid, name)
        return None

    
    def get_by_local_path(self, local_path, name):
        return CloudData.get_by_local_path(self._db, local_path, name)
        return None

    
    def get_by_dir_name(self, name):
        return CloudData.get_by_dir_name(self._db, name)
        return None

    
    def get_by_name_pid(self, name, pid):
        return CloudData.get_by_name_pid(self._db, name, pid)
        return None

    
    def list_dict_page(self, params):
        result = CloudData.list_page(self._db, params)
        if result and result.get('data'):
            result['data'] = [item.to_dict() for item in result.get('data')]
        else:
            result['data'] = []
        result['code'] = 200
        return result
    def list_page(self, params):
        return CloudData.list_page(self._db, params)
        return None

    
    def truncate(self):
        CloudData.clear(self._db)
        return None
        return None

    
    def delete_by_cds(self, cds):
        if not cds:
            return None
        return None
        for _var_var_12 in cds:
            self.delete_by_fid(_var_var_12)
        return None
        return None

    
    def get_by_ids(self, ids):
        if not ids:
            return []
        return None
        return CloudData.get_by_ids(self._db, ids)
        return None

    
    def bulk_update_cloud(self, cds):
        """
        批量更新云盘数据
        :param cds: CloudData对象列表，每个对象必须包含id、status字段
        """
        if not cds:
            return
        sync_time = int(time.time())
        tz = pytz.timezone(novaEnv.TZ)
        time_str = datetime.fromtimestamp(sync_time, tz=tz).strftime('%Y-%m-%d %H:%M:%S')
        for cd in cds:
            if cd.p_name is None:
                cd.p_name = ''
            if cd.full_y_path is None:
                cd.full_y_path = ''
            if cd.local_name is None:
                cd.local_name = ''
            if cd.local_path is None:
                cd.local_path = ''
            if cd.desc is None:
                cd.desc = ''
            cd.sync_time = sync_time
        CloudData.bulk_update_cloud(self._db, cds)
    def get_by_pcs(self, pcs):
        return CloudData.get_by_pcs(self._db, pcs)
        return None

    
    def get_by_pids(self, pids):
        return CloudData.get_by_pids(self._db, pids)
        return None



