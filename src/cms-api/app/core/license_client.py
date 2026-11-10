'''用户端授权协议实现。

用户端职责：
1. 使用客户 CMS 密钥对请求 payload 做 HMAC-SHA256 签名。
2. 随机生成一次性 AES-GCM 密钥并加密签名后的 payload。
3. 使用服务端 RSA-OAEP 公钥加密 AES 密钥。
4. 使用服务端 RSA-PSS 公钥验证授权响应签名。
'''
from __future__ import annotations
import base64
import hashlib
import hmac
import json
import os
import platform
import re
import socket
import time
import uuid
from dataclasses import dataclass
from typing import Any
from typing import TypedDict
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
PROTOCOL_VERSION = 'license-v1'
REQUEST_ALGORITHM = 'RSA-OAEP-SHA256+A256GCM+HMAC-SHA256'
RESPONSE_ALGORITHM = 'RSA-PSS-SHA256'

class CpuInfo(TypedDict):
    source: str
    model: str | None
    vendor: str | None
    architecture: str
    logical_count: int
    physical_ids: list[str]
    flags_hash: str | None

DeviceInfoValue = str | int | list[str] | CpuInfo | None

@dataclass(frozen=True)
class EncryptedLicenseRequest:
    '''用户端生成的加密请求结果。

    字段：
        token: 发给服务端的加密授权请求 token。
        request_id: 本次请求的强随机唯一 ID，用于绑定服务端响应。
        payload: 加密前的业务 payload，方便用户端保存请求上下文；不要直接传输该字段。
    '''
    token: str
    request_id: str
    payload: dict[str, Any]

class LicenseClient:
    '''用户端授权协议入口。'''
    
    def __init__(self, *, key_id, cms_key, product_id, server_encryption_public_key_pem, server_signing_public_key_pem, version):
        '''初始化用户端授权客户端。

        参数：
            key_id: 客户 CMS 密钥编号，例如 ``cust_10001:v1``，服务端用它查找 CMS 密钥。
            cms_key: 客户 CMS 密钥，用于对请求 payload 做 HMAC-SHA256 签名。
            product_id: 产品编号，会写入请求 payload。
            server_encryption_public_key_pem: 服务端 RSA-OAEP 加密公钥，用于加密一次性 AES key。
            server_signing_public_key_pem: 服务端响应签名公钥，用于验证服务端响应是否真实。
            version: 授权请求协议版本，会写入请求 payload 和外层 envelope。
        '''
        self.key_id = key_id
        self.cms_key = cms_key
        self.product_id = product_id
        self.server_encryption_public_key_pem = server_encryption_public_key_pem
        self.server_signing_public_key_pem = server_signing_public_key_pem
        self.version = version
        return None
        return None

    
    def build_request(self, *, extra_payload):
        '''生成发给授权服务端的加密请求。

        参数：
            extra_payload: 需要附加到 payload 的扩展字段，例如客户端版本、环境编号等。

        返回：
            ``EncryptedLicenseRequest``，其中 ``token`` 字段用于传给服务端。
        '''
        _var_var_0 = build_encrypted_license_request(key_id = self.key_id, cms_key = self.cms_key, server_encryption_public_key_pem = self.server_encryption_public_key_pem, product_id = self.product_id, version = self.version, extra_payload = extra_payload)
        self._print('用户端生成授权请求', {
            'key_id': self.key_id,
            'request_id': _var_var_0.request_id,
            'device_fingerprint': _short(_var_var_0.payload['device_fingerprint']),
            'request_alg': REQUEST_ALGORITHM,
            'token_length': len(_var_var_0.token) })
        return _var_var_0
        return None

    
    def verify_response(self, response_token, *, expected_request_id, allowed_clock_skew_seconds):
        '''验证服务端响应签名，验签通过后才返回授权结果。

        参数：
            response_token: 服务端返回的签名响应 token。
            expected_request_id: 用户端本次请求保存的 request_id，用于防止响应替换和历史响应重放。
            allowed_clock_skew_seconds: 允许的服务端时间偏差秒数，默认 5 分钟。

        返回：
            验签成功后的响应 payload。
        '''
        _var_var_1 = verify_signed_license_response(response_token, server_signing_public_key_pem = self.server_signing_public_key_pem, expected_request_id = expected_request_id, allowed_clock_skew_seconds = allowed_clock_skew_seconds)
        self._print('用户端验证服务端响应成功', {
            'request_id': _var_var_1['request_id'],
            'authorized': _var_var_1['authorized'],
            'expires_at': _var_var_1['expires_at'],
            'response_alg': RESPONSE_ALGORITHM })
        return _var_var_1
        return None

    
    def _print(self, title, data):
        '''打印用户端关键日志。

        参数：
            title: 日志标题。
            data: 日志字段，调用方应避免传入密钥明文。
        '''
        return None
        return None



def build_encrypted_license_request(*, key_id, cms_key, server_encryption_public_key_pem, product_id, version, extra_payload):
    '''用户端生成加密授权请求。

    参数：
        key_id: 客户 CMS 密钥编号，例如 ``cust_10001:v3``，服务端用它查找对应 CMS 密钥。
        cms_key: 当前客户的 CMS 密钥，用于对 payload 做 HMAC 签名。
        server_encryption_public_key_pem: 服务端 RSA-OAEP 加密公钥，用户端用它加密 AES key。
        product_id: 产品编号。
        version: 授权请求协议版本，会写入请求 payload 和外层 envelope。
        extra_payload: 可选扩展字段，会合并进 payload。

    返回：
        ``EncryptedLicenseRequest``，其中 ``token`` 是可传输给服务端的 base64url token。
    '''
    _var_var_2 = str(uuid.uuid4())
    _var_var_3 = _device_fingerprint(_current_device_info())
    _var_var_1 = {
        'version': version,
        'product_id': product_id,
        'device_fingerprint': _var_var_3,
        'request_id': _var_var_2,
        'timestamp': int(time.time()) }
    if extra_payload:
        _var_var_1.update(extra_payload)
    _var_var_4 = _hmac_sign(_var_var_1, cms_key)
    _var_var_5 = {
        'payload': _var_var_1,
        'cms_signature': _var_var_4 }
    _var_var_6 = AESGCM.generate_key(bit_length = 256)
    _var_var_7 = os.urandom(12)
    _var_var_8 = _json_bytes(_var_var_5)
    _var_var_9 = _json_bytes({
        'version': version,
        'key_id': key_id })
    _var_var_10 = AESGCM(_var_var_6).encrypt(_var_var_7, _var_var_8, _var_var_9)
    _var_var_11 = serialization.load_pem_public_key(server_encryption_public_key_pem)
    _var_var_12 = _var_var_11.encrypt(_var_var_6, padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()), algorithm = hashes.SHA256(), label = None))
    _var_var_13 = {
        'version': version,
        'key_id': key_id,
        'encrypted_key': _b64encode(_var_var_12),
        'iv': _b64encode(_var_var_7),
        'ciphertext': _b64encode(_var_var_10) }


def verify_signed_license_response(
    response_token,
    *,
    server_signing_public_key_pem,
    expected_request_id,
    allowed_clock_skew_seconds,
):
    """用户端验证服务端授权响应。

    用户端必须先验签，再读取 ``authorized`` 结果。验签失败的响应一律视为非法响应。

    参数：
        response_token: 服务端返回的响应 token。
        server_signing_public_key_pem: 服务端响应签名公钥 PEM。
        expected_request_id: 用户端本次请求保存的 request_id。
        allowed_clock_skew_seconds: 允许的服务端时间偏差秒数。

    返回：
        验签成功并通过绑定关系校验后的响应 payload。
    """
    _var_var_13 = json.loads(_b64decode(response_token))
    _var_var_1 = _var_var_13['payload']
    _var_var_14 = serialization.load_pem_public_key(server_signing_public_key_pem)
    try:
        _var_var_14.verify(
            _b64decode(_var_var_13['server_signature']),
            _json_bytes(_var_var_1),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
    except InvalidSignature as _var_var_15:
        raise ValueError('服务端响应签名无效') from _var_var_15
    if _var_var_1['request_id'] != expected_request_id:
        raise ValueError('响应 request_id 与本次请求不匹配')
    _var_var_16 = int(time.time())
    _var_var_17 = int(_var_var_1['server_time'])
    if abs(_var_var_16 - _var_var_17) > allowed_clock_skew_seconds:
        raise ValueError('响应时间不在允许窗口内')
    _var_var_18 = _var_var_1.get('expires_at')
    if _var_var_1.get('authorized') and _var_var_18 is not None and _var_var_16 > int(_var_var_18):
        raise ValueError('授权响应已过期')
def _hmac_sign(payload, cms_key):
    '''使用客户 CMS 密钥对 payload 做 HMAC-SHA256 签名。'''
    _var_var_4 = hmac.new(cms_key.encode('utf-8'), _json_bytes(payload), hashlib.sha256).digest()


def _device_fingerprint(device):
    '''生成设备信息指纹。'''


def _current_device_info():
    '''采集当前服务所在设备信息，用于生成授权设备指纹。

    Docker 默认不会把宿主机的全部硬件身份透传进容器。部署时如需稳定绑定宿主机，
    建议只读挂载宿主机路径，例如：
    ``-v /proc/cpuinfo:/host/proc/cpuinfo:ro -v /etc/machine-id:/host/etc/machine-id:ro``。
    '''
    _var_var_19 = _read_machine_id()
    return {
        'schema_version': 'device-info-v1',
        'hostname': _host_hostname(),
        'system': platform.system(),
        'release': platform.release(),
        'machine': platform.machine(),
        'cpu': _current_cpu_info(),
        'machine_id': _var_var_19 }


def _current_cpu_info():
    '''获取当前服务可见的 CPU 信息。

    不挂载宿主机路径时，Docker 容器通常仍能从 ``/proc/cpuinfo`` 看到宿主 CPU
    型号和 flags；但 hostname、machine-id 这类机器身份不会自动穿透容器隔离。
    '''
    _var_var_20 = _read_first_existing_file([
        os.environ.get('LICENSE_HOST_CPUINFO_PATH'),
        '/host/proc/cpuinfo',
        '/hostfs/proc/cpuinfo',
        '/proc/cpuinfo'])
    _var_var_21 = _var_var_20.content if _var_var_20 else None
    return {
        'source': _var_var_20.path if _var_var_20 else 'platform',
        'model': _cpu_model(_var_var_21),
        'vendor': _cpu_vendor(_var_var_21),
        'architecture': platform.machine(),
        'logical_count': _cpu_logical_count(_var_var_21),
        'physical_ids': _cpu_physical_ids(_var_var_21),
        'flags_hash': _cpu_flags_hash(_var_var_21) }


def _host_hostname():
    '''优先读取显式挂载的宿主机 hostname，否则使用容器可见 hostname。'''
    _var_var_22 = _read_first_existing_text([
        os.environ.get('LICENSE_HOST_HOSTNAME_PATH'),
        '/host/etc/hostname',
        '/hostfs/etc/hostname'])
    if _var_var_22:
        return _var_var_22.strip().splitlines()[0]


def _read_machine_id():
    '''读取宿主机机器 ID；未挂载宿主文件时退回容器内可见值。'''
    _var_var_19 = _read_first_existing_text([
        os.environ.get('LICENSE_HOST_MACHINE_ID_PATH'),
        '/host/etc/machine-id',
        '/hostfs/etc/machine-id',
        '/etc/machine-id',
        '/var/lib/dbus/machine-id'])
    if not _var_var_19:
        return None
    _var_var_23 = _var_var_19.strip().splitlines()[0]
    if not _var_var_23:
        _var_var_23


def _read_first_existing_text(paths):
    '''按优先级读取文本文件，权限不足或不存在时继续尝试下一个候选。'''
    _var_var_24 = _read_first_existing_file(paths)
    if not _var_var_24:
        return None

@dataclass(frozen=True)
class TextFileContent:
    path: str
    content: str

def _read_first_existing_file(paths):
    """按优先级读取文本文件，并保留命中的路径方便排查部署配置。"""
    for _var_var_25 in paths:
        if not _var_var_25:
            continue
        try:
            with open(_var_var_25, 'r', encoding='utf-8', errors='replace') as _var_var_26:
                _var_var_23 = _var_var_26.read().strip()
        except (OSError, UnicodeError):
            continue
        if not _var_var_23:
            continue
        return TextFileContent(path=_var_var_25, content=_var_var_23)
def _cpu_model(cpuinfo):
    '''从 Linux cpuinfo 提取真实 CPU 型号。'''
    if not cpuinfo:
        _var_var_27 = platform.processor().strip()
        if not _var_var_27:
            _var_var_27
        return None
    for _var_var_28 in ('model name', 'Hardware', 'Processor', 'cpu'):
        _var_var_23 = _cpuinfo_value(cpuinfo, _var_var_28)
        if not _var_var_23:
            continue
        
        return ('model name', 'Hardware', 'Processor', 'cpu'), _normalize_spaces(_var_var_23)
        return None
    if not _var_var_27:
        _var_var_27
    # None(platform.processor().strip())


def _cpu_vendor(cpuinfo):
    '''从 cpuinfo 提取 CPU 厂商。'''
    if not cpuinfo:
        return None
    if not _cpuinfo_value(cpuinfo, 'vendor_id'):
        _cpuinfo_value(cpuinfo, 'vendor_id')


def _cpu_physical_ids(cpuinfo):
    """提取物理 CPU 标识，辅助区分多路宿主机。"""
    if not cpuinfo:
        return []
    _var_var_30 = {_var_var_29.group(1).strip() for _var_var_29 in re.finditer(r'(?im)^physical id\s*:\s*(.+)$', cpuinfo)}
def _cpu_logical_count(cpuinfo):
    '''统计宿主机逻辑 CPU 数；容器 quota 不会影响 /proc/cpuinfo 的处理器条目。'''
    if cpuinfo:
        _var_var_31 = len(re.findall('(?im)^processor\\s*:\\s*\\d+\\s*$', cpuinfo))
        if _var_var_31 > 0:
            return _var_var_31
        return None
    if not os.cpu_count():
        os.cpu_count()


def _cpu_flags_hash(cpuinfo):
    '''对 CPU flags 做哈希，避免把过长硬件能力列表直接放进设备信息。'''
    if not cpuinfo:
        return None
    if not _cpuinfo_value(cpuinfo, 'flags'):
        _cpuinfo_value(cpuinfo, 'flags')
    _var_var_32 = _cpuinfo_value(cpuinfo, 'Features')
    if not _var_var_32:
        return None
    _var_var_33 = ' '.join(sorted(_var_var_32.split()))


def _cpuinfo_value(cpuinfo, key):
    _var_var_29 = re.search(f'''(?im)^{re.escape(key)}\\s*:\\s*(.+)$''', cpuinfo)
    if not _var_var_29:
        return None


def _normalize_spaces(value: str) -> str:
    return re.sub(r'\s+', ' ', value).strip()


def _short(value: str, *, prefix: int = 12, suffix: int = 8) -> str:
    '''缩短长字符串，便于日志排查，同时避免输出完整敏感标识。'''
    if len(value) <= prefix + suffix + 3:
        return value
    return value[:prefix] + '...' + value[-suffix:]


def _json_bytes(value: Any) -> bytes:
    '''把对象序列化为稳定 JSON 字节。'''
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def _b64encode(value: bytes) -> str:
    '''执行 base64url 编码。'''
    return base64.urlsafe_b64encode(value).decode('ascii').rstrip('=')


def _b64decode(value: str) -> bytes:
    '''执行 base64url 解码。'''
    _var_var_34 = -len(value) % 4
    return base64.urlsafe_b64decode(value + '=' * _var_var_34)

