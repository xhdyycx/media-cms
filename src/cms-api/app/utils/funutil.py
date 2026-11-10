import asyncio
import hashlib
import importlib.util as importlib
import inspect
import sys
from pathlib import Path
from types import ModuleType
from typing import Any
from app.log import logger

class FunUtil:
    '''动态执行指定 Python 文件中的方法。'''
    @staticmethod
    def _resolve_file_path(file_path):
        if not file_path:
            raise ValueError('file_path 不能为空')
        return Path(file_path).expanduser().resolve()

    @staticmethod
    def _load_module(file_path: str) -> ModuleType:
        _var_var_0 = FunUtil._resolve_file_path(file_path)
        _var_var_1 = hashlib.md5(str(_var_var_0).encode('utf-8')).hexdigest()
        _var_var_2 = f'funutil_dynamic_{_var_var_1}'
        _var_var_3 = importlib.util.spec_from_file_location(_var_var_2, str(_var_var_0))
        if _var_var_3 is None or _var_var_3.loader is None:
            raise ImportError(f'无法加载模块: {_var_var_0}')
        _var_var_4 = importlib.util.module_from_spec(_var_var_3)
        _var_var_5 = str(_var_var_0.parent)
        _var_var_6 = False
        if _var_var_5 not in sys.path:
            sys.path.insert(0, _var_var_5)
            _var_var_6 = True
        try:
            _var_var_3.loader.exec_module(_var_var_4)
        finally:
            if _var_var_6 and sys.path and sys.path[0] == _var_var_5:
                sys.path.pop(0)
        return _var_var_4
    @staticmethod
    def _get_callable(module: ModuleType, func_name: str):
        if not func_name:
            raise ValueError('func_name 不能为空')
        if '.' not in func_name:
            _var_var_7 = getattr(module, func_name, None)
            if _var_var_7 is None:
                raise AttributeError(f'方法不存在: {func_name}')
            if not callable(_var_var_7):
                raise TypeError(f'目标不是可调用对象: {func_name}')
            return _var_var_7
        _var_var_8, _var_var_9 = func_name.split('.', 1)
        _var_var_10 = getattr(module, _var_var_8, None)
        if _var_var_10 is None:
            raise AttributeError(f'类不存在: {_var_var_8}')
        if not inspect.isclass(_var_var_10):
            raise TypeError(f'目标不是类: {_var_var_8}')
        _var_var_11 = getattr(_var_var_10, _var_var_9, None)
        if _var_var_11 is None:
            raise AttributeError(f'方法不存在: {func_name}')
        if not callable(_var_var_11):
            raise TypeError(f'目标不是可调用对象: {func_name}')
        try:
            _var_var_12 = _var_var_10()
            return getattr(_var_var_12, _var_var_9)
        except TypeError as _var_var_13:
            raise TypeError(f'无法实例化类 {_var_var_8}，请确保无参构造或改为模块级函数: {_var_var_13}') from _var_var_13
    @staticmethod
    def execute(file_path: str, func_name: str = 'main', *args, **kwargs) -> Any:
        '''
        执行指定文件中的方法。

        示例:
        - FunUtil.execute("scripts/demo.py", "run", 1, 2, debug=True)
        - FunUtil.execute("scripts/demo.py", "MyClass.run", 1, 2)
        '''
        _var_var_4 = FunUtil._load_module(file_path)
        _var_var_7 = FunUtil._get_callable(_var_var_4, func_name)
        logger.info(f'FunUtil.execute -> file={file_path}, func={func_name}')
        if inspect.iscoroutinefunction(_var_var_7):
            try:
                return asyncio.run(_var_var_7(*args, **kwargs))
            except RuntimeError as _var_var_13:
                raise RuntimeError(f'检测到已存在事件循环，无法直接运行异步方法: {func_name}') from _var_var_13
        return _var_var_7(*args, **kwargs)
    @staticmethod
    def execute_with_params(file_path: str, params: Any = None, func_name: str = 'main') -> Any:
        '''
        执行指定文件中的方法，按 params 类型自动分发参数。

        - params 为 dict: 作为关键字参数
        - params 为 list/tuple: 作为位置参数
        - params 为 None: 无参数调用
        - 其它类型: 作为单个位置参数
        '''
        if params is None:
            return FunUtil.execute(file_path, func_name)
        if isinstance(params, dict):
            return FunUtil.execute(file_path, func_name, **params)
        if isinstance(params, (list, tuple)):
            return FunUtil.execute(file_path, func_name, *params)
        return FunUtil.execute(file_path, func_name, params)

if __name__ == '__main__':
    result = FunUtil.execute_with_params('/dev-py/v2/cloud-media-sync/app/utils/hdhive.py', {
        'item': {
            'type': 'movie',
            'tmdb_id': 1726 },
        'logger': logger }, 'HDHive.search')
    print(f'''结果: {result}''')

