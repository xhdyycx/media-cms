from app.modules.tmdbapi.tmdb import TMDb

class Change(TMDb):
    _urls = {
        'movie': '/movie/changes',
        'tv': '/tv/changes',
        'person': '/person/changes' }
    
    def _change_list(self, change_type, start_date, end_date, page):
        _var_var_0 = 'page=%s' % page
        if start_date:
            _var_var_0 += '&start_date=%s' % start_date
        if end_date:
            _var_var_0 += '&end_date=%s' % end_date
        return self._request_obj(self._urls[change_type], params = _var_var_0, key = 'results')
        return None

    
    def movie_change_list(self, start_date, end_date, page):
        '''
        Get the changes for a movie. By default only the last 24 hours are returned.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        '''
        return self._change_list('movie', start_date = start_date, end_date = end_date, page = page)
        return None

    
    def tv_change_list(self, start_date, end_date, page):
        '''
        Get a list of all of the TV show ids that have been changed in the past 24 hours.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        '''
        return self._change_list('tv', start_date = start_date, end_date = end_date, page = page)
        return None

    
    def person_change_list(self, start_date, end_date, page):
        '''
        Get a list of all of the person ids that have been changed in the past 24 hours.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        '''
        return self._change_list('person', start_date = start_date, end_date = end_date, page = page)
        return None



