from http.cookiejar import CookieJar
from app.core.m115b import M115B
from app.utils.mjson import JsonUtils
from app.log import logger
from app.core.env import configEnv
from app.core.m115_config import M115Config
from p115client import P115Client
import time

class M115v2:
    '''
    115相关操作
    '''
    
    def __init__(self, cookies, app):
        self._M115v2__app = app
        self._M115v2__client = P115Client(cookies = cookies, app = app)
        self._M115v2__m115b = M115B(self._M115v2__client, self.use_open, self.sleep1s)
        return None
        return None

    
    def get_user_id(self):
        return self._M115v2__client.user_id
        return None

    @staticmethod
    def sleep1s(ms):
        if configEnv.api_wait_time:
            ms = configEnv.api_wait_time
        time.sleep(ms)
    
    def login_info(self):
        return self._M115v2__client.login_info(self._M115v2__app, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    @staticmethod
    def login_qrcode_token(app):
        return P115Client.login_qrcode_token(app=app)
    @staticmethod
    def login_qrcode_scan_status(uid, _time, sign):
        _var_var_0 = {'uid': uid, 'time': int(_time), 'sign': sign}
        return P115Client.login_qrcode_scan_status(_var_var_0)
    @staticmethod
    def login_qrcode_scan_result(uid, app):
        return P115Client.login_qrcode_scan_result(*(uid,), **{'app': app, 'cookies': CookieJar()}, **M115Config.get_random_chrome_ua_app())
    
    def use_open(self):
        return False
        return False

    
    def seconds_upload_file(self, name, size, sha1, remote_url, pid, ua):

        def _var_var_1(sign_check):
            return self._M115v2__client.request(
                url=remote_url,
                headers={'range': f'bytes={sign_check}', 'user-agent': ua},
                parse=False,
                timeout=M115Config.REQUEST_TIMEOUT
            )

        _var_var_2 = 100
        _var_var_3 = 100
        _var_var_4 = {}
        if self.use_open():
            for _var_var_5 in range(3):
                try:
                    _var_var_4 = self._M115v2__client.upload_file_init_open(
                        filename=name,
                        filesize=int(size),
                        filesha1=sha1,
                        read_range_bytes_or_hash=_var_var_1,
                        pid=int(pid),
                        timeout=M115Config.REQUEST_TIMEOUT
                    )
                    _var_var_3 = _var_var_4.get('data', {}).get('status', '')
                    _var_var_2 = _var_var_4.get('data', {}).get('code', '')
                except Exception as _var_var_6:
                    _var_var_7 = getattr(_var_var_6, 'code', None)
                    if _var_var_5 >= 2:
                        logger.error('秒传115多次失败，放弃秒传，err={}', _var_var_6)
                        raise
                    if _var_var_7 == 401:
                        logger.warning('检测到 401 未授权，进行秒传重试')
                    continue
        else:
            for _var_var_5 in range(3):
                try:
                    _var_var_4 = self._M115v2__client.upload_file_init(
                        filename=name,
                        filesize=int(size),
                        filesha1=sha1,
                        read_range_bytes_or_hash=_var_var_1,
                        pid=int(pid),
                        timeout=M115Config.REQUEST_TIMEOUT
                    )
                    _var_var_3 = _var_var_4['status']
                    _var_var_2 = _var_var_4.get('statuscode', 0)
                except Exception as _var_var_6:
                    _var_var_7 = getattr(_var_var_6, 'code', None)
                    if _var_var_5 >= 2:
                        logger.error('秒传115多次失败，放弃秒传，err={}', _var_var_6)
                        raise
                    if _var_var_7 == 401:
                        logger.warning('检测到 401 未授权，进行秒传重试')
                    continue

        print(JsonUtils.to_str(_var_var_4))
        if _var_var_2 == 0 and _var_var_3 == 2:
            _var_var_8 = _var_var_4.get('pickcode') or _var_var_4.get('pick_code')
            logger.info(f'秒传115成功-{name} {_var_var_8}')
            return {
                'success': True,
                'file_name': name,
                'file_size': size,
                'sha1': sha1,
                'pick_code': _var_var_8
            }

        if _var_var_2 == 0 and _var_var_3 == 1:
            logger.error(f'秒传115失败-115中没有该文件-{name}')
        elif _var_var_2 == 10014:
            logger.error(f'秒传115失败-cid错误-{name}')
        else:
            logger.error(f'秒传115失败-resp={JsonUtils.to_str(_var_var_4)}')
        return {
            'success': False,
            'statuscode': _var_var_2,
            'statusmsg': _var_var_4.get('statusmsg')
        }
    def download_url_app(self, pick_code, headers):
        return self._M115v2__client.download_url_app(pick_code, headers = headers, app = self._M115v2__app, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def share_download_video_url(self, share_info, headers):
        _var_var_9 = share_info.split('_')
        if len(_var_var_9) != 3:
            logger.error(f'''share_info格式错误 - {share_info}''')
            return None
        return None
        _var_var_10 = _var_var_9[0]
        _var_var_11 = _var_var_9[1]
        _var_var_12 = int(_var_var_9[2])
        _var_var_0 = {
            'share_code': _var_var_10,
            'receive_code': _var_var_11,
            'file_id': _var_var_12 }
        return self._M115v2__client.share_download_url_app(_var_var_0, headers = headers, async_ = True, app = self._M115v2__app, timeout = M115Config.REQUEST_TIMEOUT)
        return None

    
    def fs_files_app(self, payload, sleep, use_open):
        return self._M115v2__m115b.fs_files_app(payload, sleep = sleep, use_open = use_open)
        return None

    
    def fs_delete(self, fid):
        return self._M115v2__m115b.fs_delete(fid)
        return None

    
    def fs_delete_chunk(self, fids):
        return self._M115v2__m115b.fs_delete_chunk(fids)
        return None

    
    def del_dir(self, cid, days):
        return self._M115v2__m115b.del_dir(cid, days)
        return None

    
    def recyclebin_clean_chunk(self, ids):
        return self._M115v2__m115b.recyclebin_clean_chunk(ids)
        return None

    
    def recyclebin_clean(self, days):
        return self._M115v2__m115b.recyclebin_clean(days)
        return None

    
    def recyclebin_list(self, payload):
        return self._M115v2__m115b.recyclebin_list(payload)
        return None



