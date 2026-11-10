# File: mask.py (Cleaned & Decompiled)
import re

class MarkUtils:
    @staticmethod
    def smart_mask(s: str, mask_char: str = '*') -> str:
        """
        自动识别字符串类型并脱敏
        支持：手机号 / 身份证 / 邮箱 / 银行卡 / 普通字符串
        """
        if not isinstance(s, str):
            return s
        s = s.strip()
        if not s:
            return s
        if re.fullmatch(r'1[3-9]\d{9}', s):
            return s[:3] + mask_char * 4 + s[-4:]
        if re.fullmatch(r'\d{15}|\d{17}[\dXx]', s):
            return s[:6] + mask_char * 8 + s[-4:]
        if '@' in s:
            _var_var_0 = s.find('@')
            _var_var_1 = s[:_var_var_0]
            _var_var_2 = s[_var_var_0:]
            if len(_var_var_1) <= 2:
                return mask_char + _var_var_2
            return _var_var_1[0] + mask_char * (len(_var_var_1) - 2) + _var_var_1[-1] + _var_var_2
        if re.fullmatch(r'\d{12,21}', s):
            return s[:4] + mask_char * (len(s) - 8) + s[-4:]
        if len(s) <= 2:
            return s[0] + mask_char
        if len(s) <= 4:
            return s[0] + mask_char + s[-1]
        return s[:2] + mask_char * 3 + s[-2:]