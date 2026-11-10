import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import pytz
from app.log import logger
from app.utils.mjson import JsonUtils
from app.utils.share import ShareUtil

class ResourceInfo:
    
    def __init__(self):
        self.name = None
        self.year = None
        self.resource_pix = None
        self.resource_type = None
        self.type = None
        self.link = None
        self.tmdb_id = None
        self.link_type = None
        self.source = None
        self.id = None
        self.time = None
        self.latest_episode = None
        self.season_num = None
        self.episode_num = None
        self.size = None
        self.first_text = None
        return None
        return None

    
    def to_dict(self):
        return {
            'name': self.name,
            'year': self.year,
            'resource_pix': self.resource_pix,
            'resource_type': self.resource_type,
            'type': self.type,
            'link': self.link,
            'tmdb_id': self.tmdb_id,
            'link_type': self.link_type,
            'source': self.source,
            'id': self.id,
            'time': self.time,
            'latest_episode': self.latest_episode,
            'season_num': self.season_num,
            'episode_num': self.episode_num,
            'size': self.size,
            'first_text': self.first_text,
        }
class TelegramScraper:
    
    def __init__(self, channel, name):
        if channel.startswith('https://t.me/s/'):
            self.channel = channel.split('https://t.me/s/')[1]
        elif channel.startswith('https://t.me/'):
            self.channel = channel.split('https://t.me/')[1]
        else:
            self.channel = channel
        self.base_url = f'''https://t.me/s/{self.channel}'''
        if not name:
            name
        self.name = channel
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
        return None
        return None

    @property
    def http_proxies(self):
        _var_var_0 = os.getenv('CMS_PROXY')
        if _var_var_0:
            return {'http': _var_var_0, 'https': _var_var_0}
        return None
    
    def get_page_content(self, q: str = None, after: int = None, before: int = None):
        _var_var_1 = {}
        if q:
            _var_var_1['q'] = q
        if after:
            _var_var_1['after'] = after
        if before:
            _var_var_1['before'] = before
        _var_var_2 = self.base_url
        if _var_var_1:
            _var_var_2 += '?' + '&'.join([f'{_var_var_3}={_var_var_4}' for _var_var_3, _var_var_4 in _var_var_1.items()])
        try:
            _var_var_5 = requests.get(_var_var_2, headers=self.headers, proxies=self.http_proxies, timeout=10)
            _var_var_5.raise_for_status()
            return _var_var_5.text
        except requests.RequestException as _var_var_6:
            print(f'[TG_SCRAPER][网络请求失败] error={_var_var_6}')
        except Exception as _var_var_6:
            print(f'[TG_SCRAPER][未知异常] error={_var_var_6}')
    def parse_messages(self, html_content):
        if not html_content:
            return []
        _var_var_7 = BeautifulSoup(html_content, 'html.parser')
        _var_var_8 = _var_var_7.find_all('div', class_='tgme_widget_message')
        _var_var_9 = []
        _var_var_10 = len(_var_var_8) == 20
        print('size:', len(_var_var_8))
        for _var_var_11 in _var_var_8:
            try:
                _var_var_12 = _var_var_11.find('div', class_='tgme_widget_message_text')
                _var_var_13 = _var_var_12.decode_contents() if _var_var_12 else ''
                _var_var_14 = _var_var_13.split('<br/>')
                _var_var_15 = ''
                if _var_var_14:
                    _var_var_16 = BeautifulSoup(_var_var_14[0], 'html.parser')
                    _var_var_15 = ''.join(_var_var_16.stripped_strings)
                _var_var_17 = ''.join(_var_var_12.stripped_strings) if _var_var_12 else ''
                _var_var_18 = str(_var_var_11)
                _var_var_19 = _var_var_11.find('a', class_='tgme_widget_message_date')
                if _var_var_19:
                    _var_var_20 = _var_var_19['href'].split('/')[-1]
                    _var_var_21 = _var_var_19.find('time')
                    if _var_var_21 and _var_var_21.get('datetime'):
                        _var_var_22 = datetime.fromisoformat(_var_var_21['datetime'])
                        _var_var_23 = pytz.timezone('Asia/Shanghai')
                        _var_var_24 = _var_var_22.astimezone(_var_var_23)
                        _var_var_25 = _var_var_24.strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        _var_var_20 = None
                        _var_var_25 = None
                _var_var_26 = []
                _var_var_27 = ShareUtil.get_share_down_link(_var_var_18)
                if _var_var_27['success']:
                    for _var_var_28 in _var_var_27.get('share_links', []):
                        _var_var_26.append((_var_var_28, 'share_115'))
                    for _var_var_28 in _var_var_27.get('ali_links', []):
                        _var_var_26.append((_var_var_28, 'share_aliyun'))
                    for _var_var_28 in _var_var_27.get('ed2k_links', []):
                        _var_var_26.append((_var_var_28, 'share_ed2k'))
                    for _var_var_28 in _var_var_27.get('magnet_links', []):
                        _var_var_26.append((_var_var_28, 'share_magnet'))
                if _var_var_26:
                    _var_var_29 = self.parse_resource_info(_var_var_17)
                    if _var_var_29:
                        for _var_var_28, _var_var_30 in _var_var_26:
                            _var_var_31 = ResourceInfo()
                            _var_var_31.name = _var_var_29.name
                            _var_var_31.year = _var_var_29.year
                            _var_var_31.resource_pix = _var_var_29.resource_pix
                            _var_var_31.resource_type = _var_var_29.resource_type
                            _var_var_31.type = _var_var_29.type
                            _var_var_31.tmdb_id = _var_var_29.tmdb_id
                            _var_var_31.source = _var_var_29.source
                            _var_var_31.latest_episode = _var_var_29.latest_episode
                            _var_var_31.season_num = _var_var_29.season_num
                            _var_var_31.episode_num = _var_var_29.episode_num
                            _var_var_31.size = _var_var_29.size
                            _var_var_31.link = _var_var_28
                            _var_var_31.link_type = _var_var_30
                            _var_var_31.id = _var_var_20
                            _var_var_31.time = _var_var_25
                            _var_var_31.first_text = _var_var_15
                            _var_var_9.append(_var_var_31.to_dict())
            except Exception as _var_var_6:
                print(f'Error parsing message: {_var_var_6}')
        _var_var_9.sort(key=lambda x: x['id'] if x['id'] else '', reverse=True)
        return (_var_var_10, _var_var_9)
    def parse_resource_info(self, text):
        """解析资源信息"""
        try:
            _var_var_32 = ResourceInfo()
            _var_var_32.source = self.name
            _var_var_33 = text.replace('名称：', '').replace('（', '(').replace('）', ')')
            _var_var_34 = re.search(r'更新至\s*(\d+)(?:\s*[集话])?', _var_var_33)
            if _var_var_34:
                _var_var_32.latest_episode = int(_var_var_34.group(1))
            _var_var_35 = re.search('(\d{4})[年.-]', _var_var_33)
            if _var_var_35:
                _var_var_32.year = _var_var_35.group(1)
            _var_var_36 = re.search('(4k|1080p|720p|2160p|remux|bluray)', _var_var_33, re.IGNORECASE)
            if _var_var_36:
                _var_var_32.resolution = _var_var_36.group(1).upper()
            _var_var_37 = re.search('描述[：:]\s*(.+?)(?=\n\s*\n|链接[：:]|$)', text, re.DOTALL)
            if _var_var_37:
                _var_var_32.description = _var_var_37.group(1).strip()
            _var_var_38 = re.findall('https?://[a-zA-Z0-9./?=#-_]+', text)
            if _var_var_38:
                _var_var_32.links = _var_var_38
            _var_var_39 = re.search('标签[：:]\s*(.+?)(?=\n|$)', text)
            if _var_var_39:
                _var_var_32.tags = [t.strip() for t in _var_var_39.group(1).split('#') if t.strip()]
            _var_var_40 = re.search('频道[：:]\s*(.+?)(?=\n|$)', text)
            if _var_var_40:
                _var_var_32.channel = _var_var_40.group(1).strip()
            _var_var_41 = re.search('发布时间[：:]\s*(.+?)(?=\n|$)', text)
            if _var_var_41:
                _var_var_32.pub_date = _var_var_41.group(1).strip()
            _var_var_42 = re.search('类型[：:]\s*(.+?)(?=\n|$)', text)
            if _var_var_42:
                _var_var_32.type = _var_var_42.group(1).strip()
            return _var_var_32
        except Exception as _var_var_6:
            print(f'Error parsing resource info: {_var_var_6}')
            return None

    def search(self, q, before):
        q = f'''”{q}”''' if q else None
        _var_var_53 = self.get_page_content(q = q, before = before)
        if _var_var_53:
            return self.parse_messages(_var_var_53)
        return None
        return (False, [])
        return None

    
    def search_all(self, q):
        _var_var_54 = []
        _var_var_55 = None
        (_var_var_10, _var_var_56) = self.search(q = q, before = _var_var_55)
        _var_var_54.extend(_var_var_56)
        if _var_var_10 and _var_var_56 or len(_var_var_56) == 0:
            pass
        else:
            logger.info(f'''开始获取下一页，当前已获取{len(_var_var_54)}条数据''')
            _var_var_55 = _var_var_56[-1]['id']
        return _var_var_54
        return None

    property

if __name__ == '__main__':
    tg_scraper = TelegramScraper(channel = 'https://t.me/gimy115', name = 'a')
    (is_next_page, res) = tg_scraper.search(q = f'''''', before = 6687)
    print(JsonUtils.to_str(res))

