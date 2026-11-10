import os
from blacksheep import Request
from blacksheep.server.authorization import auth
from blacksheep.server.controllers import get, post
from blacksheep.server.controllers import APIController
from blacksheep.server.responses import json
import aiohttp
import asyncio
from app.core.env import novaEnv, configEnv
from app.core.env2 import config2Env
from app.core.event import EventManager
from app.core.m123 import M123
from app.core.mconfig import AutoOrganizeConfig
from app.core.obj_factory import ObjFactory
from app.core.m115 import M115
from app.core.media_monitor import MediaImgMonitor
from app.core.task import nova_main_task, del_115_dir_task, del_115_recycle_task, del_aliyun_dir_task, del_aliyun_recycle_task, alist_sync_cmd, cover_gen_task, hdhive_checkin_task, sync_123_task, tidy_123_task, del_123_recycle_task, del_123_dir_task
from app.core.task_tidy import download_words_replace_file
from app.db import get_db
from app.db.config_op import ConfigOp
from app.db.liftlist_op import LiftListOp
from app.db.rename_op import RenameOp
from app.db.share_op import ShareDownOp
from app.log import logger
from app.modules.tg.tg_bot import TGBot
from app.scheduler import Scheduler
from app.services.message_service import MessageService
from app.utils.docker import DockerHubAPI
from app.utils.mfile import MFileUtil
from app.utils.okhttp import OkHttp

class ConfigController(APIController):
    @classmethod
    def route(cls):
        return '/api/config'
    @get('category')
    @auth('login')
    async def get_category(self):
        """获取分类配置"""
        try:
            _var_var_0 = MFileUtil.exists(novaEnv.CATEGORY_FILE_PATH)
            if not _var_var_0:
                if MFileUtil.exists(novaEnv.DEMO_CATEGORY_FILE_PATH):
                    MFileUtil.copy_file(novaEnv.DEMO_CATEGORY_FILE_PATH, novaEnv.CATEGORY_FILE_PATH)
                else:
                    MFileUtil.write_file(novaEnv.CATEGORY_FILE_PATH, '')
            _var_var_1 = MFileUtil.read_file(novaEnv.CATEGORY_FILE_PATH)
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return json({'code': 500, 'msg': f'获取分类配置失败: {str(_var_var_2)}'})
    @post('category')
    @auth('login')
    async def update_category(self, content: dict):
        """更新分类配置"""
        try:
            MFileUtil.write_file(novaEnv.CATEGORY_FILE_PATH, content.get('content', ''))
            return json({'code': 200, 'msg': '更新成功'})
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return json({'code': 500, 'msg': '更新失败'})
    @get('tidy_rule')
    @auth('login')
    async def get_tidy_rule(self):
        try:
            _var_var_0 = MFileUtil.exists(novaEnv.TIDY_FILE_PATH)
            if not _var_var_0:
                if MFileUtil.exists(novaEnv.DEMO_TIDY_FILE_PATH):
                    MFileUtil.copy_file(novaEnv.DEMO_TIDY_FILE_PATH, novaEnv.TIDY_FILE_PATH)
                else:
                    MFileUtil.write_file(novaEnv.TIDY_FILE_PATH, '')
            _var_var_1 = MFileUtil.read_file(novaEnv.TIDY_FILE_PATH)
            return json({'code': 200, 'data': _var_var_1})
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return json({'code': 500, 'msg': f'获取分类配置失败: {str(_var_var_2)}'})
    @post('tidy_rule')
    @auth('login')
    async def update_tidy_rule(self, content: dict):
        try:
            MFileUtil.write_file(novaEnv.TIDY_FILE_PATH, content.get('content', ''))
            return json({'code': 200, 'msg': '更新成功'})
        except Exception as _var_var_2:
            logger.exception(_var_var_2)
            return json({'code': 500, 'msg': '更新失败'})
    @get('{key}')
    @auth('login')
    async def get_config(self, key: str):
        """获取配置"""
        with get_db() as _var_var_3:
            _var_var_4 = ConfigOp(_var_var_3)
            _var_var_5 = _var_var_4.get_by_key(key)
            return json({'code': 200, 'data': _var_var_5})
    @post('{key}')
    @auth('login')
    async def update_config(self, key: str, config_json: dict):
        """更新配置"""
        _var_var_6 = ['plugin', 'E_115_DIR_DEL', 'E_115_RECYCLE_DEL', 'E_123_DIR_DEL', 'E_123_RECYCLE_DEL', 'E_ALIYUN_DIR_DEL', 'E_ALIYUN_RECYCLE_DEL', 'E_ALIST_SYNC', 'E_COVER_GEN', 'E_HDHIVE_CHECKIN']
        if key == 'incremental_sync':
            Scheduler().update_sync_main_job(config_json.get('SYNC_CRON'), nova_main_task)
            Scheduler().log_all_jobs()
        if key == 'monitor':
            if config_json.get('MONITOR_PATH'):
                if not os.path.exists(config_json.get('MONITOR_PATH')):
                    logger.info(f'监控路径不存在: {config_json.get("MONITOR_PATH")}')
                    return json({'code': 400, 'msg': '监控路径不存在'})
                MediaImgMonitor().stop()
                MediaImgMonitor().start(config_json.get('MONITOR_PATH'))
            else:
                MediaImgMonitor().stop()
        _var_var_7 = {}
        with get_db() as _var_var_3:
            _var_var_4 = ConfigOp(_var_var_3)
            if key in _var_var_6:
                _var_var_7 = _var_var_4.get_by_key(key)
            _var_var_4.update(key, config_json)
        if key == 'core':
            ObjFactory.refresh_instance(M115)
        if key == 'auto_organize':
            ObjFactory.refresh_instance(AutoOrganizeConfig)
        if key == 'full_sync_123':
            Scheduler().del_task('t_m123_sync', '全量同步123')
            if config2Env.m123_sync_cron:
                Scheduler().add_task('t_m123_sync', '全量同步123', config2Env.m123_sync_cron, sync_123_task)
        if key == 'tidy123':
            Scheduler().del_task('t_m123_tidy', '自动整理123')
            if config2Env.m123_tidy_cron:
                Scheduler().add_task('t_m123_tidy', '自动整理123', config2Env.m123_tidy_cron, tidy_123_task)
        if key == 'message':
            if config_json.get('telegram', {}).get('TG_BOT_STATUS', False):
                TGBot().init_bot()
            else:
                TGBot().stop_bot()
            EventManager().register_commands()
        if key in _var_var_6:
            self.updete_plugin_task(key, _var_var_7, config_json)
        return json({'code': 200, 'msg': 'success'})
    
    def updete_plugin_task(self, key, old_config, new_config):
        if key == 'plugin':
            if old_config.get('E_ALIST_SYNC') != new_config.get('E_ALIST_SYNC'):
                if configEnv.e_alist_sync_status and configEnv.e_alist_sync_cron:
                    Scheduler().add_task('t_alist_sync', 'alist同步', configEnv.e_alist_sync_cron, alist_sync_cmd)
                else:
                    Scheduler().del_task('t_alist_sync', 'alist同步')
            if old_config.get('E_115_DIR_DEL') != new_config.get('E_115_DIR_DEL'):
                if configEnv.e_115_dir_del_status and configEnv.e_115_dir_del_cron:
                    Scheduler().add_task('t_115_dir_del', '115文件夹删除', configEnv.e_115_dir_del_cron, del_115_dir_task)
                else:
                    Scheduler().del_task('t_115_dir_del', '115文件夹删除')
            if old_config.get('E_115_RECYCLE_DEL') != new_config.get('E_115_RECYCLE_DEL'):
                if configEnv.e_115_recycle_del_status and configEnv.e_115_recycle_del_cron:
                    Scheduler().add_task('t_115_recycle_del', '115回收站清空', configEnv.e_115_recycle_del_cron, del_115_recycle_task)
                else:
                    Scheduler().del_task('t_115_recycle_del', '115回收站清空')
            if old_config.get('E_123_DIR_DEL') != new_config.get('E_123_DIR_DEL'):
                if config2Env.e_123_dir_del_status and config2Env.e_123_dir_del_cron:
                    Scheduler().add_task('t_123_dir_del', '123文件夹删除', config2Env.e_123_dir_del_cron, del_123_dir_task)
                else:
                    Scheduler().del_task('t_123_dir_del', '123文件夹删除')
            if old_config.get('E_123_RECYCLE_DEL') != new_config.get('E_123_RECYCLE_DEL'):
                if config2Env.e_123_recycle_del_status and config2Env.e_123_recycle_del_cron:
                    Scheduler().add_task('t_123_recycle_del', '123回收站清空', config2Env.e_123_recycle_del_cron, del_123_recycle_task)
                else:
                    Scheduler().del_task('t_123_recycle_del', '123回收站清空')
            if old_config.get('E_ALIYUN_DIR_DEL') != new_config.get('E_ALIYUN_DIR_DEL'):
                if configEnv.e_aliyun_dir_del_status and configEnv.e_aliyun_dir_del_cron:
                    Scheduler().add_task('t_aliyun_dir_del', '阿里云盘文件夹删除', configEnv.e_aliyun_dir_del_cron, del_aliyun_dir_task)
                else:
                    Scheduler().del_task('t_aliyun_dir_del', '阿里云盘文件夹删除')
            if old_config.get('E_ALIYUN_RECYCLE_DEL') != new_config.get('E_ALIYUN_RECYCLE_DEL'):
                if configEnv.e_aliyun_recycle_del_status and configEnv.e_aliyun_recycle_del_cron:
                    Scheduler().add_task('t_aliyun_recycle_del', '阿里云盘回收站清空', configEnv.e_aliyun_recycle_del_cron, del_aliyun_recycle_task)
                else:
                    Scheduler().del_task('t_aliyun_recycle_del', '阿里云盘回收站清空')
            if old_config.get('E_COVER_GEN') != new_config.get('E_COVER_GEN'):
                if config2Env.e_cover_gen_status and config2Env.e_cover_gen_cron:
                    Scheduler().add_task('t_cover_gen', '媒体库封面生成', config2Env.e_cover_gen_cron, cover_gen_task)
                else:
                    Scheduler().del_task('t_cover_gen', '媒体库封面生成')
            if old_config.get('E_HDHIVE_CHECKIN') != new_config.get('E_HDHIVE_CHECKIN'):
                if config2Env.hdhive_checkin_status:
                    Scheduler().add_task('t_hdhive_checkin', 'RE0签到', config2Env.hdhive_checkin_cron, hdhive_checkin_task)
                else:
                    Scheduler().del_task('t_hdhive_checkin', 'RE0签到')
            elif key == 'E_115_DIR_DEL' and configEnv.e_115_dir_del_cron and configEnv.e_115_dir_del_status:
                Scheduler().add_task('e_115_dir_del_task', '115文件夹删除', configEnv.e_115_dir_del_cron, del_115_dir_task)
            elif key == 'E_115_RECYCLE_DEL' and configEnv.e_115_recycle_del_cron and configEnv.e_115_recycle_del_status:
                Scheduler().add_task('t_115_recycle_del', '115回收站清空', configEnv.e_115_recycle_del_cron, del_115_recycle_task)
            elif key == 'E_123_DIR_DEL' and config2Env.e_123_dir_del_cron and config2Env.e_123_dir_del_status:
                Scheduler().add_task('e_123_dir_del_task', '123文件夹删除', config2Env.e_123_dir_del_cron, del_123_dir_task)
            elif key == 'E_123_RECYCLE_DEL' and config2Env.e_123_recycle_del_cron and config2Env.e_123_recycle_del_status:
                Scheduler().add_task('t_123_recycle_del', '123回收站清空', config2Env.e_123_recycle_del_cron, del_123_recycle_task)
            elif key == 'E_ALIYUN_DIR_DEL' and configEnv.e_aliyun_dir_del_cron and configEnv.e_aliyun_dir_del_status:
                Scheduler().add_task('t_aliyun_dir_del', '阿里云盘文件夹删除', configEnv.e_aliyun_dir_del_cron, del_aliyun_dir_task)
            elif key == 'E_ALIYUN_RECYCLE_DEL' and configEnv.e_aliyun_recycle_del_cron and configEnv.e_aliyun_recycle_del_status:
                Scheduler().add_task('t_aliyun_recycle_del', '阿里云盘回收站清空', configEnv.e_aliyun_recycle_del_cron, del_aliyun_recycle_task)
            elif key == 'E_ALIST_SYNC' and configEnv.e_alist_sync_cron and configEnv.e_alist_sync_status:
                Scheduler().add_task('t_alist_sync', 'alist同步', configEnv.e_alist_sync_cron, alist_sync_cmd)
            elif key == 'E_COVER_GEN' and config2Env.e_cover_gen_cron and config2Env.e_cover_gen_status:
                Scheduler().add_task('t_cover_gen', '媒体库封面生成', config2Env.e_cover_gen_cron, cover_gen_task)
            elif key == 'E_HDHIVE_CHECKIN' and config2Env.hdhive_checkin_status:
                Scheduler().add_task('t_hdhive_checkin', 'RE0签到', config2Env.hdhive_checkin_cron, hdhive_checkin_task)
        return None
        return None

    @post('check_domain')
    async def check_domain(self, domain: dict):
        """检查域名连接状态"""
        if not domain or 'url' not in domain:
            return json({'code': 400, 'msg': '缺少url参数'})
        _var_var_8 = domain['url']
        if not _var_var_8.startswith(('http://', 'https://')):
            _var_var_8 = f'https://{_var_var_8}'
        try:
            _var_var_9 = aiohttp.TCPConnector(ssl=False, force_close=True)
            _var_var_10 = aiohttp.ClientTimeout(total=10)
            async with aiohttp.ClientSession(connector=_var_var_9, timeout=_var_var_10) as _var_var_11:
                async with _var_var_11.get(_var_var_8) as _var_var_12:
                    if _var_var_12.status == 200:
                        return json({'code': 200, 'msg': 'success', 'data': {'status': 'ok', 'statusCode': _var_var_12.status, 'url': _var_var_8}})
                    return json({'code': 200, 'msg': 'domain unreachable', 'data': {'status': 'error', 'statusCode': _var_var_12.status, 'url': _var_var_8}})
        except asyncio.TimeoutError:
            return json({'code': 200, 'msg': 'timeout', 'data': {'status': 'error', 'statusCode': -1, 'url': _var_var_8}})
        except Exception as _var_var_2:
            return json({'code': 200, 'msg': str(_var_var_2), 'data': {'status': 'error', 'statusCode': -1, 'url': _var_var_8}})
    @get('msg_test')
    @auth('login')
    async def msg_test(self):
        """测试消息发送"""
        MessageService().send_msg(title='测试消息-标题', text='测试消息-内容')
        return json({'code': 200, 'msg': '发送成功'})
    @get('/clear')
    async def clear(self, request: Request):
        _var_var_13 = request.query.get('token')
        _var_var_14 = request.query.get('table')
        if not _var_var_13 or not _var_var_14:
            return json({'code': '400', 'message': 'token或table为空'})
        _var_var_13 = _var_var_13[0]
        _var_var_14 = _var_var_14[0]
        if _var_var_13 != novaEnv.NOVA_API_TOKEN:
            return json({'code': '400', 'message': 'token错误'})
        if _var_var_14 == 'share_down':
            with get_db() as _var_var_3:
                _var_var_15 = ShareDownOp(_var_var_3)
                _var_var_15.clear()
                return json({'code': '200', 'message': '清空share_down数据成功'})
        if _var_var_14 == 'rename_log':
            with get_db() as _var_var_3:
                _var_var_16 = RenameOp(_var_var_3)
                _var_var_16.clear()
                return json({'code': '200', 'message': '清空rename_log数据成功'})
        return json({'code': '400', 'message': '不支持的table'})
    @post('/cache_clear')
    @auth('login')
    async def cache_clear(self, payload: dict):
        _var_var_17 = payload.get('cache_type')
        _var_var_18 = ObjFactory.get_instance(M115)
        if _var_var_17 == 'share_down':
            with get_db() as _var_var_3:
                _var_var_15 = ShareDownOp(_var_var_3)
                _var_var_15.clear()
                return json({
                    'code': 200,
                    'msg': '清除分享下载缓存成功' })
        if _var_var_17 == 'rename_log':
            with get_db() as _var_var_3:
                _var_var_16 = RenameOp(_var_var_3)
                _var_var_16.clear()
                return json({
                    'code': 200,
                    'msg': '清除自动整理缓存成功' })
        if _var_var_17 == 'lift_list':
            with get_db() as _var_var_3:
                _var_var_19 = LiftListOp(_var_var_3)
                _var_var_19.clear()
                _var_var_18.life_clear_history()
                return json({
                    'code': 200,
                    'msg': '清除115生活事件缓存成功' })
        return json({
            'code': 400,
            'msg': '不支持的类型' })
    @get('test_delay')
    async def test_delay(self, domain: str, proxy_url: str = 'NA'):
        if proxy_url == 'NA':
            proxy_url = configEnv.http_proxies
        _var_var_20 = OkHttp().test_delay(domain, proxies=proxy_url)
        if _var_var_20:
            return json({
                'code': 200,
                'msg': '测试成功',
                'data': _var_var_20 })
        return json({
            'code': 400,
            'msg': '测试失败' })
    @get('check_docker_version')
    async def check_docker_version(self):
        _var_var_21 = configEnv.http_proxies
        _var_var_22 = DockerHubAPI().get_cms_version(proxies=_var_var_21)
        return json({
            'code': 200,
            'msg': '获取成功',
            'data': _var_var_22 })
    @post('/login_account')
    @auth('login')
    async def login_account(self, payload: dict):
        if payload.get('account_type') == '123':
            _var_var_23 = ObjFactory.get_instance(M123)
            _var_var_24, _var_var_25 = _var_var_23.check_binding()
            if not _var_var_24:
                return json({
                    'code': 400,
                    'msg': _var_var_25 })
            _var_var_24 = _var_var_23.open_access_token(payload.get('client_id'), payload.get('client_secret'))
            if _var_var_24:
                return json({
                    'code': 200,
                    'msg': '123 OPENAPI 登录成功' })
        return json({
            'code': 400,
            'msg': '登录失败，请检查输入是否正确' })
    @get('/get_account_info')
    @auth('login')
    async def get_account_info(self, account_type: str):
        _var_var_26 = {}
        if account_type == '123':
            _var_var_23 = ObjFactory.get_instance(M123)
            _var_var_5 = _var_var_23.get_client_config()
            _var_var_26 = {
                'account_type': '123',
                'client_id': _var_var_5.get('client_id'),
                'client_secret': _var_var_5.get('client_secret') }
            if _var_var_23.is_enable():
                _var_var_27 = _var_var_23.open_user_info()
                if _var_var_27.get('code', 101) == 0:
                    _var_var_28 = _var_var_27.get('data', {})
                    _var_var_26['nickname'] = _var_var_28.get('nickname')
                    _var_var_26['size_used'] = _var_var_28.get('spaceUsed')
                    _var_var_26['size_total'] = int(_var_var_28.get('spacePermanent')) + int(_var_var_28.get('spaceTemp'))
                    _var_var_26['vip'] = _var_var_28.get('vip')
        return json({
            'code': 200,
            'data': _var_var_26 })
    @get('/update_github_words_replace')
    @auth('login')
    async def update_github_words_replace(self):
        '从 github 更新替换词文件'
        try:
            _var_var_29 = download_words_replace_file()
            return json({
                'code': 200,
                'data': _var_var_29.as_posix() })
        except Exception as _var_var_2:
            logger.exception('更新替换词文件失败: %s', _var_var_2)
            return json({
                'code': 500,
                'msg': '获取失败' })
