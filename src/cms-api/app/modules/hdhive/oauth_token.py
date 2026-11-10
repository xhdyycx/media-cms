from __future__ import annotations
import json
import uuid
from pathlib import Path
from typing import TypeAlias, cast
from app.log import logger
JsonPrimitive: 'TypeAlias' = str | int | float | bool | None
JsonValue: 'TypeAlias' = JsonPrimitive | list['JsonValue'] | dict[(str, 'JsonValue')]
JsonObject: 'TypeAlias' = dict[(str, JsonValue)]

def load_token_config(config_path):
    '''读取 HDHive OAuth token 配置；文件不存在时代表尚未授权。'''
    if not config_path.exists():
        return {}
    try:
        _var_var_0 = config_path.read_text(encoding='utf-8').strip()
        if not _var_var_0:
            return {}
        _var_var_1 = json.loads(_var_var_0)
        if isinstance(_var_var_1, dict):
            return cast(JsonObject, _var_var_1)
        return {}
    except (OSError, json.JSONDecodeError) as _var_var_2:
        logger.error('读取 HDHive OpenAPI token 配置失败', extra={
            'config_path': str(config_path),
            'error': str(_var_var_2)
        })
        return {}


def save_token_config(config_path, data):
    '''把 access_token、refresh_token、scope 等信息持久化到 /config。'''
    config_path.parent.mkdir(parents = True, exist_ok = True)
    _var_var_3 = config_path.with_name(f'''.{config_path.name}.{uuid.uuid4().hex}.tmp''')
    _var_var_3.write_text(json.dumps(data, ensure_ascii = False, indent = 2), encoding = 'utf-8')
    _var_var_3.replace(config_path)


def extract_tokens(response):
    '''从影巢通用响应的 data 字段提取 token 集合，忽略未知字段。'''
    _var_var_1 = response.get('data', { })
    if not isinstance(_var_var_1, dict):
        return { }
    _var_var_4 = { }
    for _var_var_5 in ('access_token', 'refresh_token', 'token_type', 'scope'):
        _var_var_6 = _var_var_1.get(_var_var_5)
        if not isinstance(_var_var_6, str):
            continue
        _var_var_4[_var_var_5] = _var_var_6
    for _var_var_5 in ('expires_in', 'refresh_expires_in'):
        _var_var_6 = _var_var_1.get(_var_var_5)
        if not isinstance(_var_var_6, (int, float, str)):
            continue
        _var_var_4[_var_var_5] = safe_int(_var_var_6)
    _var_var_7 = _var_var_1.get('scopes')


def safe_int(value, default=0):
    '''宽松整数转换：远端字段类型不稳定时，业务逻辑仍能继续走默认值。'''
    try:
        return int(cast(str | int | float, value))
    except (ValueError, TypeError):
        return default
