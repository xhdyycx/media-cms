# File: m115_util.py (Cleaned & Decompiled)
from app.log import logger
from app.utils.mjson import JsonUtils

class M115Utils:
    @staticmethod
    def check_data(attr):
        if 'path' not in attr:
            logger.warning(f'跳过处理-缺失path字段={JsonUtils.to_str(attr)}')
            return False
        if 'ancestors' not in attr:
            logger.warning(f'跳过处理-缺失ancestors字段={JsonUtils.to_str(attr)}')
            return False
        if len(attr['ancestors']) <= 2:
            logger.warning(f'跳过处理-ancestors 列表长度异常-{JsonUtils.to_str(attr)}')
            return False
        return True

    @staticmethod
    def check_path(attr):
        if 'path' not in attr:
            logger.warning(f'跳过处理-缺失path字段-请确认此文件是否存在115={JsonUtils.to_str(attr)}')
            return False
        return True

    @staticmethod
    def check_path_v2(attr, cid):
        if 'path' not in attr:
            logger.warning(f'跳过处理-请确认此文件是否还在{cid}中，如果不在忽略此日志即可={JsonUtils.to_str(attr)}')
            return False
        return True