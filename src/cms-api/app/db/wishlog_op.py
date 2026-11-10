from app.db import DbOp
from app.db.models.wishLog import WishLog

class WishLogOp(DbOp):
    
    def get_new_wish(self, num):
        return WishLog.get_new_wish(self._db, num)
        return None

    
    def get_by_status(self, status):
        return WishLog.get_by_status(self._db, status)
        return None

    
    def update_log(self, db_log):
        db_log.update(self._db, db_log.to_dict())
        return None
        return None



