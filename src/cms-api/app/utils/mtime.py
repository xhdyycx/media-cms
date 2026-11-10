# File: mtime.py (Cleaned & Decompiled)
import re
from datetime import datetime, timezone, timedelta
from app.log import logger

class TimeUtils:
    @staticmethod
    def to_timestamp(date_input) -> int:
        """
        将日期时间字符串转换为秒级时间戳（Unix 时间戳）
        date_str (str): 日期时间字符串，格式为 'YYYY-MM-DD HH:MM:SS'
        """
        if isinstance(date_input, int):
            return date_input
        if isinstance(date_input, str):
            _var_var_0 = datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
        elif isinstance(date_input, datetime):
            _var_var_0 = date_input
        else:
            raise TypeError
        _var_var_1 = int(_var_var_0.timestamp())
        return _var_var_1

    @staticmethod
    def get_current_time_str() -> str:
        """
        获取当前时间，并格式化为 %Y-%m-%d %H:%M:%S（东八区）

        Returns:
            str: 格式化的时间字符串，格式为 'YYYY-MM-DD HH:MM:SS'
        """
        _var_var_2 = timezone(timedelta(hours=8))
        _var_var_3 = datetime.now(_var_var_2)
        return _var_var_3.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def parse_time_to_timestamp(time_str):
        """
        统一解析三种时间格式为时间戳（秒级）
        支持：时间戳数字、2025-02-24 17:56:29、2025-02-24 17:56:45 +0800 CST
        """
        try:
            time_str = str(time_str).strip()
            if time_str.isdigit():
                return int(time_str)
            time_str = re.sub(r'[+-]\d+.*$', '', time_str).strip()
            _var_var_0 = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            return int(_var_var_0.timestamp())
        except Exception as _var_var_4:
            logger.error(f'时间解析失败: {time_str}, 错误: {str(_var_var_4)}')
            return 0