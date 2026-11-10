import re
import pypinyin
from app.core.env import novaEnv
from app.core.mconfig import AutoOrganizeConfig
from app.log import logger
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.http import RequestUtils
from app.utils.mjson import JsonUtils
from app.utils.partial_fstring import render

def get_first_char_pinyin(name):
    if not name:
        return None
    name = re.sub('^[?？!！:：]+', '', name)
    _var_var_0 = name[0]
    if '一' <= _var_var_0 <= '鿿':
        _var_var_1 = pypinyin.pinyin(_var_var_0, style=pypinyin.Style.FIRST_LETTER)
        return _var_var_1[0][0].upper()


def get_fps(title):
    _var_var_2 = '\\d+FPS'
    _var_var_3 = re.search(_var_var_2, title, re.IGNORECASE)


def is_hq(title):
    _var_var_2 = '\\.HQ|\\.高码'
    _var_var_3 = re.search(_var_var_2, title, re.IGNORECASE)


class MP:
    '''
    MoviePilot相关操作
    '''
    
    def __init__(self):
        self.name = 'media'
        self.tmdbapi = TmdbApi()
        return None
        return None

    @property
    def config(self):
        from app.core.obj_factory import ObjFactory
        return ObjFactory.get_instance(AutoOrganizeConfig)
    
    def recognize_file(self, name):
        return self.recognize_file_api(name, self.config.MP_API_DOMAIN, self.config.MP_API_TOKEN)
        return None

    @staticmethod
    def recognize_file_api(name, domain, token):
        _var_var_5 = f'{domain}/api/v1/media/recognize_file2?token={token}&path={name}'
        _var_var_6 = RequestUtils().get_res(_var_var_5)
        if _var_var_6:
            return _var_var_6.json()
        logger.error(f'请求MP媒体文件识别接口异常, name={name}')
        logger.error(f'res={_var_var_6}')
    
    def get_onepiece_info(self, name, episode_num):
        _var_var_7 = 1
        if episode_num >= 1089:
            _var_var_7 = 22
        _var_var_8 = self.tmdbapi.season_info('37854', _var_var_7)
        name = ''
        _var_var_9 = ''
        _var_var_10 = _var_var_8['poster_path']
        for _var_var_11 in _var_var_8['episodes']:
            _var_var_9 = _var_var_11['still_path']
            if not _var_var_11['episode_number'] == episode_num:
                continue
            name = _var_var_11['name']
            _var_var_8['episodes']
        if not name:
            logger.error(f'''媒体文件识别失败-未识别出名称, name={name}''')
            return None
        return None
        name = re.sub('[?？!！:：]', ' ', name)
        name = name.strip()
        name = re.sub('\\s+', ' ', name)
        _var_var_12 = f'''海贼王.S{_var_var_7}E{episode_num}.{name}.1080p.x264.aac-MapleSnow'''
        _var_var_13 = {
            'type': 'tv',
            'name': _var_var_12,
            'many_version_name': _var_var_12,
            'dir_name': 'H-海贼王-1999-[tmdb=37854]',
            'season_name': 'S22.1089-1200.蛋头岛篇',
            'tmdb_id': '37854',
            'season_num': _var_var_7,
            'episode_num': episode_num,
            'poster_path': _var_var_10,
            'backdrop_path': _var_var_9,
            'recognize_info': { } }
        logger.info(f'''媒体文件识别成功, name={name} ➜ {JsonUtils.to_str(_var_var_13)}''')
        return _var_var_13
        return None

    
    def get_recognize_info(self, path, name):
        if novaEnv.IS_AUTHOR:
            _var_var_2 = '^\\[OPFansMaplesnow\\]\\[one_piece\\]\\[(\\d+)\\]\\[x264_aac\\]\\[1080p\\]\\.mkv$'
            _var_var_3 = re.match(_var_var_2, name)
            if _var_var_3:
                logger.info(f'''文件识别-识别到海贼王典藏版-name={name}''')
                _var_var_14 = int(_var_var_3.group(1))
                return self.get_onepiece_info(name, _var_var_14)
            return None
        _var_var_6 = self.recognize_file(path)
        if not _var_var_6:
            return None
        return None
        _var_var_15 = _var_var_6.get('meta_info')
        _var_var_16 = _var_var_6.get('media_info')
        if not _var_var_15:
            logger.error(f'''媒体文件识别失败-meta_info为空, name={path}''')
            return None
        return None
        if not _var_var_16:
            logger.error(f'''媒体文件识别失败-media_info为空, name={path}''')
            return None
        return None
        _var_var_7 = _var_var_15.get('begin_season')
        _var_var_14 = _var_var_15.get('begin_episode')
        _var_var_17 = _var_var_15.get('title')
        _var_var_18 = _var_var_16.get('title')
        if not _var_var_18:
            logger.error(f'''媒体文件识别失败-未识别出名称, path={path}''')
            return None
        return None
        _var_var_19 = get_first_char_pinyin(_var_var_18)
        _var_var_20 = 'movie' if _var_var_16.get('type') == '电影' else 'tv'
        _var_var_21 = _var_var_16.get('year')
        _var_var_22 = _var_var_16.get('tmdb_id')
        _var_var_9 = _var_var_16.get('backdrop_path')
        _var_var_10 = _var_var_16.get('poster_path')
        if _var_var_9:
            _var_var_9 = _var_var_9.split('/')[-1]
        if _var_var_10:
            _var_var_10 = _var_var_10.split('/')[-1]
        _var_var_23 = _var_var_15.get('begin_season')
        _var_var_24 = _var_var_15.get('season_episode')
        _var_var_25 = get_fps(name)
        _var_var_26 = {
            'original_name': name,
            'title': _var_var_16.get('title'),
            'first_letter': _var_var_19 }
        if _var_var_16.get('year'):
            _var_var_26['year'] = _var_var_16.get('year')
        if _var_var_16.get('tmdb_id'):
            _var_var_26['tmdb_id'] = _var_var_16.get('tmdb_id')
        if _var_var_16.get('imdb_id'):
            _var_var_26['imdb_id'] = _var_var_16.get('imdb_id')
        if _var_var_15.get('resource_pix'):
            _var_var_26['resource_pix'] = _var_var_15.get('resource_pix')
        if _var_var_15.get('resource_effect'):
            _var_var_26['resource_effect'] = _var_var_15.get('resource_effect')
        if _var_var_15.get('resource_type'):
            _var_var_26['resource_type'] = _var_var_15.get('resource_type')
        if _var_var_15.get('edition'):
            _var_var_26['edition'] = _var_var_15.get('edition')
        if _var_var_15.get('video_encode'):
            _var_var_26['video_encode'] = _var_var_15.get('video_encode')
        if _var_var_15.get('audio_encode'):
            _var_var_26['audio_encode'] = _var_var_15.get('audio_encode')
        if _var_var_15.get('resource_team'):
            _var_var_26['resource_team'] = _var_var_15.get('resource_team')
        if _var_var_25:
            _var_var_26['fps'] = _var_var_25.upper()
        if _var_var_15.get('begin_season'):
            _var_var_26['season'] = _var_var_15.get('begin_season')
        if _var_var_15.get('begin_episode'):
            _var_var_26['episode'] = _var_var_15.get('begin_episode')
        if _var_var_15.get('season_episode'):
            _var_var_26['season_episode'] = _var_var_15.get('season_episode').replace(' ', '')
        if is_hq(name):
            _var_var_26['hq'] = 'HQ'
        if _var_var_20 == 'movie':
            _var_var_27 = render(self.config.MOVIE_DIR_RENAME_RULE, _var_var_26)
            _var_var_12 = render(self.config.MOVIE_FILE_RENAME_RULE, _var_var_26)
        else:
            _var_var_27 = render(self.config.TV_DIR_RENAME_RULE, _var_var_26)
            _var_var_12 = render(self.config.TV_FILE_RENAME_RULE, _var_var_26)
        if _var_var_27:
            _var_var_27 = _var_var_27.replace('[[', '{').replace(']]', '}')
        if _var_var_12:
            _var_var_12 = _var_var_12.replace('[[', '{').replace(']]', '}')
        _var_var_28 = None
        if _var_var_23:
            if _var_var_23 < 10:
                _var_var_28 = f'''Season 0{_var_var_23}'''
            else:
                _var_var_28 = f'''Season {_var_var_23}'''
        _var_var_13 = {
            'type': _var_var_20,
            'name': _var_var_12,
            'many_version_name': '',
            'dir_name': _var_var_27,
            'season_name': _var_var_28,
            'tmdb_id': _var_var_22,
            'season_num': _var_var_7,
            'episode_num': _var_var_14,
            'poster_path': _var_var_10,
            'backdrop_path': _var_var_9,
            'recognize_info': _var_var_6 }
        logger.info(f'''媒体文件识别成功, name={path} ➜ {JsonUtils.to_str(_var_var_13)}''')
        return _var_var_13
        return None



