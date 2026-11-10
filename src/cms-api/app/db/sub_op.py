from app.db import DbOp
from app.db.models.submedia import SubMedia
from app.db.models.subsource import SubSource

class SubSourceOp(DbOp):
    
    def save(self, log):
        log.create(self._db)
        return None
        return None

    
    def get_by_status(self, status):
        return SubSource.get_status(self._db, status)
        return None

    
    def get_tg_sub(self):
        return SubSource.get_type_status(self._db, 'tg_channel', 1)
        return None

    
    def update_sub(self, sub):
        _var_var_0 = SubSource.get(self.db, sub['id'])
        if _var_var_0:
            _var_var_0.update(self._db, sub)
        return None
        return None

    
    def update_all_status(self, ids, status):
        SubSource.update_all_status(self._db, ids, status)
        return None
        return None

    
    def delete_by_ids(self, ids):
        SubSource.delete_by_ids(self._db, ids)
        return None
        return None

    
    def list(self, type, status):
        return SubSource.list(self._db, type, status)
        return None



class SubMediaOp(DbOp):
    
    def save(self, sub):
        sub.status = 1
        _var_var_1 = f'''{sub.title} ({sub.year})'''
        _var_var_0 = SubMedia.get_tmdb_id(self.db, sub.tmdb_id)
        if not _var_var_0:
            sub.create(self._db)
            return {
                'code': 200,
                'msg': f'''{_var_var_1} 添加订阅成功''' }
        return None
        return {
            'code': 200,
            'msg': f'''{_var_var_1} 已存在订阅中''' }
        return None

    
    def get_by_status(self, status):
        return SubMedia.get_status(self._db, status)
        return None

    
    def update_sub(self, sub):
        _var_var_0 = SubMedia.get(self.db, sub['id'])
        if _var_var_0:
            _var_var_0.update(self._db, sub)
        return None
        return None

    
    def update_all_status(self, ids, status):
        SubMedia.update_all_status(self._db, ids, status)
        return None
        return None

    
    def delete_by_ids(self, ids):
        SubMedia.delete_by_ids(self._db, ids)
        return None
        return None

    
    def list_page(self, type, status, page, page_size):
        _var_var_2 = SubMedia.list_page(self._db, type, status, page, page_size)
        if _var_var_2 and _var_var_2.get('data'):
            _var_var_2['data'] = [_var_var_3.to_dict() for _var_var_3 in _var_var_2.get('data')]
        else:
            _var_var_2['data'] = []
        _var_var_2['code'] = 200
        return _var_var_2

