# File: wrapper.py (Cleaned & Decompiled)
import functools
import inspect
import time
from app.log import logger

def exception_ignore(func):
    """
    用于忽略函数中的异常，并记录错误日志。
    支持同步和异步函数。
    """
    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return None

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return None

    if inspect.iscoroutinefunction(func):
        return async_wrapper

def log_exec_time(func):
    """
    用于记录方法执行时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _var_var_4 = time.time()
        _var_var_5 = func(*args, **kwargs)
        _var_var_6 = time.time()
        _var_var_7 = _var_var_6 - _var_var_4
        logger.info(f"{func.__name__} done, time = {_var_var_7:.2f}s")
        return _var_var_5

