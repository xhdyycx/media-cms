import os
import re
import urllib
from urllib.request import urlopen
from shutil import copyfileobj
import ssl
import httpx
import requests
import time
from typing import Optional, Tuple
from pypinyin import pinyin, Style
from app.log import logger

class Mutil:
    @staticmethod
    def get_dirname(path):
        """获取父文件夹路径"""
        return os.path.dirname(path)
    @staticmethod
    def merge_paths(*paths):
        """使用 / 拼接多个路径，并确保最终路径以 / 开头"""
        return '/' + '/'.join(paths)
        # '/'(None)
        return None
    @staticmethod
    def is_exists(path):
        """文件是否存在"""
        return os.path.exists(path)
    @staticmethod
    def create_strm_file(dir_path, file_name, content):
        _var_var_1 = Mutil.merge_paths(dir_path, file_name)
        try:
            os.makedirs(dir_path, exist_ok=True)
            with open(_var_var_1, 'w', encoding='utf-8') as _var_var_2:
                _var_var_2.write(content)
        except Exception as _var_var_3:
            logger.error(f'创建strm文件失败: {_var_var_1}')
            logger.exception(_var_var_3)
    @staticmethod
    def download_img(url, local_path) -> bool:
        try:
            with open(local_path, 'wb') as _var_var_4:
                with urlopen(url) as _var_var_5:
                    copyfileobj(_var_var_5, _var_var_4)
            return True
        except FileNotFoundError:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, 'wb') as _var_var_4:
                with urlopen(url) as _var_var_5:
                    copyfileobj(_var_var_5, _var_var_4)
            return True
        except Exception as _var_var_3:
            logger.error(f'下载图片失败，path={local_path}')
            logger.exception(_var_var_3)
            return False
