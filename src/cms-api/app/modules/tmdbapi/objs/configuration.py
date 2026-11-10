import warnings
from app.modules.tmdbapi.tmdb import TMDb

class Configuration(TMDb):
    _urls = {
        'api_configuration': '/configuration',
        'countries': '/configuration/countries',
        'jobs': '/configuration/jobs',
        'languages': '/configuration/languages',
        'primary_translations': '/configuration/primary_translations',
        'timezones': '/configuration/timezones' }
    
    def info(self):
        warnings.warn('info method is deprecated use tmdbapi.Configuration().api_configuration()', DeprecationWarning)
        return self.api_configuration()
        return None

    
    def api_configuration(self):
        '''
        Get the system wide configuration info.
        '''
        return self._request_obj(self._urls['api_configuration'])
        return None

    
    def countries(self):
        '''
        Get the list of countries (ISO 3166-1 tags) used throughout TMDb.
        '''
        return self._request_obj(self._urls['countries'])
        return None

    
    def jobs(self):
        '''
        Get a list of the jobs and departments we use on TMDb.
        '''
        return self._request_obj(self._urls['jobs'])
        return None

    
    def languages(self):
        '''
        Get the list of languages (ISO 639-1 tags) used throughout TMDb.
        '''
        return self._request_obj(self._urls['languages'])
        return None

    
    def primary_translations(self):
        '''
        Get a list of the officially supported translations on TMDb.
        '''
        return self._request_obj(self._urls['primary_translations'])
        return None

    
    def timezones(self):
        '''
        Get the list of timezones used throughout TMDb.
        '''
        return self._request_obj(self._urls['timezones'])
        return None



