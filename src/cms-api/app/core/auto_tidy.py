import json
import os
import re
import time
from sqlalchemy.orm import Session
from app.core.env import ConfigEnv, configEnv
from app.core.obj_factory import ObjFactory
from app.core.media_monitor import MediaImgMonitor
from app.db.clouddata_op import CloudDataOp
from app.db.config_op import ConfigOp
from app.db.models.clouddata import CloudData
from app.db.models.rename import RenameLog
from app.db.rename_op import RenameOp
from app.db.share_op import ShareDownOp
from app.db.sub_op import SubMediaOp, SubSourceOp
from app.modules.emby.emby import EmbyApi
from app.modules.media.media_util import MediaUtil
from app.modules.media.mp import MP
from app.modules.media.tidy import TidyUtil
from app.modules.media.video_info import VideoInfo
from app.modules.tmdb.category import CategoryUtil
from app.modules.tmdb.tmdbapi import TmdbApi
from app.services.message_service import MessageService
from app.utils.ko_util import del_path, join_local_paths, change_file_suffix, get_thumb_name, rename, create_strm_file, join_cloud_paths, chunk_list, combine_episode_ranges, convert_size
from app.schemas.types import ActionEnum, StatusEnum
from app.log import logger
from app.core.m115 import M115
from app.db.liftlist_op import LiftListOp
from app.utils.mjson import JsonUtils
from app.utils.mstr import normalize_filename
from app.utils.mutil import Mutil
from app.utils.wrapper import exception_ignore, log_exec_time

class AutoTidy:
    '''
    自动整理
    '''
    
    def __init__(self, db, is_refresh_library):
        self._db = db
        self._CONFIG_ENV = ConfigEnv()
        self._cloud_data_op = CloudDataOp(self._db)
        self._rename_op = RenameOp(self._db)
        self._config_op = ConfigOp(self._db)
        self._share_down_op = ShareDownOp(self._db)
        self._sub_media_op = SubMediaOp(self._db)
        self._sub_source_op = SubSourceOp(self._db)
        self._sync_path_set = set()
        self._is_refresh_library = is_refresh_library
        self._msg_strm_count = 0
        self._msg_img_count = 0
        self._msg_nfo_count = 0
        self._batch_size = 1000
        self._batch_items = []
        self._batch_dir_items = { }
        self._AutoTidy__CONFIG = self._config_op.get_all()
        self._AutoTidy__VIDEO_SUFFIX = self._AutoTidy__CONFIG.get('VIDEO_SUFFIX', [
            'mp4',
            'mkv'])
        self._AutoTidy__IMAGE_SUFFIX = self._AutoTidy__CONFIG.get('IMAGE_SUFFIX', [])
        self._AutoTidy__MEDIA_DATA_SUFFIX = self._AutoTidy__CONFIG.get('MEDIA_DATA_SUFFIX', [])
        self._AutoTidy__SUBTITLE_SUFFIX = [
            'srt',
            'ass',
            'ssa',
            'sup']
        self._media_img_monitor = MediaImgMonitor()
        self._message = MessageService()
        self._mp = MP()
        self._tmdbapi = TmdbApi()
        self._emby_api = EmbyApi()
        self._tidy_util = TidyUtil()
        if self._AutoTidy__CONFIG.get('NEW_MEDIA_CID'):
            self._category_util = CategoryUtil()
        return None
        return None

    @property
    def _m115(self):
        return ObjFactory.get_instance(M115)
    
    def add_sync_path(self, path):
        if self._is_refresh_library:
            self._sync_path_set.add(path)
        return None
        return None

    
    def move_to_tidy(self):
        if not configEnv.auto_tidy_after_save:
            return None
        return None
        if not configEnv.share_down_dir_cid or configEnv.new_media_cid:
            return None
        return None
        if configEnv.share_down_dir_cid == configEnv.new_media_cid:
            return None
        return None
        self._m115.move_dir1_dir2(configEnv.share_down_dir_cid, configEnv.new_media_cid, '转存数据')
        time.sleep(3)
        logger.info('暂停3秒-等待转存数据移动完成...')
        return None
        return None

    
    def save_new_media(self):
        '''
        保存新媒体数据
        '''
        if not configEnv.new_media_cid:
            return None
        return None
        logger.info('开始整理待刮削库...')
        _var_var_0 = self._m115.get_all_file_and_base_path(configEnv.new_media_cid)
        if not _var_var_0:
            logger.info('未获取到视频文件')
            return None
        return None
        _var_var_1 = []
        _var_var_2 = set()
        for _var_var_3 in _var_var_0:
            if _var_var_3['ico'] in self._AutoTidy__VIDEO_SUFFIX:
                _var_var_4 = self._cloud_data_op.get_by_sha1(_var_var_3['sha1'])
                if _var_var_4:
                    logger.info(f'''当前文件sha1已存在你的媒体库中-跳过整理-{_var_var_3['sha1']}-{_var_var_3['name']}''')
                    _var_var_1.append(_var_var_3['fid'])
                    continue
                if _var_var_3['size'] < configEnv.auto_min_size:
                    logger.info(f'''文件大小小于{configEnv.auto_min_size}-跳过整理-{_var_var_3['size']}-{_var_var_3['name']}''')
                    continue
                _var_var_5 = False
                for _var_var_6 in configEnv.auto_blacklist:
                    if not re.search(_var_var_6, _var_var_3['name']):
                        continue
                    logger.info(f'''文件名匹配到黑名单正则 {_var_var_6} 跳过整理-{_var_var_3['name']}''')
                    _var_var_5 = True
                    configEnv.auto_blacklist
                if _var_var_5:
                    continue
            _var_var_7 = 'un'
            if _var_var_3['ico'] in self._AutoTidy__VIDEO_SUFFIX:
                _var_var_7 = 'video'
            elif _var_var_3['ico'] in self._AutoTidy__SUBTITLE_SUFFIX:
                _var_var_7 = 'subtitle'
            if _var_var_7 != 'un':
                _var_var_2.add(_var_var_3['pid'])
                self._rename_op.save(RenameLog(fid = _var_var_3['fid'], name = _var_var_3['name'], pid = _var_var_3['pid'], p_name = _var_var_3['p_name'], path = _var_var_3['path'], suffix = _var_var_3['ico'], sha1 = _var_var_3['sha1'], size = _var_var_3['size'], f_modify_time = _var_var_3['update_time'], status = 0, type = '', tidy_type = _var_var_7))
                continue
            logger.info(f'''跳过整理{_var_var_3['ico']}类型的文件-{_var_var_3['name']}''')
        if _var_var_1:
            if configEnv.new_media_exists_cid:
                logger.info(f'''整理视频-将已存在的sha1视频移动到-{configEnv.new_media_exists_cid_path}''')
                self._m115.fs_move_chunk(_var_var_1, configEnv.new_media_exists_cid)
            else:
                logger.error('未设置 冗余数据文件夹cid')
        return None
        return None

    
    def scrape_new_media(self):
        '''
        刮削新媒体数据
        '''
        if not configEnv.new_media_cid:
            return None
        _var_var_8 = self._rename_op.get_by_status(0, 'video')
        for _var_var_9 in _var_var_8:
            try:
                _var_var_10 = MediaUtil(_var_var_9.path, self._db).recognize_info()
                if _var_var_10:
                    _var_var_9.status = 100
                    _var_var_9.desc = '识别成功'
                    _var_var_9.type = _var_var_10['type']
                    if _var_var_10['name']:
                        if _var_var_10['name'].endswith(_var_var_9.suffix):
                            _var_var_9.new_name = _var_var_10['name']
                        else:
                            _var_var_9.new_name = f'''{_var_var_10['name']}.{_var_var_9.suffix}'''
                    _var_var_9.new_dir_name = _var_var_10['dir_name']
                    if not _var_var_9.new_dir_name:
                        self._rename_op.delete_log(_var_var_9)
                        _var_var_11 = '剧集' if _var_var_10['type'] == 'tv' else '电影'
                        logger.error(f'''重命名规则有误，请检查 {_var_var_11}文件夹命名规则''')
                        continue
                    if not _var_var_9.new_name:
                        self._rename_op.delete_log(_var_var_9)
                        _var_var_11 = '剧集' if _var_var_10['type'] == 'tv' else '电影'
                        logger.error(f'''重命名规则有误，请检查 {_var_var_11}文件命名规则''')
                        continue
                    if _var_var_10['type'] == 'tv':
                        _var_var_9.new_season_name = _var_var_10['season_name']
                        _var_var_9.season_num = _var_var_10['season_num']
                        _var_var_9.episode_num = _var_var_10['episode_num']
                    _var_var_9.tmdb_id = _var_var_10['tmdb_id']
                    _var_var_9.poster_path = _var_var_10['poster_path']
                    _var_var_9.backdrop_path = _var_var_10['backdrop_path']
                    if _var_var_9.type == 'movie':
                        _var_var_12 = self._category_util.get_movie_category(_var_var_10.get('tmdb_info'))
                    else:
                        _var_var_12 = self._category_util.get_tv_category(_var_var_10.get('tmdb_info'))
                    _var_var_13 = _var_var_10.get('video_info')
                    _var_var_13['category'] = _var_var_12
                    _var_var_13['f_modify_time'] = _var_var_9.f_modify_time
                    _var_var_9.video_info = JsonUtils.to_str(_var_var_13)
                    _var_var_9.tmdb_info = JsonUtils.to_str(_var_var_10.get('tmdb_info'))
                    self._rename_op.update_log(_var_var_9)
                else:
                    self._rename_op.delete_log(_var_var_9)
            except Exception as _var_var_14:
                logger.error(f'''识别文件失败-{_var_var_9.path}-{str(_var_var_14)}''')
                logger.exception(_var_var_14)
        return None

    
    def scrape_new_subtitle(self):
        """
        刮削新媒体字幕
        """
        _var_var_15 = self._rename_op.get_pid_by_status(0, 'subtitle')
        for _var_var_16 in _var_var_15:
            _var_var_8 = self._rename_op.get_by_pid(_var_var_16)
            _var_var_17 = [_var_var_9 for _var_var_9 in _var_var_8 if _var_var_9.tidy_type == 'video']
            _var_var_18 = [_var_var_9 for _var_var_9 in _var_var_8 if _var_var_9.tidy_type == 'subtitle']
            for _var_var_19 in _var_var_18:
                for _var_var_20 in _var_var_17:
                    _var_var_21 = _var_var_20.name[:-len(_var_var_20.suffix) - 1]
                    if not _var_var_20.new_name:
                        continue
                    _var_var_22 = _var_var_20.new_name[:-len(_var_var_20.suffix) - 1]
                    if not _var_var_19.name.startswith(_var_var_21):
                        continue
                    _var_var_19.status = 100
                    _var_var_19.desc = '识别成功'
                    _var_var_19.type = _var_var_20.type
                    _var_var_19.new_name = _var_var_19.name.replace(_var_var_21, _var_var_22)
                    _var_var_19.new_dir_name = _var_var_20.new_dir_name
                    if _var_var_20.type == 'tv':
                        _var_var_19.new_season_name = _var_var_20.new_season_name
                        _var_var_19.season_num = _var_var_20.season_num
                        _var_var_19.episode_num = _var_var_20.episode_num
                    _var_var_19.tmdb_id = _var_var_20.tmdb_id
                    _var_var_19.video_info = _var_var_20.video_info
                    _var_var_19.tmdb_info = _var_var_20.tmdb_info
                    _var_var_19.poster_path = _var_var_20.poster_path
                    _var_var_19.backdrop_path = _var_var_20.backdrop_path
                    self._rename_op.update_log(_var_var_19)
                    break
    def get_media_cid(self, log):
        _var_var_23 = {
            'exists': [] }
        _var_var_24 = self._cloud_data_op.get_by_dir_name(log.new_dir_name)
        if _var_var_24:
            _var_var_23['cid'] = _var_var_24.fid
            if log.type == 'movie':
                _var_var_25 = self._cloud_data_op.get_video_by_pid(_var_var_24.fid)
                if _var_var_25:
                    _var_var_23['exists'].extend(_var_var_25)
            return _var_var_23
        return None
        if not log.tmdb_info:
            logger.error(f'''整理视频-媒体文件夹创建失败-tmdb_info为空-{log.new_dir_name}''')
            return None
        return None
        _var_var_26 = JsonUtils.json_to_dict(log.tmdb_info)
        if log.type == 'movie':
            _var_var_27 = self._category_util.get_movie_category_cid(_var_var_26)
        else:
            _var_var_27 = self._category_util.get_tv_category_cid(_var_var_26)
        if not _var_var_27:
            logger.error(f'''整理视频-媒体文件夹创建失败-没有从二级分类策略配置获取到cid-{log.new_dir_name}''')
            return None
        return None
        _var_var_27 = int(_var_var_27)
        if not log.new_dir_name:
            logger.error('整理视频-媒体文件夹创建失败-文件夹重命名规则有误')
            self._rename_op.delete_log(log)
            return None
        return None
        _var_var_28 = self._m115.fs_mkdir(log.new_dir_name, _var_var_27)
        if not _var_var_28.get('state'):
            logger.error(f'''整理视频-媒体文件夹创建失败-{log.new_dir_name} 请确认二级分类策略里的cid: {_var_var_27}是否正确''')
            logger.error(f'''115.fs_mkdir.response={JsonUtils.to_str(_var_var_28)}''')
            self._rename_op.delete_log(log)
            return None
        return None
        _var_var_23['cid'] = _var_var_28['cid']
        logger.info(f'''整理视频-媒体文件夹创建成功-{log.new_dir_name}''')
        return _var_var_23
        return None

    
    def get_season_cid(self, log, media_cid):
        _var_var_29 = {
            'exists': [] }
        _var_var_30 = self._cloud_data_op.get_by_name_pid(log.new_season_name, media_cid)
        if _var_var_30:
            _var_var_25 = self._cloud_data_op.get_video_by_pid(_var_var_30.fid)
            if _var_var_25:
                _var_var_29['exists'].extend(_var_var_25)
            _var_var_29['cid'] = _var_var_30.fid
            return _var_var_29
        return None
        _var_var_31 = self._m115.fs_mkdir(log.new_season_name, media_cid)
        if not _var_var_31.get('state'):
            logger.error(f'''115.fs_mkdir.resp={JsonUtils.to_str(_var_var_31)}''')
            logger.error(f'''整理视频-{log.name}-季文件夹创建失败-{log.new_season_name}''')
            self._rename_op.delete_log(log)
            return None
        return None
        logger.info(f'''整理视频-{log.name}-季文件夹创建成功-{log.new_season_name}''')
        _var_var_29['cid'] = _var_var_31['cid']
        return _var_var_29
        return None

    
    def tidy_up_new_media(self):
        """
        整理新媒体数据
        """
        if not configEnv.new_media_cid:
            return
        _var_var_8 = self._rename_op.get_by_status(100, None)
        if not _var_var_8:
            logger.info('整理视频-没有待整理的数据')
            self._m115.move_dir1_dir2(configEnv.new_media_cid, configEnv.redundant_data_cid, '冗余数据')
            return
        _var_var_32 = []
        _var_var_33 = []
        _var_var_34 = []
        _var_var_35 = []
        _var_var_36 = {}
        _var_var_37 = {}
        for _var_var_9 in _var_var_8:
            if _var_var_37.get(_var_var_9.new_dir_name):
                _var_var_38 = _var_var_37[_var_var_9.new_dir_name]
            else:
                _var_var_23 = self.get_media_cid(_var_var_9)
                if not _var_var_23:
                    continue
                _var_var_38 = {'cid': _var_var_23['cid'], 'type': _var_var_9.type, 'ep': [], 'exists': _var_var_23['exists'], 'seasons': {}}
            if _var_var_9.new_season_name:
                _var_var_39 = _var_var_38['seasons']
                if not _var_var_39.get(_var_var_9.new_season_name):
                    _var_var_29 = self.get_season_cid(_var_var_9, _var_var_38['cid'])
                    if not _var_var_29:
                        continue
                    _var_var_39[_var_var_9.new_season_name] = _var_var_29['cid']
                    if _var_var_29.get('exists'):
                        _var_var_38['exists'].extend(_var_var_29.get('exists'))
            _var_var_38['ep'].append(_var_var_9)
            _var_var_37[_var_var_9.new_dir_name] = _var_var_38
        for _var_var_40, _var_var_41 in _var_var_37.items():
            _var_var_42 = _var_var_41['type'] == 'movie'
            _var_var_43 = _var_var_41['ep']
            if len(_var_var_43) <= 1:
                continue
            if _var_var_42:
                _var_var_41['ep'] = self.run_tidy_rule(_var_var_41['ep'])
                continue
            _var_var_44 = {}
            for _var_var_45 in _var_var_43:
                _var_var_46 = f'{_var_var_45.new_dir_name}{_var_var_45.new_season_name}{_var_var_45.season_num}{_var_var_45.episode_num}'
                _var_var_47 = _var_var_44.get(_var_var_46, [])
                _var_var_47.append(_var_var_45)
                _var_var_44[_var_var_46] = _var_var_47
            _var_var_48 = []
            for _var_var_49, _var_var_50 in _var_var_44.items():
                if len(_var_var_50) < 2:
                    _var_var_48.extend(_var_var_50)
                else:
                    _var_var_51 = self.run_tidy_rule(_var_var_50)
                    _var_var_48.extend(_var_var_51)
            _var_var_41['ep'] = _var_var_48
        for _var_var_40, _var_var_41 in _var_var_37.items():
            logger.info(f'整理视频-{_var_var_40}')
            _var_var_52 = _var_var_41['cid']
            _var_var_39 = _var_var_41['seasons']
            _var_var_42 = _var_var_41['type'] == 'movie'
            _var_var_53 = not _var_var_42
            _var_var_54 = _var_var_41.get('exists')
            _var_var_55 = self.get_videos(_var_var_54)
            _var_var_56 = self.get_subs(_var_var_54)
            _var_var_43 = _var_var_41['ep']
            _var_var_57 = self.get_videos(_var_var_43)
            _var_var_58 = self.get_subs(_var_var_43)
            if _var_var_42:
                if _var_var_55:
                    _var_var_59 = []
                    for _var_var_45 in _var_var_57:
                        _var_var_60 = JsonUtils.json_to_dict(_var_var_45.video_info)
                        _var_var_60['size'] = _var_var_45.size
                        _var_var_60['f_modify_time'] = _var_var_45.f_modify_time
                        _var_var_61 = False
                        _var_var_62 = False
                        _var_var_63 = 'all'
                        for _var_var_64 in _var_var_55:
                            _var_var_65 = VideoInfo(_var_var_64.name).to_dict()
                            _var_var_65['category'] = _var_var_60['category']
                            _var_var_65['size'] = _var_var_64.size
                            _var_var_65['f_modify_time'] = _var_var_64.f_modify_time
                            _var_var_66, _var_var_63 = self._tidy_util.get_tidy_rule(_var_var_65, _var_var_60)
                            if _var_var_66 == 'replace':
                                _var_var_61 = True
                                _var_var_34.append(_var_var_64.fid)
                            elif _var_var_66 == 'skip':
                                _var_var_62 = True
                            elif _var_var_66 == 'coexist':
                                _var_var_61 = True
                        if _var_var_63 == 'group' and _var_var_62:
                            continue
                        if not _var_var_61:
                            continue
                        _var_var_59.append(_var_var_45)
                    _var_var_67 = _var_var_59
                    for _var_var_68 in _var_var_58:
                        for _var_var_69 in _var_var_67:
                            _var_var_70 = _var_var_69.name.rsplit('.', 1)[0]
                            if not _var_var_68.name.startswith(_var_var_70):
                                continue
                            _var_var_59.append(_var_var_68)
                            break
                    _var_var_41['ep'] = _var_var_59
            elif _var_var_55:
                _var_var_71 = {}
                for _var_var_64 in _var_var_55:
                    if _var_var_64.is_dir:
                        continue
                    _var_var_65 = VideoInfo(_var_var_64.name).to_dict()
                    _var_var_65['size'] = _var_var_64.size
                    _var_var_65['f_modify_time'] = _var_var_64.f_modify_time
                    _var_var_65['fid'] = _var_var_64.fid
                    _var_var_49 = f'S{_var_var_65["season_num"]}E{_var_var_65["episode_num"]}'
                    _var_var_67 = _var_var_71.get(_var_var_49, [])
                    _var_var_67.append(_var_var_65)
                    _var_var_71[_var_var_49] = _var_var_67
                _var_var_59 = []
                for _var_var_45 in _var_var_57:
                    _var_var_60 = JsonUtils.json_to_dict(_var_var_45.video_info)
                    _var_var_60['size'] = _var_var_45.size
                    _var_var_60['f_modify_time'] = _var_var_45.f_modify_time
                    _var_var_49 = f'S{_var_var_60["season_num"]}E{_var_var_60["episode_num"]}'
                    _var_var_72 = _var_var_71.get(_var_var_49, [])
                    if not _var_var_72:
                        _var_var_59.append(_var_var_45)
                        continue
                    _var_var_61 = False
                    _var_var_62 = False
                    _var_var_63 = 'all'
                    for _var_var_65 in _var_var_72:
                        _var_var_65['category'] = _var_var_60['category']
                        _var_var_66, _var_var_63 = self._tidy_util.get_tidy_rule(_var_var_65, _var_var_60)
                        if _var_var_66 == 'replace':
                            _var_var_61 = True
                            _var_var_34.append(_var_var_65['fid'])
                        elif _var_var_66 == 'skip':
                            _var_var_62 = True
                        elif _var_var_66 == 'coexist':
                            _var_var_61 = True
                    if _var_var_63 == 'group' and _var_var_62:
                        continue
                    if not _var_var_61:
                        continue
                    _var_var_59.append(_var_var_45)
                _var_var_67 = _var_var_59
                for _var_var_68 in _var_var_58:
                    for _var_var_69 in _var_var_67:
                        _var_var_70 = _var_var_69.name.rsplit('.', 1)[0]
                        if not _var_var_68.name.startswith(_var_var_70):
                            continue
                        _var_var_59.append(_var_var_68)
                        break
                _var_var_41['ep'] = _var_var_59
            if not _var_var_41['ep']:
                continue
            _var_var_73 = []
            for _var_var_9 in _var_var_41['ep']:
                if _var_var_9.name != _var_var_9.new_name:
                    _var_var_35.append({'id': _var_var_9.id, 'fid': _var_var_9.fid, 'new_name': _var_var_9.new_name})
                if _var_var_9.new_season_name:
                    _var_var_16 = _var_var_39[_var_var_9.new_season_name]
                else:
                    _var_var_16 = _var_var_52
                _var_var_74 = _var_var_36.get(_var_var_16)
                if _var_var_74:
                    _var_var_74.append(_var_var_9)
                else:
                    _var_var_74 = [_var_var_9]
                _var_var_36[_var_var_16] = _var_var_74
        if _var_var_34:
            self._m115.fs_delete_chunk(_var_var_34)
            logger.info(f'整理视频-删除旧媒体-{_var_var_34}')
        if len(_var_var_35) > 0:
            _var_var_75 = list(chunk_list(_var_var_35, 500))
            for _var_var_76, _var_var_77 in enumerate(_var_var_75):
                _var_var_78 = [(_var_var_9['fid'], normalize_filename(_var_var_9['new_name'])) for _var_var_9 in _var_var_77 if _var_var_9['new_name']]
                if len(_var_var_78) > 0:
                    _var_var_79 = self._m115.fs_rename(_var_var_78)
                    if not _var_var_79.get('state'):
                        logger.error(f'fs_rename response={JsonUtils.to_str(_var_var_79)}')
                        logger.error('整理视频-重命名失败')
                        continue
                    logger.info(f'整理视频-重命名成功-{_var_var_76}')
                    if _var_var_76 == len(_var_var_75) - 1:
                        break
                    time.sleep(3)
        for _var_var_80, _var_var_81 in _var_var_36.items():
            _var_var_82 = [_var_var_9.fid for _var_var_9 in _var_var_81]
            _var_var_83 = [_var_var_9.id for _var_var_9 in _var_var_81]
            _var_var_84 = self._m115.fs_move(_var_var_82, _var_var_80)
            if not _var_var_84.get('state'):
                logger.error(f'整理视频-移动失败-{_var_var_82}->{_var_var_80}-{_var_var_84}')
                continue
            _var_var_85 = ''
            _var_var_86 = 0
            _var_var_87 = 0
            _var_var_88 = []
            for _var_var_9 in _var_var_81:
                _var_var_86 += _var_var_9.size
                _var_var_87 += 1
                if _var_var_9.type == 'movie':
                    if _var_var_9.new_name:
                        _var_var_85 = f'{_var_var_85}\n{_var_var_9.new_name}'
                    else:
                        _var_var_85 = f'{_var_var_85}\n{_var_var_9.name}'
                elif _var_var_9.tidy_type == 'video':
                    _var_var_65 = JsonUtils.json_to_dict(_var_var_9.video_info)
                    _var_var_89 = _var_var_65.get('season_episode')
                    if not _var_var_89:
                        continue
                    _var_var_88.append(_var_var_89)
            _var_var_85 = _var_var_85.lstrip(' \n')
            _var_var_90 = convert_size(_var_var_86)
            _var_var_91 = _var_var_81[0]
            _var_var_65 = JsonUtils.json_to_dict(_var_var_91.video_info)
            _var_var_26 = JsonUtils.json_to_dict(_var_var_91.tmdb_info)
            _var_var_92 = f'{_var_var_26["title"]} ({_var_var_26["year"]}) 整理成功'
            _var_var_93 = _var_var_65.get('category', '未知')
            _var_var_94 = _var_var_26['type']
            _var_var_95 = ''
            if _var_var_65.get('resource_pix'):
                _var_var_95 = _var_var_65.get('resource_pix').upper()
            if _var_var_65.get('resource_effect'):
                _var_var_95 = f'{_var_var_95} {_var_var_65.get("resource_effect")}'
            if _var_var_65.get('resource_type'):
                _var_var_95 = f'{_var_var_95} {_var_var_65.get("resource_type")}'
            _var_var_95 = _var_var_95.lstrip(' \n')
            if not _var_var_95:
                _var_var_95 = '未知'
            _var_var_96 = f'类型：{_var_var_94}，类别：{_var_var_93}，质量：{_var_var_95}'
            if _var_var_65.get('resource_team'):
                _var_var_96 = f'{_var_var_96}，制作组：{_var_var_65.get("resource_team")}'
            _var_var_96 = f'{_var_var_96}，共计：{_var_var_87}个文件 {_var_var_90}'
            if not _var_var_85:
                _var_var_85 = f'集数：{combine_episode_ranges(_var_var_88)}'
            if _var_var_91.backdrop_path:
                _var_var_97 = self._tmdbapi.build_img_h632(_var_var_91.backdrop_path)
            else:
                _var_var_97 = self._tmdbapi.build_img_h632(_var_var_91.poster_path)
            if _var_var_26.get('tagline'):
                _var_var_98 = f'{_var_var_26["tagline"]}\n{_var_var_96}\n{_var_var_85}'
            else:
                _var_var_98 = f'{_var_var_96}\n{_var_var_85}'
            self._message.send_msg(title=_var_var_92, text=_var_var_98, image=_var_var_97)
            logger.info(f'整理视频-移动成功-{_var_var_82}')
        if _var_var_32:
            if self._AutoTidy__CONFIG['NEW_MEDIA_EXISTS_CID']:
                _var_var_100 = [_var_var_99.fid for _var_var_99 in _var_var_32]
                logger.info(f'整理视频-将已存在的sha1视频移动到-{self._AutoTidy__CONFIG["NEW_MEDIA_EXISTS_CID_PATH"]}')
                self._m115.fs_move_chunk(_var_var_100, self._AutoTidy__CONFIG['NEW_MEDIA_EXISTS_CID'])
            else:
                logger.info('未设置 NEW_MEDIA_EXISTS_CID')
        self._m115.move_dir1_dir2(configEnv.new_media_cid, configEnv.redundant_data_cid, '冗余数据')
        _var_var_83 = [_var_var_99.id for _var_var_99 in _var_var_8]
        self._rename_op.delete_by_ids(_var_var_83)
    def get_videos(self, eps):
        return [_var_var_45 for _var_var_45 in eps if _var_var_45.suffix and _var_var_45.suffix in self._AutoTidy__VIDEO_SUFFIX]
    def get_subs(self, eps):
        return [_var_var_45 for _var_var_45 in eps if _var_var_45.suffix and _var_var_45.suffix in self._AutoTidy__SUBTITLE_SUFFIX]
    def run_tidy_rule(self, eps):
        _var_var_101 = { }
        for _var_var_45 in eps:
            if _var_var_45.name not in _var_var_101:
                _var_var_101[_var_var_45.name] = _var_var_45
                continue
            if not _var_var_45.size > _var_var_101[_var_var_45.name].size:
                continue
            _var_var_101[_var_var_45.name] = _var_var_45
        eps = list(_var_var_101.values())
        _var_var_102 = []
        _var_var_57 = self.get_videos(eps)
        _var_var_58 = self.get_subs(eps)
        for _var_var_76 in range(len(_var_var_57)):
            _var_var_45 = _var_var_57[_var_var_76]
            if not _var_var_102:
                _var_var_102.append(_var_var_45)
                continue
            _var_var_60 = JsonUtils.json_to_dict(_var_var_45.video_info)
            _var_var_60['size'] = _var_var_45.size
            _var_var_60['f_modify_time'] = _var_var_45.f_modify_time
            _var_var_103 = []
            _var_var_61 = False
            _var_var_62 = False
            _var_var_63 = 'all'
            for _var_var_104 in range(len(_var_var_102)):
                _var_var_105 = _var_var_102[_var_var_104]
                _var_var_65 = JsonUtils.json_to_dict(_var_var_105.video_info)
                _var_var_65['size'] = _var_var_105.size
                _var_var_65['f_modify_time'] = _var_var_105.f_modify_time
                (_var_var_66, _var_var_63) = self._tidy_util.get_tidy_rule(_var_var_65, _var_var_60)
                if _var_var_66 == 'skip':
                    _var_var_62 = True
                    continue
                if _var_var_66 == 'replace':
                    _var_var_103.append(_var_var_104)
                    _var_var_61 = True
                    continue
                if not _var_var_66 == 'coexist':
                    continue
                _var_var_61 = True
            _var_var_106 = []
            for _var_var_104 in range(len(_var_var_102)):
                if _var_var_104 in _var_var_103:
                    continue
                _var_var_106.append(_var_var_102[_var_var_104])
            _var_var_102 = _var_var_106
            if _var_var_63 == 'group' and _var_var_62:
                continue
            if not _var_var_61:
                continue
            _var_var_106.append(_var_var_45)
        _var_var_107 = []
        for _var_var_68 in _var_var_58:
            for _var_var_69 in _var_var_102:
                _var_var_70 = _var_var_69.name.rsplit('.', 1)[0]
                if not _var_var_68.name.startswith(_var_var_70):
                    continue
                _var_var_107.append(_var_var_68)
                _var_var_102
        _var_var_102.extend(_var_var_107)
        return _var_var_102
