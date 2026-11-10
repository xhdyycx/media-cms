# File: lock.py (Cleaned & Decompiled)
from contextlib import contextmanager
from multiprocessing import Lock as MpLock
from threading import Lock as ThreadLock
from app.log import logger

class TaskLock:
    _instance = None
    _instance_lock = ThreadLock()

    def __new__(cls):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, '_initialized', False):
            return
        self._current_task = None
        self._state_lock = ThreadLock()
        self._lock = MpLock()
        self._is_locked = False
        self._initialized = True

    @property
    def current_task(self):
        return self._current_task

    @current_task.setter
    def current_task(self, task):
        self._current_task = task

    def remove_lock_by_task_name(self, task_name):
        if not task_name:
            logger.warning('按任务名释放任务锁失败：task_name 为空')
            return False
        with self._state_lock:
            if self._current_task != task_name or not self._is_locked:
                logger.info('按任务名释放任务锁跳过：task_name=%s, current_task=%s, is_locked=%s', task_name, self._current_task, self._is_locked)
                return False
        return self.release_safely(force=True)

    def clear_lock_dir(self, force):
        return 0

    def acquire(self, blocking=True, timeout=-1):
        try:
            if timeout is None or timeout < 0:
                _var_var_1 = self._lock.acquire(block=blocking)
            else:
                _var_var_1 = self._lock.acquire(block=blocking, timeout=timeout)
        except Exception:
            logger.exception('获取任务锁失败')
            return False
        if _var_var_1:
            with self._state_lock:
                self._is_locked = True
        return _var_var_1

    def release(self):
        return self.release_safely(force=False)

    def release_safely(self, force=False):
        try:
            with self._state_lock:
                if not force and not self._is_locked:
                    return False
                self._is_locked = False
                self._current_task = None
            self._lock.release()
            return True
        except Exception:
            if force:
                logger.exception('强制释放任务锁失败')
            else:
                logger.exception('释放任务锁失败')
            return False

    @contextmanager
    def hold(self, task_name, blocking=True, timeout=30):
        _var_var_1 = self.acquire(blocking=blocking, timeout=timeout)
        if not _var_var_1:
            yield False
            return
        _var_var_2 = self._current_task
        if task_name is not None:
            self.current_task = task_name
        try:
            yield True
        finally:
            self.current_task = _var_var_2
            self.release_safely()

task_manager = TaskLock()
