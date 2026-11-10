# File: user_op.py (Cleaned & Decompiled)
import hashlib
import random
import string
from app.db import DbOp
from app.db.models.cmsuser import NovaUser

class UserOp(DbOp):

    def login(self, username, password):
        """
        用户登录
        :param username: 用户名
        :param password: 密码
        :return: 是否登录成功
        """
        _var_var_0 = NovaUser.get_by_username(self._db, username)
        if _var_var_0:
            _var_var_1 = get_password_hash(password, _var_var_0.salt)
            if _var_var_0.password == _var_var_1:
                return _var_var_0
            return None
        return None

    def init_admin(self, username, password):
        """
        用户注册
        :param username: 用户名
        :param password: 密码
        """
        _var_var_2 = 'admin'
        _var_var_3 = generate_random_string()
        _var_var_1 = get_password_hash(password, _var_var_3)
        _var_var_0 = NovaUser.get_by_role(self._db, _var_var_2)
        if not _var_var_0:
            _var_var_0 = NovaUser(username=username, password=_var_var_1, salt=_var_var_3, role=_var_var_2)
            _var_var_0.create(self._db)
        else:
            _var_var_0.username = username
            _var_var_0.password = _var_var_1
            _var_var_0.salt = _var_var_3
            _var_var_0.update(self._db, _var_var_0.to_dict())
        return None

def get_password_hash(password, salt):
    """
    对密码进行加盐MD5加密
    """
    password = hashlib.md5((password + salt).encode()).hexdigest()
    return password

def generate_random_string():
    """
    生成随机8位字符串
    :return: 随机生成的8位字符串
    """
    _var_var_4 = string.ascii_letters + string.digits
    _var_var_5 = ''.join(random.choice(_var_var_4) for _ in range(8))
    return _var_var_5
