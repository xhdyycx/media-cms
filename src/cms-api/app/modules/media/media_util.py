import re
import pypinyin
from sqlalchemy.orm import Session
from app.core.env import novaEnv, configEnv
from app.db.tmdb_cache_op import TmdbCacheOp
from app.log import logger
from app.modules.media.tmdb_info import TmdbInfo
from app.modules.media.types.media_info import MediaInfo
from app.modules.media.video_info import VideoInfo
from app.modules.openai.gpt import GPT
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.mjson import JsonUtils
from app.utils.mutil import Mutil
from app.utils.partial_fstring import render

class MediaUtil:
    
    def __init__(self, path, db):
        logger.info(f'''开始识别：{path}''')
        self._tmdb_cache_op = TmdbCacheOp(db)
        self.path = path
        self.is_used_gpt = False
        self.tmdbapi = TmdbApi()
        self.tmdbapi_en = TmdbApi(language = 'en-US')
        self.video_info = VideoInfo(self.path)
        self.gpt_recognize()
        self.tmdb_info = TmdbInfo(self.video_info)
        self.get_tmdb_cache()
        self.check_tmdb_info()
        self.check_tmdb_title()
        self.build_final_type()
        return None
        return None

    
    def build_final_type(self):
        if self.tmdb_info and self.video_info:
            self.video_info.type = self.tmdb_info.type
        return None
        return None

    
    def check_tmdb_title(self):
        if not self.tmdb_info.title:
            return None
        return None
        if re.search('[\\u4e00-\\u9fa5]+', self.tmdb_info.title):
            return None
        return None
        if not configEnv.gpt_recognize_status == 'disabled' or configEnv.is_zh_language:
            return None
        return None
        _var_var_0 = f'''{self.tmdb_info.title}.{self.tmdb_info.year}'''
        _var_var_1 = GPT().get_douban_title(_var_var_0)
        logger.info(f'''GPT识别中文名称的结果为：{_var_var_1}，name={_var_var_0}''')
        try:
            if _var_var_1:
                _var_var_2 = JsonUtils.json_to_dict(_var_var_1)
                if _var_var_2.get('name'):
                    self.tmdb_info.title = _var_var_2.get('name')
        except Exception as _var_var_3:
            logger.error(f'''GPT识别中文名称异常, name={_var_var_0}, error={_var_var_3}''')
            return None

    
    def check_tmdb_info(self):
        if self.tmdb_info.title or self.is_used_gpt:
            return None
        return None
        self.gpt_recognize(True)
        self.tmdb_info = TmdbInfo(self.video_info)
        return None
        return None

    
    def get_tmdb_cache(self):
        _var_var_4 = self._tmdb_cache_op.get_by_query_url(f'''/3/search/{self.tmdb_info.type}/{self.tmdb_info.tmdb_id}''')
        if not _var_var_4:
            return None
        return None
        logger.info(f'''命中TMDB识别缓存, {self.tmdb_info.title} {self.tmdb_info.year} tmdb_id={self.tmdb_info.tmdb_id}''')
        _var_var_5 = self.tmdb_info
        _var_var_6 = _var_var_4.get('query_response', '{}')
        _var_var_6 = JsonUtils.json_to_dict(_var_var_6)
        if not _var_var_6.get('title'):
            _var_var_6.get('title')
        _var_var_7 = _var_var_6.get('name')
        if _var_var_7:
            _var_var_5.title = _var_var_7
        if _var_var_6.get('origin_country'):
            _var_var_5.origin_country = _var_var_6.get('origin_country')
        if _var_var_6.get('genre_ids'):
            _var_var_5.genre_ids = _var_var_6.get('genre_ids')
        if _var_var_6.get('original_language'):
            _var_var_5.original_language = _var_var_6.get('original_language')
        if _var_var_6.get('tagline'):
            _var_var_5.tagline = _var_var_6.get('tagline')
        if _var_var_6.get('overview'):
            _var_var_5.overview = _var_var_6.get('overview')
        self.tmdb_info = _var_var_5
        return None
        return None

    
    def gpt_recognize(self, force_use=False):
        try:
            if configEnv.gpt_recognize_status == 'disabled' or not self.video_info.tmdb_id:
                return None
            _var_var_8 = force_use
            if configEnv.gpt_recognize_status == 'assist_use' and not self.video_info.name and not self.video_info.en_name:
                _var_var_8 = True
            if configEnv.gpt_recognize_status == 'force_use':
                _var_var_8 = True
            if _var_var_8:
                _var_var_9 = GPT()
                _var_var_1 = _var_var_9.recognize_media(self.path)
                self.is_used_gpt = True
                if _var_var_1:
                    _var_var_2 = JsonUtils.json_to_dict(_var_var_1)
                    if _var_var_2.get('name'):
                        self.video_info.name = _var_var_2.get('name')
                    if _var_var_2.get('year'):
                        self.video_info.year = _var_var_2.get('year')
                    if _var_var_2.get('episode'):
                        self.video_info.type = 'tv'
                        self.video_info.episode_num = _var_var_2.get('episode')
                        self.video_info.build_season_episode()
                    else:
                        self.video_info.type = 'movie'
        except Exception as _var_var_3:
            logger.error(f'GPT识别异常, path={self.path}, error={_var_var_3}')
        return None

    def get_onepiece_info(self, name, episode_num):
        _var_var_11 = 1
        if episode_num >= 1089:
            _var_var_11 = 22
        _var_var_12 = self.tmdbapi.season_info('37854', _var_var_11)
        name = ''
        _var_var_13 = ''
        _var_var_14 = _var_var_12['poster_path']
        for _var_var_15 in _var_var_12['episodes']:
            _var_var_13 = _var_var_15['still_path']
            if not _var_var_15['episode_number'] == episode_num:
                continue
            name = _var_var_15['name']
            _var_var_12['episodes']
        if not name:
            logger.error(f'''媒体文件识别失败-未识别出名称, name={name}''')
            return None
        return None
        name = re.sub('[?？!！:：]', ' ', name)
        name = name.strip()
        name = re.sub('\\s+', ' ', name)
        _var_var_16 = f'''海贼王.S{_var_var_11}E{episode_num}.{name}.1080p.x264.aac-MapleSnow'''
        _var_var_17 = {
            'type': 'tv',
            'name': _var_var_16,
            'many_version_name': _var_var_16,
            'dir_name': 'H-海贼王-1999-[tmdb=37854]',
            'season_name': 'S22.1089-1200.蛋头岛篇',
            'tmdb_id': '37854',
            'season_num': _var_var_11,
            'episode_num': episode_num,
            'poster_path': _var_var_14,
            'backdrop_path': _var_var_13,
            'video_info': self.video_info.to_dict(),
            'tmdb_info': self.tmdb_info.to_dict() }
        logger.info(f'''媒体文件识别成功, name={name} ➜ {JsonUtils.to_str(_var_var_17)}''')
        return _var_var_17
        return None

    
    def recognize_info_v2(self) -> MediaInfo | None:
        _var_var_18 = self.recognize_info()
        if _var_var_18:
            return MediaInfo(**_var_var_18)
        return None
    def recognize_info(self):
        if novaEnv.IS_AUTHOR:
            _var_var_19 = '^\\[OPFansMaplesnow\\]\\[one_piece\\]\\[(\\d+)\\]\\[x264_aac\\]\\[1080p\\]\\.mkv$'
            _var_var_20 = re.match(_var_var_19, self.video_info.original_name)
            if _var_var_20:
                logger.info(f'文件识别-识别到海贼王典藏版-name={self.video_info.original_name}')
                _var_var_10 = int(_var_var_20.group(1))
                return self.get_onepiece_info(self.video_info.original_name, _var_var_10)
        _var_var_21 = self.video_info
        _var_var_7 = self.tmdb_info.title
        if not _var_var_7:
            logger.error(f'媒体文件识别失败-未识别出名称, path={self.path}')
            return None
        _var_var_22 = get_first_char_pinyin(_var_var_7)
        _var_var_23 = self.tmdb_info.type
        if _var_var_23 == 'tv' and _var_var_21.episode_num is None:
            logger.error(f'媒体文件识别失败-未识别出集信息, path={self.path}')
            return None
        _var_var_24 = {'original_name': _var_var_21.original_name, 'title': Mutil.remove_zero_width_chars(self.tmdb_info.title), 'first_letter': _var_var_22, 'year': self.tmdb_info.year, 'tmdb_id': self.tmdb_info.tmdb_id}
        if _var_var_21.resource_pix:
            _var_var_24['resource_pix'] = _var_var_21.resource_pix
        if _var_var_21.resource_version:
            _var_var_24['resource_version'] = _var_var_21.resource_version
        if _var_var_21.resource_source:
            _var_var_24['resource_source'] = _var_var_21.resource_source
        if _var_var_21.resource_type:
            _var_var_24['resource_type'] = _var_var_21.resource_type
        if _var_var_21.resource_effect:
            _var_var_24['resource_effect'] = _var_var_21.resource_effect
        if _var_var_21.video_encode:
            _var_var_24['video_encode'] = _var_var_21.video_encode
        if _var_var_21.audio_encode:
            _var_var_24['audio_encode'] = _var_var_21.audio_encode
        if _var_var_21.resource_team:
            _var_var_24['resource_team'] = _var_var_21.resource_team
        if _var_var_21.fps:
            _var_var_24['fps'] = _var_var_21.fps
        if _var_var_21.season_num is not None:
            _var_var_24['season_num'] = _var_var_21.season_num
        if _var_var_21.episode_num is not None:
            _var_var_24['episode_num'] = _var_var_21.episode_num
        if _var_var_21.season_episode:
            _var_var_24['season_episode'] = _var_var_21.season_episode
        if _var_var_21.disc_num is not None:
            _var_var_24['disc_num'] = _var_var_21.disc_num
        if _var_var_21.custom_regex_match is not None:
            _var_var_24['custom_regex_match'] = _var_var_21.custom_regex_match
        if _var_var_21.ext:
            _var_var_24['ext'] = _var_var_21.ext
        if _var_var_23 == 'tv' and _var_var_21.season_num:
            if self.tmdb_info.season_name:
                _var_var_24['season_name'] = self.tmdb_info.season_name
            if self.tmdb_info.season_year:
                _var_var_24['season_year'] = self.tmdb_info.season_year
            if configEnv.tv_file_rename_rule and 'episode_name' in configEnv.tv_file_rename_rule:
                _var_var_12 = self.tmdbapi.season_info(self.tmdb_info.tmdb_id, _var_var_21.season_num)
                if _var_var_12:
                    if _var_var_12.get('poster_path'):
                        self.tmdb_info.poster_path = _var_var_12['poster_path']
                    for _var_var_15 in _var_var_12['episodes']:
                        if not _var_var_21.episode_num:
                            continue
                        if not (int(_var_var_15['episode_number']) == int(_var_var_21.episode_num)):
                            continue
                        if _var_var_15.get('name'):
                            _var_var_24['episode_name'] = _var_var_15['name']
        if not self.tmdb_info.en_title:
            if _var_var_23 == 'movie':
                if 'en_title' in configEnv.movie_dir_rename_rule or 'en_title' in configEnv.movie_file_rename_rule:
                    _var_var_25 = self.tmdbapi_en.get_movie_details_by_tmdb_id(self.tmdb_info.tmdb_id)
                    if Mutil.is_en_title(_var_var_25['title']):
                        self.tmdb_info.en_title = _var_var_25['title']
                    else:
                        self.tmdb_info.en_title = Mutil.chinese_to_pinyin(self.tmdb_info.title)
            if _var_var_23 == 'tv':
                if 'en_title' in configEnv.tv_dir_rename_rule or 'en_title' in configEnv.tv_file_rename_rule:
                    _var_var_26 = self.tmdbapi_en.get_tv_details(self.tmdb_info.tmdb_id)
                    if Mutil.is_en_title(_var_var_26['name']):
                        self.tmdb_info.en_title = _var_var_26['name']
                    else:
                        self.tmdb_info.en_title = Mutil.chinese_to_pinyin(self.tmdb_info.title)
        if self.tmdb_info.en_title:
            _var_var_24['en_title'] = self.tmdb_info.en_title.replace(' ', '.')
        try:
            if _var_var_23 == 'movie':
                _var_var_27 = render(configEnv.movie_dir_rename_rule, _var_var_24)
                _var_var_16 = render(configEnv.movie_file_rename_rule, _var_var_24)
            else:
                _var_var_27 = render(configEnv.tv_dir_rename_rule, _var_var_24)
                _var_var_16 = render(configEnv.tv_file_rename_rule, _var_var_24)
            if _var_var_27:
                _var_var_27 = _var_var_27.replace('[[', '{').replace(']]', '}')
            if _var_var_16:
                _var_var_16 = _var_var_16.replace('[[', '{').replace(']]', '}')
        except Exception as _var_var_3:
            logger.exception(f'重命名规则有错误的语法, error={_var_var_3}')
            return None
        _var_var_28 = None
        if _var_var_23 == 'tv' and _var_var_21.season_num is not None:
            _var_var_28 = render(configEnv.tv_season_dir_rename_rule, _var_var_24)
        _var_var_29 = self.tmdb_info.to_dict()
        _var_var_29['ext'] = self.video_info.ext
        _var_var_29['name'] = _var_var_16
        if _var_var_16.endswith(self.video_info.ext):
            _var_var_16 = _var_var_16[: -len(self.video_info.ext) - 1]
        _var_var_17 = {'type': _var_var_23, 'tidy_type': 'video', 'name': _var_var_16, 'many_version_name': '', 'dir_name': _var_var_27, 'season_name': _var_var_28, 'tmdb_id': self.tmdb_info.tmdb_id, 'season_num': _var_var_21.season_num, 'episode_num': _var_var_21.episode_num, 'poster_path': self.tmdb_info.poster_path, 'backdrop_path': self.tmdb_info.backdrop_path, 'video_info': self.video_info.to_dict(), 'tmdb_info': _var_var_29}
        logger.info(f'媒体文件识别成功, name={self.path} ➜ {JsonUtils.to_str(_var_var_17)}')
        return _var_var_17
def get_first_char_pinyin(name):
    if not name:
        return None
    name = re.sub('^[?？!！:：]+', '', name)
    _var_var_30 = name[0]
    if '一' <= _var_var_30 <= '鿿':
        _var_var_31 = pypinyin.pinyin(_var_var_30, style=pypinyin.Style.FIRST_LETTER)
        return _var_var_31[0][0].upper()
    # None(...)

if __name__ == '__main__':
    res = MediaUtil('/待整理/诺斯费拉图 4K原盘REMUX [HDR 杜比视界] [加长版] [中英特字 简繁特字]/Nosferatu.2024.Extended.2160p.BluRay.REMUX.HDR.DV.HEVC.DTS-HD.MA.TrueHD.7.1.Atmos.mkv').recognize_info()
    print(res)

