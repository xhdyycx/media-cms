import random
from app.log import logger

def generate_random_daily_cron():
    '''
    生成随机的每天执行一次的 cron 表达式
    格式: 分钟 小时 * * *
    '''
    _var_var_0 = random.randint(0, 59)
    _var_var_1 = random.randint(0, 23)
    _var_var_2 = f'{_var_var_0} {_var_var_1} * * *'
    logger.info(f'生成的随机每日 cron: {_var_var_2} (每天 {_var_var_1:02d}:{_var_var_0:02d} 执行)')
    return _var_var_2

def generate_random_weekly_cron():
    '''
    生成随机的每周执行一次的 cron 表达式
    格式: 分钟 小时 * * 星期
    '''
    _var_var_0 = random.randint(0, 59)
    _var_var_1 = random.randint(0, 23)
    _var_var_3 = random.randint(0, 6)
    _var_var_2 = f'{_var_var_0} {_var_var_1} * * {_var_var_3}'
    logger.info(f'生成的随机每周 cron: {_var_var_2} (每周 {_var_var_3} {_var_var_1:02d}:{_var_var_0:02d} 执行)')
    return _var_var_2
