import uuid
import socket
import hashlib
import json
import os
import re
import subprocess
from typing import Dict, Any, Tuple
from dataclasses import dataclass
@dataclass
class DeviceInfo:
    container_id: str = ''
    mac_address: str = ''
    hostname: str = ''
    ip_address: str = ''
    system_fingerprint: str = ''

class DeviceUtil:
    '''设备工具类，用于获取设备指纹和相关信息，针对Docker环境优化'''
    @classmethod
    def is_in_docker(cls) -> bool:
        '''检查是否在Docker容器中运行'''
        if os.path.exists('/.dockerenv'):
            return True
        try:
            with open('/proc/1/cgroup', 'r') as _var_var_0:
                return 'docker' in _var_var_0.read() or 'kubepods' in _var_var_0.read()
        except Exception:
            pass
        return False

    @classmethod
    def get_container_id(cls) -> str:
        '''获取Docker容器ID'''
        if not cls.is_in_docker():
            return 'not-in-container'
        try:
            _var_var_1 = socket.gethostname()
            if len(_var_var_1) == 12 and all(_var_var_5 in '0123456789abcdef' for _var_var_5 in _var_var_1.lower()):
                return _var_var_1
            with open('/proc/self/cgroup', 'r') as _var_var_0:
                for _var_var_2 in _var_var_0:
                    if not _var_var_2:
                        continue
                    _var_var_3 = _var_var_2.strip().split('/')
                    if not len(_var_var_3) > 2:
                        continue
                    _var_var_4 = _var_var_3[-1].split('-')
                    if not len(_var_var_4) >= 1:
                        continue
                    if not len(_var_var_4[-1]) >= 12:
                        continue
                    return _var_var_4[-1][:12]
            return _var_var_1
        except Exception:
            return 'unknown-container'

    @classmethod
    def get_mac_address(cls) -> str:
        '''获取MAC地址'''
        try:
            _var_var_6 = uuid.getnode()
            return ':'.join(['{:02x}'.format((_var_var_6 >> _var_var_7) & 255) for _var_var_7 in range(0, 48, 8)][::-1])
        except Exception:
            return 'unknown'
    @classmethod
    def get_ip_address(cls) -> str:
        '''获取IP地址'''
        try:
            _var_var_8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            _var_var_8.connect(('8.8.8.8', 80))
            _var_var_9 = _var_var_8.getsockname()[0]
            _var_var_8.close()
            return _var_var_9
        except Exception:
            try:
                return socket.gethostbyname(socket.gethostname())
            except Exception:
                return '127.0.0.1'
    @classmethod
    def get_device_id(cls) -> str:
        '''
        生成设备ID
        基于容器特定信息生成一个相对稳定的设备ID
        '''
        _var_var_1 = socket.gethostname()
        _var_var_6 = cls.get_mac_address()
        _var_var_10 = cls.get_container_id()
        _var_var_11 = f'{_var_var_1}|{_var_var_6}|{_var_var_10}'
        _var_var_12 = hashlib.sha256(_var_var_11.encode()).hexdigest()
        return _var_var_12
    @classmethod
    def get_system_fingerprint(cls) -> str:
        '''
        生成系统指纹
        针对Docker环境优化的系统指纹
        '''
        _var_var_1 = socket.gethostname()
        _var_var_10 = cls.get_container_id()
        _var_var_13 = cls.get_ip_address()
        _var_var_14 = ''
        try:
            if os.path.exists('/proc/1/stat'):
                with open('/proc/1/stat', 'r') as _var_var_0:
                    _var_var_3 = _var_var_0.read().split()
                    if len(_var_var_3) > 21:
                        _var_var_14 = _var_var_3[21]
        except Exception:
            pass
        _var_var_15 = f'{_var_var_1}|{_var_var_10}|{_var_var_13}|{_var_var_14}'
        _var_var_16 = hashlib.sha256(_var_var_15.encode()).hexdigest()
        return _var_var_16

    @classmethod
    def get_cpu_info(cls) -> str:
        '''获取CPU信息'''
        try:
            if os.path.exists('/proc/cpuinfo'):
                with open('/proc/cpuinfo', 'r') as _var_var_0:
                    for _var_var_2 in _var_var_0:
                        if not _var_var_2.startswith('model name'):
                            continue
                        return _var_var_2.split(':', 1)[1].strip()
            if os.name == 'nt':
                try:
                    _var_var_17 = subprocess.check_output('wmic cpu get name', shell=True).decode('utf-8')
                    _var_var_18 = _var_var_17.strip().split('\n')
                    if len(_var_var_18) > 1:
                        return _var_var_18[1].strip()
                except Exception:
                    pass
            if os.name != 'nt':
                try:
                    return subprocess.check_output('uname -p', shell=True).decode('utf-8').strip()
                except Exception:
                    pass
            return 'Unknown CPU'
        except Exception:
            return 'Unknown CPU'

    @classmethod
    def get_cpu_count(cls) -> int:
        '''获取CPU核心数'''
        try:
            if os.path.exists('/proc/cpuinfo'):
                with open('/proc/cpuinfo', 'r') as _var_var_0:
                    return _var_var_0.read().count('processor\t:')
            if os.name == 'nt':
                try:
                    _var_var_17 = subprocess.check_output('wmic cpu get NumberOfCores', shell=True).decode('utf-8')
                    _var_var_18 = _var_var_17.strip().split('\n')
                    if len(_var_var_18) > 1:
                        return int(_var_var_18[1].strip())
                except Exception:
                    pass
            if os.name != 'nt':
                try:
                    return int(subprocess.check_output('nproc', shell=True).decode('utf-8').strip())
                except Exception:
                    pass
            return 1
        except Exception:
            return 1

    @classmethod
    def get_memory_info(cls) -> str:
        '''获取内存型号信息'''
        try:
            if os.name == 'nt':
                _var_var_17 = subprocess.check_output('wmic memorychip get speed, capacity, devicelocator', shell=True).decode('utf-8')
                if _var_var_17:
                    _var_var_18 = [_var_var_2 for _var_var_2 in _var_var_17.split('\n') if _var_var_2.strip() and not _var_var_2.startswith('Capacity')]
                    if _var_var_18:
                        return _var_var_18[0].strip()
            try:
                _var_var_17 = subprocess.check_output("sudo dmidecode -t memory | grep -E 'Type:|Speed:|Manufacturer:|Size:'", shell=True).decode('utf-8')
                if _var_var_17:
                    _var_var_19 = re.search('Type: (.+)', _var_var_17)
                    _var_var_20 = re.search('Speed: (.+)', _var_var_17)
                    _var_var_21 = re.search('Manufacturer: (.+)', _var_var_17)
                    _var_var_22 = []
                    if _var_var_21:
                        _var_var_22.append(_var_var_21.group(1).strip())
                    if _var_var_19:
                        _var_var_22.append(_var_var_19.group(1).strip())
                    if _var_var_20:
                        _var_var_22.append(_var_var_20.group(1).strip())
                    if _var_var_22:
                        return ' '.join(_var_var_22)
            except Exception:
                pass
            if os.path.exists('/proc/meminfo'):
                with open('/proc/meminfo', 'r') as _var_var_0:
                    _var_var_23 = _var_var_0.read()
                    _var_var_24 = re.search(r'MemTotal:\s+(\d+)', _var_var_23)
                    if _var_var_24:
                        return f"RAM {round(int(_var_var_24.group(1)) / 1024 / 1024, 2)} GB"
        except Exception:
            pass
        try:
            if os.name != 'nt':
                _var_var_17 = subprocess.check_output('free -m | grep Mem:', shell=True).decode('utf-8')
                if _var_var_17:
                    return 'System RAM'
            if os.name == 'nt':
                return 'System Memory'
        except Exception:
            pass
        return 'Unknown Memory'
    @classmethod
    def get_device_info(cls) -> DeviceInfo:
        '''获取Docker优化的设备信息'''
        _var_var_10 = cls.get_container_id()
        _var_var_1 = socket.gethostname()
        return DeviceInfo(
            device_id=cls.get_device_id(),
            hostname=_var_var_1,
            ip_address=cls.get_ip_address(),
            mac_address=cls.get_mac_address(),
            container_id=_var_var_10,
            system_fingerprint=cls.get_system_fingerprint(),
            cpu_info=cls.get_cpu_info(),
            cpu_count=cls.get_cpu_count(),
            memory_info=cls.get_memory_info(),
        )
    @classmethod
    def calculate_similarity(cls, device_info1: DeviceInfo, device_info2: DeviceInfo) -> Tuple[float, Dict[str, float]]:
        '''
        计算两个设备信息的相似度

        :param device_info1: 第一个设备信息
        :param device_info2: 第二个设备信息
        :return: 元组 (总体相似度, 各项相似度明细)
        '''
        _var_var_28 = {
            'container_id': 1.0 if device_info1.container_id == device_info2.container_id else 0.0,
            'mac_address': 1.0 if device_info1.mac_address == device_info2.mac_address else 0.0,
            'hostname': 1.0 if device_info1.hostname == device_info2.hostname else 0.0,
            'ip_address': 1.0 if device_info1.ip_address == device_info2.ip_address else 0.0,
            'system_fingerprint': 1.0 if device_info1.system_fingerprint == device_info2.system_fingerprint else 0.0
        }
        _var_var_29 = sum(_var_var_28.values()) / len(_var_var_28)
        return (_var_var_29, _var_var_28)

    @classmethod
    def dummy(cls): pass