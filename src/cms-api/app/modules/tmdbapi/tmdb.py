import logging
import os
import time
import requests
# import requests.exceptions as requests
from cachetools import TTLCache
from app.modules.tmdbapi.as_obj import AsObj
from app.modules.tmdbapi.exceptions import TMDbException
from functools import lru_cache, wraps
logger = logging.getLogger(__name__)
cache = TTLCache(maxsize = 500, ttl = 3600)

def cached_with_ttl(func):
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        res = func(*args, **kwargs)
        cache[key] = res
        return res


class TMDb(object):
    _session = None
    TMDB_API_KEY = 'TMDB_API_KEY'
    TMDB_LANGUAGE = 'TMDB_LANGUAGE'
    TMDB_SESSION_ID = 'TMDB_SESSION_ID'
    TMDB_WAIT_ON_RATE_LIMIT = 'TMDB_WAIT_ON_RATE_LIMIT'
    TMDB_DEBUG_ENABLED = 'TMDB_DEBUG_ENABLED'
    TMDB_CACHE_ENABLED = 'TMDB_CACHE_ENABLED'
    TMDB_PROXIES = 'TMDB_PROXIES'
    REQUEST_CACHE_MAXSIZE = 1024
    REQUEST_TIMEOUT = 10
    TMDB_API_DOMAIN = 'TMDB_API_DOMAIN'
    
    def __init__(self, obj_cached=True, session=None, language='en-US'):
        if self.__class__._session is None or session is not None:
            self.__class__._session = session if session is not None else requests.Session()
        self._remaining = 40
        self._reset = None
        self.obj_cached = obj_cached
        self.language = language
    @property
    def _base(self):
        return f"{os.environ.get(self.TMDB_API_DOMAIN, 'https://api.tmdb.org')}/3"
    @_base.setter
    def _base(self, domain):
        os.environ[self.TMDB_API_DOMAIN] = str(domain)

    @property
    def page(self):
        return os.environ.get('page')

    @property
    def total_results(self):
        return os.environ.get('total_results')

    @property
    def total_pages(self):
        return os.environ.get('total_pages')

    @property
    def api_key(self):
        return os.environ.get(self.TMDB_API_KEY)
    @api_key.setter
    def api_key(self, api_key):
        os.environ[self.TMDB_API_KEY] = str(api_key)

    @property
    def proxies(self):
        _var_var_3 = os.environ.get(self.TMDB_PROXIES)
        if _var_var_3 is not None:
            try:
                _var_var_3 = eval(_var_var_3)
            except Exception:
                pass
        return _var_var_3
    @proxies.setter
    def proxies(self, proxies):
        if proxies is not None:
            os.environ[self.TMDB_PROXIES] = str(proxies)

    @property
    def has_session(self):
        return True if os.environ.get(self.TMDB_SESSION_ID) else False

    @property
    def session_id(self):
        if not os.environ.get(self.TMDB_SESSION_ID):
            raise TMDbException('Must Authenticate to create a session run Authentication(username, password)')
        return os.environ.get(self.TMDB_SESSION_ID)
    @session_id.setter
    def session_id(self, session_id):
        os.environ[self.TMDB_SESSION_ID] = str(session_id)

    @property
    def wait_on_rate_limit(self):
        if os.environ.get(self.TMDB_WAIT_ON_RATE_LIMIT) == 'False':
            return False
        return True
    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, wait_on_rate_limit):
        os.environ[self.TMDB_WAIT_ON_RATE_LIMIT] = str(wait_on_rate_limit)

    @property
    def debug(self):
        if os.environ.get(self.TMDB_DEBUG_ENABLED) == 'True':
            return True
        return False
    @debug.setter
    def debug(self, debug):
        os.environ[self.TMDB_DEBUG_ENABLED] = str(debug)

    @property
    def cache(self):
        if os.environ.get(self.TMDB_CACHE_ENABLED) == 'False':
            return False
        return True
    @cache.setter
    def cache(self, cache):
        os.environ[self.TMDB_CACHE_ENABLED] = str(cache)
    @staticmethod
    @cached_with_ttl
    def cached_request(method, url, data, json, proxies):
        if proxies is not None:
            proxies = eval(proxies)
        return requests.request(
            method,
            url,
            data=data,
            json=json,
            proxies=proxies,
            timeout=TMDb.REQUEST_TIMEOUT,
        )
    
    def cache_clear(self):
        return self.cached_request.cache_clear()
        return None

    
    def _request_obj(self, action, params='', call_cached=True, method='GET', data=None, json=None, key=None):
        if self.api_key is None or self.api_key == '':
            raise TMDbException('请在 核心配置-TMDB配置-API密钥 中填写API密钥')
        _var_var_4 = f'{self._base!s}{action!s}?api_key={self.api_key!s}&{params!s}&language={self.language!s}'
        if self.cache and self.obj_cached and call_cached and method != 'POST':
            _var_var_5 = self.cached_request(method, _var_var_4, data, json, str(self.proxies))
        else:
            _var_var_5 = self.__class__._session.request(
                method,
                _var_var_4,
                data,
                json,
                self.proxies,
                timeout=self.REQUEST_TIMEOUT,
            )
        _var_var_6 = _var_var_5.headers
        if 'X-RateLimit-Remaining' in _var_var_6:
            self._remaining = int(_var_var_6['X-RateLimit-Remaining'])
        if 'X-RateLimit-Reset' in _var_var_6:
            self._reset = int(_var_var_6['X-RateLimit-Reset'])
        if self._remaining < 1:
            _var_var_7 = int(time.time())
            _var_var_8 = self._reset - _var_var_7
            if self.wait_on_rate_limit:
                logger.warning('Rate limit reached. Sleeping for: %d' % _var_var_8)
                time.sleep(abs(_var_var_8))
                return self._request_obj(action, params, call_cached, method, data, json, key)
            raise TMDbException('Rate limit reached. Try again in %d seconds.' % _var_var_8)
        json = _var_var_5.json()
        if 'page' in json:
            os.environ['page'] = str(json['page'])
        if 'total_results' in json:
            os.environ['total_results'] = str(json['total_results'])
        if 'total_pages' in json:
            os.environ['total_pages'] = str(json['total_pages'])
        if self.debug:
            logger.info(json)
            logger.info(self.cached_request.cache_info())
        if 'errors' in json:
            raise TMDbException(json['errors'])
        if 'success' in json and json['success'] is False:
            raise TMDbException(json['status_message'])
        return AsObj(json, key=key)
