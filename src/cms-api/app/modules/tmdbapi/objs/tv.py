import warnings
from app.modules.tmdbapi.tmdb import TMDb
from app.modules.tmdbapi.objs.search import Search
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

class TV(TMDb):
    __module__ = __name__
    __qualname__ = 'TV'

