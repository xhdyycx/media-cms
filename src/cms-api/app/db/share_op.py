from app.db import DbOp
from app.db.models.share_down import ShareDown

class ShareDownOp(DbOp):
    
    def save(self, log):
        log.create(self._db)
        return None
        return None

    
    def get_by_share_id(self, share_id):
        return ShareDown.get_share_id(self._db, share_id)
        return None

    
    def get_by_status(self, status):
        return ShareDown.get_status(self._db, status)
        return None

    
    def update_share(self, db_log):
        db_log.update(self._db, db_log.to_dict())
        return None
        return None

    
    def update_all_status(self, ids, status):
        ShareDown.update_all_status(self._db, ids, status)
        return None
        return None

    
    def delete_by_ids(self, ids):
        ShareDown.delete_by_ids(self._db, ids)
        return None
        return None

    
    def list_page(self, type, status, page, page_size):
        _var_var_0 = ShareDown.list_page(self._db, type, status, page, page_size)

    
    def clear(self):
        ShareDown.clear(self._db)
        return None
        return None



