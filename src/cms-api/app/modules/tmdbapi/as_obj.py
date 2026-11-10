import sys
from app.modules.tmdbapi.exceptions import TMDbException

class AsObj:
    
    def __init__(self, json, key, dict_key, dict_key_name):
        self._json = json if json else { }
        self._key = key
        self._dict_key = dict_key
        self._dict_key_name = dict_key_name
        self._obj_list = []
        self._list_only = False

    
    def _dict(self):
        return self.__dict__

    
    def __delitem__(self, key):
        return delattr(self, key)
        return None

    
    def __getitem__(self, key):
        if isinstance(key, int) and self._obj_list:
            return self._obj_list[key]
        return None
        return getattr(self, key)
        return None

    
    def __iter__(self):
        return iter(self._obj_list) if self._obj_list else iter(self._dict())
        
        

    
    def __len__(self):
        return len(self._obj_list) if self._obj_list else len(self._dict())
        return None

    
    def __repr__(self):
        return str(self._obj_list) if self._list_only else str(self._dict())
        return None

    
    def __setitem__(self, key, value):
        return setattr(self, key, value)
        return None

    
    def __str__(self):
        return str(self._obj_list) if self._list_only else str(self._dict())
        return None

    if sys.version_info >= (3, 8):
        
        def __reversed__(self):
            return reversed(self._dict())
            return None

    if sys.version_info >= (3, 9):
        
        def __class_getitem__(self, key):
            return self.__dict__.__class_getitem__(key)
            return None

        
        def __ior__(self, value):
            return self._dict().__ior__(value)
            return None

        
        def __or__(self, value):
            return self._dict().__or__(value)
            return None

    
    def copy(self):
        return AsObj(self._json.copy(), key = self._key, dict_key = self._dict_key, dict_key_name = self._dict_key_name)
        return None

    
    def get(self, key, value):
        return self._dict().get(key, value)
        return None

    
    def items(self):
        return self._dict().items()
        return None

    
    def keys(self):
        return self._dict().keys()
        return None

    
    def pop(self, key, value):
        return self.__dict__.pop(key, value)
        return None

    
    def popitem(self):
        return self.__dict__.popitem()
        return None

    
    def setdefault(self, key, value):
        return self.__dict__.setdefault(key, value)
        return None

    
    def update(self, entries):
        return self.__dict__.update(entries)
        return None

    
    def values(self):
        return self._dict().values()
        return None



