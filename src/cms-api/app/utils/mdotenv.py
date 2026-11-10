import os
import re
import shutil
from datetime import datetime
from typing import Dict, Optional, List, Tuple
from app.log import logger

class DotEnvUtil:
    '''
    .env 文件操作工具类
    用于读取、写入、更新 .env 文件中的环境变量
    '''
    @staticmethod
    def read_env_file(file_path):
        """
        读取 .env 文件并解析为字典

        Args:
            file_path: .env 文件路径

        Returns:
            Dict[str, str]: 环境变量字典
        """
        _var_var_0 = {}
        if not os.path.exists(file_path):
            logger.warning(f'.env 文件不存在: {file_path}')
            return _var_var_0
        try:
            with open(file_path, 'r', encoding='utf-8') as _var_var_1:
                for _var_var_2, _var_var_3 in enumerate(_var_var_1, 1):
                    _var_var_3 = _var_var_3.strip()
                    if not _var_var_3 or _var_var_3.startswith('#'):
                        continue
                    if '=' in _var_var_3:
                        _var_var_4, _var_var_5 = DotEnvUtil._parse_line(_var_var_3)
                        if not _var_var_4:
                            continue
                        _var_var_0[_var_var_4] = _var_var_5
                    else:
                        logger.warning(f'.env 文件第 {_var_var_2} 行格式错误: {_var_var_3}')
        except Exception as _var_var_6:
            logger.error(f'读取 .env 文件失败: {str(_var_var_6)}')
        return _var_var_0

    @staticmethod
    def _parse_line(line):
        """
        解析单行环境变量
        支持格式：KEY=value, KEY="value", KEY='value'

        Args:
            line: 单行内容

        Returns:
            Tuple[Optional[str], str]: (键, 值)
        """
        _var_var_7 = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
        if not _var_var_7:
            return (None, '')
        _var_var_4 = _var_var_7.group(1)
        _var_var_5 = _var_var_7.group(2)
        if _var_var_5.startswith('"') and _var_var_5.endswith('"'):
            _var_var_5 = _var_var_5[1:-1]
        elif _var_var_5.startswith("'") and _var_var_5.endswith("'"):
            _var_var_5 = _var_var_5[1:-1]
        _var_var_5 = _var_var_5.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace("\\'", "'")
        return (_var_var_4, _var_var_5)

    @staticmethod
    def save_env_file(file_path, env_vars, backup=True):
        """
        保存环境变量到 .env 文件

        Args:
            file_path: .env 文件路径
            env_vars: 环境变量字典
            backup: 是否备份原文件

        Returns:
            bool: 是否成功
        """
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if backup and os.path.exists(file_path):
                DotEnvUtil._backup_file(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# 由 CMS 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                for k, v in sorted(env_vars.items()):
                    if DotEnvUtil._needs_quotes(v):
                        v_esc = v.replace('"', '\"').replace('\n', '\\n').replace('\t', '\\t')
                        f.write(f'{k}="{v_esc}"\n')
                    else:
                        f.write(f'{k}={v}\n')
            logger.info(f"成功保存 .env 文件: {file_path}")
            return True
        except Exception as e:
            logger.error(f"保存 .env 文件失败: {str(e)}")
            return False

    @staticmethod
    def _needs_quotes(value):
        """
        判断值是否需要用引号包围

        Args:
            value: 环境变量值

        Returns:
            bool: 是否需要引号
        """
        if not value:
            return False
        _var_var_9 = [' ', '\t', '\n', '"', "'", '#', '=']
        return any(_var_var_10 in value for _var_var_10 in _var_var_9)
    @staticmethod
    def _backup_file(file_path):
        """
        备份文件

        Args:
            file_path: 原文件路径

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_11 = f'{file_path}.backup.{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            shutil.copy2(file_path, _var_var_11)
            logger.info(f'已备份文件: {_var_var_11}')
            return True
        except Exception as _var_var_6:
            logger.error(f'备份文件失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def update_env_var(file_path, key, value):
        """
        更新单个环境变量

        Args:
            file_path: .env 文件路径
            key: 环境变量名
            value: 环境变量值

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            _var_var_0[key] = value
            return DotEnvUtil.save_env_file(file_path, _var_var_0)
        except Exception as _var_var_6:
            logger.error(f'更新环境变量失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def delete_env_var(file_path, key):
        """
        删除环境变量

        Args:
            file_path: .env 文件路径
            key: 环境变量名

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            if key in _var_var_0:
                del _var_var_0[key]
                logger.info(f'删除环境变量: {key}')
                return DotEnvUtil.save_env_file(file_path, _var_var_0)
            else:
                logger.warning(f'环境变量不存在: {key}')
                return True
        except Exception as _var_var_6:
            logger.error(f'删除环境变量失败: {str(_var_var_6)}')
            return False

    @staticmethod
    def get_env_var(file_path, key, default=None):
        """
        获取单个环境变量值

        Args:
            file_path: .env 文件路径
            key: 环境变量名
            default: 默认值

        Returns:
            str: 环境变量值
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            return _var_var_0.get(key, default)
        except Exception as _var_var_6:
            logger.error(f'获取环境变量失败: {str(_var_var_6)}')
            return default
    @staticmethod
    def update_multiple_vars(file_path, updates):
        """
        批量更新环境变量

        Args:
            file_path: .env 文件路径
            updates: 要更新的变量字典

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            _var_var_0.update(updates)
            return DotEnvUtil.save_env_file(file_path, _var_var_0)
        except Exception as _var_var_6:
            logger.error(f'批量更新环境变量失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def list_env_vars(file_path):
        """
        列出所有环境变量名

        Args:
            file_path: .env 文件路径

        Returns:
            List[str]: 环境变量名列表
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            return list(_var_var_0.keys())
        except Exception as _var_var_6:
            logger.error(f'列出环境变量失败: {str(_var_var_6)}')
            return []
    @staticmethod
    def env_var_exists(file_path, key):
        """
        检查环境变量是否存在

        Args:
            file_path: .env 文件路径
            key: 环境变量名

        Returns:
            bool: 是否存在
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(file_path)
            return key in _var_var_0
        except Exception as _var_var_6:
            logger.error(f'检查环境变量失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def clear_env_file(file_path, backup=True):
        """
        清空 .env 文件

        Args:
            file_path: .env 文件路径
            backup: 是否备份原文件

        Returns:
            bool: 是否成功
        """
        try:
            return DotEnvUtil.save_env_file(file_path, {}, backup)
        except Exception as _var_var_6:
            logger.error(f'清空 .env 文件失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def copy_env_file(src_path, dst_path):
        """
        复制 .env 文件

        Args:
            src_path: 源文件路径
            dst_path: 目标文件路径

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_0 = DotEnvUtil.read_env_file(src_path)
            return DotEnvUtil.save_env_file(dst_path, _var_var_0, backup=False)
        except Exception as _var_var_6:
            logger.error(f'复制 .env 文件失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def merge_env_files(file1_path, file2_path, output_path, file2_priority=False):
        """
        合并两个 .env 文件

        Args:
            file1_path: 第一个文件路径
            file2_path: 第二个文件路径
            output_path: 输出文件路径
            file2_priority: 当变量冲突时，是否优先使用第二个文件的值

        Returns:
            bool: 是否成功
        """
        try:
            _var_var_12 = DotEnvUtil.read_env_file(file1_path)
            _var_var_13 = DotEnvUtil.read_env_file(file2_path)
            if file2_priority:
                _var_var_14 = {**_var_var_12, **_var_var_13}
            else:
                _var_var_14 = {**_var_var_13, **_var_var_12}
            return DotEnvUtil.save_env_file(output_path, _var_var_14, backup=False)
        except Exception as _var_var_6:
            logger.error(f'合并 .env 文件失败: {str(_var_var_6)}')
            return False
    @staticmethod
    def validate_env_file(file_path: str) -> Tuple[bool, List[str]]:
        """
        验证 .env 文件格式

        Args:
            file_path: .env 文件路径

        Returns:
            Tuple[bool, List[str]]: (是否有效, 错误信息列表)
        """
        _var_var_15 = []
        if not os.path.exists(file_path):
            _var_var_15.append(f'文件不存在: {file_path}')
            return (False, _var_var_15)
        try:
            with open(file_path, 'r', encoding='utf-8') as _var_var_1:
                for _var_var_2, _var_var_3 in enumerate(_var_var_1, 1):
                    _var_var_3 = _var_var_3.strip()
                    if not _var_var_3 or _var_var_3.startswith('#'):
                        continue
                    if '=' not in _var_var_3:
                        _var_var_15.append(f'第 {_var_var_2} 行缺少等号: {_var_var_3}')
                        continue
                    _var_var_16 = _var_var_3.split('=')[0].strip()
                    if re.match('^[A-Za-z_][A-Za-z0-9_]*$', _var_var_16):
                        continue
                    _var_var_15.append(f'第 {_var_var_2} 行变量名格式错误: {_var_var_16}')
        except Exception as _var_var_6:
            _var_var_15.append(f'读取文件时发生错误: {str(_var_var_6)}')
        return (len(_var_var_15) == 0, _var_var_15)
