from app.log import logger
from app.utils.m115_util import M115Utils
from app.utils.mjson import JsonUtils
from app.utils.mutil import Mutil
from app.utils.ko_util import change_file_suffix, chunk_list, join_cloud_paths
from app.schemas.types import ActionEnum
from app.core.m115_config import M115Config
from p115client import P115Client, check_response, SUFFIX_TO_TYPE
import time

class M115B:
    '''
    115相关操作
    '''
    
    def __init__(self, client, use_open, request_sleep):
        self._M115B__client = client
        self._M115B__use_open = use_open if use_open else (lambda : False)
        self._M115B__request_sleep = request_sleep if request_sleep else (lambda : None)
        self._M115B__app = 'ios'

    
    def fs_delete(self, fid):
        self.__request_sleep()
        if self.__use_open():
            result = self.__client.fs_delete_open(fid, **M115Config.get_ios_ua_app())
            logger.info(f'115.fs_delete_open.resp={JsonUtils.to_str(result)}')
        else:
            result = self.__client.fs_delete_app(fid, **M115Config.get_ios_ua_app())
            logger.info(f'115.fs_delete_app.resp={JsonUtils.to_str(result)}')
        return result
    def fs_delete_chunk(self, fids):
        _var_var_1 = list(chunk_list(fids, 1000))
        for _var_var_2, _var_var_3 in enumerate(_var_var_1):
            _var_var_0 = self.fs_delete(','.join(_var_var_3))
            logger.info(f'''fs_delete.resp={JsonUtils.to_str(_var_var_0)}''')
            if not _var_var_2 < len(_var_var_1) - 1:
                continue
            time.sleep(3)
        return None
        return None

    
    def del_dir(self, cid, days):
        days = int(days)
        page_size = 1150
        payload = {'offset': 0, 'limit': page_size, 'cid': cid}
        fids = []
        while True:
            resp = self.fs_files_app(payload, use_open=self.__use_open())
            if not resp or not resp['state'] or len(resp['paths']) == 1:
                logger.error(f'获取文件夹内容失败, cid好像是错误的, resp={JsonUtils.to_str(resp)}')
                return {'code': '400', 'msg': '获取文件夹内容失败, cid好像是错误的'}
            cutoff = time.time() - days * 24 * 60 * 60
            fids.extend(x['fid'] for x in resp['data'] if int(x['update_time']) <= cutoff)
            if resp['offset'] + resp['limit'] >= resp['count']:
                break
            payload['offset'] += page_size
            time.sleep(3)
        if not fids:
            logger.info(f'没有需要删除的文件夹内容-{cid}-保留{days}天')
            return {'code': '201', 'msg': '没有需要删除的文件夹内容'}
        self.fs_delete_chunk(fids)
        logger.info(f'文件夹内容删除成功-{cid}-保留{days}天')
        return {'code': '200', 'msg': '文件夹内容删除成功'}

    
    def recyclebin_clean_chunk(self, ids):
        chunks = list(chunk_list(ids, 1000))
        for index, chunk in enumerate(chunks):
            if self.__use_open():
                resp = self.__client.recyclebin_clean_open(chunk, **M115Config.get_ios_ua_app())
                logger.info(f'recyclebin_clean_open resp={JsonUtils.to_str(resp)}')
            else:
                resp = self.__client.recyclebin_clean_app(chunk, **M115Config.get_ios_ua_app())
                logger.info(f'recyclebin_clean_app resp={JsonUtils.to_str(resp)}')
            if index < len(chunks) - 1:
                time.sleep(3)
    def recyclebin_clean(self, days):
        days = int(days)
        page_size = 1150
        payload = {'offset': 0, 'limit': page_size}
        ids = []
        while True:
            resp = self.recyclebin_list(payload)
            if not resp['state']:
                logger.error(f'获取回收站文件失败-{JsonUtils.to_str(resp)}')
                return {'code': '400', 'msg': f'获取回收站文件失败-{JsonUtils.to_str(resp)}'}
            if not resp.get('data'):
                logger.info('回收站为空')
                return {'code': '201', 'msg': '回收站为空'}
            cutoff = int(time.time()) - days * 24 * 60 * 60
            ids.extend(x['id'] for x in resp['data'] if int(x['dtime']) <= cutoff)
            if resp['offset'] + resp['page_size'] >= int(resp['count']):
                break
            payload['offset'] += page_size
            time.sleep(3)
        if not ids:
            logger.info(f'没有需要删除的回收站文件-保留{days}天')
            return {'code': '201', 'msg': '没有需要删除的回收站文件'}
        self.recyclebin_clean_chunk(ids)
        logger.info(f'回收站文件删除成功-保留{days}天')
        return {'code': '200', 'msg': '回收站文件删除成功'}

    
    def recyclebin_list(self, payload):
        if not self.__use_open():
            resp = self.__client.recyclebin_list_app(payload, **M115Config.get_ios_ua_app())
            logger.info(f'recyclebin_list_app resp={JsonUtils.to_str(resp)}')
            return resp
        resp = self.__client.recyclebin_list_open(payload, **M115Config.get_ios_ua_app())
        logger.info(f'recyclebin_list_open resp={JsonUtils.to_str(resp)}')
        if not resp['state']:
            return resp
        reserved = {'count', 'limit', 'offset', 'rb_pass'}
        data = resp['data']
        resp.update({'offset': data['offset'], 'page_size': data['limit'], 'count': data['count'], 'rb_pass': data['rb_pass'], 'data': [v for k, v in data.items() if k not in reserved]})
        return resp
    def fs_files_app(self, payload, sleep=None, use_open=False):
        if sleep:
            sleep_sec = float(sleep)
            logger.info(f'115API暂停{sleep_sec}s...')
            time.sleep(sleep_sec)
        out = {}
        if use_open:
            result = self.__client.fs_files_open(payload, **M115Config.get_ios_ua_app())
        else:
            result = self.__client.fs_files_app(payload, **M115Config.get_ios_ua_app())
        if not result['state']:
            logger.error(f'获取文件列表失败 - {JsonUtils.to_str(result)}')
            return None
        out['state'] = result['state']
        out['count'] = int(result['count'])
        out['offset'] = int(result['offset'])
        out['limit'] = int(result['limit'])
        entries = []
        parent_name = result['path'][-1]['name']
        for item in result['data']:
            is_dir = False if item.get('sha1') else True
            thumb = item.get('thumb', '')
            if thumb and thumb.startswith('http://thumb.115.com'):
                thumb = f'?{thumb.split("?")[1]}'
            if thumb and thumb.startswith('?'):
                thumb = f'https://imgjump.115.com{thumb}&size=0&sha1={item.get("sha1", "")}'
            entries.append({'is_dir': is_dir, 'fid': item['fid'], 'pid': item['pid'], 'name': item['fn'], 'p_name': parent_name, 'size': item.get('fs', 0), 'pick_code': item['pc'], 'sha1': item.get('sha1', ''), 'update_time': item['upt'], 'ico': item.get('ico', ''), 'thumb': thumb})
        out['data'] = entries
        paths = []
        for item in result['path']:
            paths.append({'fid': item['cid'], 'pid': item['pid'], 'name': '根目录' if item['cid'] == 0 else item['name']})
        out['paths'] = paths
        return out
    def iter_all_dirs_v2(self, cid, local_path, func):
        _var_var_20 = self.download_folders_app_and_path(cid)
        _var_var_21 = [
            _var_var_20['data']['root']]
        _var_var_21.extend(_var_var_20['data']['list'])
        for _var_var_8 in _var_var_21:
            if not M115Utils.check_path(_var_var_8):
                continue
            _var_var_22 = {
                'is_dir': True,
                'id': int(_var_var_8['fid']),
                'parent_id': _var_var_8['pid'],
                'name': _var_var_8['fn'],
                'path': _var_var_8['path'],
                'p_name': _var_var_8['p_name'],
                'utime': int(time.time()),
                'status': 1,
                'local_name': _var_var_8['fn'],
                'local_path': Mutil.get_dirname(join_cloud_paths(local_path, _var_var_8['path'])),
                'action': ActionEnum.DIR.name }
            func(cid, _var_var_22)
        return None
        return None

    
    def get_all_dirs_and_path(self, cid):
        _var_var_20 = self.download_folders_app_and_path(cid)
        _var_var_21 = [
            _var_var_20['data']['root']]
        _var_var_21.extend(_var_var_20['data']['list'])
        _var_var_23 = []
        for _var_var_8 in _var_var_21:
            _var_var_23.append({
                'is_dir': True,
                'fid': _var_var_8['fid'],
                'pid': _var_var_8['pid'],
                'name': _var_var_8['fn'],
                'size': 0,
                'pick_code': self._M115B__client.to_pickcode(_var_var_8['fid']),
                'sha1': '',
                'update_time': int(time.time()),
                'ico': '',
                'thumb': '',
                'p_name': _var_var_8['p_name'],
                'path': _var_var_8['path'] })
        return _var_var_23
        return None

    
    def iter_files_with_path_kk(self, cid, video_suffix, img_suffix, nfo_suffix, local_path, func):
        _var_var_24 = video_suffix + img_suffix + nfo_suffix
        _var_var_25 = set()
        for _var_var_26 in _var_var_24:
            _var_var_27 = SUFFIX_TO_TYPE.get('.' + _var_var_26, 0)
            _var_var_25.add(_var_var_27)
        _var_var_28 = None
        if len(_var_var_25) == 1:
            _var_var_28 = list(_var_var_25)[0]
        _var_var_29 = self.get_files_and_dirs_with_path(cid, _var_var_28)
        for _var_var_8 in _var_var_29:
            _var_var_22 = {
                'is_dir': _var_var_8['is_dir'],
                'id': int(_var_var_8['fid']),
                'parent_id': _var_var_8['pid'],
                'name': _var_var_8['name'],
                'sha1': _var_var_8['sha1'],
                'size': _var_var_8['size'],
                'path': _var_var_8['path'],
                'p_name': _var_var_8['p_name'],
                'utime': _var_var_8['update_time'],
                'pick_code': _var_var_8['pick_code'],
                'thumb': _var_var_8['thumb'],
                'ico': _var_var_8['ico'],
                'local_name': _var_var_8['name'],
                'local_path': Mutil.get_dirname(join_cloud_paths(local_path, _var_var_8['path'])) }
            if _var_var_22['is_dir']:
                _var_var_22['action'] = ActionEnum.DIR.name
                _var_var_22['status'] = 1
                func(cid, _var_var_22)
                continue
            _var_var_26 = _var_var_22['ico']
            if _var_var_26 not in _var_var_24:
                logger.info(f'''跳过处理 {_var_var_26} 文件：{_var_var_22['path']}''')
                continue
            if _var_var_26 in video_suffix:
                _var_var_22['action'] = ActionEnum.STRM.name
                _var_var_22['local_name'] = change_file_suffix(_var_var_22['name'], 'strm')
                _var_var_22['status'] = 1
            elif _var_var_26 in img_suffix:
                _var_var_22['action'] = ActionEnum.IMG.name
                _var_var_22['status'] = 0
            elif _var_var_26 in nfo_suffix:
                _var_var_22['action'] = ActionEnum.DOWN.name
                _var_var_22['status'] = 0
            else:
                _var_var_22['action'] = ActionEnum.UNKNOWN.name
                _var_var_22['status'] = 1
            func(cid, _var_var_22)
        return None
        return None

    @staticmethod
    def fill_all_path(data):
        _var_var_30 = {}
        _var_var_31 = data['root']
        _var_var_30[_var_var_31['fid']] = {'path': _var_var_31['path'], 'fn': _var_var_31['fn']}
        _var_var_32 = data['list']
        _var_var_33 = True
        while _var_var_33:
            _var_var_33 = False
            for _var_var_8 in _var_var_32:
                if 'path' in _var_var_8 and 'p_name' in _var_var_8:
                    continue
                _var_var_34 = _var_var_8['pid']
                if _var_var_34 in _var_var_30:
                    _var_var_35 = _var_var_30[_var_var_34]
                    _var_var_36 = f"{_var_var_35['path']}/{_var_var_8['fn']}"
                    _var_var_8['path'] = _var_var_36
                    _var_var_8['p_name'] = _var_var_35['fn']
                    _var_var_30[_var_var_8['fid']] = {'path': _var_var_36, 'fn': _var_var_8['fn']}
                    _var_var_33 = True
        return data
    
    def _download_folders_app(self, cid, page):
        _var_var_37 = self._M115B__client.to_pickcode(cid)
        _var_var_38 = self._M115B__client.download_folders_app({
            'pickcode': _var_var_37,
            'page': page,
            'per_page': 5000 }, app = self._M115B__app, timeout = M115Config.REQUEST_TIMEOUT)
        check_response(_var_var_38)
        return _var_var_38
        return None

    
    def download_folders_app_all(self, cid):
        _var_var_23 = []
        _var_var_39 = 1
        while True:
            logger.info('获取第 %s 页目录', _var_var_39)
            _var_var_38 = self._download_folders_app(cid, _var_var_39)
            _var_var_23.extend(_var_var_38['data']['list'])
            if _var_var_38['data']['has_next_page']:
                _var_var_39 += 1
                time.sleep(3)
            else:
                _var_var_38['data']['list'] = _var_var_23
                _var_var_40 = _var_var_38['data']
                _var_var_40['root']['path'] = f'''/{_var_var_38['data']['root']['fn']}'''
                _var_var_40['root']['p_name'] = ''
                _var_var_40['root']['pid'] = ''
                _var_var_38['data'] = self.fill_all_path(_var_var_40)
                return _var_var_38

    
    def _get_all_file(self, cid, _type, offset):
        _var_var_6 = {
            'offset': offset,
            'limit': 5000,
            'cid': cid,
            'o': 'user_utime',
            'asc': 1,
            'cur': 0,
            'show_dir': 0 }
        if _type:
            _var_var_6['type'] = _type
        _var_var_38 = self._M115B__client.fs_files_app(_var_var_6, app = self._M115B__app, timeout = M115Config.REQUEST_TIMEOUT)
        check_response(_var_var_38)
        return _var_var_38
        return None

    
    def get_all_file(self, cid, _type):
        _var_var_40 = []
        _var_var_41 = 0
        _var_var_39 = 1
        _var_var_42 = '?'
        while True:
            logger.info(f'''获取第 {_var_var_39} 页文件 {_var_var_41}/{_var_var_42}''')
            _var_var_38 = self._get_all_file(cid, _type, _var_var_41)
            for _var_var_8 in _var_var_38['data']:
                _var_var_22 = {
                    'is_dir': 0 if _var_var_8.get('sha1') else 1,
                    'fid': _var_var_8['fid'],
                    'pid': _var_var_8['pid'],
                    'name': _var_var_8['fn'],
                    'size': int(_var_var_8.get('fs', '0')),
                    'pick_code': _var_var_8['pc'],
                    'sha1': _var_var_8.get('sha1', ''),
                    'update_time': _var_var_8['upt'],
                    'ico': _var_var_8.get('ico', ''),
                    'thumb': '' }
                _var_var_18 = _var_var_8.get('thumb')
                if _var_var_18 and _var_var_18.startswith('?'):
                    _var_var_18 = f'''https://imgjump.115.com{_var_var_18}&size=0&sha1={_var_var_8['sha1']}'''
                    _var_var_22['thumb'] = _var_var_18
                _var_var_40.append(_var_var_22)
            _var_var_42 = _var_var_38['count']
            if _var_var_42 > _var_var_41 + _var_var_38['limit']:
                _var_var_39 += 1
                _var_var_41 += _var_var_38['limit']
                time.sleep(3)
            else:
                _var_var_38['data'] = _var_var_40
                return _var_var_38

    
    def get_all_file_and_path(self, cid, _type):
        _var_var_43 = self.get_all_file(cid, _type)
        _var_var_44 = _var_var_43['data']
        if not _var_var_44:
            return []
        if len(_var_var_43['path']) < 2:
            logger.error(f'''请确认 cid = {cid} 是否正确''')
            return []
        _var_var_45 = ''
        for _var_var_46, _var_var_8 in enumerate(_var_var_43['path']):
            if _var_var_46 == len(_var_var_43['path']) - 1 or _var_var_8['cid'] == 0:
                continue
            _var_var_45 = f'''{_var_var_45}/{_var_var_8['name']}'''
        _var_var_20 = self.download_folders_app_all(cid)
        _var_var_20['data']['root']['pid'] = _var_var_43['path'][-2]['cid']
        _var_var_20['data']['root']['p_name'] = _var_var_43['path'][-2]['name']
        _var_var_47 = {
            _var_var_20['data']['root']['fid']: _var_var_20['data']['root'] }
        for _var_var_8 in _var_var_20['data']['list']:
            if not _var_var_8.get('path'):
                continue
            _var_var_47[_var_var_8['fid']] = _var_var_8
        _var_var_48 = []
        for _var_var_8 in _var_var_44:
            _var_var_49 = _var_var_47.get(_var_var_8['pid'])
            if not _var_var_49:
                continue
            _var_var_8['path'] = f'''{_var_var_45}{_var_var_49['path']}/{_var_var_8['name']}'''
            _var_var_8['p_name'] = _var_var_49['p_name']
            _var_var_48.append(_var_var_8)
        return _var_var_48
        return None

    
    def get_files_and_dirs_with_path(self, cid, _type):
        _var_var_38 = []
        _var_var_50 = self.get_all_dirs_and_path(cid)
        _var_var_47 = { }
        for _var_var_8 in _var_var_50:
            _var_var_38.append(_var_var_8)
            _var_var_47[_var_var_8['fid']] = _var_var_8
        _var_var_43 = self.get_all_file(cid, _type)
        _var_var_44 = _var_var_43['data']
        for _var_var_8 in _var_var_44:
            _var_var_49 = _var_var_47.get(_var_var_8['pid'])
            if not _var_var_49:
                continue
            _var_var_8['path'] = f'''{_var_var_49['path']}/{_var_var_8['name']}'''
            _var_var_8['p_name'] = _var_var_49['p_name']
            _var_var_38.append(_var_var_8)
        return _var_var_38
        return None

    
    def download_folders_app_and_path(self, cid):
        _var_var_20 = self.download_folders_app_all(cid)
        _var_var_6 = {
            'offset': 0,
            'limit': 1,
            'cid': cid }
        _var_var_0 = self.fs_files_app(_var_var_6)
        _var_var_51 = ''
        for _var_var_46, _var_var_8 in enumerate(_var_var_0['paths']):
            if _var_var_46 == len(_var_var_0['paths']) - 1 and _var_var_8['fid'] == 0 or _var_var_8['name'] == '根目录':
                continue
            _var_var_51 = f'''{_var_var_51}/{_var_var_8['name']}'''
        _var_var_20['data']['root']['pid'] = _var_var_0['paths'][-2]['fid']
        _var_var_20['data']['root']['p_name'] = _var_var_0['paths'][-2]['name']
        if _var_var_51 != '' and _var_var_51 != '/':
            _var_var_20['data']['root']['path'] = f'''{_var_var_51}{_var_var_20['data']['root']['path']}'''
            for _var_var_8 in _var_var_20['data']['list']:
                _var_var_8['path'] = f'''{_var_var_51}{_var_var_8['path']}'''
        return _var_var_20
        return None

    
    def search_video(self, cid, offset, limit):
        payload = {'aid': 1, 'asc': 0, 'cid': cid, 'fc': 2, 'offset': offset, 'limit': limit, 'o': 'user_utime', 'type': 4, 'search_value': '.'}
        resp = self.__client.fs_search_app(payload, **M115Config.get_ios_ua_app())
        check_response(resp)
        if len(resp['data']) == 0:
            return resp
        folder = self.download_folders_app_all(cid)
        path_map = {folder['data']['root']['fid']: folder['data']['root']['path']}
        for item in folder['data']['list']:
            if not item.get('path'):
                continue
            path_map[item['fid']] = item['path']
        for item in resp['data']:
            parent = path_map.get(item['pid'])
            if not parent:
                continue
            item['path'] = f'{parent}/{item["fn"]}'
        return resp
    def search_video_all(self, cid):
        _var_var_53 = 10000
        _var_var_41 = 0
        _var_var_54 = []
        _var_var_5 = 1150
        while True:
            _var_var_14 = self.search_video(cid, _var_var_41, _var_var_5)
            _var_var_54.extend(_var_var_14['data'])
            if _var_var_14['count'] <= _var_var_14['offset'] + _var_var_14['page_size']:
                break
            if _var_var_53 <= _var_var_14['offset'] + _var_var_14['page_size']:
                break
            _var_var_41 += _var_var_14['page_size']
            if _var_var_41 + _var_var_5 > _var_var_53:
                _var_var_5 = _var_var_53 - _var_var_41
        return _var_var_54

    
    def get_auto_tidy_data_v2(self, cid, limit):
        logger.info(f'''开始获取 {cid} 目录下的视频文件...''')
        _var_var_14 = []
        for _var_var_8 in self.search_video_all(cid):
            if not M115Utils.check_path_v2(_var_var_8, cid):
                continue
            try:
                _var_var_16 = _var_var_8['path'].split('/')[-2]
                _var_var_14.append({
                    'is_dir': 0,
                    'fid': int(_var_var_8['fid']),
                    'pid': int(_var_var_8['pid']),
                    'name': _var_var_8['fn'],
                    'p_name': _var_var_16,
                    'size': int(_var_var_8.get('fs', 0)),
                    'pick_code': _var_var_8.get('pc') or _var_var_8.get('pick_code'),
                    'sha1': _var_var_8.get('sha1', ''),
                    'update_time': _var_var_8['upt'],
                    'ico': _var_var_8.get('ico', ''),
                    'thumb': _var_var_8.get('thumb', ''),
                    'path': _var_var_8['path'] })
            except Exception as _var_var_55:
                logger.exception(_var_var_55)
                logger.error(f'''视频数据获取异常 item={JsonUtils.to_str(_var_var_8)}''')
                continue
        return {
            'state': True,
            'count': len(_var_var_14),
            'data': _var_var_14 }

