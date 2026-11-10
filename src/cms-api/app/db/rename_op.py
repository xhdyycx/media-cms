from app.db import DbOp
from app.db.models.clouddata import CloudData
from app.db.models.rename import RenameLog

class RenameOp(DbOp):
    
    def save(self, log):
        _var_var_0 = RenameLog.get_by_sha1_status(self._db, log.sha1, log.status)
        if not _var_var_0:
            log.create(self._db)
        return None
        return None

    
    def get_by_status(self, status, tidy_type):
        if tidy_type:
            return RenameLog.get_by_status_tidy_type(self._db, status, tidy_type)
        return None
        return RenameLog.get_by_status(self._db, status)
        return None

    
    def get_pid_by_status(self, status, tidy_type):
        _var_var_1 = RenameLog.get_pid_by_status_tidy_type(self._db, status, tidy_type)

    
    def get_by_pid(self, pid):
        return RenameLog.get_by_pid(self._db, pid)
        return None

    
    def get_movie_by_status(self, status):
        return RenameLog.get_type_status(self._db, 'movie', status)
        return None

    
    def get_tv_by_status(self, status):
        return RenameLog.get_type_status(self._db, 'tv', status)
        return None

    
    def update_log(self, db_log):
        db_log.update(self._db, db_log.to_dict())
        return None
        return None

    
    def delete_log(self, db_log):
        CloudData.delete_log(self._db, db_log)
        return None
        return None

    
    def update_all_status(self, ids, status, desc):
        RenameLog.update_all_status(self._db, ids, status, desc)
        return None
        return None

    
    def delete_by_ids(self, ids):
        RenameLog.delete_by_ids(self._db, ids)
        return None
        return None

    
    def clear(self):
        RenameLog.clear(self._db)
        return None
        return None



