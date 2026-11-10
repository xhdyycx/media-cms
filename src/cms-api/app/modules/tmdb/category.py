from pathlib import Path
import ruamel.yaml as ruamel
from app.core.env import novaEnv
from app.log import logger

class CategoryUtil:
    '''
    二级分类
    '''
    _categorys = { }
    _movie_categorys = { }
    _tv_categorys = { }
    
    def __init__(self):
        self._category_path = novaEnv.CATEGORY_FILE_PATH
        self.init()
        return None
        return None

    
    def init(self):
        '''
        初始化
        '''
        if not self._category_path.exists():
            raise FileNotFoundError('二级分类策略文件（/config/category.yaml）不存在')
        try:
            with open(self._category_path, mode='r', encoding='utf-8') as _var_var_0:
                _var_var_1 = ruamel.yaml.YAML()
                self._categorys = _var_var_1.load(_var_var_0)
            if self._categorys:
                self._movie_categorys = self._categorys.get('movie')
                self._tv_categorys = self._categorys.get('tv')
        except Exception as _var_var_2:
            logger.error(f'二级分类策略格式错误：{str(_var_var_2)}')
            self._categorys = {}


    def is_movie_category(self):
        """
        获取电影分类标志
        """
        if self._movie_categorys:
            return True
        return False
    @property
    def is_tv_category(self):
        """
        获取电视剧分类标志
        """
        if self._tv_categorys:
            return True
        return False
    @property
    def movie_categorys(self):
        """
        获取电影分类清单
        """
        if not self._movie_categorys:
            return []
        return self._movie_categorys.keys()
    @property
    def tv_categorys(self):
        """
        获取电视剧分类清单
        """
        if not self._tv_categorys:
            return []
        return self._tv_categorys.keys()
    
    def get_movie_category_cid(self, tmdb_info, key):
        '''
        判断电影的分类
        :param tmdb_info: 识别的TMDB中的信息
        :param key: 需要返回id类型
        :return: 二级分类的名称
        '''
        return self.get_category(self._movie_categorys, tmdb_info).get(key)
        return None

    
    def get_tv_category_cid(self, tmdb_info, key):
        '''
        判断电视剧的分类，包括动漫
        :param tmdb_info: 识别的TMDB中的信息
        :param key: 需要返回id类型
        :return: 二级分类的名称
        '''
        return self.get_category(self._tv_categorys, tmdb_info).get(key)
        return None

    
    def get_movie_category(self, tmdb_info):
        '''
        判断电影的分类
        :param tmdb_info: 识别的TMDB中的信息
        :return: 二级分类的名称
        '''
        return self.get_category(self._movie_categorys, tmdb_info).get('category')
        return None

    
    def get_tv_category(self, tmdb_info):
        '''
        判断电视剧的分类，包括动漫
        :param tmdb_info: 识别的TMDB中的信息
        :return: 二级分类的名称
        '''
        return self.get_category(self._tv_categorys, tmdb_info).get('category')
        return None

    @staticmethod
    def get_category(categorys: dict, tmdb_info: dict) -> dict:
        """
        根据 TMDB信息与分类配置文件进行比较，确定所属分类
        :param categorys: 分类配置字典，包含各个分类的匹配规则
        :param tmdb_info: TMDB信息字典，包含电影/电视剧的详细信息
        :return: 返回匹配的分类信息字典，包含cid和category名称，如果未匹配则返回空字典
        """
        if not tmdb_info:
            return {}
        if not categorys:
            return {}
        for _var_var_4, _var_var_5 in categorys.items():
            if not _var_var_5:
                return {}
            _var_var_6 = True
            _var_var_7 = None
            _var_var_8 = None
            for _var_var_9, _var_var_10 in _var_var_5.items():
                if _var_var_9 == 'cid':
                    _var_var_7 = _var_var_10
                    continue
                if _var_var_9 == 'cid123':
                    _var_var_8 = _var_var_10
                    continue
                if not _var_var_10:
                    continue
                if _var_var_9 == 'name_regex':
                    _var_var_11 = tmdb_info.get('name', '')
                    if not _var_var_11:
                        _var_var_6 = False
                        break
                    import re as _var_var_12
                    if not _var_var_12.search(_var_var_10, _var_var_11, _var_var_12.IGNORECASE):
                        _var_var_6 = False
                        break
                    continue
                _var_var_13 = tmdb_info.get(_var_var_9)
                if not _var_var_13:
                    _var_var_6 = False
                    break
                if _var_var_9 == 'year':
                    if _var_var_10.find('-') != -1:
                        _var_var_15 = [int(_var_var_14) for _var_var_14 in _var_var_10.split('-') if _var_var_14]
                        _var_var_16 = _var_var_15[0]
                        _var_var_17 = _var_var_15[1]
                        if _var_var_16 <= int(_var_var_13) <= _var_var_17:
                            continue
                        _var_var_6 = False
                        break
                    _var_var_15 = [str(_var_var_14).upper() for _var_var_14 in _var_var_10.split(',') if _var_var_14]
                    if _var_var_13 not in _var_var_15:
                        _var_var_6 = False
                        break
                    continue
                if _var_var_9 == 'production_countries':
                    _var_var_18 = [str(_var_var_14.get('iso_3166_1')).upper() for _var_var_14 in _var_var_13]
                elif isinstance(_var_var_13, list):
                    _var_var_18 = [str(_var_var_14).upper() for _var_var_14 in _var_var_13]
                else:
                    _var_var_18 = [str(_var_var_13).upper()]
                if _var_var_10.find(',') != -1:
                    _var_var_15 = [str(_var_var_14).upper() for _var_var_14 in _var_var_10.split(',') if _var_var_14]
                else:
                    _var_var_15 = [str(_var_var_10).upper()]
                if set(_var_var_15).intersection(set(_var_var_18)):
                    continue
                _var_var_6 = False
                break
            if not _var_var_6:
                continue
            return {'cid': _var_var_7, 'cid123': _var_var_8, 'category': _var_var_4}
        return {}


