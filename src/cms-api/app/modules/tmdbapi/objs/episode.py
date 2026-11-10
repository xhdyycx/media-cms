from app.modules.tmdbapi.tmdb import TMDb

class Episode(TMDb):
    _urls = {
        'details': '/tv/%s/season/%s/episode/%s',
        'account_states': '/tv/%s/season/%s/episode/%s/account_states',
        'changes': '/tv/episode/%s/changes',
        'credits': '/tv/%s/season/%s/episode/%s/credits',
        'external_ids': '/tv/%s/season/%s/episode/%s/external_ids',
        'images': '/tv/%s/season/%s/episode/%s/images',
        'translations': '/tv/%s/season/%s/episode/%s/translations',
        'rate_tv_episode': '/tv/%s/season/%s/episode/%s/rating',
        'delete_rating': '/tv/%s/season/%s/episode/%s/rating',
        'videos': '/tv/%s/season/%s/episode/%s/videos' }
    
    def details(self, tv_id, season_num, episode_num, append_to_response):
        '''
        Get the TV episode details by id.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :param append_to_response: str
        :return:
        '''
        return self._request_obj(self._urls['details'] % (tv_id, season_num, episode_num), params = 'append_to_response=%s' % append_to_response)
        return None

    
    def account_states(self, tv_id, season_num, episode_num):
        '''
        Get your rating for a episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :return:
        '''
        return self._request_obj(self._urls['account_states'] % (tv_id, season_num, episode_num), params = 'session_id=%s' % self.session_id)
        return None

    
    def changes(self, episode_id, start_date, end_date, page):
        '''
        Get the changes for a TV episode. By default only the last 24 hours are returned.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param episode_id: int
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        '''
        _var_var_0 = 'page=%s' % page
        if start_date:
            _var_var_0 += '&start_date=%s' % start_date
        if end_date:
            _var_var_0 += '&end_date=%s' % end_date
        return self._request_obj(self._urls['changes'] % episode_id, params = _var_var_0, key = 'changes')
        return None

    
    def credits(self, tv_id, season_num, episode_num):
        '''
        Get the credits for TV season.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :return:
        '''
        return self._request_obj(self._urls['credits'] % (tv_id, season_num, episode_num))
        return None

    
    def external_ids(self, tv_id, season_num, episode_num):
        '''
        Get the external ids for a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :return:
        '''
        return self._request_obj(self._urls['external_ids'] % (tv_id, season_num, episode_num))
        return None

    
    def images(self, tv_id, season_num, episode_num, include_image_language):
        '''
        Get the images that belong to a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :param include_image_language: str
        :return:
        '''
        return self._request_obj(self._urls['images'] % (tv_id, season_num, episode_num), params = 'include_image_language=%s' % include_image_language if include_image_language else '', key = 'stills')
        return None

    
    def translations(self, tv_id, season_num, episode_num):
        '''
        Get the translation data for an episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :return:
        '''
        return self._request_obj(self._urls['translations'] % (tv_id, season_num, episode_num), key = 'translations')
        return None

    
    def rate_tv_episode(self, tv_id, season_num, episode_num, rating):
        '''
        Rate a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :param rating: float
        '''
        self._request_obj(self._urls['rate_tv_episode'] % (tv_id, season_num, episode_num), params = 'session_id=%s' % self.session_id, method = 'POST', json = {
            'value': rating })
        return None
        return None

    
    def delete_rating(self, tv_id, season_num, episode_num):
        '''
        Remove your rating for a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        '''
        self._request_obj(self._urls['delete_rating'] % (tv_id, season_num, episode_num), params = 'session_id=%s' % self.session_id, method = 'DELETE')
        return None
        return None

    
    def videos(self, tv_id, season_num, episode_num, include_video_language):
        '''
        Get the videos that have been added to a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :param include_video_language: str
        :return:
        '''
        _var_var_0 = ''
        if include_video_language:
            _var_var_0 += '&include_video_language=%s' % include_video_language
        return self._request_obj(self._urls['videos'] % (tv_id, season_num, episode_num), params = _var_var_0)
        return None



