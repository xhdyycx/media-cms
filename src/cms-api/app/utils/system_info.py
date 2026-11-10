'''
系统信息获取工具类
支持在Docker容器中获取宿主机的真实硬件信息
'''
import os
import platform
import psutil
import json
import subprocess
import re
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path
@dataclass
class CPUInfo:
    '''CPU信息数据类'''
    model: str
    architecture: str
    physical_cores: int
    logical_cores: int
    frequency_max: float
    frequency_min: float

@dataclass
class MemoryModuleInfo:
    '''内存条信息数据类'''
    slot: str
    size_gb: float
    manufacturer: str
    part_number: str
    memory_type: str
    speed_mhz: int
    form_factor: str
    bank_locator: str

@dataclass
class MemoryInfo:
    '''内存信息数据类'''
    total_gb: float
    total_bytes: int
    modules: list[MemoryModuleInfo]

@dataclass
class SystemInfo:
    '''系统信息数据类'''
    cpu: CPUInfo
    memory: MemoryInfo
    platform: str
    hostname: str
    is_docker: bool
    cpu_signature: str
    memory_signature: str

class SystemInfoCollector:
    '''系统信息收集器类'''
    
    def __init__(self):
        self.is_docker = self._detect_docker_environment()
        self.host_proc_path = '/host/proc' if self.is_docker else '/proc'
        self.host_sys_path = '/host/sys' if self.is_docker else '/sys'

    
    def _detect_docker_environment(self):
        '''检测是否在Docker容器中运行'''
        if os.path.exists('/.dockerenv'):
            return True
        if os.path.exists('/proc/1/cgroup'):
            try:
                with open('/proc/1/cgroup', 'r') as _var_var_0:
                    _var_var_1 = _var_var_0.read()
                    if 'docker' in _var_var_1 or 'containerd' in _var_var_1:
                        return True
            except Exception:
                return False
        return False

    
    def _read_host_file(self, file_path):
        '''读取宿主机文件内容'''
        try:
            if self.is_docker:
                _var_var_2 = file_path.replace('/proc', self.host_proc_path).replace('/sys', self.host_sys_path)
                if os.path.exists(_var_var_2):
                    with open(_var_var_2, 'r') as _var_var_0:
                        return _var_var_0.read().strip()
            if os.path.exists(file_path):
                with open(file_path, 'r') as _var_var_0:
                    return _var_var_0.read().strip()
        except Exception as _var_var_3:
            print(f'读取文件 {file_path} 失败: {_var_var_3}')
        return None

    
    def _get_cpu_model_from_proc(self):
        '''从 /proc/cpuinfo 获取CPU型号'''
        try:
            _var_var_4 = self._read_host_file('/proc/cpuinfo')
            if _var_var_4:
                for _var_var_5 in _var_var_4.split('\n'):
                    if not _var_var_5.startswith('model name'):
                        continue
                    return _var_var_5.split(':')[1].strip()
            return 'Unknown'
        except Exception:
            return 'Unknown'

    
    def _get_cpu_model_macos(self):
        """获取macOS系统的CPU型号信息"""
        try:
            result = subprocess.run(['sysctl', '-n', 'machdep.cpu.brand_string'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                cpu_model = result.stdout.strip()
                if 'Apple' in cpu_model or any(chip in cpu_model for chip in ('M1', 'M2', 'M3', 'M4', 'M5')):
                    apple_info = self._get_apple_silicon_info()
                    if apple_info:
                        return apple_info
                return cpu_model
            result = subprocess.run(['sysctl', '-n', 'hw.model'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                model_identifier = result.stdout.strip()
                apple_info = self._parse_apple_silicon_model(model_identifier)
                if apple_info:
                    return apple_info
                return model_identifier
            return self._get_cpu_from_system_profiler()
        except Exception as e:
            print(f'获取macOS CPU信息失败: {e}')
            return 'Unknown'

    
    def _get_apple_silicon_info(self):
        '''获取Apple Silicon芯片的详细信息'''
        try:
            _var_var_7 = subprocess.run(['system_profiler', 'SPHardwareDataType'], capture_output=True, text=True, timeout=10)
            if _var_var_7.returncode == 0:
                _var_var_11 = _var_var_7.stdout
                for _var_var_5 in _var_var_11.split('\n'):
                    _var_var_5 = _var_var_5.strip()
                    if 'Chip:' in _var_var_5 or 'Processor Name:' in _var_var_5:
                        _var_var_12 = _var_var_5.split(':', 1)[1].strip()
                        if not _var_var_12:
                            continue
                        if not _var_var_12 != 'Unknown':
                            continue
                        return _var_var_12
                    if 'Model Identifier:' in _var_var_5:
                        _var_var_13 = _var_var_5.split(':', 1)[1].strip()
                        _var_var_8 = self._parse_apple_silicon_model(_var_var_13)
                        if not _var_var_8:
                            continue
                        return _var_var_8
            return None
        except Exception:
            return None

    
    def _parse_apple_silicon_model(self, model_identifier):
        """从模型标识符解析Apple Silicon芯片类型"""
        try:
            model_identifier = model_identifier.upper()
            chip_map = {
                'MACBOOKAIR10,1': 'Apple M1',
                'MACBOOKAIR10,2': 'Apple M1',
                'MACBOOKAIR11,1': 'Apple M2',
                'MACBOOKAIR11,2': 'Apple M2',
                'MACBOOKAIR15,1': 'Apple M3',
                'MACBOOKAIR15,2': 'Apple M3',
                'MACBOOKAIR16,1': 'Apple M4',
                'MACBOOKAIR16,2': 'Apple M4',
                'MACBOOKPRO17,1': 'Apple M1',
                'MACBOOKPRO18,1': 'Apple M1 Pro',
                'MACBOOKPRO18,2': 'Apple M1 Pro',
                'MACBOOKPRO18,3': 'Apple M1 Pro',
                'MACBOOKPRO18,4': 'Apple M1 Max',
                'MACBOOKPRO19,1': 'Apple M2 Pro',
                'MACBOOKPRO19,2': 'Apple M2 Pro',
                'MACBOOKPRO19,3': 'Apple M2 Max',
                'MACBOOKPRO19,4': 'Apple M2 Max',
                'MACBOOKPRO20,1': 'Apple M3 Pro',
                'MACBOOKPRO20,2': 'Apple M3 Pro',
                'MACBOOKPRO20,3': 'Apple M3 Max',
                'MACBOOKPRO20,4': 'Apple M3 Max',
                'MACBOOKPRO21,1': 'Apple M4 Pro',
                'MACBOOKPRO21,2': 'Apple M4 Pro',
                'MACBOOKPRO21,3': 'Apple M4 Max',
                'MACBOOKPRO21,4': 'Apple M4 Max',
                'MACMINI9,1': 'Apple M1',
                'MACMINI10,1': 'Apple M2',
                'MACMINI10,2': 'Apple M2 Pro',
                'MACMINI11,1': 'Apple M4',
                'MACMINI11,2': 'Apple M4 Pro',
                'IMAC21,1': 'Apple M1',
                'IMAC21,2': 'Apple M1',
                'IMAC24,1': 'Apple M3',
                'IMAC24,2': 'Apple M3',
                'IMAC25,1': 'Apple M4',
                'IMAC25,2': 'Apple M4',
                'MAC15,3': 'Apple M3',
                'MAC15,4': 'Apple M3',
                'MAC16,1': 'Apple M4',
                'MAC16,2': 'Apple M4',
                'MACSTUDIO1,1': 'Apple M1 Max',
                'MACSTUDIO1,2': 'Apple M1 Ultra',
                'MACSTUDIO2,1': 'Apple M2 Max',
                'MACSTUDIO2,2': 'Apple M2 Ultra',
                'MACSTUDIO3,1': 'Apple M4 Max',
                'MACSTUDIO3,2': 'Apple M4 Ultra',
                'MACPRO7,1': 'Intel Xeon',
                'MACPRO8,1': 'Apple M2 Ultra',
                'MACPRO9,1': 'Apple M4 Ultra',
            }
            for model, chip in chip_map.items():
                if re.match(model, model_identifier):
                    return chip
            if any(prefix in model_identifier for prefix in ('MACBOOKAIR', 'MACBOOKPRO', 'MACMINI', 'IMAC', 'MACSTUDIO', 'MACPRO', 'MAC')):
                generations = ['10,', '11,', '12,', '13,', '14,', '15,', '16,', '17,', '18,', '19,', '20,', '21,', '22,', '23,', '24,', '25,', '26,', '27,', '28,', '29,']
                if any(gen in model_identifier for gen in generations):
                    return 'Apple Silicon (M系列芯片)'
            return None
        except Exception:
            return None
    def _get_cpu_from_system_profiler(self):
        """使用system_profiler获取CPU信息（备用方法）"""
        try:
            result = subprocess.run(['system_profiler', 'SPHardwareDataType'], capture_output=True, text=True, timeout=15)
            if result.returncode == 0:
                output = result.stdout
                for line in output.split('\n'):
                    line = line.strip()
                    if any(key in line for key in ('Chip:', 'Processor Name:', 'CPU:')):
                        cpu_info = line.split(':', 1)[1].strip()
                        if not cpu_info:
                            continue
                        if cpu_info == 'Unknown':
                            continue
                        return cpu_info
                for line in output.split('\n'):
                    line = line.strip()
                    if 'Model Identifier:' in line:
                        model_identifier = line.split(':', 1)[1].strip()
                        apple_info = self._parse_apple_silicon_model(model_identifier)
                        if apple_info:
                            return apple_info
                        return f'macOS Device ({model_identifier})'
            return 'Unknown macOS Processor'
        except Exception:
            return 'Unknown'

    
    def _get_cpu_model_windows(self):
        '''获取Windows系统的CPU型号信息'''
        try:
            _var_var_7 = subprocess.run(['wmic', 'cpu', 'get', 'name', '/value'], capture_output=True, text=True, timeout=10)
            if _var_var_7.returncode == 0:
                _var_var_11 = _var_var_7.stdout
                for _var_var_5 in _var_var_11.split('\n'):
                    if not _var_var_5.startswith('Name='):
                        continue
                    _var_var_21 = _var_var_5.split('=', 1)[1].strip()
                    if not _var_var_21:
                        continue
                    return _var_var_21
            _var_var_7 = subprocess.run(['powershell', '-Command', 'Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty Name'], capture_output=True, text=True, timeout=10)
            if _var_var_7.returncode == 0 and _var_var_7.stdout.strip():
                return _var_var_7.stdout.strip()
            _var_var_22 = platform.processor()
            if _var_var_22:
                return _var_var_22
            return 'Unknown Windows Processor'
        except Exception as _var_var_3:
            print(f'获取Windows CPU信息失败: {_var_var_3}')
            return platform.processor() or 'Unknown'

    
    def _get_physical_cores_from_proc(self):
        """从 /proc/cpuinfo 获取物理核心数"""
        try:
            content = self._read_host_file('/proc/cpuinfo')
            if content:
                physical_ids = set()
                cores = set()
                physical_id = None
                core_id = None
                for line in content.split('\n'):
                    if line.startswith('physical id'):
                        physical_id = line.split(':')[1].strip()
                        continue
                    if not line.startswith('core id'):
                        continue
                    core_id = line.split(':')[1].strip()
                    if physical_id is None:
                        continue
                    physical_ids.add(physical_id)
                    cores.add(f'{physical_id}:{core_id}')
                if cores:
                    return len(cores)
                return psutil.cpu_count(logical=False) or 1
            return psutil.cpu_count(logical=False) or 1
        except Exception:
            return psutil.cpu_count(logical=False) or 1
    def _get_memory_info_from_proc(self):
        '''从 /proc/meminfo 获取内存信息'''
        try:
            _var_var_27 = self._read_host_file('/proc/meminfo')
            if _var_var_27:
                _var_var_28 = { }
                for _var_var_5 in _var_var_27.split('\n'):
                    if not ':' in _var_var_5:
                        continue
                    (_var_var_29, _var_var_30) = _var_var_5.split(':', 1)
                    _var_var_31 = int(_var_var_30.strip().split()[0])
                    _var_var_28[_var_var_29.strip()] = _var_var_31 * 1024
                _var_var_32 = _var_var_28.get('MemTotal', 0)
                _var_var_33 = _var_var_28.get('MemAvailable', 0)
                if _var_var_33 == 0:
                    _var_var_34 = _var_var_28.get('MemFree', 0)
                    _var_var_35 = _var_var_28.get('Buffers', 0)
                    _var_var_36 = _var_var_28.get('Cached', 0)
                    _var_var_33 = _var_var_34 + _var_var_35 + _var_var_36
                return {
                    'total': _var_var_32,
                    'available': _var_var_33,
                    'used': _var_var_32 - _var_var_33 }
            return { }
        except Exception:
            return { }

    
    def _get_memory_modules_macos(self):
        '''获取macOS系统的内存条信息'''
        try:
            _var_var_37 = []
            _var_var_7 = subprocess.run(['system_profiler', 'SPMemoryDataType'], capture_output=True, text=True, timeout=15)
            if _var_var_7.returncode == 0:
                _var_var_11 = _var_var_7.stdout
                _var_var_37 = self._parse_macos_memory_output(_var_var_11)
            if not _var_var_37:
                _var_var_37 = self._get_macos_memory_fallback()
        except Exception as _var_var_3:
            print(f'获取macOS内存模块信息失败: {_var_var_3}')
        return _var_var_37

    
    def _parse_macos_memory_output(self, output):
        '''解析macOS system_profiler内存输出'''
        _var_var_37 = []
        try:
            _var_var_38 = { }
            _var_var_39 = output.split('\n')
            for _var_var_5 in _var_var_39:
                _var_var_5 = _var_var_5.strip()
                if _var_var_5.startswith('DIMM') or _var_var_5.startswith('BANK') or 'Memory Slot' in _var_var_5:
                    if _var_var_38:
                        _var_var_40 = self._create_memory_module_from_dict(_var_var_38)
                        if _var_var_40:
                            _var_var_37.append(_var_var_40)
                    _var_var_38 = {
                        'slot': _var_var_5 }
                    continue
                if not ':' in _var_var_5:
                    continue
                if not _var_var_38:
                    continue
                (_var_var_29, _var_var_30) = _var_var_5.split(':', 1)
                _var_var_29 = _var_var_29.strip().lower()
                _var_var_30 = _var_var_30.strip()
                if 'size' in _var_var_29:
                    _var_var_38['size'] = _var_var_30
                    continue
                if 'type' in _var_var_29:
                    _var_var_38['type'] = _var_var_30
                    continue
                if 'speed' in _var_var_29:
                    _var_var_38['speed'] = _var_var_30
                    continue
                if 'manufacturer' in _var_var_29 or 'vendor' in _var_var_29:
                    _var_var_38['manufacturer'] = _var_var_30
                    continue
                if 'part number' in _var_var_29 or 'serial number' in _var_var_29:
                    _var_var_38['part_number'] = _var_var_30
                    continue
                if not 'status' in _var_var_29:
                    continue
                _var_var_38['status'] = _var_var_30
            if _var_var_38:
                _var_var_40 = self._create_memory_module_from_dict(_var_var_38)
                if _var_var_40:
                    _var_var_37.append(_var_var_40)
        except Exception as _var_var_3:
            print(f'解析macOS内存输出失败: {_var_var_3}')
        return _var_var_37

    
    def _create_memory_module_from_dict(self, module_dict):
        '''从字典创建内存模块信息对象'''
        try:
            _var_var_41 = 0
            _var_var_42 = module_dict.get('size', '0 GB')
            if 'GB' in _var_var_42:
                _var_var_41 = float(re.findall('[\\d.]+', _var_var_42)[0])
            if 'MB' in _var_var_42:
                _var_var_41 = float(re.findall('[\\d.]+', _var_var_42)[0]) / 1024
            _var_var_43 = 0
            _var_var_44 = module_dict.get('speed', '0 MHz')
            if 'MHz' in _var_var_44:
                _var_var_45 = re.findall('[\\d]+', _var_var_44)
                if _var_var_45:
                    _var_var_43 = int(_var_var_45[0])
            if _var_var_41 <= 0:
                return None
            return MemoryModuleInfo(slot = module_dict.get('slot', 'Unknown'), size_gb = _var_var_41, manufacturer = module_dict.get('manufacturer', 'Unknown'), part_number = module_dict.get('part_number', 'Unknown'), memory_type = module_dict.get('type', 'Unknown'), speed_mhz = _var_var_43, form_factor = 'Unknown', bank_locator = 'Unknown')
        except Exception as _var_var_3:
            print(f'创建内存模块信息失败: {_var_var_3}')
            return None

    
    def _get_macos_memory_fallback(self):
        '''macOS内存信息回退方案'''
        _var_var_37 = []
        try:
            _var_var_46 = psutil.virtual_memory()
            _var_var_47 = _var_var_46.total / 1073741824
            try:
                _var_var_7 = subprocess.run([
                    'sysctl',
                    '-n',
                    'hw.memsize'], capture_output = True, text = True, timeout = 5)
                if _var_var_7.returncode == 0:
                    _var_var_48 = int(_var_var_7.stdout.strip())
                    _var_var_47 = _var_var_48 / 1073741824
            except Exception:
                pass
            if platform.machine() == 'arm64':
                _var_var_49 = 'LPDDR5' if _var_var_47 >= 16 else 'LPDDR4X'
                _var_var_37.append(MemoryModuleInfo(slot = 'Unified Memory', size_gb = round(_var_var_47, 2), manufacturer = 'Apple', part_number = 'Unified Memory', memory_type = _var_var_49, speed_mhz = 6400 if 'LPDDR5' in _var_var_49 else 4266, form_factor = 'On-Package', bank_locator = 'System'))
            elif _var_var_47 <= 8:
                _var_var_37.append(MemoryModuleInfo(slot = 'DIMM0', size_gb = _var_var_47, manufacturer = 'Unknown', part_number = 'Unknown', memory_type = 'DDR4', speed_mhz = 2667, form_factor = 'SO-DIMM', bank_locator = 'BANK 0'))
            else:
                _var_var_50 = _var_var_47 / 2
                for _var_var_51 in range(2):
                    _var_var_37.append(MemoryModuleInfo(slot = f'''DIMM{_var_var_51}''', size_gb = _var_var_50, manufacturer = 'Unknown', part_number = 'Unknown', memory_type = 'DDR4', speed_mhz = 2667, form_factor = 'SO-DIMM', bank_locator = f'''BANK {_var_var_51}'''))
        except Exception as _var_var_3:
            print(f'''macOS内存回退方案失败: {_var_var_3}''')
        return _var_var_37

    
    def _get_memory_modules_linux(self):
        '''获取Linux系统的内存条信息'''
        _var_var_37 = []
        try:
            _var_var_52 = [
                self._get_linux_memory_from_dmidecode,
                self._get_linux_memory_from_lshw,
                self._get_linux_memory_from_proc]
            for _var_var_53 in _var_var_52:
                _var_var_37 = _var_var_53()
                if _var_var_37:
                    break
            if not _var_var_37:
                _var_var_37 = self._get_linux_memory_fallback()
        except Exception as _var_var_3:
            print(f'''Linux内存获取方法失败: {_var_var_3}''')
        return _var_var_37

    
    def _get_linux_memory_from_dmidecode(self):
        '''使用dmidecode获取Linux内存信息'''
        _var_var_37 = []
        try:
            _var_var_7 = subprocess.run([
                'dmidecode',
                '-t',
                'memory'], capture_output = True, text = True, timeout = 10)
            if _var_var_7.returncode == 0:
                _var_var_37 = self._parse_dmidecode_output(_var_var_7.stdout)
        except Exception:
            pass
        return _var_var_37

    
    def _parse_dmidecode_output(self, output):
        '''解析dmidecode输出'''
        _var_var_37 = []
        try:
            _var_var_38 = { }
            _var_var_39 = output.split('\n')
            _var_var_54 = False
            for _var_var_5 in _var_var_39:
                _var_var_5 = _var_var_5.strip()
                if 'Memory Device' in _var_var_5:
                    if _var_var_38 and _var_var_38.get('size_mb', 0) > 0:
                        _var_var_40 = self._create_linux_memory_module(_var_var_38)
                        if _var_var_40:
                            _var_var_37.append(_var_var_40)
                    _var_var_38 = { }
                    _var_var_54 = True
                    continue
                if not _var_var_54:
                    continue
                if not ':' in _var_var_5:
                    continue
                (_var_var_29, _var_var_30) = _var_var_5.split(':', 1)
                _var_var_29 = _var_var_29.strip().lower()
                _var_var_30 = _var_var_30.strip()
                if 'size' in _var_var_29:
                    _var_var_38['size'] = _var_var_30
                    continue
                if 'locator' in _var_var_29 and 'bank' not in _var_var_29:
                    _var_var_38['locator'] = _var_var_30
                    continue
                if 'bank locator' in _var_var_29:
                    _var_var_38['bank_locator'] = _var_var_30
                    continue
                if 'type' in _var_var_29 and 'detail' not in _var_var_29:
                    _var_var_38['type'] = _var_var_30
                    continue
                if 'speed' in _var_var_29:
                    _var_var_38['speed'] = _var_var_30
                    continue
                if 'manufacturer' in _var_var_29:
                    _var_var_38['manufacturer'] = _var_var_30
                    continue
                if 'part number' in _var_var_29:
                    _var_var_38['part_number'] = _var_var_30
                    continue
                if not 'form factor' in _var_var_29:
                    continue
                _var_var_38['form_factor'] = _var_var_30
            if _var_var_38 and _var_var_38.get('size', '0') != '0':
                _var_var_40 = self._create_linux_memory_module(_var_var_38)
                if _var_var_40:
                    _var_var_37.append(_var_var_40)
        except Exception as _var_var_3:
            print(f'''解析dmidecode输出失败: {_var_var_3}''')
        return _var_var_37

    
    def _create_linux_memory_module(self, module_dict):
        '''从Linux系统信息创建内存模块对象'''
        try:
            _var_var_41 = 0
            _var_var_42 = module_dict.get('size', '0 MB')
            if 'No Module Installed' in _var_var_42 or 'Unknown' in _var_var_42:
                return None
            if 'GB' in _var_var_42:
                _var_var_41 = float(re.findall('[\\d.]+', _var_var_42)[0])
            if 'MB' in _var_var_42:
                _var_var_41 = float(re.findall('[\\d.]+', _var_var_42)[0]) / 1024
            if _var_var_41 <= 0:
                return None
            _var_var_43 = 0
            _var_var_44 = module_dict.get('speed', '0 MT/s')
            _var_var_45 = re.findall('[\\d]+', _var_var_44)
            if _var_var_45:
                _var_var_43 = int(_var_var_45[0])
            return MemoryModuleInfo(slot = module_dict.get('locator', 'Unknown'), size_gb = _var_var_41, manufacturer = module_dict.get('manufacturer', 'Unknown').strip(), part_number = module_dict.get('part_number', 'Unknown').strip(), memory_type = module_dict.get('type', 'Unknown').strip(), speed_mhz = _var_var_43, form_factor = module_dict.get('form_factor', 'Unknown').strip(), bank_locator = module_dict.get('bank_locator', 'Unknown').strip())
        except Exception as _var_var_3:
            print(f'''创建Linux内存模块失败: {_var_var_3}''')
            return None

    
    def _get_linux_memory_from_lshw(self):
        '''使用lshw获取Linux内存信息'''
        _var_var_37 = []
        try:
            _var_var_7 = subprocess.run([
                'lshw',
                '-class',
                'memory',
                '-short'], capture_output = True, text = True, timeout = 10)
            if _var_var_7.returncode == 0:
                pass
        except Exception:
            pass
        return _var_var_37

    
    def _get_linux_memory_from_proc(self):
        '''从/proc文件系统获取Linux内存信息'''
        _var_var_37 = []
        try:
            _var_var_27 = self._read_host_file('/proc/meminfo')
            if _var_var_27:
                for _var_var_5 in _var_var_27.split('\n'):
                    if not _var_var_5.startswith('MemTotal'):
                        continue
                    _var_var_55 = int(_var_var_5.split()[1])
                    _var_var_47 = _var_var_55 / 1048576
                    _var_var_37.append(MemoryModuleInfo(slot = 'System Memory', size_gb = round(_var_var_47, 2), manufacturer = 'Unknown', part_number = 'Unknown', memory_type = 'Unknown', speed_mhz = 0, form_factor = 'Unknown', bank_locator = 'Unknown'))
        except Exception:
            pass
        return _var_var_37

    
    def _get_linux_memory_fallback(self):
        '''Linux内存信息回退方案'''
        _var_var_37 = []
        try:
            _var_var_46 = psutil.virtual_memory()
            _var_var_47 = _var_var_46.total / 1073741824
            _var_var_37.append(MemoryModuleInfo(slot = 'System Memory', size_gb = round(_var_var_47, 2), manufacturer = 'Unknown', part_number = 'Unknown', memory_type = 'DDR4', speed_mhz = 2400, form_factor = 'DIMM', bank_locator = 'Unknown'))
        except Exception as _var_var_3:
            print(f'''Linux内存回退方案失败: {_var_var_3}''')
        return _var_var_37

    
    def _get_memory_modules_windows(self):
        '''获取Windows系统的内存条信息'''
        _var_var_37 = []
        try:
            _var_var_52 = [
                self._get_windows_memory_from_wmic,
                self._get_windows_memory_from_powershell]
            for _var_var_53 in _var_var_52:
                _var_var_37 = _var_var_53()
                if _var_var_37:
                    break
            if not _var_var_37:
                _var_var_37 = self._get_windows_memory_fallback()
        except Exception as _var_var_3:
            print(f'''Windows内存获取方法失败: {_var_var_3}''')
        return _var_var_37

    
    def _get_windows_memory_from_wmic(self):
        '''使用wmic获取Windows内存信息'''
        _var_var_37 = []
        try:
            _var_var_7 = subprocess.run([
                'wmic',
                'memorychip',
                'get',
                'DeviceLocator,Capacity,Manufacturer,PartNumber,MemoryType,Speed,FormFactor,BankLabel',
                '/format:csv'], capture_output = True, text = True, timeout = 15)
            if _var_var_7.returncode == 0:
                _var_var_37 = self._parse_wmic_memory_output(_var_var_7.stdout)
        except Exception as _var_var_3:
            print(f'''wmic内存查询失败: {_var_var_3}''')
        return _var_var_37

    
    def _parse_wmic_memory_output(self, output):
        """解析wmic内存输出"""
        modules = []
        try:
            lines = output.strip().split('\n')
            if len(lines) < 2:
                return modules
            headers = [h.strip() for h in lines[0].split(',')]
            for line in lines[1:]:
                if not line.strip():
                    continue
                values = [v.strip() for v in line.split(',')]
                if len(values) != len(headers):
                    continue
                row = dict(zip(headers, values))
                capacity = int(row.get('Capacity', 0) or 0)
                if capacity <= 0:
                    continue
                size_gb = capacity / 1073741824
                type_code = int(row.get('MemoryType', 0) or 0)
                memory_type = self._decode_windows_memory_type(type_code)
                form_factor_code = int(row.get('FormFactor', 0) or 0)
                form_factor = self._decode_windows_form_factor(form_factor_code)
                module = MemoryModuleInfo(
                    slot=row.get('DeviceLocator', 'Unknown'),
                    size_gb=round(size_gb, 2),
                    manufacturer=row.get('Manufacturer', 'Unknown'),
                    part_number=row.get('PartNumber', 'Unknown'),
                    memory_type=memory_type,
                    speed_mhz=int(row.get('Speed', 0) or 0),
                    form_factor=form_factor,
                    bank_locator=row.get('BankLabel', 'Unknown'),
                )
                modules.append(module)
            return modules
        except Exception as e:
            print(f'解析wmic内存输出失败: {e}')
            return modules
    def _decode_windows_memory_type(self, type_code):
        """解码Windows内存类型代码"""
        type_names = {
            0: 'Unknown',
            1: 'Other',
            2: 'DRAM',
            3: 'Synchronous DRAM',
            4: 'Cache DRAM',
            5: 'EDO',
            6: 'EDRAM',
            7: 'VRAM',
            8: 'SRAM',
            9: 'RAM',
            10: 'ROM',
            11: 'Flash',
            12: 'EEPROM',
            13: 'FEPROM',
            14: 'EPROM',
            15: 'CDRAM',
            16: '3DRAM',
            17: 'SDRAM',
            18: 'SGRAM',
            19: 'RDRAM',
            20: 'DDR',
            21: 'DDR2',
            22: 'DDR2 FB-DIMM',
            24: 'DDR3',
            25: 'FBD2',
            26: 'DDR4',
            27: 'LPDDR',
            28: 'LPDDR2',
            29: 'LPDDR3',
            30: 'LPDDR4',
            31: 'Logical non-volatile device',
            32: 'HBM',
            33: 'HBM2',
            34: 'DDR5',
            35: 'LPDDR5',
        }
        return type_names.get(type_code, f'Unknown ({type_code})')
    def _decode_windows_form_factor(self, form_factor_code):
        """解码Windows内存Form Factor代码"""
        form_factors = {
            0: 'Unknown',
            1: 'Other',
            2: 'SIP',
            3: 'DIP',
            4: 'ZIP',
            5: 'SOJ',
            6: 'Proprietary',
            7: 'SIMM',
            8: 'DIMM',
            9: 'TSOP',
            10: 'PGA',
            11: 'RIMM',
            12: 'SODIMM',
            13: 'SRIMM',
            14: 'SMD',
            15: 'SSMP',
            16: 'QFP',
            17: 'TQFP',
            18: 'SOIC',
            19: 'LCC',
            20: 'PLCC',
            21: 'BGA',
            22: 'FPBGA',
            23: 'LGA',
        }
        return form_factors.get(form_factor_code, f'Unknown ({form_factor_code})')
    def _get_windows_memory_from_powershell(self):
        '''使用PowerShell获取Windows内存信息'''
        _var_var_37 = []
        try:
            _var_var_67 = '\n            Get-WmiObject -Class Win32_PhysicalMemory | Select-Object\n            DeviceLocator,Capacity,Manufacturer,PartNumber,MemoryType,Speed,FormFactor,BankLabel |\n            ConvertTo-Json\n            '
            _var_var_7 = subprocess.run([
                'powershell',
                '-Command',
                _var_var_67], capture_output = True, text = True, timeout = 15)
            if _var_var_7.returncode == 0:
                import json as _var_var_68
                _var_var_60 = _var_var_68.loads(_var_var_7.stdout)
                if isinstance(_var_var_60, dict):
                    _var_var_60 = [
                        _var_var_60]
                for _var_var_69 in _var_var_60:
                    _var_var_61 = int(_var_var_69.get('Capacity', 0) or 0)
                    if _var_var_61 <= 0:
                        continue
                    _var_var_41 = _var_var_61 / 1073741824
                    _var_var_62 = int(_var_var_69.get('MemoryType', 0) or 0)
                    _var_var_63 = int(_var_var_69.get('FormFactor', 0) or 0)
                    _var_var_40 = MemoryModuleInfo(slot = _var_var_69.get('DeviceLocator', 'Unknown'), size_gb = round(_var_var_41, 2), manufacturer = _var_var_69.get('Manufacturer', 'Unknown'), part_number = _var_var_69.get('PartNumber', 'Unknown'), memory_type = self._decode_windows_memory_type(_var_var_62), speed_mhz = int(_var_var_69.get('Speed', 0) or 0), form_factor = self._decode_windows_form_factor(_var_var_63), bank_locator = _var_var_69.get('BankLabel', 'Unknown'))
                    _var_var_37.append(_var_var_40)
        except Exception as _var_var_3:
            print(f'''PowerShell内存查询失败: {_var_var_3}''')
        return _var_var_37

    
    def _get_windows_memory_fallback(self):
        '''Windows内存信息回退方案'''
        _var_var_37 = []
        try:
            _var_var_46 = psutil.virtual_memory()
            _var_var_47 = _var_var_46.total / 1073741824
            _var_var_37.append(MemoryModuleInfo(slot = 'System Memory', size_gb = round(_var_var_47, 2), manufacturer = 'Unknown', part_number = 'Unknown', memory_type = 'DDR4', speed_mhz = 2400, form_factor = 'DIMM', bank_locator = 'Unknown'))
        except Exception as _var_var_3:
            print(f'''Windows内存回退方案失败: {_var_var_3}''')
        return _var_var_37

    
    def get_cpu_info(self):
        '''获取CPU信息'''
        try:
            if platform.system() == 'Linux':
                _var_var_70 = self._get_cpu_model_from_proc()
            elif platform.system() == 'Darwin':
                _var_var_70 = self._get_cpu_model_macos()
            elif platform.system() == 'Windows':
                _var_var_70 = self._get_cpu_model_windows()
            else:
                _var_var_70 = platform.processor() or 'Unknown'
            _var_var_71 = platform.machine()
            _var_var_72 = psutil.cpu_count(logical = True)
            if platform.system() == 'Linux' and self.is_docker:
                _var_var_73 = self._get_physical_cores_from_proc()
            _var_var_73 = psutil.cpu_count(logical = False) or _var_var_72
            _var_var_74 = psutil.cpu_freq()
            if _var_var_74:
                _var_var_75 = _var_var_74.max
                _var_var_76 = _var_var_74.min
            else:
                _var_var_75 = 0
                _var_var_76 = 0
            return CPUInfo(model = _var_var_70, architecture = _var_var_71, physical_cores = _var_var_73, logical_cores = _var_var_72, frequency_max = _var_var_75, frequency_min = _var_var_76)
        except Exception as _var_var_3:
            print(f'''获取CPU信息失败: {_var_var_3}''')
            return CPUInfo(model = 'Unknown', architecture = platform.machine(), physical_cores = 1, logical_cores = 1, frequency_max = 0, frequency_min = 0)

    
    def get_memory_info(self):
        '''获取内存信息'''
        try:
            if platform.system() == 'Linux' and self.is_docker:
                _var_var_77 = self._get_memory_info_from_proc()
                if _var_var_77:
                    _var_var_48 = _var_var_77['total']
                else:
                    _var_var_46 = psutil.virtual_memory()
                    _var_var_48 = _var_var_46.total
            _var_var_46 = psutil.virtual_memory()
            _var_var_48 = _var_var_46.total
            _var_var_47 = _var_var_48 / 1073741824
            _var_var_37 = self._get_memory_modules()
            return MemoryInfo(total_gb = round(_var_var_47, 2), total_bytes = _var_var_48, modules = _var_var_37)
        except Exception as _var_var_3:
            print(f'''获取内存信息失败: {_var_var_3}''')
            return MemoryInfo(total_gb = 0, total_bytes = 0, modules = [])

    
    def _get_memory_modules(self):
        '''获取内存模块信息'''
        try:
            _var_var_78 = platform.system()
            if _var_var_78 == 'Darwin':
                return self._get_memory_modules_macos()
            if _var_var_78 == 'Linux':
                return self._get_memory_modules_linux()
            if _var_var_78 == 'Windows':
                return self._get_memory_modules_windows()
            return []
        except Exception as _var_var_3:
            print(f'''获取内存模块信息失败: {_var_var_3}''')
            return []

    
    def _generate_cpu_signature(self, cpu_info):
        '''生成CPU设备签名'''
        try:
            _var_var_70 = cpu_info.model if cpu_info.model and cpu_info.model != 'Unknown' else 'Unknown CPU'
            _var_var_79 = cpu_info.architecture if cpu_info.architecture else 'Unknown'
            _var_var_73 = cpu_info.physical_cores if cpu_info.physical_cores > 0 else 0
            _var_var_72 = cpu_info.logical_cores if cpu_info.logical_cores > 0 else 0
            _var_var_80 = f'''{_var_var_73}P/{_var_var_72}L'''
            _var_var_81 = ''
            if cpu_info.frequency_max > 0:
                _var_var_81 = f''' | {cpu_info.frequency_max:.0f}MHz'''
            _var_var_82 = f'''{_var_var_70} | {_var_var_79} | {_var_var_80}{_var_var_81}'''
            return _var_var_82
        except Exception as _var_var_3:
            print(f'''生成CPU签名失败: {_var_var_3}''')
            return 'Unknown CPU Signature'

    
    def _generate_memory_signature(self, memory_info):
        """生成内存设备签名"""
        try:
            total_gb = memory_info.total_gb if memory_info.total_gb > 0 else 0
            total_str = f'{total_gb:.0f}GB'
            modules = memory_info.modules
            if not modules:
                return f'{total_str} | Unknown Memory'
            count = len(modules)
            type_list = [m.memory_type for m in modules if m.memory_type and m.memory_type != 'Unknown']
            if type_list:
                type_count = {}
                for t in type_list:
                    type_count[t] = type_count.get(t, 0) + 1
                main_type = max(type_count.items(), key=lambda x: x[1])[0]
            else:
                main_type = 'Unknown'
            speeds = [m.speed_mhz for m in modules if m.speed_mhz > 0]
            if speeds:
                speed_count = {}
                for s in speeds:
                    speed_count[s] = speed_count.get(s, 0) + 1
                main_speed = max(speed_count.items(), key=lambda x: x[1])[0]
                speed_str = f' | {main_speed}MHz'
            else:
                speed_str = ''
            signature = f'{total_str} | {count}x {main_type}{speed_str}'
            return signature
        except Exception as e:
            print(f'生成内存签名失败: {e}')
            return 'Unknown Memory Signature'

    def get_system_info(self):
        '''获取完整的系统信息'''
        _var_var_20 = self.get_cpu_info()
        _var_var_28 = self.get_memory_info()
        _var_var_93 = self._generate_cpu_signature(_var_var_20)
        _var_var_94 = self._generate_memory_signature(_var_var_28)
        return SystemInfo(cpu = _var_var_20, memory = _var_var_28, platform = platform.system(), hostname = platform.node(), is_docker = self.is_docker, cpu_signature = _var_var_93, memory_signature = _var_var_94)

    
    def get_system_info_dict(self):
        '''获取系统信息的字典格式'''
        _var_var_95 = self.get_system_info()
        return asdict(_var_var_95)

    
    def get_system_info_json(self):
        '''获取系统信息的JSON格式'''
        return json.dumps(self.get_system_info_dict(), indent = 2, ensure_ascii = False)


def main():
    '''主函数 - 演示用法'''
    _var_var_96 = SystemInfoCollector()
    print('=== 系统信息收集器 ===')
    print(f'''运行环境: {'Docker容器' if _var_var_96.is_docker else '宿主机'}''')
    print()
    _var_var_95 = _var_var_96.get_system_info()
    print('CPU信息:')
    print(f'''  型号: {_var_var_95.cpu.model}''')
    print(f'''  架构: {_var_var_95.cpu.architecture}''')
    print(f'''  物理核心数: {_var_var_95.cpu.physical_cores}''')
    print(f'''  逻辑核心数: {_var_var_95.cpu.logical_cores}''')
    if _var_var_95.cpu.frequency_max > 0:
        print(f'''  最大频率: {_var_var_95.cpu.frequency_max:.2f} MHz''')
    if _var_var_95.cpu.frequency_min > 0:
        print(f'''  最小频率: {_var_var_95.cpu.frequency_min:.2f} MHz''')
    print()
    print('内存信息:')
    print(f'''  总内存: {_var_var_95.memory.total_gb:.2f} GB''')
    if _var_var_95.memory.modules:
        print(f'''  内存条数量: {len(_var_var_95.memory.modules)}''')
        for _var_var_51, _var_var_40 in enumerate(_var_var_95.memory.modules, 1):
            print(f'''  内存条 {_var_var_51}:''')
            print(f'''    插槽: {_var_var_40.slot}''')
            print(f'''    容量: {_var_var_40.size_gb:.2f} GB''')
            print(f'''    制造商: {_var_var_40.manufacturer}''')
            print(f'''    型号: {_var_var_40.part_number}''')
            print(f'''    类型: {_var_var_40.memory_type}''')
            if _var_var_40.speed_mhz > 0:
                print(f'''    速度: {_var_var_40.speed_mhz} MHz''')
            print(f'''    规格: {_var_var_40.form_factor}''')
    print()
    print('系统信息:')
    print(f'''  平台: {_var_var_95.platform}''')
    print(f'''  主机名: {_var_var_95.hostname}''')
    print(f'''  Docker环境: {_var_var_95.is_docker}''')
    print()
    print('设备签名:')
    print(f'''  CPU签名: {_var_var_95.cpu_signature}''')
    print(f'''  内存签名: {_var_var_95.memory_signature}''')

if __name__ == '__main__':
    main()
    sys_info = SystemInfoCollector().get_system_info()
    print(sys_info.cpu_signature)
    print(sys_info.memory_signature)
