import warnings
from app.modules.tmdbapi.tmdb import TMDb
from app.modules.tmdbapi.objs.find import Find
from app.modules.tmdbapi.objs.search import Search

class Movie(TMDb):
    __module__ = __name__
    __qualname__ = 'Movie'


