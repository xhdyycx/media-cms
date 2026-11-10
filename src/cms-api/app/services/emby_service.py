from datetime import datetime
import re
from sqlalchemy.orm import Session
from app.core.con_storage import StorageApi
from app.core.env2 import config2Env
from app.core.m115 import M115
from app.core.m123 import M123
from app.core.obj_factory import ObjFactory
from app.db.clouddata_op import CloudDataOp
import pytz
from app.core.env import novaEnv, configEnv
from app.dbv2.config.cloud123_mapper import Cloud123Mapper, Cloud123
from app.modules.emby.emby import EmbyApi
from app.log import logger
from app.modules.tmdb.tmdbapi import TmdbApi
from app.services.message_service import MessageService
from app.utils.mjson import JsonUtils

class EmbyNotificationService:
    
    def __init__(self, db):
        self._db = db
        self.emby = EmbyApi()
        self.tmdb = TmdbApi()
        self._message = MessageService()
        self._clouddata_op = CloudDataOp(self._db)
        self.mp_cloud123 = Cloud123Mapper()
        self._m115 = ObjFactory.get_instance(M115)
        self._m123 = ObjFactory.get_instance(M123)
        self.storageapi = StorageApi()
        return None
        return None

    
    def send_msg(self, data):
        try:
            logger.info(data)
            _var_var_0 = data.get('tmdb_id')
            _var_var_1 = data.get('emby_id')
            _var_var_2 = None
            _var_var_3 = data.get('overview', '')
            _var_var_14 = f'''播放: {data.get('item_name', '')}\n时间: {data.get('time', '')}'''
            self._message.send_msg(title = data.get('title', 'Emby播放通知'), text = _var_var_14, image = _var_var_2)
        except Exception as _var_var_13:
            logger.error(f'获取媒体图片失败, {_var_var_13}')

    def delete_pcs(self, data):
        '''同步删除云盘文件'''
        _var_var_16 = data.get('del_pcs')
        _var_var_17 = data.get('del_123')
        if not _var_var_16 and _var_var_17:
            logger.error('同步删除云盘文件-获取CMS直连信息失败')
            return '同步删除云盘文件失败-非CMS直连'
        return '同步删除云盘文件失败-非CMS直连'
        _var_var_18 = []
        if _var_var_16:
            _var_var_19 = self.delete_115(data, _var_var_16)
            _var_var_18.append(_var_var_19)
        if _var_var_17:
            _var_var_20 = self.storageapi.delete_cloud_file(data, _var_var_17)
            _var_var_18.append(_var_var_20)
        return '，'.join(_var_var_18)
        return None

    
    def delete_115(self, data, pcs):
        '''同步删除云盘文件'''
        _var_var_21 = self._clouddata_op.get_by_pcs(pcs)
        if not _var_var_21:
            logger.error(f'''同步删除115云盘文件失败-同步记录不存在-pcs={pcs}''')
            return '同步删除115云盘文件失败-同步记录不存在'
        return '同步删除115云盘文件失败-同步记录不存在'
        _var_var_22 = data.get('type')
        _var_var_23 = { }
        for _var_var_24 in _var_var_21:
            if _var_var_24.pid in _var_var_23:
                _var_var_23[_var_var_24.pid].append(_var_var_24)
                continue
            _var_var_23[_var_var_24.pid] = [
                _var_var_24]
        _var_var_25 = []
        _var_var_26 = []
        _var_var_27 = []
        _var_var_28 = []
        for _var_var_29 in _var_var_23:
            _var_var_30 = self._clouddata_op.get_by_pid(_var_var_29)
            _var_var_31 = False
            for _var_var_32 in _var_var_30:
                if _var_var_32.is_dir == 1 or _var_var_32.pick_code in pcs:
                    continue
                if not _var_var_32.suffix:
                    continue
                if not _var_var_32.suffix in configEnv.video_suffix:
                    continue
                _var_var_31 = True
            if _var_var_31:
                logger.info(f'''同步删除115云盘文件 {_var_var_29}-{_var_var_30[0].p_name} 下还有其它视频文件，仅删除视频文件''')
                for _var_var_33 in _var_var_23[_var_var_29]:
                    _var_var_25.append(_var_var_33)
                    _var_var_27.append(_var_var_33.fid)
                continue
            logger.info(f'''同步删除115云盘文件 {_var_var_29}-{_var_var_30[0].p_name} 下没有其它视频文件，删除整个文件夹''')
            _var_var_34 = self._clouddata_op.get_by_fid(_var_var_29)
            _var_var_25.append(_var_var_34)
            _var_var_27.append(_var_var_29)
            _var_var_26.append(_var_var_29)
            if not _var_var_22 == 'Season' and _var_var_22 == 'Series':
                continue
            _var_var_28.append(_var_var_34.pid)
        if _var_var_28:
            _var_var_35 = set(_var_var_28)
            for _var_var_29 in _var_var_35:
                _var_var_30 = self._clouddata_op.get_by_pid(_var_var_29)
                _var_var_36 = True
                for _var_var_32 in _var_var_30:
                    if _var_var_32.is_dir == 1 and _var_var_32.fid not in _var_var_26:
                        _var_var_36 = False
                        break
                    elif not _var_var_32.suffix:
                        continue
                    if _var_var_32.suffix not in configEnv.video_suffix:
                        continue
                    _var_var_36 = False
                    break
                if _var_var_36:
                    logger.info(f'''同步删除115云盘文件 {_var_var_29}-{_var_var_30[0].p_name} 下已经没有子文件夹或视频文件，删除整个文件夹''')
                    _var_var_34 = self._clouddata_op.get_by_fid(_var_var_29)
                    _var_var_25.append(_var_var_34)
                    _var_var_27.append(_var_var_29)
                else:
                    logger.info(f'''同步删除115云盘文件 {_var_var_29}-{_var_var_30[0].p_name} 下还有子文件夹或视频文件，跳过删除''')
        if _var_var_27:
            self._m115.fs_delete_chunk(_var_var_27)
            logger.info('同步删除115云盘文件-删除云盘文件成功')
        if _var_var_25:
            self._clouddata_op.delete_by_cds(_var_var_25)
            logger.info('同步删除115云盘文件-删除同步记录成功')
        logger.info(f'''同步删除115云盘文件-{data['title']}-{_var_var_22}-共{len(pcs)}个视频文件''')
        return '同步删除115云盘文件成功'
        return '同步删除115云盘文件成功'

    
    def _get_tmdb_details(self, tmdb_id, media_type):
        '''获取TMDB图片信息'''
        if not tmdb_id:
            return None
        return None
        if media_type == 'Movie':
            return self.tmdb.get_movie_details_by_tmdb_id(tmdb_id)
        return None
        if media_type == 'Episode' and media_type == 'Series' or media_type == 'Season':
            return self.tmdb.get_tv_details_by_tmdb_id(tmdb_id)
        return None
        logger.error(f'''未知媒体类型: {media_type}''')
        return None
        return None

    
    def _get_image_url(self, images):
        '''从TMDB图片信息中获取URL'''
        if not images:
            return ''
        return ''
        _var_var_37 = ''
        if images.get('backdrops'):
            _var_var_37 = images['backdrops'][0]['file_path']
        elif images.get('posters'):
            _var_var_37 = images['posters'][0]['file_path']
        return self.tmdb.build_img_h632(_var_var_37) if _var_var_37 else ''
        return None

    
    def _get_image_url_by_details(self, details):
        '''从TMDB详情信息中获取URL'''
        if not details:
            return ''
        return ''
        _var_var_37 = ''
        if details.get('backdrop_path'):
            _var_var_37 = details['backdrop_path']
        elif details.get('poster_path'):
            _var_var_37 = details['poster_path']
        return self.tmdb.build_img_h632(_var_var_37) if _var_var_37 else ''
        return None

    
    def _handle_media_event(self, notification):
        '''处理媒体事件通知'''
        try:
            _var_var_38 = notification['Title']
            _var_var_39 = notification.get('Description')
            if _var_var_39 and re.match('^S\\d+.+', _var_var_39):
                _var_var_40 = _var_var_39.split('\n')[0]
            else:
                _var_var_40 = None
            _var_var_41 = None
            _var_var_42 = []
            if _var_var_39:
                _var_var_43 = re.search('TmdbId: (\\d+)', _var_var_39)
                if _var_var_43:
                    _var_var_41 = _var_var_43.group(1)
                _var_var_44 = re.findall('/d/([a-zA-Z0-9]{15,25})', _var_var_39)
                if _var_var_44:
                    _var_var_42.extend(_var_var_44)
            return True
        except (ValueError, AttributeError):
            return False


    def _handle_notification_test(self):
        self._message.send_msg(title = 'EMBY通知测试')
        return None
        return None

    
    def handle_notification(self, notification):
        '''处理通知的主方法'''
        if not notification:
            logger.info('Emby通知为空, 请确认请求内容类型为 application/json')
            return None
        try:
            _var_var_47 = notification.get('Event', '')
            if _var_var_47 in ('library.deleted', 'library.new', 'playback.start', 'playback.pause', 'playback.stop', 'deep.delete'):
                self._handle_media_event(notification)
            elif _var_var_47 == 'system.notificationtest':
                self._handle_notification_test()
            else:
                logger.info(f'跳过处理emby通知: {_var_var_47}')
            return None
        except Exception as _var_var_13:
            logger.error('处理Emby通知失败')
            logger.exception(_var_var_13)



