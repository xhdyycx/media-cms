import inspect
from types import FunctionType
from typing import Any, Callable

class ObjectUtils:
    @staticmethod
    def is_obj(obj: Any):
        if isinstance(obj, list) or isinstance(obj, dict) or isinstance(obj, tuple):
            return True
        if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, bool) or isinstance(obj, bytes):
            return False
        return str(obj).startswith('{') or str(obj).startswith('[')

    @staticmethod
    def arguments(func: Callable) -> int:
        """
        返回函数的参数个数
        """
        _var_var_0 = inspect.signature(func)
        _var_var_1 = _var_var_0.parameters
        return len(list(_var_var_1.keys()))
    @staticmethod
    def check_method(func: FunctionType) -> bool:
        """
        检查函数是否已实现
        """
        try:
            _var_var_2 = inspect.getsource(func)
            _var_var_3 = False
            for _var_var_4 in _var_var_2.split('\n'):
                _var_var_4 = _var_var_4.strip()
                if not _var_var_4:
                    continue
                if _var_var_4.startswith('"""') or _var_var_4.startswith("'''"):
                    _var_var_3 = not _var_var_3
                    continue
                if _var_var_3:
                    continue
                if _var_var_4.startswith('#'):
                    continue
                if _var_var_4 == 'pass':
                    continue
                if _var_var_4.startswith('@'):
                    continue
                if _var_var_4.startswith('def '):
                    continue
                return True
            return False
        except Exception as _var_var_5:
            print(str(_var_var_5))
            return func.__code__.co_code not in (b'd\x01S\x00', b'\x97\x00d\x00S\x00')
