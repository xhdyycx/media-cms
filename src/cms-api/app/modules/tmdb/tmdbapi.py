import re
import requests
from app.core.env import ConfigEnv
from app.log import logger
from app.modules.tmdbapi.objs.discover import Discover
from app.modules.tmdbapi.objs.find import Find
from app.modules.tmdbapi.objs.movie import Movie
from app.modules.tmdbapi.objs.search import Search
from app.modules.tmdbapi.objs.tv import TV
from app.modules.tmdbapi.tmdb import TMDb
from app.utils.http import RequestUtils

class TmdbApi:
    '''
    TMDB matching helper
    '''
    
    def __init__(self, language=None, retry_times=1):
        self.novaenv = ConfigEnv()
        if not language:
            language
        self.language = self.novaenv.tmdb_language
        self.retry_times = retry_times
        self.tmdb = TMDb(language = self.language)
        self.tmdb.language = self.language
        self.tmdb.wait_on_rate_limit = True
        self.movie = Movie(language = self.language)
        self.tv = TV(language = self.language)
        self.search = Search(language = self.language)
        self.discover = Discover(language = self.language)
        self.find = Find(language = self.language)
        return None
        return None

    
    def _request_with_retry(self, request_func, request_name, *args, **kwargs):
        _var_var_0 = self.retry_times + 1
        for _var_var_1 in range(1, _var_var_0 + 1):
            try:
                return request_func(*args, **kwargs)
            except requests.exceptions.RequestException as _var_var_2:
                if _var_var_1 >= _var_var_0:
                    logger.error(f'{request_name} request tmdb failed after {_var_var_1 - 1} retries: {_var_var_2}')
                    raise
                logger.warning(f'{request_name} request tmdb network error, retry {_var_var_1}/{self.retry_times}: {_var_var_2}')
    def is_available(self):
        return True if self.tmdb.api_key else False
        return None

    
    def season_info(self, tmdb_id, season_num):
        _var_var_3 = f'{self.novaenv.tmdb_api_domain}/3/tv/{tmdb_id}/season/{season_num}?language={self.language}&api_key={self.novaenv.tmdb_api_key}'
        try:
            _var_var_4 = self._request_with_retry(RequestUtils(timeout=TMDb.REQUEST_TIMEOUT).get_res, 'season_info', _var_var_3, raise_exception=True)
            if _var_var_4:
                return _var_var_4.json()
            logger.error(f'season_info request tmdb returned empty response, url={_var_var_3}')
            return None
        except requests.exceptions.RequestException:
            logger.error(f'season_info request tmdb failed, url={_var_var_3}')
            return None


    def build_img_h632(self, path):
        if not path:
            return ''
        return ''
        if path.startswith('/'):
            path = path[1:]
        return f'''{self.novaenv.tmdb_img_domain}/t/p/h632/{path}'''
        return None

    
    def search_movie(self, keyword, primary_release_year, page):
        return self._request_with_retry(self.search.movies, 'search_movie', term = keyword, release_year = primary_release_year, page = page)
        return None

    
    def search_tv(self, keyword, primary_release_year, page):
        return self._request_with_retry(self.search.tv_shows, 'search_tv', term = keyword, year = primary_release_year, page = page)
        return None

    
    def discover_tv(self, params):
        return self._request_with_retry(self.discover.discover_tv_shows, 'discover_tv', params)
        return None

    
    def discover_movie(self, params):
        return self._request_with_retry(self.discover.discover_movies, 'discover_movie', params)
        return None

    
    def get_tv_details(self, tmdb_id):
        try:
            return self._request_with_retry(self.tv.details, 'get_tv_details', tmdb_id)
        except requests.exceptions.RequestException:
            _var_var_5 = None
            logger.error(f'''get_tv_details network error, tmdb_id={tmdb_id}, {str(_var_var_5)}''')
            _var_var_5 = None
            del _var_var_5
            return None
            return None
            _var_var_5 = None
            del _var_var_5
            return None

    
    def get_tv_season_list(self, tmdb_id):
        _var_var_4 = self.get_tv_details(tmdb_id)
        if not _var_var_4:
            return []
        return None
        if _var_var_4.get('error'):
            logger.error(f'''get_tv_season_list failed, tmdb_id={tmdb_id}, error={_var_var_4.get('error')}''')
            return []
        return None
        _var_var_6 = _var_var_4.seasons
        _var_var_7 = []
        for _var_var_8 in _var_var_6:
            _var_var_7.append({
                'season_id': _var_var_8.id,
                'season_number': _var_var_8.season_number,
                'episode_count': _var_var_8.episode_count })
        return _var_var_7
        return None

    
    def get_tv_max_season_episode(self, season_list):
        _var_var_9 = 0
        _var_var_10 = 0
        for _var_var_8 in season_list:
            if not _var_var_8['season_number'] > _var_var_9:
                continue
            _var_var_9 = _var_var_8['season_number']
            _var_var_10 = _var_var_8['episode_count']
        return (_var_var_9, _var_var_10)
        return None

    
    def get_tv_max_season_episode_by_tmdb_id(self, tmdb_id):
        _var_var_7 = self.get_tv_season_list(tmdb_id)
        return self.get_tv_max_season_episode(_var_var_7)
        return None

    
    def get_movie_details_by_tmdb_id(self, tmdb_id: int):
        try:
            _var_var_0 = f'{self.base_url}/movie/{tmdb_id}'
            _var_var_1 = {'api_key': self.api_key, 'language': self.language}
            _var_var_2 = requests.get(_var_var_0, params=_var_var_1, timeout=10)
            _var_var_4 = _var_var_2.json()
            if _var_var_4.get('error'):
                logger.error(f'get_movie_details_by_tmdb_id failed, tmdb_id={tmdb_id}, res={_var_var_4}')
                return None
            return _var_var_4
        except requests.exceptions.RequestException as _var_var_5:
            logger.error(f'get_movie_details_by_tmdb_id network error, tmdb_id={tmdb_id}, {str(_var_var_5)}')
            return None

    def get_tv_details_by_tmdb_id(self, tmdb_id):
        if not tmdb_id:
            return None
        try:
            _var_var_4 = self._request_with_retry(self.tv.details, 'get_tv_details_by_tmdb_id', tmdb_id)
            if _var_var_4.get('error'):
                logger.error(f'get_tv_details_by_tmdb_id failed, tmdb_id={tmdb_id}, res={_var_var_4}')
                return None
            return _var_var_4
        except requests.exceptions.RequestException as _var_var_5:
            logger.error(f'get_tv_details_by_tmdb_id network error, tmdb_id={tmdb_id}, {str(_var_var_5)}')
            return None
        except Exception as _var_var_6:
            logger.error(f'get_tv_details_by_tmdb_id error, tmdb_id={tmdb_id}, {str(_var_var_6)}')
            return None


