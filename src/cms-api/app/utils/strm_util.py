import time
import fnmatch
import os
from app.log import logger

class STRMUtils:
    @staticmethod
    def process_file(file_path, old_string, new_string):
        """直接读取处理单个文件的替换逻辑"""
        try:
            with open(file_path, 'r', encoding='utf-8') as _var_var_0:
                _var_var_1 = _var_var_0.read()
            if old_string in _var_var_1:
                _var_var_2 = _var_var_1.replace(old_string, new_string)
                with open(file_path, 'w', encoding='utf-8') as _var_var_0:
                    _var_var_0.write(_var_var_2)
                logger.info(f'已更新: {file_path}')
                return True
            return False
        except Exception as _var_var_3:
            logger.error(f'处理文件 {file_path} 时出错: {_var_var_3}')
            return False
    @staticmethod
    def find_strm_files(directory, recursive=False):
        """使用生成器高效地查找 .strm 文件"""
        if recursive:
            for _var_var_4, _var_var_5, _var_var_6 in os.walk(directory):
                for _var_var_7 in fnmatch.filter(_var_var_6, '*.strm'):
                    yield os.path.join(_var_var_4, _var_var_7)
        else:
            with os.scandir(directory) as _var_var_8:
                for _var_var_9 in _var_var_8:
                    if _var_var_9.is_file() and _var_var_9.name.endswith('.strm'):
                        yield _var_var_9.path
    @staticmethod
    def replace_in_strm_files(directory, old_string, new_string, recursive=False):
        """
        替换指定目录中所有 .strm 文件中的字符串 - 简化版

        参数:
            directory (str): 要处理的目录路径
            old_string (str): 要被替换的字符串
            new_string (str): 替换后的新字符串
            recursive (bool): 是否递归处理子目录，默认为否

        返回:
            int: 成功处理的文件数量
        """
        _var_var_10 = time.time()
        _var_var_11 = STRMUtils.find_strm_files(directory, recursive)
        _var_var_12 = 0
        for _var_var_13 in _var_var_11:
            if STRMUtils.process_file(_var_var_13, old_string, new_string):
                _var_var_12 += 1
        _var_var_14 = time.time()
        _var_var_15 = _var_var_14 - _var_var_10
        _var_var_16 = f'STRM字符串替换-共处理了 {_var_var_12} 个文件，耗时 {_var_var_15:.2f} 秒'
        logger.info(_var_var_16)
        return _var_var_16

if __name__ == '__main__':
    replaced_count = STRMUtils.replace_in_strm_files('/path/to/media', '127.0.0.1:9528', '127.0.0.9:9529', True)

