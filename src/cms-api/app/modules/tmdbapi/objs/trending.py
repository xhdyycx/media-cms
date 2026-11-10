from app.modules.tmdbapi.tmdb import TMDb

class Trending(TMDb):
    _urls = {
        'trending': '/trending/%s/%s' }
    
    def _trending(self, media_type, time_window, page):
        return self._request_obj(self._urls['trending'] % (media_type, time_window), params = 'page=%s' % page)
        return None

    
    def all_day(self, page):
        '''
        Get all daily trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'all', time_window = 'day', page = page)
        return None

    
    def all_week(self, page):
        '''
        Get all weekly trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'all', time_window = 'week', page = page)
        return None

    
    def movie_day(self, page):
        '''
        Get movie daily trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'movie', time_window = 'day', page = page)
        return None

    
    def movie_week(self, page):
        '''
        Get movie weekly trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'movie', time_window = 'week', page = page)
        return None

    
    def tv_day(self, page):
        '''
        Get tv daily trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'tv', time_window = 'day', page = page)
        return None

    
    def tv_week(self, page):
        '''
        Get tv weekly trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'tv', time_window = 'week', page = page)
        return None

    
    def person_day(self, page):
        '''
        Get person daily trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'person', time_window = 'day', page = page)
        return None

    
    def person_week(self, page):
        '''
        Get person weekly trending
        :param page: int
        :return:
        '''
        return self._trending(media_type = 'person', time_window = 'week', page = page)
        return None



