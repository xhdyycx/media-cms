from cachetools import TTLCache
from app.core.env import novaEnv, configEnv
from app.core.env2 import config2Env
from app.core.obj_factory import ObjFactory
from app.core.task import save_ali_share_task, auto_tidy_task
from app.db import get_db
from app.db.models.submedia import SubMedia
from app.db.sub_op import SubMediaOp, SubSourceOp
from app.log import logger
from app.modules.hdhive.hdhive import HDHive
from app.modules.hdhive.hdhive_proxy import HDHiveProxyClient
from app.modules.tg.tg_scraper import TelegramScraper
from app.modules.tmdb.tmdbapi import TmdbApi
from app.scheduler import Scheduler
from app.services.message_service import MessageService
from app.services.share_down import ShareDownService
from app.utils.mjson import JsonUtils
DATA_CACHE: TTLCache[(str, dict)] = TTLCache(100, ttl = 10800)

class MsgService:
    
    def __init__(self):
        '''初始化外部服务客户端与消息发送能力。'''
        self._tmdbApi = TmdbApi()
        self._message_service = MessageService()
        self._share_down_service = ShareDownService()
        self._hdHive = ObjFactory.get_instance(HDHiveProxyClient)

    @staticmethod
    def _build_cache_key(msg_type, userid, select_type = None):
        """根据消息类型、用户和可选选择器构建缓存键。"""
        if select_type:
            return f'{msg_type}_{select_type}_{userid}'
        return f'{msg_type}_{userid}'
    @staticmethod
    def _calc_page(cache_data, action):
        """按上一页/下一页动作计算分页边界内的目标页码。"""
        _var_var_0 = int(cache_data.get('page', 1))
        _var_var_1 = int(cache_data.get('total_pages', 1))
        if action == 'search_next_page':
            return min(_var_var_0 + 1, _var_var_1)
        if action == 'search_prev_page':
            return max(_var_var_0 - 1, 1)
        return 1
    @staticmethod
    def _save_cache(key, indexed_data, page=None, total_pages=None, **extra):
        """按 1..N 序号写入缓存，并附加分页与扩展字段。"""
        indexed = {i: item for i, item in enumerate(indexed_data, 1)}
        if page is not None:
            indexed['page'] = page
        if total_pages is not None:
            indexed['total_pages'] = total_pages
        indexed.update(extra)
        DATA_CACHE[key] = indexed
    
    def _build_image(self, *image_paths):
        '''按传参顺序选择首个可用图片路径并构建 TMDB 图片完整地址。'''
        _var_var_5 = next((_var_var_6 for _var_var_6 in image_paths if _var_var_6), None)
        if not _var_var_5:
            return None
        return self._tmdbApi.build_img_h632(_var_var_5)

    @staticmethod
    def _build_tmdb_cache_item(result):
        """把 TMDB 原始结果标准化为缓存结构。"""
        _var_var_7 = result.get('title') or result.get('name') or '未知标题'
        _var_var_8 = (result.get('release_date') or result.get('first_air_date') or '')[:4] or '未知'
        return {'tmdb_id': result.get('id'), 'media_type': result.get('media_type'), 'title': _var_var_7, 'year': _var_var_8, 'backdrop_path': result.get('backdrop_path'), 'poster_path': result.get('poster_path')}
    
    def _search_tmdb_media(self, name, page):
        """执行 TMDB 多类型搜索，并过滤 movie/tv。"""
        result = self._tmdbApi.search_multi(keywords=name, page=page)
        if not result or not result.get('results'):
            return (None, None)
        if isinstance(result, dict):
            results = result.get('results', [])
        else:
            results = getattr(result, 'results', None) or []
        items = [x for x in results if x.get('media_type') in {'tv', 'movie'}]
        items.sort(key=lambda x: x.get('vote_count', 0), reverse=True)
        return (items, result.get('total_pages', 1))
    def _transfer_share_link(self, link):
        '''对分享链接做去重入库并触发后续保存/整理任务。'''
        _var_var_13 = self._share_down_service.get_not_exist_share_down_link(link, False)
        if not _var_var_13.get('success'):
            return None
        _var_var_9 = self._share_down_service.add_share_down_impl(_var_var_13)
        if not _var_var_9.get('success'):
            return _var_var_9
        if _var_var_9.get('ali_links'):
            _var_var_14 = ','.join(_var_var_9.get('ali_links'))
            Scheduler().add_one_job(_id = 'save_ali_share_task', name = '保存阿里云盘分享', func = save_ali_share_task, kwargs = {
                'ali_links': _var_var_14,
                'tidy_type': 2 if _var_var_9['is_lift_sync'] else 3 }, seconds = 2)
        elif _var_var_9.get('is_lift_sync'):
            Scheduler().add_one_job(_id = 'auto_tidy_task', name = '自动整理', func = auto_tidy_task, seconds = 2)
        return _var_var_9

    
    def _build_tmdb_list_payload(self, results, msg_type, button_action):
        '''将 TMDB 结果组装为消息文本、图片、按钮与缓存行。'''
        _var_var_15 = []
        _var_var_16 = []
        _var_var_17 = []
        _var_var_18 = []
        for _var_var_2, _var_var_11 in enumerate(results, 1):
            _var_var_19 = self._build_tmdb_cache_item(_var_var_11)
            _var_var_18.append(_var_var_19)
            _var_var_20 = f'''{_var_var_2:02d}. {_var_var_19['title']} ({_var_var_19['year']})'''
            _var_var_15.append(_var_var_20)
            _var_var_5 = self._build_image(_var_var_19.get('poster_path'), _var_var_19.get('backdrop_path'))
            if _var_var_5:
                _var_var_16.append({
                    'image': _var_var_5,
                    'text': _var_var_20,
                    'url': f'''https://www.themoviedb.org/{_var_var_19['media_type']}/{_var_var_19['tmdb_id']}''' })
            _var_var_17.append({
                'k': f'''{_var_var_2}''',
                'v': f'''button={msg_type}={button_action}={_var_var_2}''' })
        return (_var_var_15, _var_var_16, _var_var_17, _var_var_18)

    
    def _resolve_paging_with_cache(self, action, key, userid, name, not_found_title, source = None):
        '''处理翻页动作，必要时从缓存恢复查询名与页码。'''
        if action not in frozenset({'search_next_page', 'search_prev_page'}):
            return (1, name, False)
        _var_var_4 = DATA_CACHE.get(key)
        if not _var_var_4:
            self._message_service.send_msg(title = not_found_title, text = '未找到相关资源', userid = userid, source = source)
            return (None, name, True)
        _var_var_0 = self._calc_page(_var_var_4, action)
        return (_var_var_0, _var_var_4.get('name', name), True)

    
    def _select_from_cache(self, key, num):
        '''按序号读取缓存中的选择项。'''
        _var_var_4 = DATA_CACHE.get(key)
        if not _var_var_4:
            return (None, None)
        return (_var_var_4, _var_var_4.get(int(num)))

    
    def _select_subscribe_delete(self, userid, key, num, source = None):
        '''处理订阅取消场景下的选择动作。'''
        (_var_var_4, _var_var_21) = self._select_from_cache(key, num)
        if not _var_var_4:
            logger.error('缓存数据不存在，无法处理选择操作')
            return True
        if not _var_var_21:
            self._message_service.send_msg(title = '取消订阅结果', text = f'''未找到序号 {num} 对应的资源''', userid = userid, source = source)
            return True
        _var_var_5 = self._build_image(_var_var_21.get('backdrop_path'), _var_var_21.get('poster_path'))
        with get_db() as _var_var_22:
            _var_var_23 = SubMediaOp(_var_var_22)
            _var_var_23.delete_by_ids([
                int(_var_var_21.get('id'))])
            self._message_service.send_msg(title = f'''{_var_var_21.get('title')} ({_var_var_21.get('year')}) 取消订阅成功''', image = _var_var_5, userid = userid, source = source)
        return True

    
    def _send_subscribe_delete_list(self, userid, key, page, pagesize = 10, source = None):
        """发送当前订阅列表，并更新取消订阅场景缓存。"""
        with get_db() as db:
            sub_op = SubMediaOp(db)
            resp = sub_op.list_page(None, None, page, pagesize)
        total = resp.get('total', 0)
        if total == 0:
            self._message_service.send_msg(title='当前订阅 🔔', text='没有订阅中的资源', userid=userid, source=source)
            return
        total_pages = total // pagesize + (1 if total % pagesize > 0 else 0)
        title = '当前订阅 🔔'
        if int(total_pages) > 1:
            title += f' {page}/{total_pages}'
        status_map = {0: '⏸️暂停订阅', 1: '🟢订阅中', 2: '✅完成订阅', 3: '🧼洗版中'}
        texts = []
        images = []
        keyboards = []
        rows = resp.get('data', [])
        for i, row in enumerate(rows, 1):
            status_text = status_map.get(int(row['status']), f'❓未知状态({row["status"]})')
            line = f'{i:02d}. {row["title"]} ({row["year"]}) {status_text}'
            texts.append(line)
            image = self._build_image(row.get('poster_path'), row.get('backdrop_path'))
            if image:
                images.append({'image': image, 'text': line, 'url': f'https://www.themoviedb.org/{row["type"]}/{row["tmdb_id"]}'})
            keyboards.append({'k': f'{i}', 'v': 'button=subscribe_delete=subdel=%s' % i})
        texts.append('\n回复 序号 进行订阅取消')
        text = '\n'.join(texts).strip()
        self._message_service.send_msg(title=title, text=f'\n{text}', userid=userid, images=images, source=source, keyboards=keyboards)
        self._save_cache(key, rows, page=page, total_pages=total_pages)
    def _select_subscribe_task(self, userid, key, num, name, source = None):
        """处理订阅新增场景下的选择动作并写库。"""
        found, item = self._select_from_cache(key, num)
        if not found:
            self._message_service.send_msg(title=f'{name} 的搜索结果 🎭', text='未找到相关资源', userid=userid, source=source)
            return True
        if not item:
            self._message_service.send_msg(title=f'{name} 的搜索结果 🎭', text=f'未找到序号 {num} 对应的资源', userid=userid, source=source)
            return True
        sub = SubMedia(tmdb_id=item.get('tmdb_id'), type=item.get('media_type'), title=item.get('title'), year=item.get('year'), poster_path=item.get('poster_path'), backdrop_path=item.get('backdrop_path'))
        image = self._build_image(sub.backdrop_path, sub.poster_path)
        msg_text = f'{item.get("title")} ({item.get("year")}) 已添加订阅'
        with get_db() as db:
            sub_op = SubMediaOp(db)
            if sub.type == 'tv':
                season_list = self._tmdbApi.get_tv_season_list(sub.tmdb_id)
                max_season, max_season_episodes = self._tmdbApi.get_tv_max_season_episode(season_list)
                sub.season_info = JsonUtils.to_str(season_list)
                sub.max_season = max_season
                sub.max_season_episodes = max_season_episodes
            saved = sub_op.save(sub)
        self._message_service.send_msg(title=saved.get('msg', msg_text), image=image, userid=userid, source=source)
        return True
    def _search_and_send_tmdb_list(self, userid, key, name, page, msg_type, button_action, hint, select_type = None, source = None):
        """搜索 TMDB 并发送可选列表，同时缓存结果。"""
        found, total_pages = self._search_tmdb_media(name, page)
        if found is None:
            self._message_service.send_msg(title=f'{name} 的搜索结果 🎭', text='未找到相关资源', userid=userid, source=source)
            return
        if not found:
            self._message_service.send_msg(title=f'{name} 的搜索结果 🎭', text='未找到 movie/tv 类型结果', userid=userid, source=source)
            return
        title = f'{name} 的搜索结果 🎭'
        if int(total_pages) > 1:
            title += f' {page}/{total_pages}'
        texts, images, keyboards, indexed_data = self._build_tmdb_list_payload(found, msg_type, button_action)
        texts.append(f'\n{hint}')
        text = '\n'.join(texts).strip()
        self._message_service.send_msg(title=title, text=f'\n{text}', userid=userid, images=images, source=source, keyboards=keyboards)
        if select_type:
            config2Env.msg_select_type = select_type
        self._save_cache(key, indexed_data, page=page, total_pages=total_pages, name=name)
    def _select_search_task(self, userid, key, num, name, source = None):
        '''处理资源搜索场景下的选择转存动作。'''
        (_var_var_4, _var_var_21) = self._select_from_cache(key, num)
        if not _var_var_4:
            return True
        if not _var_var_21:
            self._message_service.send_msg(title = f'''{name} 的资源搜索结果 🎭''', text = f'''未找到序号 {num} 对应的资源''', userid = userid, source = source)
            return True
        self._transfer_share_link(_var_var_21['link'])
        return True

    
    def _collect_subsource_search_results(self, name):
        """遍历订阅源执行搜索并聚合结果。"""
        with get_db() as db:
            sub_op = SubSourceOp(db)
            subs = sub_op.list('tg_channel', 1)
        results = {}
        for sub in subs:
            scraper = TelegramScraper(channel=sub.sub_url, name=sub.sub_name)
            found = scraper.search_all(q=name)
            logger.info(f'订阅源: {sub.sub_name} 资源搜索结果: {found}')
            if not found:
                continue
            results[sub.sub_name] = found
        return results
    def _send_search_task_results(self, userid, key, name, page, ret_dict, source = None):
        '''发送订阅源搜索结果列表并写入缓存。'''
        if not ret_dict:
            self._message_service.send_msg(title = f'''{name} 的资源搜索结果 🎭''', text = '未找到相关资源', userid = userid, source = source)
            return None
        _var_var_15 = []
        _var_var_18 = []
        _var_var_17 = []
        for _var_var_39, _var_var_12 in ret_dict.items():
            _var_var_15.append(f'''以下资源来自订阅源: {_var_var_39}\n''')
            for _var_var_11 in _var_var_12:
                _var_var_40 = f'''{_var_var_11['name']} ({_var_var_11['year']})'''
                if _var_var_11.get('season_num') and _var_var_11.get('episode_num'):
                    _var_var_40 = f'''{_var_var_40} S{_var_var_11['season_num']:02d}E{_var_var_11['episode_num']:02d}'''
                _var_var_7 = _var_var_11.get('first_text') or _var_var_40
                _var_var_2 = len(_var_var_18) + 1
                _var_var_15.append(f'''{_var_var_2:02d}. {_var_var_7}\n{_var_var_11['link']}''')
                _var_var_18.append(_var_var_11)
                _var_var_17.append({
                    'k': f'''{_var_var_2}''',
                    'v': f'''button=search_task=search={_var_var_2}''' })
            _var_var_15.append('\n')
        _var_var_15.append('回复 序号 进行转存')
        _var_var_29 = '\n'.join(_var_var_15)
        self._message_service.send_msg(title = f'''{name} 的资源搜索结果 🎭''', text = f'''\n{_var_var_29}''', userid = userid, source = source, keyboards = _var_var_17)
        self._save_cache(key, _var_var_18, page = page, name = name)
        return None

    
    def _select_tmdb_task_hdhive(self, userid, selected, source = None):
        '''处理 tmdb_task 中 hdhive 选择后的解锁与转存。'''
        _var_var_9 = self._hdHive.open_unlock_resource(slug = selected['slug'])
        if not _var_var_9.get('success'):
            self._message_service.send_msg(title = '资源转存失败 🎭', text = _var_var_9.get('message') or _var_var_9.get('code'), userid = userid, source = source)
            self._message_service.send_msg(title = '资源转存失败 🎭', text = '获取分享链接失败', userid = userid, source = source)
            return None
        _var_var_41 = _var_var_9.get('data', { }).get('full_url')
        _var_var_42 = self._transfer_share_link(_var_var_41)
        if not _var_var_42 or not _var_var_42.get('success'):
            self._message_service.send_msg(title = '资源转存失败 🎭', text = '获取分享链接失败', userid = userid, source = source)
        return None

    
    def _send_hdhive_search_results(self, userid, title, year, image, data, source = None):
        '''发送 RE0 内 hdhive 资源列表并写入 tmdb_task 缓存。'''
        _var_var_15 = []
        _var_var_18 = []
        _var_var_17 = []
        for _var_var_2, _var_var_11 in enumerate(data, 1):
            _var_var_43 = [*(_var_var_11.get('video_resolution') or []), *(_var_var_11.get('source') or []), *(_var_var_11.get('subtitle_language') or []), *(_var_var_11.get('subtitle_type') or [])]
            _var_var_44 = ' '.join(_var_var_43)
            _var_var_45 = _var_var_11.get('pan_type', '未知')
            if _var_var_11.get('pan_type') == '115':
                _var_var_45 = '115'
            elif _var_var_11.get('pan_type') == 'aliPan':
                _var_var_45 = '阿里'
            elif _var_var_11.get('pan_type') == 'ed2k':
                _var_var_45 = 'ed2k'
            _var_var_46 = f'''{_var_var_11['unlock_points']}💰''' if _var_var_11['unlock_points'] > 0 else '🆓'
            _var_var_47 = '🟡'
            if _var_var_11.get('validate_status', 'UN') == 'valid':
                _var_var_47 = '🟢'
            elif _var_var_11.get('validate_status', 'UN') == 'invalid':
                _var_var_47 = '🔴'
            _var_var_20 = f'''<blockquote>{_var_var_2:02d}. {_var_var_45} {_var_var_47} {_var_var_46} {_var_var_11['share_size']}\n📦{_var_var_44}\n'''
            _var_var_20 = f'''{_var_var_20}🧛{_var_var_11['user']['nickname']} {_var_var_11['updated_at']}'''
            if _var_var_11.get('remark'):
                _var_var_20 = f'''{_var_var_20}\n📝{_var_var_11['remark']}</blockquote>'''
            else:
                _var_var_20 = f'''{_var_var_20}</blockquote>'''
            _var_var_15.append(_var_var_20)
            _var_var_18.append({
                'slug': _var_var_11['slug'],
                'title': title,
                'tag': _var_var_44 })
            _var_var_17.append({
                'k': f'''{_var_var_2}''',
                'v': f'''button=tmdb_task=hdhive={_var_var_2}''' })
        _var_var_15.append('回复 序号 进行转存')
        self._message_service.send_msg(title = f'''{title} ({year})''', image = image, userid = userid, source = source)
        _var_var_29 = '\n'.join(_var_var_15)
        self._message_service.send_msg(title = 'RE0内的搜索结果 🎭', text = f'''\n{_var_var_29}''', userid = userid, source = source, keyboards = _var_var_17)
        config2Env.msg_select_type = 'hdhive'
        _var_var_48 = self._build_cache_key('tmdb_task', userid, 'hdhive')
        self._save_cache(_var_var_48, _var_var_18)
        return None

    
    def _select_tmdb_task_tmdb(self, userid, selected, source = None):
        '''处理 tmdb_task 中 tmdb 选择后的 RE0 资源搜索与发送。'''
        _var_var_7 = selected.get('title')
        _var_var_8 = selected.get('year')
        _var_var_5 = self._build_image(selected.get('backdrop_path'), selected.get('poster_path'))
        _var_var_9 = self._hdHive.open_resources(resource_type = selected.get('media_type'), tmdb_id = selected.get('tmdb_id'))
        if not _var_var_9.get('success'):
            self._message_service.send_msg(title = 'RE0资源搜索失败 🎭', text = JsonUtils.to_str(_var_var_9), image = _var_var_5, userid = userid, source = source)
            return None
        _var_var_27 = _var_var_9.get('data', [])
        if not _var_var_27:
            self._message_service.send_msg(title = 'RE0资源搜索结果 🎭', text = '未找到相关资源', image = _var_var_5, userid = userid, source = source)
            return None
        self._send_hdhive_search_results(userid, _var_var_7, _var_var_8, _var_var_5, _var_var_27, source = source)
        return None

    
    def _select_tmdb_task(self, userid, key, num, name, msg_select_type, source = None):
        '''按 msg_select_type 分派 tmdb_task 的选择动作。'''
        _var_var_21 = DATA_CACHE.get(key, { }).get(int(num), { })
        if not _var_var_21:
            self._message_service.send_msg(title = f'''{name} 的搜索结果 🎭''', text = f'''未找到序号 {num} 对应的资源''', userid = userid, source = source)
            return True
        if msg_select_type == 'hdhive':
            self._select_tmdb_task_hdhive(userid, _var_var_21, source = source)
            return True
        self._select_tmdb_task_tmdb(userid, _var_var_21, source = source)
        return True

    
    def subscribe_delete(self, item):
        '''取消订阅任务入口。'''
        _var_var_49 = 'subscribe_delete'
        _var_var_50 = item.get('userid')
        _var_var_51 = item.get('source')
        _var_var_52 = self._build_cache_key(_var_var_49, _var_var_50)
        config2Env.msg_type = _var_var_49
        _var_var_53 = item.get('num')
        _var_var_0 = 1
        _var_var_54 = item.get('action')
        if _var_var_54 in frozenset({'search_next_page', 'search_prev_page'}):
            _var_var_0 = self._calc_page(DATA_CACHE.get(_var_var_52, { }), _var_var_54)
        elif _var_var_54 == 'select':
            if self._select_subscribe_delete(_var_var_50, _var_var_52, _var_var_53, source = _var_var_51):
                return None
        self._send_subscribe_delete_list(_var_var_50, _var_var_52, _var_var_0, source = _var_var_51)
        return None

    
    def subscribe_task(self, item):
        '''订阅新增任务入口。'''
        _var_var_49 = 'subscribe_task'
        _var_var_50 = item.get('userid')
        _var_var_51 = item.get('source')
        _var_var_52 = self._build_cache_key(_var_var_49, _var_var_50)
        config2Env.msg_type = _var_var_49
        _var_var_53 = item.get('num')
        _var_var_55 = item.get('name')
        _var_var_54 = item.get('action')
        (_var_var_0, _var_var_55, _var_var_56) = self._resolve_paging_with_cache(_var_var_54, _var_var_52, _var_var_50, _var_var_55, f'''{_var_var_55} 的搜索结果 🎭''', source = _var_var_51)
        if _var_var_0 is None:
            return None
        if _var_var_54 == 'select':
            if self._select_subscribe_task(_var_var_50, _var_var_52, _var_var_53, _var_var_55, source = _var_var_51):
                return None
        self._search_and_send_tmdb_list(userid = _var_var_50, key = _var_var_52, name = _var_var_55, page = _var_var_0, msg_type = _var_var_49, button_action = 'sub', hint = '回复 序号 进行订阅', source = _var_var_51)
        return None

    
    def search_task(self, item):
        '''订阅源资源搜索任务入口。'''
        _var_var_49 = 'search_task'
        _var_var_50 = item.get('userid')
        _var_var_51 = item.get('source')
        _var_var_52 = self._build_cache_key(_var_var_49, _var_var_50)
        config2Env.msg_type = _var_var_49
        _var_var_53 = item.get('num')
        _var_var_55 = item.get('name')
        _var_var_54 = item.get('action')
        (_var_var_0, _var_var_55, _var_var_56) = self._resolve_paging_with_cache(_var_var_54, _var_var_52, _var_var_50, _var_var_55, f'''{_var_var_55} 的资源搜索结果 🎭''', source = _var_var_51)
        if _var_var_0 is None:
            return None
        if _var_var_54 == 'select':
            if self._select_search_task(_var_var_50, _var_var_52, _var_var_53, _var_var_55, source = _var_var_51):
                return None
        _var_var_36 = self._collect_subsource_search_results(_var_var_55)
        self._send_search_task_results(_var_var_50, _var_var_52, _var_var_55, _var_var_0, _var_var_36, source = _var_var_51)
        return None

    
    def tmdb_task(self, item):
        '''TMDB 搜索与选择转存任务入口。'''
        _var_var_49 = 'tmdb_task'
        _var_var_50 = item.get('userid')
        _var_var_51 = item.get('source')
        _var_var_57 = item.get('msg_select_type', config2Env.msg_select_type)
        _var_var_52 = self._build_cache_key(_var_var_49, _var_var_50, _var_var_57)
        config2Env.msg_type = _var_var_49
        _var_var_53 = item.get('num', 0)
        _var_var_55 = item.get('name')
        _var_var_54 = item.get('action')
        (_var_var_0, _var_var_55, _var_var_56) = self._resolve_paging_with_cache(_var_var_54, _var_var_52, _var_var_50, _var_var_55, f'''{_var_var_55} 的搜索结果 🎭''', source = _var_var_51)
        if _var_var_0 is None:
            return None
        if _var_var_54 == 'select':
            if self._select_tmdb_task(_var_var_50, _var_var_52, _var_var_53, _var_var_55, _var_var_57, source = _var_var_51):
                return None
        _var_var_58 = self._build_cache_key(_var_var_49, _var_var_50, 'tmdb')
        self._search_and_send_tmdb_list(userid = _var_var_50, key = _var_var_58, name = _var_var_55, page = _var_var_0, msg_type = _var_var_49, button_action = 'tmdb', hint = '回复 序号 将在RE0内搜索', select_type = 'tmdb', source = _var_var_51)
        return None
