from blacksheep import auth
from blacksheep.server.controllers import get, post
from blacksheep.server.controllers import APIController
from blacksheep.server.responses import json
from app.core.task_tidy import load_words_replace_file
from app.modules.media.media_util import MediaUtil
from app.modules.media.mp import MP
from app.modules.tmdb.category import CategoryUtil
from app.utils.partial_fstring import render

class MediaController(APIController):
    @classmethod
    def route(cls):
        return '/api/media'
    @post('format_name')
    async def format_name(self, data: dict):
        """格式化文件名"""
        _var_var_0 = data.get('template')
        _var_var_1 = data.get('media_data')
        if not _var_var_0 or not _var_var_1:
            return json({'code': 400, 'msg': '缺少参数'})
        _var_var_2 = render(_var_var_0, _var_var_1)
        return json({'code': 200, 'data': _var_var_2})
    @post('get_recognize_info')
    async def recognize_info_api(self, data: dict):
        """格式化文件名"""
        _var_var_0 = data.get('template')
        _var_var_2 = data.get('name')
        _var_var_3 = MP().get_recognize_info(_var_var_2, _var_var_2)
        return json({'code': 200, 'data': _var_var_3})
    @post('recognize_info_test')
    async def recognize_info_test(self, data: dict):
        """测试识别接口"""
        _var_var_4 = data.get('MP_API_DOMAIN')
        _var_var_5 = data.get('MP_API_TOKEN')
        _var_var_2 = data.get('name')
        if not _var_var_4 or not _var_var_5 or not _var_var_2:
            return json({'code': 400, 'msg': '缺少参数'})
        _var_var_3 = MP().recognize_file_api(_var_var_2, _var_var_4, _var_var_5)
        if not _var_var_3:
            return json({'code': 400, 'msg': '连接失败，请检查MP域名和令牌'})
        return json({'code': 200, 'msg': '连接成功', 'data': _var_var_3})
    @post('file_recognize')
    @auth('login')
    async def file_recognize(self, data: dict):
        """文件识别测试"""
        load_words_replace_file()
        _var_var_3 = MediaUtil(data.get('path')).recognize_info()
        print(_var_var_3)
        if _var_var_3['type'] == 'movie':
            _var_var_6 = CategoryUtil().get_movie_category(_var_var_3.get('tmdb_info'))
        else:
            _var_var_6 = CategoryUtil().get_tv_category(_var_var_3.get('tmdb_info'))
        _var_var_3['category'] = _var_var_6
        print(_var_var_3)
        return json({'code': 200, 'msg': '识别成功', 'data': _var_var_3})
