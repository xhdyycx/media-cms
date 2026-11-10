import sqlite3
from blacksheep import json
from blacksheep.server.authorization import auth
from blacksheep.server.controllers import APIController, post
from app.core.env import novaEnv, configEnv
from app.core.task import cover_gen_task, del_115_dir_task, del_115_recycle_task, del_aliyun_dir_task, del_aliyun_recycle_task, del_123_dir_task, del_123_recycle_task, hdhive_checkin_task
from app.scheduler import Scheduler
from app.utils.mjson import JsonUtils
from app.utils.strm_util import STRMUtils

class PluginController(APIController):
    @classmethod
    def route(cls):
        return '/api/plugin'
    @post('/sql_exec')
    @auth('login')
    async def sql_exec(self, params: dict):
        _var_var_0 = params.get('sql')
        try:
            with sqlite3.connect(novaEnv.SQL_PATH) as _var_var_1:
                _var_var_1.row_factory = sqlite3.Row
                _var_var_2 = _var_var_1.cursor()
                _var_var_2.execute(_var_var_0)
                if _var_var_0.strip().upper().startswith('SELECT'):
                    _var_var_3 = _var_var_2.fetchall()
                    return json({'code': 200, 'data': [dict(_var_var_4) for _var_var_4 in _var_var_3]})
                _var_var_5 = _var_var_2.rowcount
                _var_var_1.commit()
                return json({'code': 200, 'data': _var_var_5})
        except sqlite3.Error as _var_var_6:
            return json({'code': 400, 'msg': f'数据库错误: {str(_var_var_6)}'})
        except Exception as _var_var_6:
            return json({'code': 400, 'msg': f'执行SQL时发生错误: {str(_var_var_6)}'})
    @post('/run')
    @auth('login')
    async def run(self, payload: dict):
        _var_var_7 = '未指定任务'
        _var_var_8 = payload.get('func')
        if _var_var_8 == 'E_115_DIR_DEL':
            _var_var_7 = del_115_dir_task()
        elif _var_var_8 == 'E_115_RECYCLE_DEL':
            _var_var_7 = del_115_recycle_task()
        elif _var_var_8 == 'E_123_DIR_DEL':
            _var_var_7 = del_123_dir_task()
        elif _var_var_8 == 'E_123_RECYCLE_DEL':
            _var_var_7 = del_123_recycle_task()
        elif _var_var_8 == 'E_ALIYUN_DIR_DEL':
            _var_var_7 = del_aliyun_dir_task()
        elif _var_var_8 == 'E_ALIYUN_RECYCLE_DEL':
            _var_var_7 = del_aliyun_recycle_task()
        elif _var_var_8 == 'E_STRM_REPLACE':
            _var_var_7 = STRMUtils.replace_in_strm_files(configEnv.e_strm_replace_path, configEnv.e_strm_replace_old, configEnv.e_strm_replace_new, True)
        elif _var_var_8 == 'E_COVER_GEN':
            Scheduler().add_one_job(_id='cover_gen_task_one', name='媒体库封面生成任务-一次', func=cover_gen_task, seconds=3)
            _var_var_7 = '媒体库封面生成一次-请注意日志查看进度'
        elif _var_var_8 == 'E_HDHIVE_CHECKIN':
            Scheduler().add_one_job(_id='t_hdhive_checkin_one', name='RE0签到-一次', func=hdhive_checkin_task, seconds=3)
            _var_var_7 = 'RE0签到-请注意日志查看进度'
        return json({'code': 200, 'msg': _var_var_7})
