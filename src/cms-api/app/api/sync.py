# File: sync.py (Cleaned & Decompiled)
from blacksheep import json, Request
from blacksheep.server.controllers import APIController, get, post
from blacksheep.server.authorization import auth
from app.core.env import configEnv, novaEnv
from app.core.task import (
    alist_sync_task, full_sync_task, lift_sync_task, auto_tidy_task,
    share115_sync_task, common_sync_path_task, common_tidy_media_dir_task
)
from app.db import get_db
from app.db.config_op import ConfigOp
from app.log import logger
from app.scheduler import Scheduler, MTask
from app.utils.mjson import JsonUtils

class SyncController(APIController):

    @classmethod
    def route(cls):
        return '/api/sync'

    @get('lift')
    @auth('login')
    def lift_sync_api(self):
        Scheduler().add_once_job(MTask('lift_sync_one', '增量同步一次', lift_sync_task))
        return json({'code': 200, 'msg': '创建任务成功-增量同步一次-请注意日志打印'})

    @get('lift_by_token')
    def lift_by_token(self, request: Request):
        _var_var_0 = request.query.get('token')
        if not _var_var_0:
            return json({'code': '400', 'message': 'token不能为空'})
        _var_var_0 = _var_var_0[0]
        if _var_var_0 != novaEnv.NOVA_API_TOKEN:
            return json({'code': '400', 'message': 'token错误'})
        _var_var_1 = request.query.get('type')
        if not _var_var_1:
            _var_var_1 = 'lift_sync'
        else:
            _var_var_1 = _var_var_1[0]
        if _var_var_1 == 'lift_sync':
            Scheduler().add_once_job(MTask('lift_sync_one', '增量同步一次', lift_sync_task))
        elif _var_var_1 == 'auto_organize':
            Scheduler().add_once_job(MTask('auto_organize_once', '自动整理一次', auto_tidy_task))
        else:
            return json({'code': '400', 'message': 'type错误'})
        return json({'code': 200, 'msg': '创建任务成功-增量同步一次-请注意日志打印'})

    @get('auto_organize')
    @auth('login')
    def auto_organize_once(self):
        Scheduler().add_once_job(MTask('auto_organize_once', '自动整理一次', auto_tidy_task))
        return json({'code': 200, 'msg': '创建任务成功-自动整理一次-请注意日志打印'})

    @get('full')
    @auth('login')
    def full_sync_api(self, sync_types):
        if sync_types:
            _var_var_2 = sync_types[0]
        else:
            _var_var_2 = 'video'
        _var_var_3 = configEnv.media_115_cid
        _var_var_4 = configEnv.local_path
        if not _var_var_3:
            return json({'code': 400, 'msg': '115媒体库cid为空，点保存了吗？'})
        Scheduler().add_once_job(MTask('full_sync_task_once', '全量同步一次', full_sync_task, [_var_var_3, _var_var_4, _var_var_2]))
        return json({'code': 200, 'msg': '创建任务成功-全量同步一次-请注意日志打印'})

    @get('get_all_jobs')
    def get_all_jobs_api(self):
        _var_var_5 = Scheduler().get_all_jobs()
        job_list = []
        for j in _var_var_5:
            job_list.append({
                'id': getattr(j, 'id', str(j)),
                'name': getattr(j, 'name', str(j)),
                'trigger': str(getattr(j, 'trigger', 'interval')),
                'next_run_time': str(getattr(j, 'next_run_time', '')) if getattr(j, 'next_run_time', None) else ''
            })
        return json({'code': 200, 'data': job_list, 'msg': 'ok'})
    @get('start_job/{task_id}')
    def start_job_api(self, task_id):
        Scheduler().start_job_async(task_id)
        return 'ok'

    @post('alist')
    @auth('login')
    def alist_sync_api(self, params: dict):
        _var_var_4 = params.get('paths', [])
        if not _var_var_4:
            return json({'code': 400, 'msg': '路径不能为空'})
        _var_var_7 = JsonUtils.to_str(_var_var_4)
        Scheduler().add_once_job(MTask('alist_sync_task_once', 'alist同步一次', alist_sync_task, [_var_var_7]))
        return json({'code': 200, 'msg': '创建任务成功-alist同步一次-请注意日志打印'})

    @post('share115')
    @auth('login')
    def share115_sync_api(self, params: dict):
        Scheduler().add_once_job(MTask('share115_sync_task_once', '115分享同步一次', share115_sync_task, [params]))
        return json({'code': 200, 'msg': '创建任务成功-115分享同步一次-请注意日志打印'})

    @get('full_sync')
    @auth('login')
    def full_sync(self, sync_type):
        if sync_type and sync_type[0] == '123':
            Scheduler().add_once_job(MTask('common_sync_path_task_once', '全量同步123一次', common_sync_path_task, [{'a': '1'}]))
            return json({'code': 200, 'msg': '创建任务成功-全量同步123一次-请注意日志打印'})
        return json({'code': 400, 'msg': '创建任务失败-请查看日志打印'})

    @get('auto_tidy_up')
    @auth('login')
    def auto_tidy_up(self, tidy_type):
        tidy_type = tidy_type[0]
        Scheduler().add_once_job(MTask(f'common_tidy_media_dir_task_once_{tidy_type}', f'自动整理{tidy_type}一次', common_tidy_media_dir_task, [{'tidy_type': tidy_type}]))
        return json({'code': 200, 'msg': f'创建任务成功-自动整理{tidy_type}一次-请注意日志打印'})