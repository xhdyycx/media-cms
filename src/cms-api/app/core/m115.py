import httpx
from app.core.m115b import M115B
from app.utils.m115_util import M115Utils
from app.utils.mutil import Mutil
from app.utils.mjson import JsonUtils
from app.utils.ko_util import chunk_list, save_file
from app.log import logger
from app.core.env import novaEnv, configEnv
from app.core.m115_config import M115Config
from p115client import P115Client
import re
import time
import threading
from datetime import datetime
from pathlib import Path

class M115:
    '''
    115相关操作
    '''
    __client: P115Client = None
    __android = 'android'
    __USE_OPEN_API = False
    __OPEN_API_STATUS = False
    __ENABLE = True
    __TOKEN_EXPIRES_TIME = 0
    __REFRESH_FAIL_TIME = 0
    __REFRESH_TOKEN_LOCK = threading.Lock()
    MONITOR_BEHAVIOR = [
        'upload_file',
        'upload_image_file',
        'receive_files',
        'copy_folder',
        'new_folder',
        'delete_file',
        'folder_rename',
        'move_file',
        'move_image_file',
        'copy_file',
        'rename_file']
    
    def __init__(self, path, device):
        self._CONFIG_ENV = configEnv
        if not path:
            path = f'''{novaEnv.CONFIG_PATH}/115-cookies.txt'''
        if not Path(path).exists():
            save_file(path, '')
            logger.error(f'''{path}不存在，已创建，请重新扫描登录''')
            return None
        self._M115__device = device
        self.__client = P115Client(Path(path).expanduser(), app = M115Config.get_ios_ua_app()['app'])
        self._M115__m115b = M115B(self.__client, self.use_open, self.sleep1s)
        self.life_calendar_setoption()
        self.login_another_open()
        self.check_binding()

    
    def check_binding(self):
        if not novaEnv.BINDING_123 and novaEnv.BINDING_115:
            self.__client.cookies = ''
            self.__ENABLE = False
            logger.error('请指定docker变量 BINDING_115=xxx，值为你的115号（账号ID）')
        if novaEnv.BINDING_115 and self.__client.user_id != int(novaEnv.BINDING_115):
            self.__client.cookies = ''
            self.__ENABLE = False
            logger.error('已在环境变量指定BINDING_115=xxx，不能使用其它115账号')
        return None
        return None

    
    def get_user_id(self):
        return self.__client.user_id
        return None

    
    def use_open(self):
        if not self.__ENABLE:
            return False
        _var_var_0 = int(time.time())
        if self.__USE_OPEN_API and _var_var_0 > self.__TOKEN_EXPIRES_TIME and _var_var_0 > self.__REFRESH_FAIL_TIME:
            self.refresh_token()
        return self.__USE_OPEN_API and self.__OPEN_API_STATUS

    
    def refresh_token(self):
        locked = self.__REFRESH_TOKEN_LOCK.acquire(timeout = 30)
        if not locked:
            logger.warning('刷新openapi访问token等待锁超时(30秒)，跳过本次刷新')
            return None
        try:
            now = int(time.time())
            if now <= self.__TOKEN_EXPIRES_TIME:
                self.__REFRESH_TOKEN_LOCK.release()
                return None
            res = self.__client.login_refresh_token_open(self.__client.refresh_token, **M115Config.get_ios_ua())
            if res['state']:
                self.__client.refresh_token = res['data']['refresh_token']
                self.__client.access_token = res['data']['access_token']
                self.__TOKEN_EXPIRES_TIME = int(time.time()) + int(res['data']['expires_in']) - 300
                self.__OPEN_API_STATUS = True
                logger.info(f'''刷新openapi访问token成功，有效期为：{res['data']['expires_in']}秒''')
            elif res.get('code') == 40140116:
                logger.info('检测到原授权已失效，尝试重新登录获取授权')
                self.login_another_open()
            else:
                self.__OPEN_API_STATUS = False
                self.__REFRESH_FAIL_TIME = int(time.time()) + 600
                logger.error(f'''刷新openapi访问token失败-{JsonUtils.to_str(res)}''')
            self.__REFRESH_TOKEN_LOCK.release()
        except:
            # 异常表 316..1032 -> handler 只做 release + RERAISE，即裸 except 释放锁后原样抛出
            self.__REFRESH_TOKEN_LOCK.release()
            raise
    def login_another_open(self):
        try:
            if self._CONFIG_ENV.use_115_open_api and self._CONFIG_ENV.m115_app_id:
                self.__client.login_another_open(self._CONFIG_ENV.m115_app_id, replace = True, **M115Config.get_ios_ua())
                self.__USE_OPEN_API = True
                self.__TOKEN_EXPIRES_TIME = int(time.time()) + 6000
                self.__OPEN_API_STATUS = True
                logger.info('115 OPENAPI 登录成功')
                return True
        except Exception as e:
            logger.error(f'''115 OPENAPI 登录失败 - {e.__str__()}''')
        self.__USE_OPEN_API = False
        return False
    def life_calendar_setoption(self):
        res = self.__client.life_calendar_setoption(**M115Config.get_ios_ua_app())
        if res['state']:
            logger.info('115生活事件启用成功')
        else:
            logger.error(f'''115生活事件启用失败-{JsonUtils.to_str(res)}''')
    def life_clear_history(self):
        res = self.__client.life_clear_history(**M115Config.get_ios_ua_app())
        if res['state']:
            logger.info('115生活事件清空成功')
        else:
            logger.error(f'''115生活事件清空失败-{JsonUtils.to_str(res)}''')
    # 原名被 pyarmor 抹为 _var_var_N，此处按语义命名：
    #   _var_var_4=page_size(30) _var_var_5=max_limit(1000) _var_var_6=fail_count(0)
    #   _var_var_7=first_page(True) _var_var_8=params _var_var_2=res _var_var_9=i _var_var_10=item
    #   _var_var_11=behavior_type _var_var_3=e
    def life_behavior_sync(self, max_id, collect):
        logger.info('开始获取最新115生活事件...')
        page_size = 30
        max_limit = 1000
        fail_count = 0
        first_page = True
        params = {'offset': 0, 'limit': page_size}
        while fail_count < 1:
            try:
                res = self.__client.life_behavior_detail_app(params, **M115Config.get_ios_ua_app())
                if not res['state']:
                    logger.error(f'''获取生活事件失败-{JsonUtils.to_str(res)}''')
                    if res['error'] == '请重新登录':
                        logger.error('cookie失效，请重新扫描登录')
                    return None
                logger.info(f'''获取到{len(res['data']['list'])}条生活事件...''')
                for i, item in enumerate(res['data']['list']):
                    if max_id and int(item['id']) <= int(max_id):
                        logger.info(f'''新事件匹配完成-结束获取-{item['id']}''')
                        return None
                    behavior_type = M115Config.BEHAVIOR_TYPE_TO_NAME_MY.get(item['type'], '')
                    item['behavior_type'] = behavior_type
                    item['update_time_str'] = str(datetime.fromtimestamp(item['update_time']))
                    if first_page and i == 0:
                        collect(item)
                        continue
                    if behavior_type not in self.MONITOR_BEHAVIOR:
                        continue
                    collect(item)
                if not res['data']['next_page']:
                    logger.info('获取到所有事件-结束获取')
                    break
                params['limit'] = max_limit
                if first_page:
                    params['offset'] += page_size
                    first_page = False
                else:
                    params['offset'] += max_limit
                logger.info(f'''3s后开始获取下一页-{params}''')
                time.sleep(3)
            except Exception as e:
                logger.exception(e)
                fail_count += 1
    @staticmethod
    def sleep1s(ms=1):
        if configEnv.api_wait_time:
            ms = configEnv.api_wait_time
        time.sleep(ms)
    
    def upload_file(self, local_file_path, file_name, pid):
        self.sleep1s()
        if self.use_open():
            return self.__client.upload_file_open(file = local_file_path, pid = pid, filename = file_name, timeout = M115Config.REQUEST_TIMEOUT)
        return None
        return self.__client.upload_file(file = local_file_path, pid = pid, filename = file_name, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def seconds_upload_file(self, name, size, sha1, remote_url, pid):
        
        def _var_var_12(sign_check):
            '''读取 115 秒传校验所需的远端文件分片。'''
            _var_var_18 = httpx.get(remote_url, headers = {
                'Range': f'''bytes={sign_check}''' }, follow_redirects = True, timeout = 30)
            _var_var_18.raise_for_status()
            return _var_var_18.content

        self.sleep1s()
        _var_var_13 = 100
        _var_var_14 = 100
        _var_var_2 = { }
        if self.use_open():
            logger.info(f'''使用openapi接口秒传115文件-{name}''')
            for _var_var_15 in range(3):
                try:
                    _var_var_2 = self.__client.upload_file_init_open(filename = name, filesize = int(size), filesha1 = sha1, read_range_bytes_or_hash = _var_var_12, pid = int(pid), timeout = M115Config.REQUEST_TIMEOUT)
                    _var_var_14 = _var_var_2.get('data', { }).get('status', '')
                    _var_var_13 = _var_var_2.get('data', { }).get('code', '')
                except Exception as _var_var_16:
                    _var_var_17 = getattr(_var_var_16, 'code', None)
                    if _var_var_15 == 2:
                        logger.error('秒传115多次失败，放弃秒传，err={}', _var_var_16)
                        raise
                    if _var_var_17 == 401:
                        logger.warning('检测到 401 未授权，1s后进行秒传重试')
                        time.sleep(1)
        else:
            for _var_var_15 in range(3):
                try:
                    _var_var_2 = self.__client.upload_file_init(filename = name, filesize = int(size), filesha1 = sha1, read_range_bytes_or_hash = _var_var_12, pid = int(pid), timeout = M115Config.REQUEST_TIMEOUT)
                    _var_var_14 = _var_var_2['status']
                    _var_var_13 = _var_var_2.get('statuscode', 0)
                except Exception as _var_var_16:
                    _var_var_17 = getattr(_var_var_16, 'code', None)
                    if _var_var_15 == 2:
                        logger.error('秒传115多次失败，放弃秒传，err={}', _var_var_16)
                        raise
                    if _var_var_17 == 401:
                        logger.warning('检测到 401 未授权，1s后进行秒传重试')
                        time.sleep(1)
        if _var_var_13 == 0 and _var_var_14 == 2:
            logger.info(f'''秒传115成功-{name}''')
            return {
                'success': True,
                'file_name': name,
                'file_size': size,
                'sha1': sha1 }
        if _var_var_13 == 0 and _var_var_14 == 1:
            logger.error(f'''秒传115失败-115中没有该文件-{name}''')
        else:
            logger.error(f'''秒传115失败-resp={JsonUtils.to_str(_var_var_2)}''')
        return {
            'success': False }

    
    def login_info(self):
        return self.__client.login_info(**M115Config.get_ios_ua_app())
    def fs_delete(self, fid):
        return self._M115__m115b.fs_delete(fid)
        return None

    
    def fs_delete_chunk(self, fids):
        return self._M115__m115b.fs_delete_chunk(fids)
        return None

    
    def del_dir(self, cid, days):
        return self._M115__m115b.del_dir(cid, days)
        return None

    
    def recyclebin_clean_chunk(self, ids):
        return self._M115__m115b.recyclebin_clean_chunk(ids)
        return None

    
    def recyclebin_clean(self, days):
        return self._M115__m115b.recyclebin_clean(days)
        return None

    
    def recyclebin_list(self, payload):
        return self._M115__m115b.recyclebin_list(payload)
        return None

    
    def fs_files_app(self, payload, sleep):
        return self._M115__m115b.fs_files_app(payload, sleep = sleep, use_open = self.use_open())
        return None

    
    def get_auto_tidy_data_v2(self, cid, limit):
        return self._M115__m115b.get_auto_tidy_data_v2(cid, limit)
        return None

    
    def fs_category_get(self, cid):
        return self.__client.fs_category_get_app(cid, **M115Config.get_ios_ua_app())
    def download_url(self, pick_code, headers):
        return self.__client.download_url_app(pick_code, headers = headers, app = M115Config.get_ios_ua_app()['app'], timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def download_pick_code(self, pick_code, path):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 AppleWebKit/600 Safari/600 Chrome/124.0.0.0'}
        headers = M115Config.get_ios_ua_app()['headers']
        try:
            if self.use_open():
                url = self.download_url_open(pick_code, headers = headers)
            else:
                res = self.download_url(pick_code, headers)
                if not res or not res['state']:
                    logger.error(f'''获取直连失败 - {pick_code} res={JsonUtils.to_str(res)}''')
                    return None
                url = res['data']['url']
            Mutil.download_file_v2(url, path, headers)
        except Exception as e:
            logger.error(f'''下载文件失败 - {path}''')
            logger.exception(e)
    def download_share_file(self, share_code, receive_code, fid, path):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        payload = {
            'share_code': share_code,
            'receive_code': receive_code,
            'file_id': fid}
        try:
            res = self.__client.share_download_url_app(payload, headers = headers, async_ = False, app = 'ios', timeout = M115Config.REQUEST_TIMEOUT)
            if not res or not res['state']:
                logger.error(f'''获取分享直连失败 - share_code={share_code} - receive_code={receive_code} - fid={fid} - path={path}''')
                logger.error(JsonUtils.to_str(res))
                return None
            url = res['data']['url']['url']
            Mutil.download_file_v2(url, path, headers)
        except Exception as e:
            logger.error(f'''下载分享文件失败 - {path}''')
            logger.exception(e)
    def download_url_open_async(self, pick_code, headers):
        return self.__client.download_url_info_open(pick_code, headers = headers, app = M115Config.get_ios_ua_app()['app'], async_ = True, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def download_url_app_async(self, pick_code, headers):
        return self.__client.download_url_app(pick_code, headers = headers, app = M115Config.get_ios_ua_app()['app'], async_ = True, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def download_url_app(self, pick_code, headers):
        return self.__client.download_url_app(pick_code, headers = headers, app = M115Config.get_ios_ua_app()['app'], timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def download_url_chrome(self, pick_code, headers):
        return self.__client.download_url_app(pick_code, headers = headers, app = 'chrome', timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def to_id(self, pick_code):
        return self.__client.to_id(pick_code)
        return None

    
    def download_url_open(self, pick_code, headers):
        return self.__client.download_url_open(pick_code, headers = headers, app = M115Config.get_ios_ua_app()['app'], timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def share_download_video_url(self, share_info, headers):
        _var_var_22 = share_info.split('_')
        if len(_var_var_22) != 3:
            logger.error(f'''share_info格式错误 - {share_info}''')
            return None
        _var_var_23 = _var_var_22[0]
        _var_var_24 = _var_var_22[1]
        _var_var_25 = int(_var_var_22[2])
        _var_var_8 = {
            'share_code': _var_var_23,
            'receive_code': _var_var_24,
            'file_id': _var_var_25 }
        return self.__client.share_download_url_app(_var_var_8, headers = headers, async_ = True, app = 'ios', timeout = M115Config.REQUEST_TIMEOUT)

    
    def share_receive_by_url(self, share_url, cid):
        _var_var_26 = 's\\/(\\w+)\\?password=(\\w{4})'
        _var_var_27 = re.search(_var_var_26, share_url)
        if _var_var_27:
            _var_var_23 = _var_var_27.group(1)
            _var_var_24 = _var_var_27.group(2)
            _var_var_28 = self.share_snap(_var_var_23, _var_var_24, '')
            if not _var_var_28['state']:
                return {
                    'state': False,
                    'error': _var_var_28.get('error') or '提取分享码和接收码失败',
                    'errno': 'CMS-100002',
                    'share_id': _var_var_23,
                    'share_pwd': _var_var_24,
                    'share_name': '' }
            _var_var_29 = _var_var_28['data']
            _var_var_30 = []
            for _var_var_10 in _var_var_29:
                if int(_var_var_10['cid']) == 0:
                    _var_var_30.append(_var_var_10['fid'])
                    continue
                _var_var_30.append(_var_var_10['cid'])
            _var_var_31 = self.share_receive(_var_var_23, _var_var_24, _var_var_30, cid)
            logger.info(f'''share_receive.resp={JsonUtils.to_str(_var_var_31)}''')
            _var_var_31['share_url'] = f'''https://115.com/s/{_var_var_23}?password={_var_var_24}'''
            _var_var_31['share_id'] = _var_var_23
            _var_var_31['share_pwd'] = _var_var_24
            _var_var_31['share_name'] = _var_var_28['share_name']
            return _var_var_31
        return {
            'state': False,
            'error': '提取分享码和接收码失败',
            'errno': 'CMS-100001',
            'share_id': '',
            'share_pwd': '',
            'share_name': '' }

    
    def share_receive(self, share_code, receive_code, fids, cid):
        '''接收分享链接的某些文件或文件夹
        payload:
            - share_code: str
            - receive_code: str
            - fids: str | list             # 有多个时，用逗号 "," 分隔
            - cid: int | str = <default>     # 这是你网盘的文件夹 cid
        '''
        if isinstance(fids, int):
            file_id = fids
        elif isinstance(fids, str):
            file_id = int(fids)
        elif isinstance(fids, list):
            file_id = ','.join(fids)
        else:
            raise TypeError('fids格式错误')
        payload = {
            'share_code': share_code,
            'receive_code': receive_code,
            'file_id': file_id,
            'cid': cid,
            'user_id': self.__client.user_id}
        return self.__client.share_receive(payload, **M115Config.get_ios_ua_app())
    # 原名被 pyarmor 抹为 _var_var_N，此处按语义命名：
    #   _var_var_32=offset(0) _var_var_33=limit(1000) _var_var_34=items([])
    #   _var_var_28=result({}) _var_var_8=payload _var_var_35=resp _var_var_10=item
    def share_snap(self, share_code, receive_code, cid):
        '''获取分享链接的某个文件夹中的文件和子文件夹的列表（包含详细信息）
        payload:
            - share_code: str
            - receive_code: str
            - cid: int | str = 0
            - limit: int = 32
            - offset: int = 0
            - asc: 0 | 1 = <default> # 是否升序排列
            - o: str = <default>
                # 用某字段排序：
                # - 文件名："file_name"
                # - 文件大小："file_size"
                # - 文件种类："file_type"
                # - 修改时间："user_utime"
                # - 创建时间："user_ptime"
                # - 上次打开时间："user_otime"
        '''
        offset = 0
        limit = 1000
        items = []
        result = {}
        while True:
            payload = {
                'share_code': share_code,
                'receive_code': receive_code,
                'cid': cid,
                'offset': offset,
                'limit': limit,
                'o': 'file_name'}
            resp = self.__client.share_snap_app(payload, **M115Config.get_ios_ua_app())
            logger.info(JsonUtils.to_str(resp))
            result['state'] = resp['state']
            result['error'] = resp.get('error')
            if not resp['state']:
                logger.error(f'''115.share_snap.resp={JsonUtils.to_str(resp)}''')
                break
            result['share_name'] = resp['data']['shareinfo']['share_title']
            items += resp['data']['list']
            if resp['data']['count'] <= offset + limit:
                break
            offset += limit
            self.sleep1s()
        for item in items:
            if not item.get('cid'):
                item['cid'] = item.get('pid')
            if not item.get('sha'):
                item['sha'] = item.get('sha1')
            if item.get('sha'):
                item['cid'] = item.get('pid')
            else:
                item['cid'] = item.get('fid')
                item['pid'] = item.get('pid')
            if not item.get('n'):
                item['n'] = item.get('fn')
            if not item.get('s'):
                item['s'] = item.get('fs')
            if item.get('u'):
                continue
            if not item.get('thumb'):
                continue
            item['u'] = f'''https://imgjump.115.com{item.get('thumb')}&size=0&sha1={item.get('sha', '')}'''
        result['data'] = items
        return result
    def offline_add_urls(self, urls, cid):
        if self.use_open():
            res = self.__offline_add_urls_open(urls, cid)
            logger.info(f'''offline_add_urls_open.resp={JsonUtils.to_str(res)}''')
            res['error_msg'] = res.get('message')
            return res
        payload = {f'''url[{i}]''': url for i, url in enumerate(urls)}
        payload['wp_path_id'] = str(cid)
        res = self.__client.clouddownload_task_add_urls(payload, **M115Config.get_ios_ua_app())
        logger.info(f'''clouddownload_task_add_urls.resp={JsonUtils.to_str(res)}''')
        return res
    def __offline_add_urls_open(self, urls, cid):
        if isinstance(urls, (list, set)):
            urls = '\n'.join(urls)
        payload = {
            'urls': urls,
            'wp_path_id': cid}
        return self.__client.request(url = 'https://proapi.115.com/open/offline/add_task_urls', method = 'POST', data = payload, **M115Config.get_ios_ua_app())
    def fs_mkdir(self, name, cid):
        self.sleep1s()
        if self.use_open():
            res = self.__client.fs_mkdir_open(name, pid = cid, **M115Config.get_ios_ua_app())
            if not res.get('state'):
                logger.error(f'''fs_mkdir_open.resp={JsonUtils.to_str(res)}''')
                return res
            res['cid'] = res['data']['file_id']
            return res
        return self.__client.fs_mkdir(name, pid = cid, **M115Config.get_ios_ua_app())
    # [静态推断] 该 code object 在任务包内只有 [Names]/[Constants]，Disassembly 段缺失，
    # 指令级依据不可得。以下按 [Names]（sleep1s / use_open / fs_move_open / logger.info /
    # JsonUtils.to_str / join / fs_move）与本文件 fs_mkdir 的对称写法还原，行级逻辑未逐条对指令核验。
    def fs_move(self, fids, pid):
        self.sleep1s()
        if self.use_open():
            res = self.__client.fs_move_open(fids, pid, **M115Config.get_ios_ua_app())
            logger.info(f'''fs_move_open.resp={JsonUtils.to_str(res)}''')
            return res
        return self.__client.fs_move(','.join(fids), pid, **M115Config.get_ios_ua_app())
    def fs_move_chunk(self, fids, pid):
        _var_var_38 = list(chunk_list(fids, 500))
        for _var_var_36, _var_var_39 in enumerate(_var_var_38):
            _var_var_2 = self.fs_move(_var_var_39, pid)
            if _var_var_36 == len(_var_var_38) - 1:
                break
            time.sleep(3)
        return None

    
    def fs_rename(self, fid_names):
        self.sleep1s()
        return self.__client.fs_rename(fid_names, **M115Config.get_ios_ua_app())
    def login_qrcode_token(self):
        try:
            return self.__client.login_qrcode_token(**M115Config.get_chrome_ua_app())
        except ModuleNotFoundError as e:
            logger.exception(e)
            logger.error(f'''获取115登录二维码失败, {str(e)}''')
    def login_qrcode_scan_status(self, uid, _time, sign):
        payload = {
            'uid': uid,
            'time': int(_time),
            'sign': sign}
        return self.__client.login_qrcode_scan_status(payload, **M115Config.get_chrome_ua_app())
    def login_qrcode_scan_result(self, uid, app):
        return self.__client.login_qrcode_scan_result(uid, app = app, headers = M115Config.get_chrome_ua_app()['headers'], timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    # 原名被 pyarmor 抹为 _var_var_N，此处按语义命名：
    #   _var_var_31=res _var_var_40=names([]) _var_var_41=p _var_var_42=file_name
    #   _var_var_43=cur _var_var_44=full_path _var_var_45=paths
    def fs_category_get_app(self, cid):
        res = self.__client.fs_category_get_app(cid, **M115Config.get_ios_ua_app())
        logger.info(f'''115.fs_category_get_app.data={JsonUtils.to_str(res)}''')
        if not res:
            logger.error('输入的cid有误')
            return None
        if 'state' in res and not res['state']:
            logger.error('state==False，cookie可能已过期，请重新扫描登录')
            return None
        names = []
        for p in res['paths']:
            if 'file_name' not in p:
                continue
            file_name = p['file_name']
            if file_name == '根目录':
                continue
            names.append(file_name)
        cur = res.get('file_name', '')
        if cur:
            if not names or names[-1] != cur:
                names.append(cur)
        full_path = '/'.join(names)
        if not full_path.startswith('/'):
            full_path = '/' + full_path
        res['full_path'] = full_path
        paths = res['paths']
        res['pid'] = paths[-1]['file_id']
        res['pname'] = paths[-1]['file_name']
        return res
    def move_dir1_dir2(self, cid1, cid2, tag):
        if not cid1 or cid2:
            return None
        _var_var_8 = {
            'offset': 0,
            'limit': 1150,
            'cid': cid1 }
        _var_var_2 = self.fs_files_app(_var_var_8, self._CONFIG_ENV.api_wait_time)
        _var_var_46 = []
        for _var_var_10 in _var_var_2['data']:
            _var_var_46.append(_var_var_10['fid'])
        if _var_var_46:
            time.sleep(3)
            logger.info(f'''自动整理-暂停3s，等待移动{tag}''')
            self.fs_move_chunk(_var_var_46, cid2)
            logger.info(f'''自动整理-移动{tag}-成功''')

    
    def get_copy_pick_code(self, fid, pid, name):
        res = self.__client.fs_copy_app(fid, pid, **M115Config.get_ios_ua_app())
        if not res['state']:
            logger.error(f'''fs_copy_app={JsonUtils.to_str(res)}''')
            return None
        params = {
            'offset': 0,
            'limit': 32,
            'cid': pid,
            'asc': 0,
            'fc_mix': 1,
            'o': 'user_utime'}
        files = self.fs_files_app(params)
        for f in files['data']:
            if f['is_dir']:
                continue
            name = name.rsplit('.', 1)[0]
            if not f['name'].startswith(name):
                continue
            return f['pick_code']
    def iter_all_dirs_v2(self, cid, local_path, func):
        self._M115__m115b.iter_all_dirs_v2(cid, local_path, func)
        return None
        return None

    
    def iter_files_with_path_kk(self, cid, video_suffix, img_suffix, nfo_suffix, local_path, func):
        self._M115__m115b.iter_files_with_path_kk(cid, video_suffix, img_suffix, nfo_suffix, local_path, func)
        return None
        return None

    
    def get_all_file_and_base_path(self, cid):
        return self._M115__m115b.get_all_file_and_path(cid)
        return None

