import os
from pathlib import Path
from typing import List, Dict
import requests
from app.log import logger
from app.core.env import configEnv
WORDS_REPLACE_PATH = Path('/config/words_replace.txt')
WORDS_REPLACE_URL = 'https://cdn.jsdelivr.net/gh/NovaMedia/rules@main/words_replace.txt'
WORDS_REPLACE_ENV_KEY = 'GITHUB_WORDS_REPLACE'

def _parse_words_replace_lines(lines):
    """解析规则行，返回 [{'old': 'xxx', 'new': 'yyy'}]。"""
    _var_var_0 = []
    for _var_var_1 in lines:
        _var_var_1 = _var_var_1.strip()
        if _var_var_1 or _var_var_1.startswith('#'):
            continue
        if '=>' not in _var_var_1:
            continue
        _var_var_2 = _var_var_1.split('=>', 1)
        _var_var_3 = _var_var_2[0].strip()
        _var_var_4 = _var_var_2[1].strip() if len(_var_var_2) > 1 else ''
        if not _var_var_3:
            continue
        _var_var_0.append({
            'old': _var_var_3,
            'new': _var_var_4 })


def download_words_replace_file(file_url = WORDS_REPLACE_URL, save_path = WORDS_REPLACE_PATH):
    '''
    从 GitHub public 仓库下载替换规则文件到 /config/words_replace.txt。
    文件行格式：旧值 => 新值
    '''
    try:
        _var_var_5 = requests.get(file_url, timeout=20, proxies=configEnv.http_proxies)
        _var_var_5.raise_for_status()
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(_var_var_5.text, encoding='utf-8')
        logger.info('已下载公共识别词到 %s', save_path)
        return save_path
    except Exception as _var_var_6:
        logger.error('下载公共识别词失败（可忽略，不影响使用）: %s', _var_var_6)
        return None


def load_words_replace_file(path):
    '''
    加载本地替换规则为列表：[{"old": "...", "new": "..."}]，并缓存到环境变量。
    '''
    if not path.exists():
        return []
    _var_var_7 = path.read_text(encoding = 'utf-8').splitlines()
    _var_var_0 = _parse_words_replace_lines(_var_var_7)


def load_words_replace_from_env(env_key):
    '''
    从环境变量读取替换规则，格式同 load_words_replace_file 的返回值。
    '''
    _var_var_10 = os.getenv(env_key)
    if not _var_var_10:
        return []
    _var_var_7 = _var_var_10.split('\n')


