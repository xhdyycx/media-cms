from app.modules.tmdbapi.tmdb import TMDb

class Provider(TMDb):
    _urls = {
        'regions': '/watch/providers/regions',
        'movie': '/watch/providers/movie',
        'tv': '/watch/providers/tv' }
    
    def available_regions(self):
        '''
        Returns a list of all of the countries we have watch provider (OTT/streaming) data for.
        :return:
        '''
        return self._request_obj(self._urls['regions'], key = 'results')
        return None

    
    def movie_providers(self, region):
        '''
        Returns a list of the watch provider (OTT/streaming) data we have available for movies.
        :return:
        '''
        return self._request_obj(self._urls['movie'], params = 'watch_region=%s' % region if region else '', key = 'results')
        return None

    
    def tv_providers(self, region):
        '''
        Returns a list of the watch provider (OTT/streaming) data we have available for TV series.
        :return:
        '''
        return self._request_obj(self._urls['tv'], params = 'watch_region=%s' % region if region else '', key = 'results')
        return None



