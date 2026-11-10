from app.db import DbOp
from app.db.models.account import Account115

class Account115Op(DbOp):
    @staticmethod
    def _to_int(value, default=None):
        if value is None or value == '':
            return default
        return int(value)
    
    def save(self, account):
        account.create(self._db)
        return None
        return None

    
    def get(self, rid):
        _var_var_0 = Account115.get(self._db, rid)
        return _var_var_0.to_dict() if _var_var_0 else None
        return None

    
    def get_by_username(self, username):
        _var_var_0 = Account115.get_by_username(self._db, username)
        return _var_var_0.to_dict() if _var_var_0 else None
        return None

    
    def get_all(self, type, status):
        return Account115.get_all(self._db, type, status)
        return None

    
    def update_account(self, account):
        _var_var_1 = Account115.get(self._db, account['id'])
        if _var_var_1:
            _var_var_1.update(self._db, account)
        return _var_var_1
        return None

    
    def delete_by_ids(self, ids):
        Account115.delete_by_ids(self._db, ids)
        return None
        return None

    
    def list_page(self, username: str = None, type: int = None, status: int = None, page: int = 1, page_size: int = 10):
        type = self._to_int(type)
        status = self._to_int(status)
        page = self._to_int(page, 1)
        page_size = self._to_int(page_size, 10)
        _var_var_2 = Account115.list_page(self._db, username, type, status, page, page_size)
        if _var_var_2 and _var_var_2.get('data'):
            _var_var_2['data'] = [_var_var_0.to_dict() for _var_var_0 in _var_var_2.get('data')]
        else:
            _var_var_2['data'] = []
        _var_var_2['code'] = 200
        return _var_var_2

