import sys
import uvicorn
from blacksheep import Application
from guardpost.common import AuthenticatedRequirement
import urllib3.fields
from app.core.emby_user import emby_user_util

if not hasattr(urllib3.fields, 'format_header_param') and hasattr(urllib3.fields, 'format_header_param_rfc2231'):
    urllib3.fields.format_header_param = urllib3.fields.format_header_param_rfc2231

from blacksheep.server.authorization import Policy
from app.core.auth import ProPolicy
from app.core.env import configEnv, novaEnv
from app.core.env2 import config2Env
from app.core.license import LicenseInfo
from app.core.lock import task_manager
from app.core.media_monitor import MediaImgMonitor
from app.core.event import EventManager
import app.api
from app.core.task import (
    check_donate_code, nova_main_task, del_115_dir_task, del_115_recycle_task,
    del_aliyun_dir_task, del_aliyun_recycle_task, alist_sync_cmd, cover_gen_task,
    hdhive_checkin_task, tidy_123_task, sync_123_task, check_123_token,
    del_123_dir_task, del_123_recycle_task, net_test
)
from app.core.task_tidy import download_words_replace_file
from app.db import init_db, get_db, update_db
from app.db.config_op import ConfigOp
from app.db.liftlist_op import LiftListOp
from app.db.user_op import UserOp
from app.dbv2 import init_dbv2
from app.log import logger
from app.scheduler import Scheduler
from app.middleware.auth_handler import JWTAuthenticationHandler
from app.middleware.log_handler import log_handler_middlewares
from app.utils.mrandom import generate_random_weekly_cron
from version import APP_VERSION_CODE

app = Application()
app.use_authentication().add(JWTAuthenticationHandler())
app.use_authorization().add(Policy('login', AuthenticatedRequirement())).add(ProPolicy())
app.middlewares.append(log_handler_middlewares)


@app.on_start
async def on_start():
    net_test()
    logger.info(f'{APP_VERSION_CODE}')
    logger.info('开始初始化DB....')
    init_db()
    init_dbv2()
    if novaEnv.IS_SQLITE:
        logger.info('开始同步DB结构变动....')
        update_db()


@app.on_stop
async def on_stop():
    Scheduler().stop()
    MediaImgMonitor().stop()
    logger.info('novamedia stopping...')


@app.after_start
async def after_start():
    with get_db() as _var_var_0:
        _var_var_1 = ConfigOp(_var_var_0)
        _var_var_1.init_env()
        configEnv.refresh()
    
    logger.info('开始校验授权....')
    check_donate_code()
    logger.info('校验授权结束....')
    
    if LicenseInfo().is_free():
        logger.error('授权校验未通过，请检查配置后重启容器')
        await on_stop()
        sys.exit(1)
        
    with get_db() as _var_var_0:
        _var_var_3 = UserOp(_var_var_0)
        _var_var_3.init_admin(novaEnv.ADMIN_USERNAME, novaEnv.ADMIN_PASSWORD)
        _var_var_1 = ConfigOp(_var_var_0)
        _var_var_4 = LiftListOp(_var_var_0)
        _var_var_4.del_useless_data()
        
        if novaEnv.RUN_ENV != 'dev1':
            Scheduler().update_sync_main_job(configEnv.sync_cron, nova_main_task)
            init_123_task()
            init_plugin_task()
            init_words_replace_task()
            Scheduler().log_all_jobs()
            _var_var_5 = _var_var_1.get_by_key('monitor')
            MediaImgMonitor().start(_var_var_5.get('MONITOR_PATH'))
            if novaEnv.IS_CREATE_MENU:
                EventManager().register_commands()
            else:
                logger.info('IS_CREATE_MENU != YES, 重启不创建菜单')
                
    emby_user_util.refresh_cache()
    task_manager.clear_lock_dir(force=True)
    logger.info('novamedia starting success...')
    logger.info(f'Version: {novaEnv.APP_VERSION}')


def init_123_task():
    Scheduler().add_task('check_123_token', '检查123token是否可用', '15 7 * * *', check_123_token)


def init_plugin_task():
    try:
        if configEnv.e_115_dir_del_cron and configEnv.e_115_dir_del_status:
            Scheduler().add_task('t_115_dir_del', '115文件夹删除', configEnv.e_115_dir_del_cron, del_115_dir_task)
        if configEnv.e_115_recycle_del_cron and configEnv.e_115_recycle_del_status:
            Scheduler().add_task('t_115_recycle_del', '115回收站清空', configEnv.e_115_recycle_del_cron, del_115_recycle_task)
        if config2Env.e_123_dir_del_status and config2Env.e_123_dir_del_cron:
            Scheduler().add_task('t_123_dir_del', '123文件夹删除', config2Env.e_123_dir_del_cron, del_123_dir_task)
        if config2Env.e_123_recycle_del_cron and config2Env.e_123_recycle_del_status:
            Scheduler().add_task('t_123_recycle_del', '123回收站清空', config2Env.e_123_recycle_del_cron, del_123_recycle_task)
        if configEnv.e_aliyun_dir_del_cron and configEnv.e_aliyun_dir_del_status:
            Scheduler().add_task('t_aliyun_dir_del', '阿里云盘文件夹删除', configEnv.e_aliyun_dir_del_cron, del_aliyun_dir_task)
        if configEnv.e_aliyun_recycle_del_cron and configEnv.e_aliyun_recycle_del_status:
            Scheduler().add_task('t_aliyun_recycle_del', '阿里云盘回收站清空', configEnv.e_aliyun_recycle_del_cron, del_aliyun_recycle_task)
        if configEnv.e_alist_sync_status and configEnv.e_alist_sync_cron:
            Scheduler().add_task('t_alist_sync', 'alist同步', configEnv.e_alist_sync_cron, alist_sync_cmd)
        if config2Env.e_cover_gen_cron and config2Env.e_cover_gen_status:
            Scheduler().add_task('t_cover_gen', '媒体库封面生成', config2Env.e_cover_gen_cron, cover_gen_task)
        if config2Env.hdhive_checkin_status:
            Scheduler().add_task('t_hdhive_checkin', 'RE0签到', config2Env.hdhive_checkin_cron, hdhive_checkin_task)
        if config2Env.m123_tidy_cron:
            Scheduler().add_task('t_m123_tidy', '自动整理123', config2Env.m123_tidy_cron, tidy_123_task)
        if config2Env.m123_sync_cron:
            Scheduler().add_task('t_m123_sync', '全量同步123', config2Env.m123_sync_cron, sync_123_task)
    except Exception as _var_var_6:
        logger.exception(_var_var_6)
        logger.error('初始化插件任务失败')


def init_words_replace_task():
    try:
        Scheduler().add_one_job('t_download_words_replace_file_one', '公共识别词下载（一次）', download_words_replace_file, None, 60)
        Scheduler().add_task('t_download_words_replace_file', '公共识别词下载', generate_random_weekly_cron(), download_words_replace_file)
    except Exception as _var_var_6:
        logger.exception(_var_var_6)
        logger.error('初始化【公共识别词下载】任务失败')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9528, proxy_headers=True, forwarded_allow_ips='*')
