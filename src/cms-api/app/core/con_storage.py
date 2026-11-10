import os
import re
from typing import Dict
from urllib.request import urlopen
from shutil import copyfileobj
from app.core.env import configEnv
from app.core.env2 import config2Env
from app.core.m123 import M123
from app.core.obj_factory import ObjFactory
from app.dbv2.config.cloud123_mapper import Cloud123Mapper, Cloud123
from app.log import logger
from app.modules.emby.emby import EmbyApi
from app.modules.media.types.media_info import MediaInfo
from app.modules.tmdb.category import CategoryUtil
from app.modules.tmdb.tmdbapi import TmdbApi
from app.services.message_service import MessageService
from app.types.con_file import ConFile
from app.utils.ko_util import convert_size, combine_episode_ranges, del_path
from app.utils.mjson import JsonUtils
from app.utils.mtime import TimeUtils
from app.utils.mutil import Mutil

class StorageApi:
    
    def __init__(self):
        self.storage_type = '123'
        self.direct_302_domain = configEnv.direct_115_302_domain
        self.MP_CD123 = Cloud123Mapper()
        self._category_util = CategoryUtil()
        self._message = MessageService()
        self._emby_api = EmbyApi()
        self._tmdbapi = TmdbApi()
        self.img_ext = [
            'jpg',
            'png',
            'jpeg',
            'bmp',
            'exif',
            'gif',
            'heic',
            'heif']
        self.video_ext = [
            '3g2',
            '3gp',
            '3gp2',
            '3gpp',
            'asf',
            'avi',
            'dat',
            'divx',
            'f4v',
            'flv',
            'iso',
            'm2ts',
            'm4v',
            'mkv',
            'mov',
            'mp4',
            'mpe',
            'mpeg',
            'mpeg4',
            'mpg',
            'mts',
            'ram',
            'rm',
            'rmvb',
            'swf',
            'ts',
            'vob',
            'webm',
            'wmv']
        self.nfo_ext = [
            'nfo']
        self.subtitle_ext = [
            'srt',
            'ass',
            'ssa',
            'sup']
        self._is_refresh_library = configEnv.emby_refresh_status
        self._sync_path_set = set()
        self.strm_count = 0
        self.img_count = 0
        self.nfo_count = 0
        return None

    @property
    def _m123(self):
        return ObjFactory.get_instance(M123)
    
    def db_exits(self, _file):
        if self.storage_type == '123':
            return self.MP_CD123.get_by_unique_id(_file.md5)
        return False

    
    def execute_del_old_files(self, files):
        if not files:
            return None
        fids = [item.fid for item in files]
        names = [f'{item.fid} {item.name}' for item in files]
        logger.info(f'自动整理-删除旧媒体-{names}')
        if self.storage_type == '123':
            self._m123.open_fs_delete_to_trash_batch(fids)
        for item in files:
            self.delete_local_file(item)
        return None
    def execute_rename(self, files):
        if not files:
            return None
        names = [f'{item.fid} {item.name}' for item in files]
        logger.info(f'自动整理-重命名-{names}')
        if self.storage_type == '123':
            rename_args = [f'{item.fid}|{self.sanitize_filename(item.media_info.name)}' for item in files]
            self._m123.open_fs_rename_batch(rename_args)
        return None
    def sanitize_filename(self, name):
        _var_var_4 = '["\\\\/:*?|><]'
        _var_var_5 = re.sub(_var_var_4, ' ', name)
        _var_var_5 = re.sub('\\s+', ' ', _var_var_5)
        _var_var_5 = _var_var_5.strip()
        if len(_var_var_5) > 256:
            _var_var_5 = _var_var_5[:256]
            _var_var_5 = _var_var_5.strip()
        return _var_var_5

    
    def execute_move(self, move_data):
        if not move_data:
            return None
        media_infos = []
        if self.storage_type == '123':
            for pid, items in move_data.items():
                names = [f'{item.fid} {item.name}' for item in items]
                logger.info(f'自动整理-最终移动-{names}')
                fids = [item.fid for item in items]
                self._m123.open_fs_move_batch(fids, pid)
                media_infos = [item.media_info for item in items]
                db_files = []
                for item in items:
                    item.pid = pid
                    db_files.append(self.download_file(item))
                self.save_to_db(db_files)
                self.send_tidy_result(media_infos)
        return None
    def execute_move_repeat_data(self, repeat_data):
        if not repeat_data:
            return None
        names = [f'{item.fid} {item.md5} {item.name}' for item in repeat_data]
        logger.info(f'自动整理-移动在媒体库里已存在的文件（md5）-{names}')
        if self.storage_type == '123':
            fids = [item.fid for item in repeat_data]
            if fids:
                self._m123.open_fs_move_batch(fids, config2Env.m123_md5_repeat_id)
        return None
    def move_redundant_data(self, dir_info, old_data):
        if not old_data:
            return None
        ok, file_list, dir_list = self.fs_list({'fid': dir_info.fid})
        if not ok:
            return None
        old_fids = [item.fid for item in old_data]
        file_list.extend(dir_list)
        matches = []
        for item in file_list:
            if item.fid in old_fids:
                matches.append(item)
        names = [f'{item.fid} {item.name}' for item in matches]
        logger.info(f'自动整理-移动冗余数据-{names}')
        if self.storage_type == '123':
            fids = [item.fid for item in matches]
            if fids:
                self._m123.open_fs_move_batch(fids, config2Env.m123_redundant_data_id)
        return None
    def sync_delete(self, fid, file_list, dir_list):
        exists_map = {}
        for con_file in file_list:
            exists_map[str(con_file.fid)] = con_file.name
        for con_file in dir_list:
            exists_map[str(con_file.fid)] = con_file.name
        if self.storage_type == '123':
            records = self.MP_CD123.get_by_pid(fid)
            if not records:
                return None
            for con_file in records:
                key = str(con_file.fid)
                if key in list(exists_map.keys()) and exists_map[key] == con_file.name:
                    continue
                self.delete_local_file(ConFile(**con_file.to_dict()))
        return None
    def delete_local_file(self, con_file):
        try:
            self.add_sync_path(con_file.local_path)
            _var_var_23 = Mutil.merge_paths(con_file.local_path, con_file.local_name)
            logger.info(f'''同步删除: {_var_var_23}''')
            del_path(_var_var_23)
            self.MP_CD123.delete_by_fid(con_file.fid, con_file.is_dir)
            if con_file.is_dir == 0 and con_file.ext in self.video_ext:
                _var_var_24 = Mutil.change_file_suffix(_var_var_23, 'nfo')
                del_path(_var_var_24)
        except Exception as _var_var_25:
            logger.error(f'''删除本地文件异常: {_var_var_25}''')
        return None

    
    def fs_list(self, params):
        if self.storage_type == '123':
            (_var_var_13, _var_var_26) = self._m123.open_fs_list_v2_all(params.get('fid'))
            _var_var_14 = []
            _var_var_15 = []
            for _var_var_27 in _var_var_26:
                if _var_var_27['trashed'] == 1:
                    continue
                _var_var_28 = 0
                if _var_var_27['type'] == 1:
                    _var_var_28 = 1
                _var_var_29 = ConFile(is_dir = _var_var_28, fid = _var_var_27['fileId'], pid = _var_var_27['parentFileId'], name = _var_var_27['filename'], size = _var_var_27['size'], s3_key_flag = _var_var_27['s3KeyFlag'], md5 = _var_var_27['etag'], f_modify_time = _var_var_27['updateAt'])
                if _var_var_28 == 0 and '.' in _var_var_27['filename']:
                    _var_var_29.ext = _var_var_27['filename'].split('.')[-1]
                self.build_url(_var_var_29)
                if _var_var_28 == 1:
                    _var_var_15.append(_var_var_29)
                    continue
                if not _var_var_29.ext:
                    continue
                _var_var_14.append(_var_var_29)
            return (_var_var_13, _var_var_14, _var_var_15)
        return (False, [], [])

    
    def build_url(self, _file):
        _var_var_30 = ''
        if self.storage_type == '123':
            _var_var_30 = f'''{self.direct_302_domain}/d123/{_file.fid}'''
            if config2Env.keep_suffix:
                _var_var_30 = f'''{_var_var_30}.{_file.ext}'''
            if configEnv.strm_type == 'pick_code_name':
                _var_var_30 = f'''{_var_var_30}?/{_file.name}'''
        _file.url = _var_var_30
        return None

    
    def get_download_url(self, _file):
        if self.storage_type == '123':
            download_info = self._m123.download_info(_file.fid)
            if download_info is None or download_info.get('code', 101) != 0:
                logger.error(f'{JsonUtils.to_str(download_info)}')
                return ''
            return download_info['data']['downloadUrl']
        if self.storage_type == 'alist':
            return _file.url
        return ''
    def save_to_db(self, results):
        if self.storage_type == '123':
            rows = []
            for item in results:
                if item.status in ('skip',):
                    continue
                row = Cloud123(**{'fid': item.fid, 'name': item.name, 'ext': item.ext, 'pid': item.pid, 'p_name': item.p_name, 'f_modify_time': item.f_modify_time, 'size': item.size, 'is_dir': item.is_dir, 'md5': item.md5, 's3_key_flag': item.s3_key_flag, 'full_y_path': item.full_y_path, 'local_name': item.local_name, 'local_path': item.local_path, 'sync_time': item.sync_time, 'desc': item.desc, 'status': item.status})
                rows.append(row)
            if rows:
                self.MP_CD123.insert_all(rows)
        return None
    def get_media_dir_id(self, _file):
        _var_var_29 = None
        if self.storage_type == '123':
            _var_var_29 = self.__get_media_id_123(_file)
        if _var_var_29 and _var_var_29['pid'] != 0:
            if self.save_new_dir_to_db(_file, _var_var_29):
                return _var_var_29
            return None
        return _var_var_29

    
    def __get_media_id_123(self, _file):
        _var_var_33 = 'cid123'
        _var_var_34 = {
            'exists': [],
            'cid': '',
            'pid': 0 }
        _var_var_35 = _file.media_info
        _var_var_36 = _var_var_35.dir_name
        _var_var_37 = _var_var_35.type
        _var_var_38 = self.MP_CD123.get_by_dir_name(_var_var_36)
        if _var_var_38:
            _var_var_34['cid'] = _var_var_38.fid
            _var_var_34['p_name'] = _var_var_38.name
            _var_var_34['p_full_y_path'] = _var_var_38.full_y_path
            _var_var_34['p_full_local_path'] = f'''{_var_var_38.local_path}/{_var_var_38.local_name}'''
            if _var_var_37 == 'movie':
                _var_var_39 = self.MP_CD123.get_video_by_pid(_var_var_38.fid)
                if _var_var_39:
                    _var_var_34['exists'].extend(_var_var_39)
            return _var_var_34
        _var_var_40 = _var_var_35.tmdb_info
        if _var_var_37 == 'movie':
            _var_var_41 = self._category_util.get_movie_category_cid(_var_var_40, _var_var_33)
        else:
            _var_var_41 = self._category_util.get_tv_category_cid(_var_var_40, _var_var_33)
        if not _var_var_41:
            logger.error(f'''整理视频-媒体文件夹创建失败-没有从二级分类策略配置获取到{_var_var_33}-{_var_var_36}''')
            return None
        _var_var_41 = int(_var_var_41)
        _var_var_42 = self._m123.open_fs_mkdir(_var_var_36, _var_var_41)
        if _var_var_42.get('code', -1) != 0:
            logger.error(f'''整理视频-媒体文件夹创建失败-{_var_var_36}''')
            logger.error(f'''123.open_fs_mkdir.resp={JsonUtils.to_str(_var_var_42)}''')
            return None
        _var_var_34['cid'] = _var_var_42['data']['dirID']
        _var_var_34['pid'] = _var_var_41
        logger.info(f'''整理视频-媒体文件夹创建成功-{_var_var_36}''')
        return _var_var_34

    
    def save_new_dir_to_db(self, _file, temp, dir_type='media'):
        _var_var_41 = temp['cid']
        _var_var_7 = temp['pid']
        if self.storage_type == '123':
            _var_var_43 = self.MP_CD123.get_by_fid(_var_var_7)
            if not _var_var_43:
                logger.error(f'''整理视频-获取二级分类策略id记录失败-{_var_var_7}''')
                return False
            if dir_type == 'media':
                _var_var_44 = _file.media_info.dir_name
            else:
                _var_var_44 = _file.media_info.season_name
            _var_var_45 = ConFile(fid = _var_var_41, name = _var_var_44, pid = _var_var_7, p_name = _var_var_43.name, f_modify_time = TimeUtils.get_current_time_str(), is_dir = 1, full_y_path = f'''{_var_var_43.full_y_path}/{_var_var_44}''', local_name = _var_var_44, local_path = f'''{_var_var_43.local_path}/{_var_var_43.local_name}''', sync_time = TimeUtils.get_current_time_str(), status = 'success')
            self.save_to_db([
                _var_var_45])
            temp['p_name'] = _var_var_45.name
            temp['p_full_y_path'] = _var_var_45.full_y_path
            temp['p_full_local_path'] = f'''{_var_var_45.local_path}/{_var_var_45.local_name}'''
            return True
        return False

    
    def get_season_dir_id(self, _file):
        _var_var_29 = None
        if self.storage_type == '123':
            _var_var_29 = self.__get_season_dir_id_123(_file)
        if _var_var_29 and _var_var_29['pid'] != 0:
            if self.save_new_dir_to_db(_file, _var_var_29, 'season'):
                return _var_var_29
            return None
        return _var_var_29

    
    def __get_season_dir_id_123(self, _file):
        _var_var_46 = {
            'exists': [],
            'cid': '',
            'pid': 0 }
        _var_var_33 = 'cid123'
        _var_var_35 = _file.media_info
        _var_var_36 = _var_var_35.season_name
        _var_var_37 = _var_var_35.type
        _var_var_47 = self.MP_CD123.get_by_dir_name_and_pid(_var_var_36, _file.pid)
        if _var_var_47:
            _var_var_39 = self.MP_CD123.get_video_by_pid(_var_var_47.fid)
            if _var_var_39:
                _var_var_46['exists'].extend(_var_var_39)
            _var_var_46['cid'] = _var_var_47.fid
            _var_var_46['p_full_y_path'] = _var_var_47.full_y_path
            _var_var_46['p_full_local_path'] = f'''{_var_var_47.local_path}'''
            return _var_var_46
        _var_var_42 = self._m123.open_fs_mkdir(_var_var_36, _file.pid)
        if _var_var_42.get('code', -1) != 0:
            logger.error(f'''整理视频-季文件夹创建失败-{_var_var_36}''')
            logger.error(f'''123.open_fs_mkdir.resp={JsonUtils.to_str(_var_var_42)}''')
            return None
        logger.info(f'''整理视频-季文件夹创建成功-{_var_var_35.dir_name}-{_var_var_36}''')
        _var_var_46['cid'] = _var_var_42['data']['dirID']
        _var_var_46['pid'] = _file.pid
        return _var_var_46

    
    def send_tidy_result(self, _logs):
        _var_var_48 = ''
        _var_var_49 = 0
        _var_var_50 = 0
        _var_var_51 = []
        for _var_var_9 in _logs:
            _var_var_52 = _var_var_9.video_info
            _var_var_40 = _var_var_9.tmdb_info
            _var_var_49 += _var_var_52['size']
            _var_var_50 += 1
            if _var_var_9.type == 'movie':
                if not _var_var_9.name:
                    _var_var_9.name
                _var_var_53 = _var_var_52['original_name']
                _var_var_48 = f'''{_var_var_48}\n{_var_var_53}'''
                continue
            if not _var_var_9.tidy_type == 'video':
                continue
            _var_var_54 = _var_var_52.get('season_episode')
            if not _var_var_54:
                continue
            _var_var_51.append(_var_var_54)
        _var_var_48 = _var_var_48.lstrip(' \n')
        _var_var_55 = convert_size(_var_var_49)
        _var_var_56 = _logs[0]
        _var_var_52 = _var_var_56.video_info
        _var_var_40 = _var_var_56.tmdb_info
        _var_var_57 = f'''{_var_var_40['title']} ({_var_var_40['year']}) 整理成功'''
        _var_var_58 = _var_var_52.get('category', '未知')
        _var_var_59 = _var_var_40['type']
        _var_var_60 = ''
        if _var_var_52.get('resource_pix'):
            _var_var_60 = _var_var_52.get('resource_pix').upper()
        if _var_var_52.get('resource_effect'):
            _var_var_60 = f'''{_var_var_60} {_var_var_52.get('resource_effect')}'''
        if _var_var_52.get('resource_type'):
            _var_var_60 = f'''{_var_var_60} {_var_var_52.get('resource_type')}'''
        _var_var_60 = _var_var_60.lstrip(' \n')
        if not _var_var_60:
            _var_var_60 = '未知'
        _var_var_61 = f'''类型：{_var_var_59}，类别：{_var_var_58}，质量：{_var_var_60}'''
        if _var_var_52.get('resource_team'):
            _var_var_61 = f'''{_var_var_61}，制作组：{_var_var_52.get('resource_team')}'''
        _var_var_61 = f'''{_var_var_61}，共计：{_var_var_50}个文件 {_var_var_55}'''
        if not _var_var_48:
            _var_var_48 = f'''集数：{combine_episode_ranges(_var_var_51)}'''
        if _var_var_56.backdrop_path:
            _var_var_62 = self._tmdbapi.build_img_h632(_var_var_56.backdrop_path)
        else:
            _var_var_62 = self._tmdbapi.build_img_h632(_var_var_56.poster_path)
        if _var_var_40.get('tagline'):
            _var_var_63 = f'''{_var_var_40['tagline']}\n{_var_var_61}\n{_var_var_48}'''
        else:
            _var_var_63 = f'''{_var_var_61}\n{_var_var_48}'''
        self._message.send_msg(title = _var_var_57, text = _var_var_63, image = _var_var_62)
        return None

    
    def add_sync_path(self, path):
        if self._is_refresh_library and path:
            self._sync_path_set.add(path)
        return None

    
    def download_file(self, _file):
        self.build_url(_file)
        _var_var_64 = _file.local_path
        _var_var_65 = Mutil.merge_paths(_var_var_64, _file.name)
        _file.status = 'fail'
        _file.sync_time = TimeUtils.get_current_time_str()
        if not _file.ext:
            logger.info(f'''跳过无后缀文件, name: {_file.name}''')
            _file.status = 'skip'
            return _file
        try:
            if _file.ext in self.video_ext:
                _var_var_65 = Mutil.change_file_suffix(_var_var_65, 'strm')
                _file.local_name = Mutil.change_file_suffix(_file.name, 'strm')
                if not os.path.exists(_var_var_65):
                    os.makedirs(_var_var_64, exist_ok = True)
                    with open(_var_var_65, 'w') as _var_var_66:
                        _var_var_66.write(_file.url)
                    logger.info(f'''strm生成成功: {_var_var_65}''')
                    self.add_sync_path(_var_var_64)
                    self.strm_count += 1
                    _file.status = 'success'
                else:
                    _file.status = 'exists'
            elif _file.ext in self.img_ext or _file.ext in self.nfo_ext:
                _file.local_name = _file.name
                if not os.path.exists(_var_var_65):
                    os.makedirs(_var_var_64, exist_ok = True)
                    _var_var_67 = self.get_download_url(_file)
                    if not _var_var_67:
                        logger.error(f'''获取下载链接失败: {_var_var_65}''')
                        _file.desc = '获取下载链接失败'
                        return _file
                    with open(_var_var_65, 'wb') as _var_var_66:
                        with urlopen(_var_var_67) as _var_var_68:
                            copyfileobj(_var_var_68, _var_var_66)
                    logger.info(f'''下载文件成功: {_var_var_65}''')
                    self.nfo_count += 1
                    _file.status = 'success'
                else:
                    _file.status = 'exists'
            else:
                logger.info(f'''跳过{_file.ext}文件, name: {_file.name}''')
                _file.status = 'skip'
        except Exception as _var_var_25:
            logger.error(f'''下载文件失败: {_var_var_65}''')
            logger.error(f'''下载文件异常: {_var_var_25}''')
            _file.desc = '发生异常'
        return _file

    
    def refresh_emby_library(self):
        if not self._sync_path_set or not self._is_refresh_library:
            self._sync_path_set.clear()
            logger.info('不刷新emby库')
            return None
        logger.info(f'''转换路径之前-{self._sync_path_set}''')
        _var_var_69 = list(set(self._sync_path_set))
        _var_var_70 = []
        for _var_var_65 in _var_var_69:
            if configEnv.emby_path_replace_rule:
                _var_var_71 = configEnv.emby_path_replace_rule.split('#')
                if len(_var_var_71) == 2:
                    _var_var_65 = _var_var_65.replace(_var_var_71[0], _var_var_71[1], 1)
            if configEnv.emby_path_style == 'windows':
                _var_var_65 = _var_var_65.replace('/', '\\')
            elif configEnv.emby_path_style == 'unix':
                _var_var_65 = _var_var_65.replace('\\', '/')
            _var_var_70.append(_var_var_65)
        logger.info(f'''转换路径之后-{_var_var_70}''')
        self._emby_api.refresh_libraries_by_paths(_var_var_70)
        self._sync_path_set.clear()
        return None

    
    def send_sync_result_msg(self):
        _var_var_63 = ''
        _var_var_72 = False
        if self.strm_count > 0:
            _var_var_63 = f'''{_var_var_63}\n视频STRM：{self.strm_count} 个'''
            _var_var_72 = True
        if self.nfo_count > 0:
            _var_var_63 = f'''{_var_var_63}\n图片字幕等：{self.nfo_count} 个'''
            _var_var_72 = True
        if _var_var_72:
            self._message.send_msg(title = f'''🌟{self.storage_type}同步结果🌟''', text = _var_var_63.strip('\n'))
        self.strm_count = 0
        self.nfo_count = 0
        return None

    
    def delete_cloud_file(self, data, del_123):
        records = self.MP_CD123.get_by_fids(del_123)
        if not records:
            logger.error(f'同步删除123云盘文件失败-同步记录不存在-fids={del_123}')
            return '同步删除123云盘文件失败-同步记录不存在'
        data_type = data.get('type')
        pid_map = {}
        for record in records:
            if record.pid in pid_map:
                pid_map[record.pid].append(record)
            else:
                pid_map[record.pid] = [record]
        parent_pids = []
        video_files = []
        dir_files = []
        deleted_pids = []
        for pid in pid_map:
            children = self.MP_CD123.get_by_pid(pid)
            has_other_video = False
            for child in children:
                if child.is_dir == 1 or child.fid in del_123:
                    continue
                if not child.ext:
                    continue
                if not child.ext in config2Env.m123_video_suffix:
                    continue
                has_other_video = True
                break
            if has_other_video:
                logger.info(f'同步删除123云盘文件 {pid}-{children[0].p_name} 下还有其它视频文件，仅删除视频文件')
                for record in pid_map[pid]:
                    video_files.append(ConFile(**record.to_dict()))
            else:
                logger.info(f'同步删除123云盘文件 {pid}-{children[0].p_name} 下没有其它视频文件，删除整个文件夹')
                pid_file = self.MP_CD123.get_by_fid(pid)
                if pid_file:
                    dir_files.append(ConFile(**pid_file.to_dict()))
                deleted_pids.append(pid)
                if data_type in ('Season', 'Series', 'Episode'):
                    parent_pids.append(pid_file.pid)
        if parent_pids:
            for pid in set(parent_pids):
                children = self.MP_CD123.get_by_pid(pid)
                can_delete = True
                for child in children:
                    if child.is_dir == 1 and child.fid not in deleted_pids:
                        can_delete = False
                        break
                    if child.is_dir == 0 and child.ext and child.ext in config2Env.m123_video_suffix:
                        can_delete = False
                        break
                if can_delete:
                    logger.info(f'同步删除123云盘文件 {pid}-{children[0].p_name} 下已经没有子文件夹或视频文件，删除整个文件夹')
                    pid_file = self.MP_CD123.get_by_fid(pid)
                    if not pid_file:
                        continue
                    dir_files.append(ConFile(**pid_file.to_dict()))
                else:
                    logger.info(f'同步删除123云盘文件 {pid}-{children[0].p_name} 下还有子文件夹或视频文件，跳过删除')
        if video_files:
            self.delete_all('123', video_files)
        if dir_files:
            self.delete_all('123', dir_files)
        logger.info(f'同步删除123云盘文件-{data["title"]}-{data_type}-共{len(del_123)}个视频文件')
        return '同步删除123云盘文件成功'
    def delete_all(self, storage_type, files):
        fids = [item.fid for item in files]
        if storage_type == '123':
            self._m123.open_fs_delete_to_trash_batch(fids)
            logger.info('同步删除123云盘文件-删除云盘文件成功')
        for item in files:
            self.delete_local_file_and_log(storage_type, item)
        return None
    def delete_local_file_and_log(self, storage_type, con_file):
        try:
            _var_var_23 = Mutil.merge_paths(con_file.local_path, con_file.local_name)
            logger.info(f'''删除本地文件（夹）: {_var_var_23}''')
            del_path(_var_var_23)
            if storage_type == '123':
                self.MP_CD123.delete_by_fid(con_file.fid, con_file.is_dir)
            if con_file.is_dir == 0 and con_file.ext in self.video_ext:
                _var_var_24 = Mutil.change_file_suffix(_var_var_23, 'nfo')
                del_path(_var_var_24)
        except Exception as _var_var_25:
            logger.error(f'''删除本地文件异常: {_var_var_25}''')
        return None
