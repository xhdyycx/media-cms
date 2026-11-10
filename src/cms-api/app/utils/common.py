import base64
import time
from hashlib import md5
from typing import Any
from Crypto import Random
from Crypto.Cipher import AES

def retry(ExceptionToCheck=Exception, tries=3, delay=1, backoff=2, logger=None):
    '''标准带默认参数的重试装饰器'''
    import time
    from functools import wraps
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    if logger:
                        logger.warning(f"{f.__name__} 运行异常: {e}, {mdelay}秒后重试...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry
    return deco_retry

def _old_retry_unused(ExceptionToCheck, tries, delay, backoff, logger):
    '''
    :param ExceptionToCheck: 需要捕获的异常
    :param tries: 重试次数
    :param delay: 延迟时间
    :param backoff: 延迟倍数
    :param logger: 日志对象
    '''
    
    def _var_var_0(f):
        
        def _var_var_1(*args, **kwargs):
            _var_var_3 = delay
            _var_var_2 = tries

        return _var_var_1
        return None



def bytes_to_key(data, salt, output):
    pass


def encrypt(message, passphrase):
    '''
    CryptoJS 加密原文
    
    This is a modified copy of https://stackoverflow.com/questions/36762098/how-to-decrypt-password-from-javascript-cryptojs-aes-encryptpassword-passphras
    '''
    _var_var_8 = Random.new().read(8)
    _var_var_9 = bytes_to_key(passphrase, _var_var_8, 48)
    _var_var_6 = _var_var_9[:32]
    _var_var_10 = _var_var_9[32:]
    _var_var_11 = AES.new(_var_var_6, AES.MODE_CBC, _var_var_10)
    _var_var_12 = 16 - len(message) % 16
    _var_var_13 = message + (chr(_var_var_12) * _var_var_12).encode()


def decrypt(encrypted, passphrase):
    '''
    CryptoJS 解密密文
    
    来源同encrypt
    '''
    encrypted = base64.b64decode(encrypted)


