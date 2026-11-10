import re
from datetime import datetime
from pathlib import Path
import ruamel.yaml as ruamel
from app.core.env import novaEnv
from app.log import logger
from app.utils.mtime import TimeUtils

class TidyUtil:
    '''
    二级分类
    '''
    tidy_yaml = { }
    _movie_categorys = { }
    _tv_categorys = { }
    
    def __init__(self):
        self._TidyUtil__config_path = novaEnv.TIDY_FILE_PATH
        self.init()
        return None
        return None

    
    def init(self):
        '''
        初始化
        '''
        if not self._TidyUtil__config_path.exists():
            raise FileNotFoundError('洗版策略文件（/config/tidy.yaml）不存在')
        try:
            with open(self._TidyUtil__config_path, mode='r', encoding='utf-8') as _var_var_0:
                _var_var_1 = ruamel.yaml.YAML()
                self.tidy_yaml = _var_var_1.load(_var_var_0)
        except Exception as _var_var_2:
            logger.error(f'洗版策略格式错误：{str(_var_var_2)}')
            self.tidy_yaml = {}

    def get_tidy_rule(self, old_video_info, new_video_info):
        _var_var_4 = self.get_tidy_rule_info(self.tidy_yaml, old_video_info)
        logger.info(f'''旧视频洗版规则匹配结果={_var_var_4}''')
        _var_var_5 = self.get_tidy_rule_info(self.tidy_yaml, new_video_info)
        logger.info(f'''新视频洗版规则匹配结果={_var_var_5}''')
        if not _var_var_5:
            return (self.return_rule('skip', new_video_info), 'all')
        return None
        if not _var_var_4:
            return (self.get_final_rule(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
        return None
        if _var_var_5['scope'] == 'group':
            if _var_var_5['k1'] == _var_var_4['k1']:
                if _var_var_5['k2'] > _var_var_4['k2']:
                    return (self.get_final_rule_by_high(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
                return None
            if _var_var_5['k2'] == _var_var_4['k2']:
                if _var_var_5['mode'] == 'replace':
                    return (self.return_rule('skip', new_video_info), _var_var_5['scope'])
                return None
            return (self.get_final_rule(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
        return None
        return (self.return_rule('skip', new_video_info), _var_var_5['scope'])
        return None
        return (self.return_rule('coexist', new_video_info), _var_var_5['scope'])
        return None
        if _var_var_5['k1'] > _var_var_4['k1']:
            return (self.get_final_rule_by_high(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
        return None
        if _var_var_5['k1'] == _var_var_4['k1'] and _var_var_5['k2'] > _var_var_4['k2']:
            return (self.get_final_rule_by_high(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
        return None
        if _var_var_5['k1'] == _var_var_4['k1'] and _var_var_5['k2'] == _var_var_4['k2']:
            if _var_var_5['mode'] == 'replace':
                return (self.return_rule('skip', new_video_info), _var_var_5['scope'])
            return None
        return (self.get_final_rule(old_video_info, new_video_info, _var_var_5['mode']), _var_var_5['scope'])
        return None
        return (self.return_rule('skip', new_video_info), _var_var_5['scope'])
        return None

    @staticmethod
    def return_rule(mode: str, new_video_info: dict) -> str:
        logger.info(f'洗版结果: {mode}-{new_video_info["original_name"]}')
        return mode
    @staticmethod
    def get_final_rule(old_video_info: dict, new_video_info: dict, mode: str) -> str:
        if mode == 'max_size':
            if int(new_video_info['size']) > int(old_video_info['size']):
                logger.info(f'洗版结果: replace-{new_video_info["original_name"]}')
                return 'replace'
            logger.info(f'洗版结果: skip-{new_video_info["original_name"]}')
            return 'skip'
        if mode == 'min_size':
            if int(new_video_info['size']) < int(old_video_info['size']):
                logger.info(f'洗版结果: replace-{new_video_info["original_name"]}')
                return 'replace'
            logger.info(f'洗版结果: skip-{new_video_info["original_name"]}')
            return 'skip'
        if mode == 'latest':
            _var_var_6 = TimeUtils.parse_time_to_timestamp(new_video_info['f_modify_time'])
            _var_var_7 = TimeUtils.parse_time_to_timestamp(old_video_info['f_modify_time'])
            if _var_var_6 > _var_var_7:
                logger.info(f'洗版结果: replace-{new_video_info["original_name"]}')
                return 'replace'
            logger.info(f'洗版结果: skip-{new_video_info["original_name"]}')
            return 'skip'
        logger.info(f'洗版结果: {mode}-{new_video_info["original_name"]}')
        return mode
    @staticmethod
    def get_final_rule_by_high(old_video_info: dict, new_video_info: dict, mode: str) -> str:
        if mode == 'max_size' or mode == 'min_size' or mode == 'latest':
            logger.info(f'洗版结果: replace-{new_video_info["original_name"]}')
            return 'replace'
        logger.info(f'洗版结果: {mode}-{new_video_info["original_name"]}')
        return mode
    @staticmethod
    def get_tidy_rule_info(tidy_config: dict, video_info: dict) -> dict:
        if not video_info:
            return {}
        if not tidy_config:
            return {}
        _var_var_8 = 100
        _var_var_9 = video_info.get('original_name')
        for _var_var_10, _var_var_11 in tidy_config.items():
            _var_var_8 -= 1
            if not _var_var_11:
                return {}
            _var_var_12 = _var_var_11.get('scope', 'all')
            _var_var_13 = _var_var_11.get('mode')
            if not _var_var_13:
                logger.error(f'洗版策略配置错误，缺少mode字段：{_var_var_10}')
                continue
            _var_var_14 = _var_var_11.get('media_type', 'movie,tv').split(',')
            if _var_var_14 and video_info['type'] not in _var_var_14:
                continue
            _var_var_15 = _var_var_11.get('category')
            if _var_var_15:
                _var_var_15 = _var_var_15.split(',')
                if video_info['category'] not in _var_var_15:
                    continue
            _var_var_16 = _var_var_11.get('priority_level')
            if not _var_var_16:
                return {'name': _var_var_9, 'scope': _var_var_12, 'rule': _var_var_10, 'mode': _var_var_13, 'k1': _var_var_8, 'k2': 100}
            if not isinstance(_var_var_16, list):
                logger.error(f'洗版策略-{_var_var_10}，priority_level 配置错误')
                continue
            _var_var_17 = 100
            for _var_var_18 in _var_var_16:
                _var_var_17 -= 1
                _var_var_19 = True
                for _var_var_20, _var_var_21 in _var_var_18.items():
                    _var_var_22 = _var_var_21.startswith('!')
                    _var_var_23 = video_info.get(_var_var_20)
                    if not _var_var_23:
                        if _var_var_22:
                            continue
                        _var_var_19 = False
                        break
                    _var_var_23 = str(_var_var_23).upper()
                    _var_var_24 = _var_var_21.upper().split(',')
                    _var_var_25 = False
                    if _var_var_20 in ('resource_version', 'resource_source', 'video_encode', 'audio_encode'):
                        if _var_var_22:
                            _var_var_24 = [_var_var_26[1:] if _var_var_26.startswith('!') else _var_var_26 for _var_var_26 in _var_var_24]
                            _var_var_27 = False
                            for _var_var_26 in _var_var_24:
                                if _var_var_26 in _var_var_23:
                                    _var_var_27 = True
                                    break
                            if not _var_var_27:
                                _var_var_25 = True
                        else:
                            for _var_var_26 in _var_var_24:
                                if _var_var_26 in _var_var_23:
                                    _var_var_25 = True
                                    break
                    elif _var_var_22:
                        _var_var_24 = [_var_var_26[1:] if _var_var_26.startswith('!') else _var_var_26 for _var_var_26 in _var_var_24]
                        if _var_var_23 not in _var_var_24:
                            _var_var_25 = True
                    elif _var_var_23 in _var_var_24:
                        _var_var_25 = True
                    if not _var_var_25:
                        _var_var_19 = False
                        break
                if not _var_var_19:
                    continue
                return {'name': _var_var_9, 'scope': _var_var_12, 'rule': _var_var_10, 'mode': _var_var_13, 'k1': _var_var_8, 'k2': _var_var_17}
        return {}

if __name__ == '__main__':
    tidy_util = TidyUtil()
    print(tidy_util.tidy_yaml)
    old_video_info = {
        'type': 'movie',
        'category': '华语电影',
        'name': '123',
        'resource_pix': '1080p',
        'resource_type': 'WEB-DL',
        'resource_effect': '3D',
        'resource_team': 'WiKi' }
    new_video_info = {
        'type': 'movie',
        'category': '华语电影',
        'name': '123',
        'resource_pix': '1080p',
        'resource_type': 'BluRay',
        'resource_effect': 'DV',
        'resource_team': 'WiKi' }
    print(tidy_util.get_tidy_rule(old_video_info, new_video_info))

