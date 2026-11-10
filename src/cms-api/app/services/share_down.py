import re
from sqlalchemy.orm import Session
from app.core.env import configEnv
from app.core.obj_factory import ObjFactory
from app.core.media_monitor import MediaImgMonitor
from app.db.clouddata_op import CloudDataOp
from app.db.config_op import ConfigOp
from app.db.models.clouddata import CloudData
from app.db.models.share_down import ShareDown
from app.db.rename_op import RenameOp
from app.db.share_op import ShareDownOp
from app.db.sub_op import SubMediaOp, SubSourceOp
from app.modules.emby.emby import EmbyApi
from app.modules.media.media_util import get_first_char_pinyin
from app.modules.media.video_info import VideoInfo
from app.modules.tg.tg_scraper import TelegramScraper
from app.modules.tmdb.tmdbapi import TmdbApi
from app.log import logger
from app.core.m115 import M115
from app.db.liftlist_op import LiftListOp
from app.services.message_service import MessageService
from app.utils.mjson import JsonUtils
from app.core.aliyun import AliyunApi
from app.utils.partial_fstring import render
from app.utils.share import ShareUtil

class ShareDownService:
    '''
    媒体库同步类
    '''
    
    def __init__(self, db):
        self._db = db
        self._lift_list_op = LiftListOp(self._db)
        self._cloud_data_op = CloudDataOp(self._db)
        self._rename_op = RenameOp(self._db)
        self._config_op = ConfigOp(self._db)
        self._share_down_op = ShareDownOp(self._db)
        self._sub_media_op = SubMediaOp(self._db)
        self._sub_source_op = SubSourceOp(self._db)
        self._ShareDownService__CONFIG = self._config_op.get_all()
        self._ShareDownService__VIDEO_SUFFIX = self._ShareDownService__CONFIG.get('VIDEO_SUFFIX', [
            'mp4',
            'mkv'])
        self._ShareDownService__IMAGE_SUFFIX = self._ShareDownService__CONFIG.get('IMAGE_SUFFIX', [
            'png',
            'jpg'])
        self._ShareDownService__MEDIA_DATA_SUFFIX = self._ShareDownService__CONFIG.get('MEDIA_DATA_SUFFIX', [])
        self._media_img_monitor = MediaImgMonitor()
        self._message_service = MessageService()
        self._tmdbapi = TmdbApi()
        self._aliyun_api = AliyunApi()
        self._emby_api = EmbyApi()
        return None
        return None

    @property
    def _m115(self):
        return ObjFactory.get_instance(M115)
    
    def fs_115_files(self, cid):
        try:
            _var_var_0 = 1150
            _var_var_1 = {'offset': 0, 'limit': _var_var_0, 'cid': cid}
            _var_var_2 = []
            _var_var_4 = self._m115.fs_files_app(_var_var_1, self._ShareDownService__CONFIG['basic'].get('API_WAIT_TIME'))
            if _var_var_4 and 'data' in _var_var_4:
                _var_var_2.extend(_var_var_4['data'])
            return _var_var_2
        except Exception as _var_var_5:
            logger.error('接口列表请求异常')
            logger.exception(_var_var_5)
            return []

    def save_ali_share_to_db(self):
        self._aliyun_api.save_ali_share_to_db()
        return None
        return None

    
    def miao_chuan_aliyun_file_to_115(self):
        '''秒传阿里云盘文件到115'''
        try:
            _var_var_9 = False
            _var_var_10 = self._rename_op.get_by_status(1, 'alipan')
            if not _var_var_10:
                return _var_var_9
            _var_var_11 = {}
            _var_var_12 = self.fs_115_files(configEnv.aliyun_to_115_dir_cid)
            for _var_var_8 in _var_var_12:
                if not _var_var_8.is_dir:
                    continue
                _var_var_11[_var_var_8.name] = _var_var_8.fid
            for _var_var_13 in _var_var_10:
                _var_var_14 = _var_var_13.path.strip().strip('/').strip('\\').split('/')
                _var_var_15 = configEnv.aliyun_to_115_dir_cid
                for _var_var_16 in _var_var_14:
                    if _var_var_16 not in _var_var_11:
                        _var_var_17 = self._m115.fs_mkdir(_var_var_16, _var_var_15)
            return True
        except Exception as _var_var_5:
            logger.exception(_var_var_5)
            logger.error('获取阿里云盘下载链接失败')
            return False


    def add_share_down(self, _url, remove_repeat):
        _var_var_20 = self.get_not_exist_share_down_link(_url, remove_repeat)
        if not _var_var_20['success']:
            return {
                'success': False,
                'msg': _var_var_20['msg'],
                'is_lift_sync': False,
                'ali_links': [] }
        return None
        return self.add_share_down_impl(_var_var_20)
        return None

    
    def get_not_exist_share_down_link(self, _url, remove_repeat):
        _var_var_20 = ShareUtil.get_share_down_link(_url)
        if not _var_var_20['success']:
            return {
                'success': False,
                'msg': '提取分享链接失败',
                'is_lift_sync': False,
                'ali_links': [] }
        return None
        if remove_repeat:
            return self.remove_exist_share_link(_var_var_20)
        return None
        return _var_var_20
        return None

    
    def remove_exist_share_link(self, share_down_info):
        '''去除已存在分享链接'''
        _var_var_21 = []
        _var_var_22 = []
        _var_var_23 = []
        _var_var_24 = []
        _var_var_25 = False
        for _var_var_26 in share_down_info['share_links']:
            _var_var_27 = 's\\/(\\w+)\\?password=(\\w{4})'
            _var_var_28 = re.search(_var_var_27, _var_var_26)
            if _var_var_28:
                _var_var_29 = _var_var_28.group(1)
            else:
                logger.error(f'''提取share_id失败: {_var_var_26}''')
            _var_var_30 = self._share_down_op.get_by_share_id(_var_var_29)
            if _var_var_30:
                continue
            _var_var_25 = True
            _var_var_21.append(_var_var_26)
        for _var_var_26 in share_down_info['ali_links']:
            _var_var_31 = re.search('https://www\\.(?:alipan|aliyundrive)\\.com/s/([a-zA-Z0-9]+)', _var_var_26)
            if _var_var_31:
                _var_var_29 = _var_var_31.group(1)
            else:
                logger.error(f'''提取share_id失败: {_var_var_26}''')
            _var_var_30 = self._share_down_op.get_by_share_id(_var_var_29)
            if _var_var_30:
                continue
            _var_var_25 = True
            _var_var_22.append(_var_var_26)
        for _var_var_26 in share_down_info['magnet_links']:
            _var_var_30 = self._share_down_op.get_by_share_id(_var_var_26)
            if _var_var_30:
                continue
            _var_var_25 = True
            _var_var_24.append(_var_var_26)
        for _var_var_26 in share_down_info['ed2k_links']:
            _var_var_30 = self._share_down_op.get_by_share_id(_var_var_26)
            if _var_var_30:
                continue
            _var_var_25 = True
            _var_var_23.append(_var_var_26)
        share_down_info = {
            'success': _var_var_25,
            'msg': '提取分享链接成功' if _var_var_25 else '当前分享链接已存在，请先去转存记录删除。',
            'share_links': _var_var_21,
            'ali_links': _var_var_22,
            'magnet_links': _var_var_24,
            'ed2k_links': _var_var_23 }
        logger.info(f'''去除已存在分享链接后: {share_down_info}''')
        return share_down_info
        return None

    
    def add_share_down_impl(self, share_down_info):
        '''添加分享下载任务'''
        _var_var_21 = share_down_info['share_links']
        _var_var_24 = share_down_info['magnet_links']
        _var_var_23 = share_down_info['ed2k_links']
        _var_var_22 = share_down_info['ali_links']
        _var_var_9 = False
        for _var_var_26 in _var_var_21:
            logger.info(f'''添加保存分享任务: {_var_var_26}''')
            _var_var_32 = self._m115.share_receive_by_url(_var_var_26, configEnv.share_down_dir_cid)
            _var_var_33 = 1
            self._message_service.send_msg(title = _var_var_34, text = _var_var_35, userid = '')
            self._share_down_op.save(ShareDown(type = 'share_115', share_id = _var_var_32.get('share_id'), share_pwd = _var_var_32.get('share_pwd'), share_name = _var_var_32.get('share_name'), status = _var_var_33, remark = _var_var_32.get('error')))
        if _var_var_24:
            logger.info(f'''添加离线下载任务: {_var_var_24}''')
            _var_var_32 = self._m115.offline_add_urls(_var_var_24, configEnv.share_down_dir_cid)
            _var_var_33 = 1
            _var_var_35 = '\n'.join(_var_var_24)
            if _var_var_32['state']:
                _var_var_9 = True
                _var_var_34 = '云下载任务创建成功 (磁力)'
            else:
                _var_var_33 = 2
                _var_var_34 = '云下载任务创建失败 (磁力)'
                _var_var_35 = f'''{_var_var_32.get('error_msg')}\n{_var_var_35}'''
            self._message_service.send_msg(title = _var_var_34, text = _var_var_35, userid = '')
            for _var_var_36 in _var_var_24:
                self._share_down_op.save(ShareDown(type = 'magnet', share_id = _var_var_36, status = _var_var_33, remark = _var_var_32.get('error_msg')))
        if _var_var_23:
            logger.info(f'''添加ed2k下载任务: {_var_var_23}''')
            _var_var_32 = self._m115.offline_add_urls(_var_var_23, configEnv.share_down_dir_cid)
            _var_var_33 = 1
            _var_var_35 = '\n'.join(_var_var_23)
            if _var_var_32['state']:
                _var_var_9 = True
                _var_var_34 = '转存成功 (ed2k)'
            else:
                _var_var_33 = 2
                _var_var_34 = '转存失败 (ed2k)'
                _var_var_35 = f'''原因: {_var_var_32.get('error_msg')}\n{_var_var_35}'''
            self._message_service.send_msg(title = _var_var_34, text = _var_var_35, userid = '')
            for _var_var_36 in _var_var_23:
                _var_var_37 = re.search('\\|file\\|([^|]+)\\|', _var_var_36).group(1)
                self._share_down_op.save(ShareDown(type = 'ed2k', share_id = _var_var_36, share_name = _var_var_37, status = _var_var_33, remark = _var_var_32.get('error_msg')))
        return {
            'success': True,
            'msg': '添加成功',
            'is_lift_sync': _var_var_9,
            'ali_links': _var_var_22 }
        return None

    
    def save_ali_share(self, links):
        if not links:
            return False
        return False
        _var_var_22 = links.split(',')
        for _var_var_26 in _var_var_22:
            logger.info(f'''添加阿里云盘分享转存任务: {_var_var_26}''')
            _var_var_32 = self._aliyun_api.save_share_link(_var_var_26)
            self._message_service.send_msg(title = _var_var_34, text = _var_var_35, userid = '')
        return True
        return True

    
    def sync_sub(self):
        '''同步订阅处理逻辑'''
        _var_var_38 = []
        _var_var_39 = self._sub_source_op.list(type=None, status=1)
        _var_var_40 = self._sub_media_op.get_by_status(1)
        if not _var_var_39 or not _var_var_40:
            return _var_var_38
        for _var_var_41 in _var_var_40:
            try:
                logger.info(f'开始处理订阅: {_var_var_41.title} ({_var_var_41.year})')
                _var_var_42 = 0
                _var_var_43 = {
                    'title': _var_var_41.title,
                    'first_letter': get_first_char_pinyin(_var_var_41.title),
                    'year': _var_var_41.year,
                    'tmdb_id': _var_var_41.tmdb_id
                }
            except Exception as _var_var_5:
                logger.error(f'订阅处理异常: {_var_var_5}')
                continue
        return _var_var_38

    def get_max_ep(eps):
        _var_var_54 = 0
        _var_var_42 = 0
        for _var_var_62 in eps:
            _var_var_63 = int(_var_var_62[1:].split('E')[0])
            _var_var_64 = int(_var_var_62.split('E')[1])
            if _var_var_63 > _var_var_54:
                _var_var_54 = _var_var_63
                _var_var_42 = _var_var_64
            elif _var_var_63 == _var_var_54 and _var_var_64 > _var_var_42:
                _var_var_42 = _var_var_64
        return _var_var_54, _var_var_42
    @staticmethod
    def is_sub_success(season_num, episode_num, tmdb_info):
        if not tmdb_info:
            return False
        _var_var_65 = tmdb_info.get('status', 'unknow')
        _var_var_66 = tmdb_info.get('next_episode_to_air', {})
        _var_var_67 = tmdb_info.get('last_episode_to_air', {})
        if not _var_var_67:
            return False
        _var_var_68 = _var_var_67.get('episode_type', '')
        _var_var_69 = _var_var_68 == 'finale'
        if _var_var_67:
            logger.info(f"当前媒体库已有S{season_num}E{episode_num}，tmdb中status={_var_var_65}，最后一集为S{_var_var_67.get('season_number', '')}E{_var_var_67.get('episode_number', '')} {_var_var_68}")
        if _var_var_65 == 'Ended' and _var_var_69 and int(season_num) >= int(_var_var_67.get('season_number', '0')) and int(episode_num) >= int(_var_var_67.get('episode_number', '0')):
            return True
        return False
