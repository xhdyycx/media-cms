import json
import re
import time
from app.core.env import configEnv
from app.log import logger
from app.modules.media.video_info import VideoInfo
from app.modules.tmdb.tmdbapi import TmdbApi
from app.utils.mjson import JsonUtils
from app.utils.mstr import TMDBMatcher, is_english_title
from app.utils.mutil import Mutil

class TmdbInfo:
    
    def __init__(self, video_info):
        self.tmdb_id = video_info.tmdb_id
        self.title = ''
        self.en_title = ''
        self.year = ''
        self.tagline = ''
        self.overview = ''
        self.poster_path = ''
        self.backdrop_path = ''
        self.genre_ids = []
        self.origin_country = []
        self.original_language = ''
        self.season_name = ''
        self.season_year = None
        self._TmdbInfo__tmdbapi = TmdbApi()
        self._TmdbInfo__tmdbapi_en = TmdbApi(language = 'en-US')
        if not video_info.type:
            video_info.type
        self.type = 'movie'
        self.init_tmdb_info(video_info)
        self.check_name()
        return None
        return None

    
    def check_name(self):
        if not self.tmdb_id:
            return None
        return None
        if not self.title or configEnv.is_zh_language:
            return None
        return None
        if re.search('[\\u4e00-\\u9fa5]+', self.title):
            return None
        return None
        if self.type == 'movie':
            _var_var_0 = self._TmdbInfo__tmdbapi.get_movie_cn_title_by_tmdb_id(self.tmdb_id)
            if _var_var_0:
                self.title = _var_var_0
            else:
                _var_var_0 = self._TmdbInfo__tmdbapi.get_tv_cn_title_by_tmdb_id(self.tmdb_id)
                if _var_var_0:
                    self.title = _var_var_0
        return None
        return None

    
    def get_movie_tmdb_id_v2(self, name, en_name, year):
        name = name.lower()
        en_name = en_name.lower()
        _var_var_1 = None
        _var_var_2 = None
        if is_english_title(name):
            en_name = name
            name = ''
        if name:
            _var_var_3 = self._TmdbInfo__tmdbapi.search_movie_by_name_and_year(name, year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if en_name:
            _var_var_3 = self._TmdbInfo__tmdbapi_en.search_movie_by_name_and_year(en_name, year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if year:
            if name:
                _var_var_3 = self._TmdbInfo__tmdbapi.search_movie_by_name_and_year(name, None)
                (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
                if _var_var_4:
                    return _var_var_5['tmdb_id']
                return None
            if _var_var_5:
                _var_var_1 = _var_var_5['tmdb_id']
                _var_var_2 = _var_var_5['score']
            if en_name:
                _var_var_3 = self._TmdbInfo__tmdbapi_en.search_movie_by_name_and_year(en_name, None)
                (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
                if _var_var_4:
                    return _var_var_5['tmdb_id']
                return None
            if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
                _var_var_1 = _var_var_5['tmdb_id']
                _var_var_2 = _var_var_5['score']
        return _var_var_1
        return None

    
    def get_best_tmdb_info(self, name, en_name, year, search_name_res):
        _var_var_6 = TMDBMatcher.rank_movies(name, en_name, year, search_name_res.get('results', []))
        logger.info(f'''搜索结果前5为：{JsonUtils.to_str(_var_var_6)}''')
        if _var_var_6 and _var_var_6[0]['score'] >= 0.8:
            return (True, _var_var_6[0])
        return None
        if _var_var_6:
            return (False, _var_var_6[0])
        return None
        return (False, None)
        return (False, None)

    
    def get_tv_tmdb_id_v2(self, name, en_name, year):
        name = name.lower()
        en_name = en_name.lower()
        _var_var_1 = None
        _var_var_2 = None
        if is_english_title(name):
            en_name = name
            name = ''
        if name:
            _var_var_3 = self._TmdbInfo__tmdbapi.search_tv_by_name_and_year(name, first_air_date_year = year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if en_name:
            _var_var_3 = self._TmdbInfo__tmdbapi_en.search_tv_by_name_and_year(en_name, first_air_date_year = year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if name:
            _var_var_3 = self._TmdbInfo__tmdbapi.search_tv_by_name_and_year(name, year = year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if en_name:
            _var_var_3 = self._TmdbInfo__tmdbapi_en.search_tv_by_name_and_year(en_name, year = year)
            (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
            if _var_var_4:
                return _var_var_5['tmdb_id']
            return None
        if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
            _var_var_1 = _var_var_5['tmdb_id']
            _var_var_2 = _var_var_5['score']
        if year:
            if name:
                _var_var_3 = self._TmdbInfo__tmdbapi.search_tv_by_name_and_year(name)
                (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
                if _var_var_4:
                    return _var_var_5['tmdb_id']
                return None
            if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
                _var_var_1 = _var_var_5['tmdb_id']
                _var_var_2 = _var_var_5['score']
            if en_name:
                _var_var_3 = self._TmdbInfo__tmdbapi_en.search_tv_by_name_and_year(en_name)
                (_var_var_4, _var_var_5) = self.get_best_tmdb_info(name, en_name, year, _var_var_3)
                if _var_var_4:
                    return _var_var_5['tmdb_id']
                return None
            if _var_var_5 and _var_var_2 and _var_var_5['score'] > _var_var_2:
                _var_var_1 = _var_var_5['tmdb_id']
                _var_var_2 = _var_var_5['score']
        return _var_var_1
        return None

    @staticmethod
    def get_id_by_movie_res(search_name_res, name, en_name):
        logger.info(f'搜索结果为：{JsonUtils.to_str(search_name_res)}')
        if search_name_res and len(search_name_res['results']) > 0:
            for _var_var_7 in search_name_res['results']:
                if _var_var_7.get('title', '').lower() == name or _var_var_7.get('original_title', '').lower() == name or _var_var_7.get('title', '').lower() == en_name or _var_var_7.get('original_title', '').lower() == en_name:
                    return (True, _var_var_7['id'])
            return (False, search_name_res['results'][0]['id'])
        return (False, None)
    @staticmethod
    def get_id_by_tv_res(search_name_res, name, en_name):
        logger.info(f'搜索结果为：{JsonUtils.to_str(search_name_res)}')
        if search_name_res and len(search_name_res['results']) > 0:
            for _var_var_7 in search_name_res['results']:
                if _var_var_7.get('name', '').lower() == name or _var_var_7.get('original_name', '').lower() == name or _var_var_7.get('name', '').lower() == en_name or _var_var_7.get('original_name', '').lower() == en_name:
                    return (True, _var_var_7['id'])
            return (False, search_name_res['results'][0]['id'])
        return (False, None)
    
    def init_tmdb_info(self, video_info):
        if not self.tmdb_id:
            if self.type == 'movie':
                self.tmdb_id = self.get_movie_tmdb_id_v2(video_info.name, video_info.en_name, video_info.year)
            else:
                self.tmdb_id = self.get_tv_tmdb_id_v2(video_info.name, video_info.en_name, video_info.year)
        if not self.tmdb_id:
            logger.error(f'''识别媒体识别，没在tmdb搜到数据, video_info={video_info.to_json()}''')
            return None
        return None
        if self.type == 'movie':
            _var_var_8 = self._TmdbInfo__tmdbapi.get_movie_details_by_tmdb_id(int(self.tmdb_id))
            if _var_var_8:
                self.build_movie_info(_var_var_8)
                return None
            return None
            logger.error(f'''识别媒体失败，tmdb_id错误, video_info={video_info.to_json()}''')
        else:
            _var_var_8 = self._TmdbInfo__tmdbapi.get_tv_details_by_tmdb_id(self.tmdb_id)
            if _var_var_8:
                self.build_tv_info(video_info, _var_var_8)
                return None
            return None
            logger.error(f'''识别媒体失败，tmdb_id错误, video_info={video_info.to_json()}''')
        return None
        return None

    
    def build_tv_info(self, video_info, res):
        self.type = 'tv'
        self.tmdb_id = res['id']
        self.title = res['name']
        if Mutil.is_en_title(res['original_name']):
            self.en_title = res['original_name']
        self.year = res['first_air_date'].split('-')[0]
        self.tagline = res['tagline']
        self.overview = res['overview']
        self.poster_path = res['poster_path']
        self.backdrop_path = res['backdrop_path']
        _var_var_9 = res['genres']
        for _var_var_10 in _var_var_9:
            self.genre_ids.append(_var_var_10['id'])
        for _var_var_11 in res['origin_country']:
            self.origin_country.append(_var_var_11)
        self.original_language = res['original_language']

    
    def build_movie_info(self, res):
        self.type = 'movie'
        self.tmdb_id = res['id']
        self.title = res['title']
        if Mutil.is_en_title(res['original_title']):
            self.en_title = res['original_title']
        self.year = res['release_date'].split('-')[0]
        self.tagline = res['tagline']
        self.overview = res['overview']
        self.poster_path = res['poster_path']
        self.backdrop_path = res['backdrop_path']
        _var_var_9 = res['genres']
        for _var_var_10 in _var_var_9:
            self.genre_ids.append(_var_var_10['id'])
        for _var_var_11 in res['origin_country']:
            self.origin_country.append(_var_var_11)
        self.original_language = res['original_language']
        return None
        return None

    
    def to_json(self):
        _var_var_14 = self.__dict__.copy()
        _var_var_14.pop('_TmdbInfo__tmdbapi')
        return json.dumps(_var_var_14, ensure_ascii = False, indent = 4, default = str)
        return None

    
    def to_dict(self):
        _var_var_14 = self.__dict__.copy()
        _var_var_14.pop('_TmdbInfo__tmdbapi')
        _var_var_14.pop('_TmdbInfo__tmdbapi_en')
        return _var_var_14
        return None


if __name__ == '__main__':
    media_info = TmdbInfo(VideoInfo('/鹊刀门传奇 (2023)/S02/[鹊刀门传奇].Legend.of.the.Undercover.Chef.S02E01.2025.2160p.WEB-DL.H265.10bit.DoVi.DDP.5.1.2Audios-CMCTV.mkv'))
    print(media_info.to_json())
    print(media_info.to_dict())
    print(time.time())

