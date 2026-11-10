# File: mexception.py (Cleaned & Decompiled)
import re
from app.log import logger

class MExcUtils:
    @staticmethod
    def log(exception: Exception):
        """
        判断是否为连接超时异常
        :return: 如果是连接超时异常返回请求地址,否则返回None
        """
        _var_var_0 = str(exception)
        print(_var_var_0)
        if 'Connection timed out' in _var_var_0 or 'Max retries exceeded' in _var_var_0:
            _var_var_1 = re.search("host='([^']+)'", _var_var_0)
            if _var_var_1:
                _var_var_2 = _var_var_1.group(1)
                logger.error(f'请求域名: {_var_var_2} 失败，请检查网络是否正常，或者核心配置里的代理配置是否可用')
                return None
            else:
                logger.exception(exception)
        else:
            logger.exception(exception)