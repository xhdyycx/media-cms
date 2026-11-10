import copy
from typing import List, Dict
from app.core.con_storage import StorageApi
from app.core.m123 import M123
from app.core.obj_factory import ObjFactory
from app.modules.media.media_util import MediaUtil
from app.modules.media.tidy import TidyUtil
from app.modules.media.types.media_info import MediaInfo
from app.modules.media.video_info import VideoInfo
from app.modules.tmdb.category import CategoryUtil
from app.types.con_file import ConFile
from app.log import logger
from app.utils.mutil import Mutil

class CommonTidy(StorageApi):
    '''
    自动整理
    '''
    
    def __init__(self, video_ext, img_ext, nfo_ext, storage_type, is_refresh_library):
        super().__init__()
        self._sync_path_set = set()
        self._is_refresh_library = is_refresh_library
        self._msg_strm_count = 0
        self._msg_img_count = 0
        self._msg_nfo_count = 0
        self._tidy_util = TidyUtil()
        self.storage_type = storage_type
        self.min_size = 0
        self.min_size_mb = 0
        self.img_ext = img_ext
        self.video_ext = video_ext
        self.nfo_ext = nfo_ext
        self._category_util = CategoryUtil()
    @property
    def _m123(self):
        return ObjFactory.get_instance(M123)
    
    def add_sync_path(self, path):
        if self._is_refresh_library:
            self._sync_path_set.add(path)
        return None
        return None

    
    def tidy_media_dir(self, dir_info):
        _var_var_0 = []
        self.tidy_media_dir_impl(dir_info, True, _var_var_0)
        self.move_redundant_data(dir_info, _var_var_0)
        logger.info(f'''{self.storage_type}整理完成, path: {dir_info.full_y_path}, 共生成{self.strm_count}个strm文件, {self.nfo_count}个字幕文件''')
        self.send_sync_result_msg()
        self.refresh_emby_library()
        return None
        return None

    
    def tidy_media_dir_impl(self, dir_info, is_root_path, old_data):
        _var_var_1 = dir_info.fid
        logger.info(f'''开始整理{self.storage_type}文件夹: {_var_var_1} {dir_info.full_y_path}''')
        (_var_var_2, _var_var_3, _var_var_4) = self.fs_list({
            'fid': _var_var_1 })
        if not _var_var_2:
            return None
        return None
        if is_root_path:
            old_data.extend(_var_var_3)
            old_data.extend(_var_var_4)
        _var_var_5 = []
        _var_var_6 = []
        _var_var_7 = { }
        _var_var_8 = []
        for _var_var_9 in _var_var_3:
            if _var_var_9.ext in self.video_ext and int(_var_var_9.size) < self.min_size:
                logger.info(f'''视频小于 {self.min_size_mb}, 不整理: {_var_var_9.name}''')
                continue
            _var_var_9.full_y_path = f'''{dir_info.full_y_path}/{_var_var_9.name}'''
            if _var_var_9.ext in self.video_ext:
                _var_var_10 = self.db_exits(_var_var_9)
                if _var_var_10:
                    _var_var_8.append(_var_var_9)
                    continue
                (_var_var_2, _var_var_11) = self.recognize_file(_var_var_9)
                if not _var_var_2:
                    logger.error(f'''识别失败-{_var_var_9.full_y_path}''')
                    continue
                _var_var_9.media_info = _var_var_11
                _var_var_5.append(_var_var_9)
                if _var_var_11.season_name:
                    _var_var_14 = _var_var_12['seasons']
                    if not _var_var_14.get(_var_var_11.season_name):
                        _var_var_9.pid = _var_var_12['cid']
                        _var_var_15 = self.get_season_dir_id(_var_var_9)
                        if not _var_var_15:
                            continue
                        _var_var_14[_var_var_11.season_name] = _var_var_15['cid']
                        if _var_var_15.get('exists'):
                            _var_var_12['exists'].extend(_var_var_15.get('exists'))
                if _var_var_11.name:
                    _var_var_9.name = _var_var_11.name
                _var_var_9.pid = _var_var_12['cid']
                _var_var_12['ep'].append(_var_var_9)
                _var_var_7[_var_var_11.dir_name] = _var_var_12
            if not _var_var_9.ext in self.subtitle_ext:
                continue
            _var_var_6.append(_var_var_9)
        _var_var_16 = self.convert_subtitle(_var_var_6, _var_var_5)
        self.run_tidy_rul_by_new_video(_var_var_7)
        _var_var_17 = []
        _var_var_18 = []
        _var_var_19 = { }
        for _var_var_20, _var_var_21 in _var_var_7.items():
            logger.info(f'''整理视频-{_var_var_20}''')
            _var_var_22 = _var_var_21['cid']
            _var_var_14 = _var_var_21['seasons']
            _var_var_23 = _var_var_21['type'] == 'movie'
            _var_var_24 = not _var_var_23
            _var_var_25 = _var_var_21.get('exists')
            _var_var_26 = _var_var_21['ep']
            _var_var_27 = _var_var_26
            if _var_var_23 or _var_var_25:
                _var_var_28 = []
                for _var_var_29 in _var_var_27:
                    _var_var_30 = _var_var_29.media_info.video_info
                    _var_var_30['size'] = _var_var_29.size
                    _var_var_30['f_modify_time'] = _var_var_29.f_modify_time
                    _var_var_31 = False
                    _var_var_32 = False
                    _var_var_33 = 'all'
                    for _var_var_34 in _var_var_25:
                        _var_var_35 = VideoInfo(_var_var_34.name).to_dict()
                        _var_var_35['category'] = _var_var_30['category']
                        _var_var_35['size'] = _var_var_34.size
                        _var_var_35['f_modify_time'] = _var_var_34.f_modify_time
                        (_var_var_36, _var_var_33) = self._tidy_util.get_tidy_rule(_var_var_35, _var_var_30)
                        if _var_var_36 == 'replace':
                            _var_var_31 = True
                            _var_var_17.append(_var_var_34)
                            continue
                        if _var_var_36 == 'skip':
                            _var_var_32 = True
                            continue
                        if not _var_var_36 == 'coexist':
                            continue
                        _var_var_31 = True
                    if _var_var_33 == 'group' and _var_var_32:
                        continue
                    if not _var_var_31:
                        continue
                    _var_var_28.append(_var_var_29)
                _var_var_21['ep'] = _var_var_28
            elif _var_var_25:
                _var_var_37 = { }
                for _var_var_34 in _var_var_25:
                    if _var_var_34.is_dir:
                        continue
                    _var_var_35 = VideoInfo(_var_var_34.name).to_dict()
                    _var_var_35['size'] = _var_var_34.size
                    _var_var_35['f_modify_time'] = _var_var_34.f_modify_time
                    _var_var_34.media_info = MediaInfo(video_info = _var_var_35)
                    _var_var_38 = f'''S{_var_var_35['season_num']}E{_var_var_35['episode_num']}'''
                    _var_var_39 = _var_var_37.get(_var_var_38, [])
                    _var_var_39.append(_var_var_34)
                    _var_var_37[_var_var_38] = _var_var_39
                _var_var_28 = []
                for _var_var_29 in _var_var_27:
                    _var_var_30 = _var_var_29.media_info.video_info
                    _var_var_30['size'] = _var_var_29.size
                    _var_var_30['f_modify_time'] = _var_var_29.f_modify_time
                    _var_var_38 = f'''S{_var_var_30['season_num']}E{_var_var_30['episode_num']}'''
                    _var_var_40 = _var_var_37.get(_var_var_38, [])
                    if not _var_var_40:
                        _var_var_28.append(_var_var_29)
                        continue
                    _var_var_31 = False
                    _var_var_32 = False
                    _var_var_33 = 'all'
                    for _var_var_41 in _var_var_40:
                        _var_var_35 = _var_var_41.media_info.video_info
                        _var_var_35['category'] = _var_var_30['category']
                        (_var_var_36, _var_var_33) = self._tidy_util.get_tidy_rule(_var_var_35, _var_var_30)
                        if _var_var_36 == 'replace':
                            _var_var_31 = True
                            _var_var_17.append(_var_var_41)
                            continue
                        if _var_var_36 == 'skip':
                            _var_var_32 = True
                            continue
                        if not _var_var_36 == 'coexist':
                            continue
                        _var_var_31 = True
                    if _var_var_33 == 'group' and _var_var_32:
                        continue
                    if not _var_var_31:
                        continue
                    _var_var_28.append(_var_var_29)
                _var_var_21['ep'] = _var_var_28
            if not _var_var_21['ep']:
                continue
            for _var_var_42 in _var_var_21['ep']:
                if _var_var_42.name != _var_var_42.media_info.video_info['original_name']:
                    _var_var_18.append(_var_var_42)
                _var_var_44 = _var_var_19.get(_var_var_43, [])
                _var_var_44.append(_var_var_42)
                _var_var_45 = _var_var_16.get(_var_var_42.media_info.name)
                if _var_var_45:
                    for _var_var_46 in _var_var_45:
                        if _var_var_46.name != _var_var_46.media_info.video_info['original_name']:
                            _var_var_18.append(_var_var_46)
                        _var_var_44.append(_var_var_46)
                _var_var_19[_var_var_43] = _var_var_44
        self.execute_del_old_files(_var_var_17)
        self.execute_rename(_var_var_18)
        self.execute_move(_var_var_19)
        self.execute_move_repeat_data(_var_var_8)
        for _var_var_47 in _var_var_4:
            _var_var_47.full_y_path = f'''{dir_info.full_y_path}/{_var_var_47.name}'''
            self.tidy_media_dir_impl(_var_var_47, False, [])
        return None
        return None

    
    def run_tidy_rul_by_new_video(self, media_s):
        for _var_var_20, _var_var_21 in media_s.items():
            _var_var_23 = _var_var_21['type'] == 'movie'
            _var_var_26 = _var_var_21['ep']
            if len(_var_var_26) <= 1:
                continue
            if _var_var_23:
                _var_var_21['ep'] = self.run_tidy_rule(_var_var_21['ep'])
                continue
            _var_var_48 = { }
            for _var_var_29 in _var_var_26:
                _var_var_11 = _var_var_29.media_info
                _var_var_49 = f'''{_var_var_11.dir_name}{_var_var_11.season_name}{_var_var_11.season_num}{_var_var_11.episode_num}'''
                _var_var_50 = _var_var_48.get(_var_var_49, [])
                _var_var_50.append(_var_var_29)
                _var_var_48[_var_var_49] = _var_var_50
            _var_var_51 = []
            for _var_var_38, _var_var_52 in _var_var_48.items():
                if len(_var_var_52) < 2:
                    _var_var_51.extend(_var_var_52)
                    continue
                _var_var_53 = self.run_tidy_rule(_var_var_52)
                _var_var_51.extend(_var_var_53)
            _var_var_21['ep'] = _var_var_51
        return None
        return None

    
    def run_tidy_rule(self, eps):
        _var_var_54 = { }
        for _var_var_29 in eps:
            if _var_var_29.name not in _var_var_54:
                _var_var_54[_var_var_29.name] = _var_var_29
                continue
            if not _var_var_29.size > _var_var_54[_var_var_29.name].size:
                continue
            _var_var_54[_var_var_29.name] = _var_var_29
        eps = list(_var_var_54.values())
        _var_var_55 = []
        for _var_var_56 in range(len(eps)):
            _var_var_29 = eps[_var_var_56]
            if not _var_var_55:
                _var_var_55.append(_var_var_29)
                continue
            _var_var_30 = _var_var_29.media_info.video_info
            _var_var_30['size'] = _var_var_29.size
            _var_var_30['f_modify_time'] = _var_var_29.f_modify_time
            _var_var_57 = []
            _var_var_31 = False
            _var_var_32 = False
            _var_var_33 = 'all'
            for _var_var_58 in range(len(_var_var_55)):
                _var_var_59 = _var_var_55[_var_var_58]
                _var_var_35 = _var_var_59.media_info.video_info
                _var_var_35['size'] = _var_var_59.size
                _var_var_35['f_modify_time'] = _var_var_59.f_modify_time
                (_var_var_36, _var_var_33) = self._tidy_util.get_tidy_rule(_var_var_35, _var_var_30)
                if _var_var_36 == 'skip':
                    _var_var_32 = True
                    continue
                if _var_var_36 == 'replace':
                    _var_var_57.append(_var_var_58)
                    _var_var_31 = True
                    continue
                if not _var_var_36 == 'coexist':
                    continue
                _var_var_31 = True
            _var_var_60 = []
            for _var_var_58 in range(len(_var_var_55)):
                if _var_var_58 in _var_var_57:
                    continue
                _var_var_60.append(_var_var_55[_var_var_58])
            _var_var_55 = _var_var_60
            if _var_var_33 == 'group' and _var_var_32:
                continue
            if not _var_var_31:
                continue
            _var_var_60.append(_var_var_29)
        return _var_var_55
        return None

    
    def convert_subtitle(self, sub_files, video_files):
        _var_var_16 = { }
        for _var_var_61 in sub_files:
            for _var_var_62 in video_files:
                _var_var_63 = _var_var_62.media_info.video_info['original_name'][:-(len(_var_var_62.ext) + 1)]
                _var_var_11 = copy.deepcopy(_var_var_62.media_info)
                _var_var_64 = _var_var_62.name
                if not _var_var_64:
                    continue
                _var_var_65 = _var_var_64[:-(len(_var_var_62.ext) + 1)]
                if not _var_var_61.name.startswith(_var_var_63):
                    continue
                _var_var_11.name = _var_var_61.name.replace(_var_var_63, _var_var_65)
                _var_var_11.video_info['original_name'] = _var_var_61.name
                _var_var_61.name = _var_var_11.name
                _var_var_11.tidy_type = 'subtitle'
                _var_var_61.media_info = _var_var_11
                _var_var_61.p_name = _var_var_62.p_name
                _var_var_61.pid = _var_var_62.pid
                _var_var_61.full_y_path = Mutil.replace_last_path(_var_var_62.full_y_path, _var_var_61.name)
                _var_var_61.local_path = _var_var_62.local_path
                _var_var_45 = _var_var_16.get(_var_var_64, [])
                _var_var_45.append(_var_var_61)
                _var_var_16[_var_var_64] = _var_var_45
                video_files
        return _var_var_16
        return None

    
    def recognize_file(self, _file):
        try:
            _var_var_11 = MediaUtil(_file.full_y_path).recognize_info_v2()
            if _var_var_11:
                if not _var_var_11.name and _var_var_11.name.endswith(_file.ext):
                    _var_var_11.name = f'{_var_var_11.name}.{_file.ext}'
                if _var_var_11.type == 'movie':
                    _var_var_66 = self._category_util.get_movie_category(_var_var_11.tmdb_info)
                else:
                    _var_var_66 = self._category_util.get_tv_category(_var_var_11.tmdb_info)
                _var_var_11.video_info['category'] = _var_var_66
                _var_var_11.video_info['size'] = _file.size
                return (True, _var_var_11)
            return (False, None)
        except Exception as _var_var_67:
            logger.error(f'识别文件失败-{_file.full_y_path}-{str(_var_var_67)}')
            return (False, None)
