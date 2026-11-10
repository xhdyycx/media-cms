from app.modules.tmdbapi.tmdb import TMDb

class Network(TMDb):
    _urls = {
        'details': '/network/%s',
        'alternative_names': '/network/%s/alternative_names',
        'images': '/network/%s/images' }
    
    def details(self, network_id):
        '''
        Get a networks details by id.
        :param network_id: int
        :return:
        '''
        return self._request_obj(self._urls['details'] % network_id)
        return None

    
    def alternative_names(self, network_id):
        '''
        Get the alternative names of a network.
        :param network_id: int
        :return:
        '''
        return self._request_obj(self._urls['alternative_names'] % network_id, key = 'results')
        return None

    
    def images(self, network_id):
        '''
        Get the TV network logos by id.
        :param network_id: int
        :return:
        '''
        return self._request_obj(self._urls['images'] % network_id, key = 'logos')
        return None



