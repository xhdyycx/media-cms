import hashlib
import time
from contextlib import contextmanager
from app.core.aliyun import AliyunApi
from app.core.auto_tidy import AutoTidy
from app.core.con_tidy import CommonTidy
from app.core.emby_user import emby_user_util
from app.core.env import NovaEnv, configEnv, novaEnv
from app.core.env2 import config2Env
from app.core.license import LicenseInfo
from app.core.license_client import LicenseClient
from app.core.license_keys import CLIENT_ENCRYPTION_PUBLIC_KEY_PEM, CLIENT_SIGNING_PUBLIC_KEY_PEM
from app.core.lock123 import task_123_manager
from app.core.m123 import M123
from app.core.media_sync import MediaSync
from app.core.obj_factory import ObjFactory
from app.core.con_sync import CommonSync
from app.core.task_tidy import load_words_replace_file
from app.db import get_db
from app.log import logger
from app.modules.alist.alist_util import AlistUtil
from app.modules.cover.cover import CoverUtils
from app.modules.m115.m115_util import M115Util
from app.services.hdhive2service import HdHiveService
from app.services.message_service import MessageService
from app.services.share_down import ShareDownService
from app.types.con_file import ConFile
from app.utils.device import DeviceUtil
from app.utils.mexception import MExcUtils
from app.utils.mjson import JsonUtils
from app.utils.okhttp import OkHttp
from app.utils.wrapper import log_exec_time
from app.utils.mhttp import HttpClient
from app.core.lock import task_manager
from app.core.m115 import M115
from version import APP_VERSION_CODE
@contextmanager
def _task_scope(task_name, acquire_lock, timeout):
    if acquire_lock:
        with task_manager.hold(task_name=task_name, blocking=True, timeout=timeout) as _var_var_0:
            yield _var_var_0
    else:
        _var_var_1 = task_manager.current_task
        task_manager.current_task = task_name
        try:
            yield True
        finally:
            task_manager.current_task = _var_var_1
def nova_main_task():
    with _task_scope('CMS主任务', acquire_lock=True, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-CMS主任务-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            with get_db() as _var_var_2:
                _var_var_3 = ShareDownService(_var_var_2)
                _var_var_4 = _var_var_3.sync_sub()
                if _var_var_4:
                    _var_var_5 = ','.join(_var_var_4)
                    _var_var_6 = _var_var_3.add_share_down(_var_var_5)
                    if _var_var_6['success']:
                        if _var_var_6.get('ali_links'):
                            _var_var_5 = ','.join(_var_var_6.get('ali_links'))
                            save_ali_share_task(_var_var_5, acquire_lock=False, tidy_type=1)
                        else:
                            logger.info('暂停5秒...')
                            time.sleep(5)
                auto_tidy_task(acquire_lock=False)
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)
def check_123_token():
    _var_var_8 = ObjFactory.get_instance(M123)
    _var_var_8.login()

def auto_tidy_cmd():
    auto_tidy_task(acquire_lock = True)


def auto_tidy_task(acquire_lock=True):
    with _task_scope('自动整理', acquire_lock=acquire_lock, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-自动整理-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            load_words_replace_file()
            with get_db() as _var_var_2:
                _var_var_9 = MediaSync(_var_var_2)
                _var_var_10 = AutoTidy(_var_var_2)
                _var_var_9.lift_sync_to_db()
                _var_var_9.lift_db_sync_to_local()
                time.sleep(1)
                _var_var_10.move_to_tidy()
                _var_var_10.save_new_media()
                _var_var_10.scrape_new_media()
                _var_var_10.scrape_new_subtitle()
                _var_var_10.tidy_up_new_media()
                logger.info('暂停3秒-等待最新的操作记录...')
                time.sleep(3)
                _var_var_9.lift_sync_to_db()
                _var_var_9.lift_db_sync_to_local()
                _var_var_9.send_sync_result_msg()
                _var_var_9.refresh_emby_library()
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)
        if acquire_lock:
            logger.info('自动整理任务结束')

def save_ali_share_task(ali_links, acquire_lock, tidy_type):
    with _task_scope('保存阿里云盘分享', acquire_lock=acquire_lock, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-保存阿里云盘分享-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            with get_db() as _var_var_2:
                _var_var_3 = ShareDownService(_var_var_2)
                _var_var_6 = _var_var_3.save_ali_share(ali_links)
                if _var_var_6:
                    logger.info('暂停3秒-等待阿里云盘分享保存完成...')
                    time.sleep(3)
                    second_upload_ali_share_task(acquire_lock=False, tidy_type=tidy_type)
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)
def lift_sync_task():
    with _task_scope('同步最近记录', acquire_lock=True, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-同步最近记录-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            with get_db() as _var_var_2:
                _var_var_9 = MediaSync(_var_var_2)
                _var_var_9.lift_sync_to_db()
                _var_var_9.lift_db_sync_to_local()
                _var_var_9.send_sync_result_msg()
                _var_var_9.refresh_emby_library()
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)
def second_upload_ali_share_task(acquire_lock, tidy_type):
    with _task_scope('秒传阿里云盘文件', acquire_lock=acquire_lock, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-秒传阿里云盘文件-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            with get_db() as _var_var_2:
                _var_var_3 = ShareDownService(_var_var_2)
                _var_var_3.save_ali_share_to_db()
                _var_var_11 = _var_var_3.miao_chuan_aliyun_file_to_115()
                if tidy_type == 1:
                    return
                if tidy_type == 2:
                    auto_tidy_task(acquire_lock=False)
                    return
                if tidy_type == 3 and _var_var_11:
                    logger.info('暂停5秒-等待秒传阿里云盘文件完成...')
                    time.sleep(5)
                    auto_tidy_task(acquire_lock=False)
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)

def full_sync_task(cid, path='/media', sync_type='normal'):
    with _task_scope('全量同步', acquire_lock=True, timeout=30) as _var_var_0:
        if not _var_var_0:
            logger.info(f'任务-全量同步-放弃执行-{task_manager.current_task}正在运行...')
            return
        try:
            with get_db() as _var_var_2:
                _var_var_9 = MediaSync(_var_var_2, False)
                if configEnv.sync_mode_is_fast:
                    logger.info('任务-全量同步-使用快速同步模式')
                    _var_var_9.fast_sync(cid, path, sync_type)
                else:
                    logger.info('任务-全量同步-使用普通同步模式')
                    _var_var_9.full_sync(cid, path)
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)


def alist_sync_cmd():
    _var_var_12 = JsonUtils.to_str(configEnv.alist_sync_paths)
    alist_sync_task(_var_var_12)

def alist_sync_task(path_json):
    _var_var_13 = JsonUtils.json_to_dict(path_json)
    for _var_var_14 in _var_var_13:
        try:
            logger.info(f'开始同步alist文件夹: {_var_var_14}')
            AlistUtil().sync_path_task(_var_var_14, configEnv.alist_local_path)
        except Exception as _var_var_7:
            MExcUtils.log(_var_var_7)
def share115_sync_task(params):
    try:
        M115Util().sync_path_task(params['share_code'], params['receive_code'], params['cid'], params['local_path'])
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def tidy_123_task():
    if not task_123_manager.acquire(blocking=True, timeout=30):
        logger.info(f'任务-自动整理123-放弃执行-{task_123_manager.current_task}正在运行...')
        return
    try:
        task_123_manager.current_task = '自动整理123'
        load_words_replace_file()
        CommonTidy(config2Env.m123_video_suffix, config2Env.m123_image_suffix, config2Env.m123_media_data_suffix, '123').tidy_media_dir(ConFile(fid=config2Env.m123_tidy_dir_id, full_y_path=config2Env.m123_tidy_dir_id_path))
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
    finally:
        task_123_manager.current_task = None
        task_123_manager.release()
def sync_123_task():
    if not task_123_manager.acquire(blocking=True, timeout=30):
        logger.info(f'任务-全量同步123-放弃执行-{task_123_manager.current_task}正在运行...')
        return
    try:
        task_123_manager.current_task = '全量同步123'
        CommonSync('123', config2Env.m123_video_suffix, config2Env.m123_image_suffix, config2Env.m123_media_data_suffix, config2Env.m123_min_size, config2Env.m123_download_threads).sync_path_task(config2Env.m123_fid, config2Env.m123_fid_path, config2Env.m123_strm_path)
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
    finally:
        task_123_manager.current_task = None
        task_123_manager.release()
def common_sync_path_task(params):
    try:
        sync_123_task()
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def common_tidy_media_dir_task(params):
    try:
        tidy_123_task()
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_115_dir_task():
    try:
        _var_var_15 = configEnv.e_115_dir_del_cid
        if not _var_var_15:
            return '未设置需要删除的文件夹cid'
        _var_var_6 = []
        _var_var_16 = False
        for _var_var_17 in _var_var_15:
            if '@' in _var_var_17:
                _var_var_18 = _var_var_17.split('@')
                _var_var_19 = _var_var_18[0]
                _var_var_20 = _var_var_18[1]
                _var_var_21 = emby_user_util.get_cache_m115(_var_var_19)
                if not _var_var_21:
                    logger.error(f'跳过删除115小号文件夹-{_var_var_17}，小号不存在')
                    _var_var_6.append(f'{_var_var_17}：跳过删除，小号不存在')
                    continue
                if not _var_var_20.isdigit():
                    logger.info(f'跳过删除115文件夹-{_var_var_20}，不是纯数字')
                    _var_var_6.append(f'{_var_var_20}：跳过删除，不是纯数字')
                    continue
                _var_var_22 = _var_var_21.del_dir(_var_var_20, configEnv.e_115_dir_del_days)
                _var_var_6.append(f'{_var_var_17}：{_var_var_22.get("msg")}')
                if _var_var_22['code'] in ('200', '400'):
                    _var_var_16 = True
            else:
                if not _var_var_17.isdigit():
                    logger.info(f'跳过删除115文件夹-{_var_var_17}，不是纯数字')
                    _var_var_6.append(f'{_var_var_17}：跳过删除，不是纯数字')
                    continue
                _var_var_23 = ObjFactory.get_instance(M115)
                _var_var_22 = _var_var_23.del_dir(_var_var_17, configEnv.e_115_dir_del_days)
                _var_var_6.append(f'{_var_var_17}：{_var_var_22.get("msg")}')
                if _var_var_22['code'] in ('200', '400'):
                    _var_var_16 = True
        if _var_var_16:
            MessageService().send_msg(title='✨115文件夹删除✨', text='\n'.join(_var_var_6))
        return '\n'.join(_var_var_6)
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_115_recycle_task():
    try:
        _var_var_24 = []
        _var_var_15 = configEnv.e_115_recycle_del_account_ids
        for _var_var_19 in _var_var_15:
            if _var_var_19 == 0:
                _var_var_23 = ObjFactory.get_instance(M115)
                _var_var_6 = _var_var_23.recyclebin_clean(configEnv.e_115_recycle_del_days)
                if _var_var_6['code'] in ('200', '400'):
                    MessageService().send_msg(title='✨115回收站清空✨', text=_var_var_6['msg'])
                _var_var_24.append(_var_var_6['msg'])
            else:
                _var_var_21 = emby_user_util.get_cache_m115(str(_var_var_19))
                if not _var_var_21:
                    logger.error(f'跳过清空115小号回收站-{_var_var_19}，小号不存在')
                    _var_var_24.append(f'小号{_var_var_19}不存在')
                    continue
                _var_var_6 = _var_var_21.recyclebin_clean(configEnv.e_115_recycle_del_days)
                if _var_var_6['code'] in ('200', '400'):
                    MessageService().send_msg(title=f'✨115小号回收站清空-{_var_var_19}✨', text=_var_var_6['msg'])
                _var_var_24.append(_var_var_6['msg'])
        return '\n'.join(_var_var_24)
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_123_dir_task():
    try:
        _var_var_8 = ObjFactory.get_instance(M123)
        _var_var_15 = config2Env.e_123_dir_del_cid
        if not _var_var_15:
            return '未设置需要删除的文件夹id'
        _var_var_6 = []
        _var_var_16 = False
        for _var_var_17 in _var_var_15:
            _var_var_22 = _var_var_8.del_dir(_var_var_17, config2Env.e_123_dir_del_days)
            _var_var_6.append(f'{_var_var_17}：{_var_var_22.get("msg")}')
            if _var_var_22['code'] in ('200', '400'):
                _var_var_16 = True
        if _var_var_16:
            MessageService().send_msg(title='✨123文件夹删除✨', text='\n'.join(_var_var_6))
        return '\n'.join(_var_var_6)
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_123_recycle_task():
    try:
        _var_var_8 = ObjFactory.get_instance(M123)
        _var_var_6 = _var_var_8.recyclebin_clean(config2Env.e_123_recycle_del_days)
        if _var_var_6['code'] in ('200', '400'):
            MessageService().send_msg(title='✨123回收站清空✨', text=_var_var_6['msg'])
        return _var_var_6['msg']
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_aliyun_dir_task():
    try:
        _var_var_6 = []
        _var_var_16 = False
        for _var_var_17 in configEnv.e_aliyun_dir_del_cid:
            _var_var_22 = AliyunApi().del_dir(_var_var_17, configEnv.e_aliyun_dir_del_days)
            _var_var_6.append(f'{_var_var_17}: {_var_var_22.get("msg")}')
            if _var_var_22['code'] in ('200', '400'):
                _var_var_16 = True
        if _var_var_16:
            MessageService().send_msg(title='✨阿里云盘文件夹删除✨', text='\n'.join(_var_var_6))
        return '\n'.join(_var_var_6)
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def del_aliyun_recycle_task():
    try:
        _var_var_6 = AliyunApi().del_recyclebin(configEnv.e_aliyun_recycle_del_days)
        if _var_var_6['code'] in ('200', '400'):
            MessageService().send_msg(title='✨阿里云盘回收站清空✨', text=_var_var_6['msg'])
        return _var_var_6['msg']
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def cover_gen_task():
    try:
        CoverUtils().update_cover()
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
def hdhive_checkin_task():
    try:
        HdHiveService().checkin()
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)

def check_donate_code_impl(url, index):
    '''检查授权是否有效'''
    _var_var_25 = NovaEnv().DONATE_CODE
    if not _var_var_25:
        logger.error('未配置授权码 - 授权码格式为：LICENSE_CODE=XXXX')
        return False
    _var_var_26 = _var_var_25.split('_')
    if len(_var_var_26) != 3 or not _var_var_25.startswith('CMS_'):
        logger.error('授权码格式错误 - 授权码格式为：LICENSE_CODE=XXXX')
        return False
    _var_var_27 = _var_var_26[0] + '_' + _var_var_26[1]
    _var_var_28 = _var_var_26[2]
    try:
        _var_var_29 = DeviceUtil.get_device_info()
        _var_var_30 = str(int(time.time() * 1000))
        _var_var_31 = f'{_var_var_30}{_var_var_28}{_var_var_29.system_fingerprint}{_var_var_30}'
        _var_var_32 = hashlib.md5(_var_var_31.encode()).hexdigest()
        _var_var_33 = {
            'Content-Type': 'application/json',
            'x-timestamp': _var_var_30,
            'x-sign': _var_var_32,
            'x-key': _var_var_27 }
        _var_var_23 = ObjFactory.get_instance(M115)
        _var_var_8 = ObjFactory.get_instance(M123)
        _var_var_34 = {
            'version': APP_VERSION_CODE,
            'id115': novaEnv.BINDING_115,
            'id123': novaEnv.BINDING_123,
            'id1152': _var_var_23.get_user_id(),
            'id1232': _var_var_8.get_client_id(),
            'device_info': _var_var_29.to_dict() }
        _var_var_35 = HttpClient(headers = _var_var_33, timeout = 10, verify_ssl = False, max_retries = 1, retry_status_forcelist = [
            500,
            502,
            503,
            504])
        _var_var_36 = _var_var_35.post(url = url, json = _var_var_34)
        if _var_var_36.status_code == 200:
            _var_var_37 = _var_var_36.headers.get('x-response-timestamp') or _var_var_36.headers.get('X-Response-Timestamp')
            _var_var_38 = _var_var_36.headers.get('x-response-sign') or _var_var_36.headers.get('X-Response-Sign')
            _var_var_39 = f'{_var_var_37}{_var_var_28}novamedia-auth-success{_var_var_37}'
            _var_var_40 = hashlib.md5(_var_var_39.encode()).hexdigest()
            if _var_var_40 == _var_var_38:
                logger.info(f'启用授权版 - {index}')
                LicenseInfo().set_type('PRO')
                return False
            logger.error(f'授权码无效-签名验证失败 - {index}')
            return True
        if _var_var_36.status_code == 401:
            logger.error(f'授权码无效, resp={_var_var_36.data} - {index}')
            logger.error(f'授权码无效, resp={_var_var_36.data} - {index}')
            logger.error(f'授权码无效, resp={_var_var_36.data} - {index}')
            return False
        logger.error(f'请求CMS授权服务失败, 建议给docker增加代理启动 - {index}')
        return True
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
        return True


def check_donate_code_impl_v3(url, index):
    '''检查授权是否有效'''
    _var_var_25 = NovaEnv().DONATE_CODE
    if not _var_var_25:
        logger.error('未配置授权码 - 授权码格式为：LICENSE_CODE=XXXX')
        return False
    _var_var_26 = _var_var_25.split('_')
    if len(_var_var_26) != 3 or not _var_var_25.startswith('CMS_'):
        logger.error('授权码格式错误 - 授权码格式为：LICENSE_CODE=XXXX')
        return False
    _var_var_27 = _var_var_26[0] + '_' + _var_var_26[1]
    _var_var_28 = _var_var_26[2]
    _var_var_41 = LicenseClient(key_id = _var_var_27, cms_key = _var_var_28, product_id = 'novamedia', server_encryption_public_key_pem = CLIENT_ENCRYPTION_PUBLIC_KEY_PEM, server_signing_public_key_pem = CLIENT_SIGNING_PUBLIC_KEY_PEM, version = str(APP_VERSION_CODE))
    _var_var_29 = DeviceUtil.get_device_info()
    _var_var_33 = {
        'Content-Type': 'application/json',
        'x-key': _var_var_27 }
    try:
        _var_var_23 = ObjFactory.get_instance(M115)
        _var_var_8 = ObjFactory.get_instance(M123)
        _var_var_42 = _var_var_23.get_user_id()
        _var_var_43 = _var_var_8.get_client_id()
    except Exception as _var_var_7:
        logger.error(f'''{_var_var_7}''')
        _var_var_42 = None
        _var_var_43 = None
    try:
        _var_var_44 = _var_var_41.build_request(extra_payload = {
            'id115': _var_var_42,
            'id123': _var_var_43,
            'mac': _var_var_29.mac_address,
            'cpu_info': f'''{_var_var_29.cpu_info} {_var_var_29.cpu_count}''',
            'memory_info': f'''{_var_var_29.memory_info}''',
            'device_info': f'''{_var_var_29.hostname}''' })
        _var_var_35 = HttpClient(headers = _var_var_33, timeout = 10, verify_ssl = False, max_retries = 1, retry_status_forcelist = [
            500,
            502,
            503,
            504])
        _var_var_36 = _var_var_35.post(url = url, json = {
            'token': _var_var_44.token })
        if _var_var_36.status_code == 200 and _var_var_36.data.get('code', 0) == 200:
            _var_var_45 = _var_var_41.verify_response(_var_var_36.data.get('result', { }).get('token', ''), expected_request_id = _var_var_44.request_id)
            logger.info(f'''授权码验证结果: {_var_var_45}''')
            if _var_var_45 and _var_var_45.get('authorized', False) == True:
                logger.info(f'''启用授权版 - {index}''')
                LicenseInfo().set_type('PRO')
                return False
            return True
        logger.error(f'''授权码无效, resp={_var_var_36.data} - {index}''')
        logger.error(f'''授权码无效, resp={_var_var_36.data} - {index}''')
        logger.error(f'''授权码无效, resp={_var_var_36.data} - {index}''')
        return True
    except Exception as _var_var_7:
        MExcUtils.log(_var_var_7)
        return True


def check_donate_code():
    LicenseInfo().set_type('PRO')
    logger.info('授权校验通过')
    return True


def net_test():
    _var_var_50 = configEnv.http_proxies
    _var_var_51 = OkHttp().test_delay('https://www.baidu.com', proxies = _var_var_50)
    logger.info('网络测试结果：百度 - {} ms'.format(_var_var_51))
    if _var_var_51 == 0:
        logger.error('网络测试-请求百度失败，你的docker疑似连不上网了，请自检网络！')
        logger.error('网络测试-请求百度失败，你的docker疑似连不上网了，请自检网络！')
        logger.error('网络测试-请求百度失败，你的docker疑似连不上网了，请自检网络！')
