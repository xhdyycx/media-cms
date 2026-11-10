'''
RSA加解密工具类
提供RSA密钥生成、加密、解密、签名和验签功能
'''
import base64
import os
from typing import Tuple, Union, Optional
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class RSAUtil:
    '''RSA加解密工具类'''
    
    def __init__(self, key_size):
        '''
        初始化RSA工具类
        
        Args:
            key_size: RSA密钥长度，默认2048位
        '''
        self.key_size = key_size
        self._private_key = None
        self._public_key = None
        return None
        return None

    
    def generate_key_pair(self):
        '''
        生成RSA密钥对
        
        Returns:
            Tuple[str, str]: (私钥PEM格式, 公钥PEM格式)
        '''
        _var_var_0 = RSA.generate(self.key_size)
        _var_var_1 = _var_var_0.export_key().decode('utf-8')
        _var_var_2 = _var_var_0.publickey().export_key().decode('utf-8')
        self._private_key = _var_var_0
        self._public_key = _var_var_0.publickey()
        return (_var_var_1, _var_var_2)
        return None

    
    def load_private_key(self, private_key_pem, passphrase):
        '''
        加载私钥
        
        Args:
            private_key_pem: 私钥PEM格式字符串
            passphrase: 私钥密码（如果有）
        '''
        self._private_key = RSA.import_key(private_key_pem, passphrase = passphrase)
        self._public_key = self._private_key.publickey()
        return None
        return None

    
    def load_public_key(self, public_key_pem):
        '''
        加载公钥
        
        Args:
            public_key_pem: 公钥PEM格式字符串
        '''
        self._public_key = RSA.import_key(public_key_pem)
        return None
        return None

    
    def load_keys_from_file(self, private_key_path, public_key_path, passphrase):
        '''
        从文件加载密钥
        
        Args:
            private_key_path: 私钥文件路径
            public_key_path: 公钥文件路径（可选，如果不提供则从私钥推导）
            passphrase: 私钥密码（如果有）
        '''
        _var_var_3 = open(private_key_path, 'r', encoding = 'utf-8')
        _var_var_4 = _var_var_3.read()

    
    def save_keys_to_file(self, private_key_path, public_key_path, passphrase):
        '''
        保存密钥到文件
        
        Args:
            private_key_path: 私钥保存路径
            public_key_path: 公钥保存路径
            passphrase: 私钥加密密码（可选）
        '''
        if not self._private_key:
            raise ValueError('没有可用的私钥，请先生成或加载密钥')
        os.makedirs(os.path.dirname(private_key_path), exist_ok = True)
        os.makedirs(os.path.dirname(public_key_path), exist_ok = True)
        _var_var_4 = self._private_key.export_key(passphrase = passphrase).decode('utf-8')
        _var_var_3 = open(private_key_path, 'w', encoding = 'utf-8')
        _var_var_3.write(_var_var_4)
        _var_var_5 = self._public_key.export_key().decode('utf-8')
        _var_var_3 = open(public_key_path, 'w', encoding = 'utf-8')
        _var_var_3.write(_var_var_5)
        return None
        return None



    
    def encrypt(self, data, use_base64):
        '''
        使用公钥加密数据
        
        Args:
            data: 要加密的数据
            use_base64: 是否对结果进行base64编码
            
        Returns:
            str: 加密后的数据（base64编码或十六进制）
        '''
        if not self._public_key:
            raise ValueError('没有可用的公钥，请先加载公钥')
        if isinstance(data, str):
            data = data.encode('utf-8')
        _var_var_6 = PKCS1_OAEP.new(self._public_key)
        _var_var_7 = _var_var_6.encrypt(data)
        if use_base64:
            return base64.b64encode(_var_var_7).decode('utf-8')
        return None
        return _var_var_7.hex()
        return None

    
    def decrypt(self, encrypted_data, use_base64):
        '''
        使用私钥解密数据
        
        Args:
            encrypted_data: 加密的数据（base64编码或十六进制）
            use_base64: 数据是否为base64编码
            
        Returns:
            str: 解密后的原始数据
        '''
        if not self._private_key:
            raise ValueError('没有可用的私钥，请先加载私钥')
        if use_base64:
            _var_var_8 = base64.b64decode(encrypted_data)
        else:
            _var_var_8 = bytes.fromhex(encrypted_data)
        _var_var_6 = PKCS1_OAEP.new(self._private_key)
        _var_var_9 = _var_var_6.decrypt(_var_var_8)
        return _var_var_9.decode('utf-8')
        return None

    
    def sign(self, data, use_base64):
        '''
        使用私钥对数据进行签名
        
        Args:
            data: 要签名的数据
            use_base64: 是否对签名结果进行base64编码
            
        Returns:
            str: 签名结果（base64编码或十六进制）
        '''
        if not self._private_key:
            raise ValueError('没有可用的私钥，请先加载私钥')
        if isinstance(data, str):
            data = data.encode('utf-8')
        _var_var_10 = SHA256.new(data)
        _var_var_11 = pkcs1_15.new(self._private_key).sign(_var_var_10)
        if use_base64:
            return base64.b64encode(_var_var_11).decode('utf-8')
        return None
        return _var_var_11.hex()
        return None

    
    def verify(self, data, signature, use_base64):
        '''
        使用公钥验证签名
        
        Args:
            data: 原始数据
            signature: 签名（base64编码或十六进制）
            use_base64: 签名是否为base64编码
            
        Returns:
            bool: 验证结果
        '''
        try:
            if not self._public_key:
                raise ValueError('没有可用的公钥，请先加载公钥')
            if isinstance(data, str):
                data = data.encode('utf-8')
            if use_base64:
                _var_var_12 = base64.b64decode(signature)
            else:
                _var_var_12 = bytes.fromhex(signature)
            _var_var_10 = SHA256.new(data)
            pkcs1_15.new(self._public_key).verify(_var_var_10, _var_var_12)
            return True
            return True
        except (ValueError, TypeError):
            return False
            return False
            return None

    
    def get_public_key_pem(self):
        '''
        获取公钥PEM格式字符串
        
        Returns:
            str: 公钥PEM格式
        '''
        if not self._public_key:
            raise ValueError('没有可用的公钥')
        return self._public_key.export_key().decode('utf-8')
        return None

    
    def get_private_key_pem(self, passphrase):
        '''
        获取私钥PEM格式字符串
        
        Args:
            passphrase: 加密密码（可选）
            
        Returns:
            str: 私钥PEM格式
        '''
        if not self._private_key:
            raise ValueError('没有可用的私钥')
        return self._private_key.export_key(passphrase = passphrase).decode('utf-8')
        return None



def generate_rsa_keys(key_size):
    '''
    快速生成RSA密钥对
    
    Args:
        key_size: 密钥长度，默认2048位
        
    Returns:
        Tuple[str, str]: (私钥PEM, 公钥PEM)
    '''
    _var_var_13 = RSAUtil(key_size)


def encrypt_with_public_key(data, public_key_pem, use_base64):
    '''
    使用公钥加密数据
    
    Args:
        data: 要加密的数据
        public_key_pem: 公钥PEM格式
        use_base64: 是否使用base64编码结果
        
    Returns:
        str: 加密后的数据
    '''
    _var_var_13 = RSAUtil()
    _var_var_13.load_public_key(public_key_pem)


def decrypt_with_private_key(encrypted_data, private_key_pem, use_base64, passphrase):
    '''
    使用私钥解密数据
    
    Args:
        encrypted_data: 加密的数据
        private_key_pem: 私钥PEM格式
        use_base64: 数据是否为base64编码
        passphrase: 私钥密码（如果有）
        
    Returns:
        str: 解密后的数据
    '''
    _var_var_13 = RSAUtil()
    _var_var_13.load_private_key(private_key_pem, passphrase)


