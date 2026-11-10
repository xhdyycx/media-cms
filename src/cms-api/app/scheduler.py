import json
import traceback
from datetime import datetime, timedelta
import pytz
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_MAX_INSTANCES
from app.services.m115service import M115Service
from app.core.env import novaEnv
from app.log import logger
from app.utils.singleton import Singleton

class Scheduler(metaclass=Singleton):
    '''Scheduler'''
    __doc__ = '\n    定时任务管理\n    '
    
    _scheduler = None
    
    def __init__(self):
        
        self.init()
        return None
        
        

    
    def init(self):
        '''
        初始化定时服务
        '''
        
        self._scheduler = BackgroundScheduler(timezone = 'Asia/Shanghai', executors = {
            'default': ThreadPoolExecutor(32) })
        if novaEnv.IS_AUTHOR:
            self._scheduler.add_job(id = 't13', name = '115签到', func = M115Service().sign, kwargs = {
                'data': {
                    'random_delay': '10-600' } }, trigger = CronTrigger.from_crontab('30 0 * * *'), max_instances = 1, misfire_grace_time = 10)
        self._scheduler.add_listener(self.job_listener, EVENT_JOB_MAX_INSTANCES)
        self._scheduler.start()
        return None
        
        

    
    def job_listener(self, event):
        
        if event.code == EVENT_JOB_MAX_INSTANCES:
            logger.info(f'''任务{event.job_id}正在运行，结束重复任务执行.''')
        return None
        
        

    
    def start_job(self, task_id):
        
        _var_var_0 = self._scheduler.get_job(task_id)
        if _var_var_0:
            _var_var_0.func(*_var_var_0.args)
        return None
        
        

    
    def start_job_async(self, task_id):
        
        _var_var_0 = self._scheduler.get_job(task_id)
        if _var_var_0:
            self._scheduler.add_job(id = _var_var_0.id + '_once', name = _var_var_0.name + '_once', func = _var_var_0.func, args = _var_var_0.args, kwargs = _var_var_0.kwargs, trigger = 'date', run_date = datetime.now(tz = pytz.timezone(novaEnv.TZ)) + timedelta(seconds = 3))
        return None
        
        

    
    def add_once_job(self, mt):
        
        _var_var_0 = self._scheduler.get_job(mt.id)
        if _var_var_0:
            logger.info('当前任务id已存在,先删除再添加')
            self._scheduler.remove_job(mt.id)
        logger.info(f'''增加一次性任务,task={mt.to_json()}''')
        self._scheduler.add_job(id = mt.id, name = mt.name, func = mt.func, args = mt.args, trigger = 'date', run_date = datetime.now(tz = pytz.timezone(novaEnv.TZ)) + timedelta(seconds = 3))
        return None
        
        

    
    def add_one_job(self, _id, name, func, kwargs, seconds):
        
        _var_var_0 = self._scheduler.get_job(_id)
        if _var_var_0:
            logger.info('当前任务id已存在,先删除再添加')
            self._scheduler.remove_job(_id)
        logger.info(f'''增加一次性任务-{name}''')
        self._scheduler.add_job(id = _id, name = name, func = func, kwargs = kwargs, trigger = 'date', run_date = datetime.now(tz = pytz.timezone(novaEnv.TZ)) + timedelta(seconds = seconds))
        return None
        
        

    
    def update_sync_main_job(self, cron_str, func):
        if cron_str is None or cron_str == '':
            cron_str = '*/20 8-23 * * *'
        _var_var_1 = 'nova_main_task'
        _var_var_0 = self._scheduler.get_job(_var_var_1)
        if _var_var_0:
            logger.info('媒体库整理同步任务已存在，先删除再添加')
            self._scheduler.remove_job(_var_var_1)
        self._scheduler.add_job(id=_var_var_1, name='媒体库整理同步', func=func, trigger=CronTrigger.from_crontab(cron_str), max_instances=1, misfire_grace_time=10)
        logger.info('媒体库整理同步任务-添加成功')

    
    def add_task(self, task_id, task_name, cron_str, func, kwargs=None):
        
        _var_var_0 = self._scheduler.get_job(task_id)
        if _var_var_0:
            logger.info(f'''{task_name}已存在，先删除再添加''')
            self._scheduler.remove_job(task_id)
        self._scheduler.add_job(id = task_id, name = task_name, func = func, trigger = CronTrigger.from_crontab(cron_str), kwargs = kwargs, max_instances = 1, misfire_grace_time = 10)
        logger.info(f'''【{task_name}】任务-添加成功''')
        return None
        
        

    
    def del_task(self, task_id, task_name):
        
        _var_var_0 = self._scheduler.get_job(task_id)
        if _var_var_0:
            logger.info(f'''【{task_name}】任务-删除成功''')
            self._scheduler.remove_job(task_id)
        return None
        
        

    
    def log_all_jobs(self):
        
        _var_var_2 = self._scheduler.get_jobs()
        logger.info('--------------定时任务--------------')
        for _var_var_0 in _var_var_2:
            logger.info(f'''{_var_var_0.id}-【{_var_var_0.name}】-{_var_var_0.trigger}''')
        return None
        
        

    
    def get_all_jobs(self):
        
        _var_var_2 = self._scheduler.get_jobs()
        _var_var_3 = []
        for _var_var_0 in _var_var_2:
            _var_var_3.append({
                'id': _var_var_0.id,
                'name': _var_var_0.name,
                'trigger': _var_var_0.trigger,
                'func': _var_var_0.func,
                'args': _var_var_0.args })
        return _var_var_3
        # None(None)
        return None
        
        

    
    def stop(self):
        '''
        关闭定时服务
        '''
        try:
            if self._scheduler:
                logger.info('正在停止定时任务...')
                self._scheduler.remove_all_jobs()
                if self._scheduler.running:
                    self._scheduler.shutdown()
                self._scheduler = None
                logger.info('定时任务停止完成')
        except Exception as _var_var_4:
            logger.error(f'停止定时任务失败：：{str(_var_var_4)} - {traceback.format_exc()}')
        return None
    
    



class MTask(object):
    '''
    任务对象
    '''
    
    
    def __init__(self, id, name, func, args):
        
        self.id = id
        self.name = name
        self.func = func
        self.args = args
        return None
        
        

    
    def to_json(self):
        
        return json.dumps(self.__dict__, ensure_ascii = False, default = str)
        # None(None)
        return None


