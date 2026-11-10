# File: task_msg.py (Cleaned & Decompiled)
from app.services.msg_service import MsgService
from app.utils.mexception import MExcUtils

def subscribe_task(item):
    try:
        MsgService().subscribe_task(item)
    except Exception as _var_var_0:
        MExcUtils.log(_var_var_0)

def search_task(item):
    try:
        MsgService().search_task(item)
    except Exception as _var_var_0:
        MExcUtils.log(_var_var_0)

def subscribe_delete(item):
    try:
        MsgService().subscribe_delete(item)
    except Exception as _var_var_0:
        MExcUtils.log(_var_var_0)

def tmdb_task(item):
    try:
        MsgService().tmdb_task(item)
    except Exception as _var_var_0:
        MExcUtils.log(_var_var_0)