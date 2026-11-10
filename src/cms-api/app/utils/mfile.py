import os
import shutil
from datetime import datetime
from app.log import logger

class MFileUtil:
    @staticmethod
    def read_file(file_path: str) -> str:
        """读取文件内容
        Args:
            file_path: 文件路径
        Returns:
            str: 文件内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as _var_var_0:
                return _var_var_0.read()
        except Exception as _var_var_1:
            logger.error(f'读取文件失败: {str(_var_var_1)}')
            return ''
    @staticmethod
    def write_file(file_path: str, content: str = '') -> bool:
        """写文件(如果文件不存在则创建,如果文件所在目录不存在则创建目录)
        Args:
            file_path: 文件路径
            content: 文件内容
        Returns:
            bool: 是否成功
        """
        try:
            dir_path = os.path.dirname(file_path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                if content:
                    f.write(content)
            return True
        except Exception as e:
            raise Exception(f"创建文件失败: {str(e)}")

    @staticmethod
    def delete_file(file_path: str) -> bool:
        """删除文件
        Args:
            file_path: 文件路径
        Returns:
            bool: 是否成功
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            return True
        except Exception:
            return False

    @staticmethod
    def copy_file(src_path: str, dst_path: str) -> bool:
        """复制文件
        Args:
            src_path: 源文件路径
            dst_path: 目标文件路径
        Returns:
            bool: 是否成功
        """
        try:
            shutil.copy2(src_path, dst_path)
            return True
        except Exception as _var_var_1:
            raise Exception(f'复制文件失败: {str(_var_var_1)}')
    @staticmethod
    def move_file(src_path: str, dst_path: str) -> bool:
        """移动文件
        Args:
            src_path: 源文件路径
            dst_path: 目标文件路径
        Returns:
            bool: 是否成功
        """
        try:
            shutil.move(src_path, dst_path)
            return True
        except Exception as _var_var_1:
            raise Exception(f'移动文件失败: {str(_var_var_1)}')
    @staticmethod
    def get_file_info(file_path: str) -> dict:
        """获取文件信息
        Args:
            file_path: 文件路径
        Returns:
            dict: 文件信息
        """
        try:
            _var_var_2 = os.stat(file_path)
            return {
                'size': _var_var_2.st_size,
                'created_time': _var_var_2.st_ctime,
                'modified_time': _var_var_2.st_mtime
            }
        except Exception:
            return {}

    @staticmethod
    def exists(path: str) -> bool:
        """判断文件或目录是否存在"""
        return os.path.exists(path)

    @staticmethod
    def is_file(path: str) -> bool:
        """判断是否是文件
        Args:
            path: 路径
        Returns:
            bool: 是否是文件
        """
        return os.path.isfile(path)
    @staticmethod
    def is_dir(path: str) -> bool:
        """判断是否是目录
        Args:
            path: 路径
        Returns:
            bool: 是否是目录
        """
        return os.path.isdir(path)

if __name__ == '__main__':
    print(MFileUtil.get_file_info('D:/test.txt'))

