# File: base_mapper.py (Cleaned & Decompiled)
from typing import TypeVar, Generic, Union, List
from abc import ABC
import threading
import sqlite_utils
from app.types.Type import DatClass
from app.utils.mtime import TimeUtils

T = TypeVar('T', bound=DatClass)

class BaseMapper(Generic[T], ABC):
    """
    数据映射器基类，提供通用的数据库操作方法

    子类需要在 __init__ 方法中设置：
    - self.db_path: 数据库文件路径
    - self.table: 表名字符串
    """

    def __init__(self):
        self.db_path = None
        self.table = None
        self._local = threading.local()

    @property
    def db(self) -> sqlite_utils.Database:
        """
        获取当前线程的数据库连接
        每个线程都会有自己独立的数据库连接
        """
        if not hasattr(self._local, 'db') or self._local.db is None:
            if self.db_path is None:
                raise ValueError('db_path 未设置')
            self._local.db = sqlite_utils.Database(self.db_path)
        return self._local.db

    def insert_all(self, items: Union[T, List[T]]):
        """
        批量插入数据到数据库

        Args:
            items: 要插入的数据，可以是单个对象或对象列表
        """
        _var_var_0 = []
        if not isinstance(items, list):
            items = [items]
        for _var_var_1 in items:
            _var_var_1.updated_at = TimeUtils.get_current_time_str()
            _var_var_0.append(_var_var_1.to_dict(ignore_none=True))
        self.db[self.table].insert_all(_var_var_0, alter=True)