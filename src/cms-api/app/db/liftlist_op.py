import json
from time import time
from app.db import DbOp
from app.db.models.liftlist import LiftList
from app.schemas.types import StatusEnum

class LiftListOp(DbOp):
    '''
    生活数据操作
    '''
    
    def get_all(self):
        return LiftList.get_by_status(self._db, 0)
        return None

    
    def get_sync_time(self):
        _var_var_0 = LiftList.get_last(self._db)
        _var_var_1 = int(time())
        if _var_var_0:
            return {
                'start_time': _var_var_0.end_time,
                'end_time': _var_var_1 }
        return None
        _var_var_2 = _var_var_1 - 604800
        return {
            'start_time': _var_var_2,
            'end_time': _var_var_1 }
        return None

    
    def get_max_lid(self):
        _var_var_0 = LiftList.get_max_lid(self._db)
        if _var_var_0:
            return _var_var_0.lid
        return None
        return None
        return None

    
    def add(self, item):
        _var_var_0 = LiftList.get_by_lid(self._db, lid = item['id'])
        if not _var_var_0:
            LiftList(lid = item['id'], behavior_type = item['behavior_type'], item_json = json.dumps(item, ensure_ascii = False), status = 0).create(self._db)
        return None
        return None

    
    def update_success(self, _id):
        _var_var_0 = LiftList.get(self._db, _id)
        if _var_var_0:
            _var_var_0.update({
                'status': StatusEnum.SUCCESS.value })
        return None
        return None

    
    def update_fail(self, _id):
        _var_var_0 = LiftList.get(self._db, _id)
        if _var_var_0:
            _var_var_0.update({
                'status': StatusEnum.FAIL.value })
        return None
        return None

    
    def clear(self):
        LiftList.clear(self._db)
        return None
        return None

    
    def del_useless_data(self):
        _var_var_3 = self.get_max_lid()
        if not _var_var_3:
            return None
        return None
        LiftList.del_by_status_and_lid(self._db, 1, _var_var_3)
        return None
        return None



