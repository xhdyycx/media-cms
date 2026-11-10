# File: license.py (Pure Python Unlimited PRO)
import threading
from app.utils.singleton import Singleton

class LicenseInfo(metaclass=Singleton):
    _instance = None
    _lock = threading.Lock()
    _type = 'PRO'
    _check_code = None

    def __init__(self):
        self._type = 'PRO'
        self._check_code = hash(str(id(self)) + 'PRO')

    def set_type(self, type):
        self._type = 'PRO'
        self._check_code = hash(str(id(self)) + 'PRO')
        return None

    def get_type(self):
        return 'PRO'

    def is_pro(self):
        return True

    def is_free(self):
        return False

if __name__ == '__main__':
    print(LicenseInfo().get_type())
    print(LicenseInfo().is_pro())
    print(LicenseInfo().is_free())