# File: m123old.py (Cleaned & Decompiled)
import time
from datetime import datetime
from p123client import P123Client
from app.core.env import novaEnv
from app.log import logger
from app.utils.singleton import ExpiredSingleton

class M123Old(metaclass=ExpiredSingleton):
    client = None

    def __init__(self):
        self._username = novaEnv.P123_USERNAME
        self._password = novaEnv.P123_PASSWORD
        self.interval = 1
        if not self.client:
            logger.info('初始化P123Client')
            self.client = P123Client(self._username, self._password)

    def sync_file(self, page, parentFileId):
        _var_var_0 = {
            'Page': page,
            'parentFileId': parentFileId,
            'orderBy': 'update_at',
            'orderDirection': 'desc'
        }
        if self.interval > 0:
            time.sleep(self.interval)
        print(f'Syncing file...{parentFileId}')
        _var_var_1 = self.client.fs_list_new(_var_var_0)
        for _var_var_2 in _var_var_1['data']['InfoList']:
            _var_var_3 = _var_var_2['Type'] == 1
            _var_var_4 = _var_var_2['FileId']
            if not _var_var_3:
                _var_var_5 = _var_var_2['S3KeyFlag']
                _var_var_6 = _var_var_2['Size']
                _var_var_7 = _var_var_2['Etag']
                _var_var_8 = _var_var_2['FileName']
                if not _var_var_8.endswith('.mkv'):
                    continue
                _var_var_9 = f'{_var_var_8}|{_var_var_6}|{_var_var_7}?{_var_var_5}'
                print(_var_var_9)
                continue
            self.sync_file(1, _var_var_4)
        if _var_var_1['data']['Next'] == '-1':
            return None
        self.sync_file(page + 1, parentFileId)

if __name__ == '__main__':
    pass