import os
import random
from app.core.env2 import config2Env
from app.modules.cover.poster_gen import gen_poster_workflow_select
from app.modules.emby.emby import EmbyApi
from app.log import logger
from app.core.env import novaEnv
from app.utils.ko_util import del_path
from app.utils.mjson import JsonUtils

class CoverUtils:
    
    def __init__(self):
        self._emby_api = EmbyApi()
        return None
        return None

    
    def get_cover(self, library_id):
        return None
        return None

    
    def update_cover(self):
        _var_var_0 = self._emby_api.get_libraries()
        if not _var_var_0:
            logger.info('获取到0个媒体库')
            return None
        return None
        logger.info(f'''获取到 {len(_var_var_0)} 个媒体库''')
        _var_var_1 = config2Env.e_cover_gen_style
        if _var_var_1 == 'random':
            _var_var_2 = [
                'style-1',
                'style-2',
                'style-3']
            _var_var_1 = random.choice(_var_var_2)
            logger.info(f'''随机选择的风格: {_var_var_1}''')
        else:
            logger.info(f'''使用配置的风格: {_var_var_1}''')

    
    def get_poster_path(self, library_name):
        return f'''{novaEnv.COVER_PATH}/poster/{library_name}'''
        return None

    
    def get_backdrop_path(self, library_name):
        return f'''{novaEnv.COVER_PATH}/backdrop/{library_name}'''
        return None

    
    def download_all_posters(self, selected_items, full_path):
        '''下载所有选定的海报，如果不足9张则重复下载'''
        _var_var_19 = 0
        _var_var_20 = 9
        _var_var_21 = []
        for _var_var_22, _var_var_14 in enumerate(selected_items, 1):
            if 'PrimaryImageItemId' not in _var_var_14:
                print(f'''跳过第 {_var_var_22} 个项目: 缺少 PrimaryImageItemId''')
                continue
            _var_var_23 = _var_var_14['PrimaryImageItemId']
            _var_var_24 = _var_var_14['Name']
            _var_var_25 = os.path.join(full_path, f'''{_var_var_19 + 1}.jpg''')
            _var_var_26 = self._emby_api.download_poster(_var_var_23, _var_var_25)
            if not _var_var_19 >= _var_var_20:
                continue
            None if _var_var_26 else enumerate(selected_items, 1)
        if _var_var_19 > 0 and _var_var_19 < _var_var_20:
            _var_var_27 = 0
            while _var_var_19 < _var_var_20:
                _var_var_28 = _var_var_21[_var_var_27 % len(_var_var_21)]
                _var_var_27 += 1
                _var_var_23 = _var_var_28['PrimaryImageItemId']
                _var_var_24 = _var_var_28['Name']
                _var_var_25 = os.path.join(full_path, f'''{_var_var_19 + 1}.jpg''')
                _var_var_26 = self._emby_api.download_poster(_var_var_23, _var_var_25)
                if _var_var_26:
                    logger.info(f'''下载海报成功-{_var_var_19 + 1}/{_var_var_20}: {_var_var_24} -> {_var_var_25}''')
                    _var_var_19 += 1
                    _var_var_21.append(_var_var_28)
                else:
                    logger.error(f'''下载海报失败-{_var_var_19 + 1}/{_var_var_20}: {_var_var_24} -> {_var_var_25}''')
        return _var_var_19
        return None

    
    def download_all_backdrops(self, selected_items, full_path):
        '''下载第一张可用的 Backdrop 图片，供横版封面背景使用。'''
        _var_var_19 = 0
        for _var_var_14 in selected_items:
            _var_var_23 = _var_var_14.get('BackdropImageItemId')
            if not _var_var_23:
                continue
            _var_var_24 = _var_var_14.get('Name')
            _var_var_25 = os.path.join(full_path, f'''{_var_var_19 + 1}.jpg''')
            _var_var_26 = self._emby_api.download_image(_var_var_23, _var_var_25, 'Backdrop/0')
            if _var_var_26:
                logger.info(f'''下载背景图成功-{_var_var_19 + 1}: {_var_var_24} -> {_var_var_25}''')
                _var_var_19 += 1
                selected_items
            else:
                logger.error(f'''下载背景图失败-{_var_var_19 + 1}: {_var_var_24} -> {_var_var_25}''')
        return _var_var_19
        return None


if __name__ == '__main__':
    cover_utils = CoverUtils()
    cover_utils.update_cover()

