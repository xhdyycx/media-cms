from concurrent.futures import ThreadPoolExecutor, wait
import weakref
import threading
from app.log import logger

class ThreadUtil:
    '''
    线程池管理
    '''
    
    def __init__(self, max_workers, queue_size):
        '''
        初始化线程池
        :param max_workers: 最大工作线程数
        :param queue_size: 最大队列大小
        '''
        self.pool = ThreadPoolExecutor(max_workers = max_workers)
        self.tasks = weakref.WeakSet()
        self.queue_size = queue_size
        self._task_count_lock = threading.Lock()
        self._task_count = 0
        self._task_available = threading.Condition(self._task_count_lock)
        return None
        return None

    
    def submit(self, func, *args, **kwargs):
        '''
        提交任务，当队列满时会阻塞等待
        :param func: 函数
        :param args: 参数
        :param kwargs: 参数
        :return: future
        '''
        with self._task_count_lock:
            while self._task_count >= self.queue_size:
                self._task_available.wait()
            self._task_count += 1

        def _var_var_0(*args, **kwargs):  # co_name = wrapped_func
            try:
                return func(*args, **kwargs)
            finally:
                with self._task_count_lock:
                    self._task_count -= 1
                    self._task_available.notify()

        _var_var_1 = self.pool.submit(_var_var_0, *args, **kwargs)
        self.tasks.add(_var_var_1)
        return _var_var_1


    
    def shutdown(self):
        '''
        关闭线程池
        :return:
        '''
        self.pool.shutdown()
        return None
        return None

    
    def __del__(self):
        self.shutdown()
        return None
        return None

    
    def wait_for_all_tasks(self):
        '''
        等待所有线程任务完成但不关闭线程池
        '''
        wait(list(self.tasks))
        return None
        return None

    
    def get_task_count(self):
        '''
        获取当前任务数
        :return: int 当前正在处理的任务总数
        '''
        self._task_count_lock
        return 
        return None
        with None:
            if not None:
                pass
        return None
        return None

    
    def submit_and_get_result(self, func, *args, timeout=None, **kwargs):
        '''
        提交任务并等待获取返回结果
        :param func: 函数
        :param args: 参数
        :param timeout: 超时时间（秒），None表示无限等待
        :param kwargs: 参数
        :return: 函数执行结果
        :raises: 如果函数执行过程中出现异常，会重新抛出该异常
        '''
        _var_var_1 = self.submit(func, *args, **kwargs)
        try:
            return _var_var_1.result(timeout=timeout)
        except Exception as _var_var_2:
            logger.error(f'线程执行任务时发生异常: {_var_var_2}')
            raise
    def submit_batch_async_and_wait_results(self, tasks, timeout):
        '''
        批量异步提交任务，立即返回futures，然后等待所有任务完成并获取结果
        这种方式不会阻塞任务的提交，所有任务会立即提交到线程池，然后统一等待结果
        :param tasks: 任务列表，每个任务是一个元组 (func, args, kwargs) 或 (func, args)
        :param timeout: 超时时间（秒），None表示无限等待
        :return: 结果列表，按提交顺序返回
        :raises: 如果任何任务执行过程中出现异常，会重新抛出该异常
        '''
        _var_var_3 = []
        for _var_var_4, _var_var_5 in enumerate(tasks):
            if len(_var_var_5) == 2:
                _var_var_6, _var_var_7 = _var_var_5
                _var_var_8 = {}
            elif len(_var_var_5) == 3:
                _var_var_6, _var_var_7, _var_var_8 = _var_var_5
            else:
                raise ValueError('任务格式错误，应为 (func, args) 或 (func, args, kwargs)')
            _var_var_1 = self.submit(_var_var_6, *_var_var_7, **_var_var_8)
            _var_var_3.append(_var_var_1)

        _var_var_9 = []
        for _var_var_4, _var_var_1 in enumerate(_var_var_3):
            try:
                _var_var_10 = _var_var_1.result(timeout=timeout)
                _var_var_9.append(_var_var_10)
            except Exception as _var_var_2:
                logger.error(f'批量任务第{_var_var_4 + 1}个任务执行时发生异常: {_var_var_2}')
                raise
        return _var_var_9
    def submit_multiple_and_collect_results(self, task_funcs, task_args_list, timeout):
        '''
        提交多个相同函数的任务，使用不同参数，等待所有完成后返回结果
        适用于需要并行执行同一个函数但参数不同的场景
        :param task_func: 要执行的函数
        :param task_args_list: 参数列表，每个元素是 (args, kwargs) 或 args
        :param timeout: 超时时间（秒）
        :return: 结果列表
        '''
        if not isinstance(task_funcs, list):
            task_funcs = [task_funcs] * len(task_args_list)
        _var_var_11 = []
        for _var_var_4, (_var_var_6, _var_var_7) in enumerate(zip(task_funcs, task_args_list)):
            if isinstance(_var_var_7, tuple) and len(_var_var_7) == 2 and isinstance(_var_var_7[1], dict):
                _var_var_11.append((_var_var_6, _var_var_7[0], _var_var_7[1]))
                continue
            _var_var_11.append((_var_var_6, _var_var_7))
        return self.submit_batch_async_and_wait_results(_var_var_11, timeout)
