'''
RSA加解密工具类使用示例
'''
from app.utils.rsa_util import RSAUtil, generate_rsa_keys, encrypt_with_public_key, decrypt_with_private_key

def example_basic_usage():
    '''基本使用示例'''
    print('=== RSA工具类基本使用示例 ===')
    _var_var_0 = RSAUtil(key_size = 2048)
    (_var_var_1, _var_var_2) = _var_var_0.generate_key_pair()
    print('生成的公钥:')
    print(_var_var_2)
    print('\n生成的私钥:')
    print(_var_var_1[:100] + '...')
    _var_var_3 = '这是一个需要加密的重要信息！'
    _var_var_4 = _var_var_0.encrypt(_var_var_3)
    print(f'''\n原始数据: {_var_var_3}''')
    print(f'''加密后数据: {_var_var_4}''')
    _var_var_5 = _var_var_0.decrypt(_var_var_4)
    print(f'''解密后数据: {_var_var_5}''')
    print(f'''加解密是否成功: {_var_var_3 == _var_var_5}''')


def example_signature():
    '''数字签名示例'''
    print('\n=== 数字签名示例 ===')
    _var_var_0 = RSAUtil()
    _var_var_0.generate_key_pair()
    _var_var_6 = '这是需要签名的重要文档内容'
    _var_var_7 = _var_var_0.sign(_var_var_6)
    print(f'''原始数据: {_var_var_6}''')
    print(f'''数字签名: {_var_var_7}''')
    _var_var_8 = _var_var_0.verify(_var_var_6, _var_var_7)
    print(f'''签名验证结果: {_var_var_8}''')
    _var_var_9 = '这是被篡改的文档内容'
    _var_var_10 = _var_var_0.verify(_var_var_9, _var_var_7)
    print(f'''篡改数据的签名验证结果: {_var_var_10}''')


def example_key_management():
    '''密钥管理示例'''
    print('\n=== 密钥管理示例 ===')
    _var_var_0 = RSAUtil()
    (_var_var_11, _var_var_12) = _var_var_0.generate_key_pair()
    _var_var_13 = RSAUtil()
    _var_var_13.load_private_key(_var_var_11)
    _var_var_14 = '测试密钥加载功能'
    _var_var_15 = _var_var_13.encrypt(_var_var_14)
    _var_var_16 = _var_var_13.decrypt(_var_var_15)
    print(f'''密钥加载测试: {_var_var_14 == _var_var_16}''')


def example_convenience_functions():
    '''便捷函数使用示例'''
    print('\n=== 便捷函数使用示例 ===')
    (_var_var_1, _var_var_2) = generate_rsa_keys(2048)
    print('使用便捷函数生成密钥对成功')
    print(_var_var_2)
    print(_var_var_1)
    _var_var_17 = '使用便捷函数进行加密测试'
    _var_var_15 = encrypt_with_public_key(_var_var_17, _var_var_2)
    print(f'''便捷加密结果: {_var_var_15[:50]}...''')
    _var_var_16 = decrypt_with_private_key(_var_var_15, _var_var_1)
    print(f'''便捷解密结果: {_var_var_16}''')
    print(f'''便捷函数测试成功: {_var_var_17 == _var_var_16}''')


def example_different_formats():
    '''不同编码格式示例'''
    print('\n=== 不同编码格式示例 ===')
    _var_var_0 = RSAUtil()
    _var_var_0.generate_key_pair()
    _var_var_17 = '测试不同编码格式'
    _var_var_18 = _var_var_0.encrypt(_var_var_17, use_base64 = True)
    _var_var_19 = _var_var_0.decrypt(_var_var_18, use_base64 = True)
    print(f'''Base64格式 - 加密: {_var_var_18[:50]}...''')
    print(f'''Base64格式 - 解密成功: {_var_var_17 == _var_var_19}''')
    _var_var_20 = _var_var_0.encrypt(_var_var_17, use_base64 = False)
    _var_var_21 = _var_var_0.decrypt(_var_var_20, use_base64 = False)
    print(f'''十六进制格式 - 加密: {_var_var_20[:50]}...''')
    print(f'''十六进制格式 - 解密成功: {_var_var_17 == _var_var_21}''')


def example_error_handling():
    '''错误处理示例'''
    print('\n=== 错误处理示例 ===')
    _var_var_0 = RSAUtil()
    _var_var_0.encrypt('测试数据')
    _var_var_0.decrypt('fake_encrypted_data')
    try:
        _var_var_0.generate_key_pair()
        _var_var_0.decrypt('invalid_encrypted_data')
    except ValueError:
        _var_var_22 = None
        print(f'''预期错误 - 没有公钥: {_var_var_22}''')
        _var_var_22 = None
        del _var_var_22
