from app.modules.tmdbapi.tmdb import TMDb
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

class Search(TMDb):
    _urls = {
        'companies': '/search/company',
        'collections': '/search/collection',
        'keywords': '/search/keyword',
        'movies': '/search/movie',
        'multi': '/search/multi',
        'people': '/search/person',
        'tv_shows': '/search/tv' }
    
    def companies(self, term, page):
        '''
        Search for companies.
        :param term: str
        :param page: int
        :return:
        '''
        return self._request_obj(self._urls['companies'], params = f'''query={quote(term)!s}&page={page!s}''', key = 'results')
        return None

    
    def collections(self, term, page):
        '''
        Search for collections.
        :param term: str
        :param page: int
        :return:
        '''
        return self._request_obj(self._urls['collections'], params = f'''query={quote(term)!s}&page={page!s}''', key = 'results')
        return None

    
    def keywords(self, term, page):
        '''
        Search for keywords.
        :param term: str
        :param page: int
        :return:
        '''
        return self._request_obj(self._urls['keywords'], params = f'''query={quote(term)!s}&page={page!s}''', key = 'results')
        return None

    
    def movies(self, term, adult, region, year, release_year, page):
        '''
        Search for movies.
        :param term: str
        :param adult: bool
        :param region: str
        :param year: int
        :param release_year: int
        :param page: int
        :return:
        '''
        _var_var_0 = f'''query={quote(term)!s}&page={page!s}'''
        if adult is not None:
            _var_var_0 += ('&include_adult=%s' % 'true') if adult else 'false'
        if region is not None:
            _var_var_0 += '&region=%s' % quote(region)
        if year is not None:
            _var_var_0 += '&year=%s' % year
        if release_year is not None:
            _var_var_0 += '&primary_release_year=%s' % release_year
        return self._request_obj(self._urls['movies'], params=_var_var_0, key='results')
    def multi(self, term, adult, region, page):
        '''
        Search multiple models in a single request.
        Multi search currently supports searching for movies, tv shows and people in a single request.
        :param term: str
        :param adult: bool
        :param region: str
        :param page: int
        :return:
        '''
        _var_var_0 = f'''query={quote(term)!s}&page={page!s}'''
        if adult is not None:
            _var_var_0 += ('&include_adult=%s' % 'true') if adult else 'false'
        if region is not None:
            _var_var_0 += '&region=%s' % quote(region)
        return self._request_obj(self._urls['multi'], params=_var_var_0, key='results')
    def people(self, term, adult, region, page):
        '''
        Search for people.
        :param term: str
        :param adult: bool
        :param region: str
        :param page: int
        :return:
        '''
        _var_var_0 = f'''query={quote(term)!s}&page={page!s}'''
        if adult is not None:
            _var_var_0 += ('&include_adult=%s' % 'true') if adult else 'false'
        if region is not None:
            _var_var_0 += '&region=%s' % quote(region)
        return self._request_obj(self._urls['people'], params=_var_var_0, key='results')
    def tv_shows(self, term, adult, first_air_date_year, year, page):
        '''
        Search for a TV show.
        :param term: str
        :param adult: bool
        :param first_air_date_year: int
        :param year: int
        :param page: int
        :return:
        '''
        _var_var_0 = f'''query={quote(term)!s}&page={page!s}'''
        if adult is not None:
            _var_var_0 += ('&include_adult=%s' % 'true') if adult else 'false'
        if first_air_date_year is not None:
            _var_var_0 += '&first_air_date_year=%s' % first_air_date_year
        if year is not None:
            _var_var_0 += '&year=%s' % year
        return self._request_obj(self._urls['tv_shows'], params=_var_var_0, key='results')

