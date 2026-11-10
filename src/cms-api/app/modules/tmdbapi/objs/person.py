import warnings
from app.modules.tmdbapi.tmdb import TMDb
from app.modules.tmdbapi.objs.search import Search

class Person(TMDb):
    _urls = {
        'details': '/person/%s',
        'changes': '/person/%s/changes',
        'movie_credits': '/person/%s/movie_credits',
        'tv_credits': '/person/%s/tv_credits',
        'combined_credits': '/person/%s/combined_credits',
        'external_ids': '/person/%s/external_ids',
        'images': '/person/%s/images',
        'tagged_images': '/person/%s/tagged_images',
        'translations': '/person/%s/translations',
        'latest': '/person/latest',
        'popular': '/person/popular',
        'search_people': '/search/person' }
    
    def details(self, person_id, append_to_response):
        '''
        Get the primary person details by id.
        :param append_to_response: str
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['details'] % person_id, params = 'append_to_response=%s' % append_to_response)
        return None

    
    def changes(self, person_id, start_date, end_date, page):
        '''
        Get the changes for a person. By default only the last 24 hours are returned.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param person_id: int
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
        return self._request_obj(self._urls['changes'] % person_id, params = _var_var_0, key = 'changes')
        return None

    
    def movie_credits(self, person_id):
        '''
        Get the movie credits for a person.
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['movie_credits'] % person_id)
        return None

    
    def tv_credits(self, person_id):
        '''
        Get the TV show credits for a person.
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['tv_credits'] % person_id)
        return None

    
    def combined_credits(self, person_id):
        '''
        Get the movie and TV credits together in a single response.
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['combined_credits'] % person_id)
        return None

    
    def external_ids(self, person_id):
        '''
        Get the external ids for a person. We currently support the following external sources.
        IMDB ID, Facebook, Freebase MID, Freebase ID, Instagram, TVRage ID, and Twitter
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['external_ids'] % person_id)
        return None

    
    def images(self, person_id):
        '''
        Get the images for a person.
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['images'] % person_id, key = 'profiles')
        return None

    
    def tagged_images(self, person_id, page):
        '''
        Get the images that this person has been tagged in.
        :param person_id: int
        :param page: int
        :return:
        '''
        return self._request_obj(self._urls['tagged_images'] % person_id, params = 'page=%s' % page, key = 'results')
        return None

    
    def translations(self, person_id):
        '''
        Get a list of translations that have been created for a person.
        :param person_id: int
        :return:
        '''
        return self._request_obj(self._urls['translations'] % person_id, key = 'translations')
        return None

    
    def latest(self):
        '''
        Get the most newly created person. This is a live response and will continuously change.
        :return:
        '''
        return self._request_obj(self._urls['latest'])
        return None

    
    def popular(self, page):
        '''
        Get the list of popular people on TMDb. This list updates daily.
        :param page: int
        :return:
        '''
        return self._request_obj(self._urls['popular'], params = 'page=%s' % page, key = 'results')
        return None

    
    def search(self, term, page):
        '''
        Search for people.
        :param term: string
        :param page: int
        :return:
        '''
        warnings.warn('search method is deprecated use tmdbapi.Search().people(params)', DeprecationWarning)
        return Search().people(term, page = page)
        return None



