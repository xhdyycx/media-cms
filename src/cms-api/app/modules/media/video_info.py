import os
import json
import re
from pathlib import Path
from app.core.env import configEnv
from app.core.task_tidy import load_words_replace_from_env
from app.modules.media.team import TeamMatcher
from app.utils.mutil import Mutil

class VideoInfo:
    del_separators = '[ \\[\\]【】()（）\\-——_\\*！!&]'
    re_cn_name = '[0-9]*[\\u4e00-\\u9fff]+[\\u4e00-\\u9fff\\dA-Za-z：:!！"\\\'·，,~～、&ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ]*'
    re_en_name = '[a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ\\.²\\d：:!！"\\\'·，,~～、&\\sⅠ-Ⅻⅰ-ⅹⅺⅻ]*'
    re_year_num = '(?:19[0-9]{2}|20[0-9]{2})'
    re_year_x = '(?<![0-9a-zA-Z])[12][0-9]{3}(?![0-9a-zA-Z])'
    
    def __init__(self, file_path):
        self.original_name = ''
        self.ext = ''
        self.name = ''
        self.en_name = ''
        self.name_aliases = []
        self.year = ''
        self.tmdb_id = ''
        self.type = ''
        self.season_num = None
        self.episode_num = None
        self.season_episode = None
        self.disc_num = None
        self.fps = None
        self.resource_type = None
        self.resource_source = None
        self.resource_version = None
        self.resource_effect = None
        self.resource_pix = None
        self.video_encode = None
        self.audio_encode = None
        self.resource_team = None
        self.custom_regex_match = None
        self.format_name = ''
        if not file_path:
            return
        _var_var_0 = Path(file_path)
        _var_var_1 = str(_var_var_0.name)
        self.original_name = _var_var_1
        _var_var_2 = ''
        _var_var_3 = ''
        if _var_var_0.parent:
            _var_var_2 = str(_var_var_0.parent.name)
            self._VideoInfo__p_name = _var_var_2
            if _var_var_0.parent.parent:
                _var_var_3 = str(_var_var_0.parent.parent.name)
                self._VideoInfo__pp_name = _var_var_3
        self.format_filename(_var_var_1)
        self.build_tmdb_id()
        self.build_name()
        self.build_year()
        _var_var_1 = self.format_name
        self.ext = os.path.splitext(_var_var_1)[1].lstrip('.')
        _var_var_4 = os.path.splitext(_var_var_1)[0]
        if re.match('^\\d+$', _var_var_4):
            self.type = 'tv'
            self.build_season_num(_var_var_2)
            if self.season_num is None:
                self.season_num = 1
            self.episode_num = int(_var_var_4)
            self.build_season_episode()
            return
        if re.match(f'^{self.re_cn_name}$', _var_var_4):
            self.type = 'movie'
            self.name = _var_var_4
            return
        self.build_season_num(_var_var_1)
        self.build_season_num(_var_var_2)
        self.build_episode_num(_var_var_1)
        if not self.type:
            self.type = 'movie'
        if self.type == 'tv' and self.season_num is None and self.episode_num:
            self.season_num = 1
        self.build_season_episode()
        _var_var_5 = re.search('\\d{3,4}[ip]|4k|8k|16k', _var_var_1, re.I)
        if _var_var_5:
            self.resource_pix = _var_var_5.group(0)
        if re.search('\\.DV\\.|DOVI|Dolby[ .]?Vision', _var_var_1, re.I):
            self.resource_effect = 'DV'
            if re.search('HDR', _var_var_1, re.I):
                self.resource_effect = 'DV.HDR'
        elif re.search('HDR10|HDR\\.10', _var_var_1, re.I):
            self.resource_effect = 'HDR10'
        elif re.search('HDR', _var_var_1, re.I):
            self.resource_effect = 'HDR'
        elif re.search('SDR', _var_var_1, re.I):
            self.resource_effect = 'SDR'
        elif re.search('EDR', _var_var_1, re.I):
            self.resource_effect = 'EDR'
        if re.search('REMUX', _var_var_1, re.I):
            self.video_encode = 'REMUX'
        elif re.search('[HX]\\.?264|AVC|MPEG-4', _var_var_1, re.I):
            self.video_encode = 'H264'
            if re.search('10[ .]?bit', _var_var_1, re.I):
                self.video_encode += '.10bit'
            elif re.search('8[ .]?bit', _var_var_1, re.I):
                self.video_encode += '.8bit'
        elif re.search('[HX]\\.?265|HEVC', _var_var_1, re.I):
            self.video_encode = 'H265'
            if re.search('10[ .]?bit', _var_var_1, re.I):
                self.video_encode += '.10bit'
            elif re.search('8[ .]?bit', _var_var_1, re.I):
                self.video_encode += '.8bit'
        _var_var_6 = re.search('(?<![A-Za-z])TrueHD(?:\\.|\\s)?(?:Atmos)?(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)', _var_var_1, re.I)
        if _var_var_6:
            self.audio_encode = f'TrueHD.{_var_var_6.group(1)}'
        if not self.audio_encode:
            _var_var_7 = re.search('(?<![A-Za-z])DTS\\.HD(?:\\.|\\s)?(MA)?(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0|1\\.0)', _var_var_1, re.I)
            if _var_var_7:
                _var_var_8 = '.MA' if _var_var_7.group(1) else ''
                self.audio_encode = f'DTS-HD{_var_var_8}.{_var_var_7.group(2)}'
            else:
                _var_var_9 = re.search('(?<![A-Za-z])DTS(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)?', _var_var_1, re.I)
                if _var_var_9:
                    _var_var_10 = f'.{_var_var_9.group(1)}' if _var_var_9.group(1) else ''
                    self.audio_encode = f'DTS{_var_var_10}'
        if not self.audio_encode:
            _var_var_11 = re.search('(?<![A-Za-z])LPCM(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)?', _var_var_1, re.I)
            if _var_var_11:
                _var_var_10 = f'.{_var_var_11.group(1)}' if _var_var_11.group(1) else ''
                self.audio_encode = f'LPCM{_var_var_10}'
        if not self.audio_encode:
            _var_var_12 = re.search('(?<![A-Za-z])DDP(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)?', _var_var_1, re.I)
            if _var_var_12:
                _var_var_10 = f'.{_var_var_12.group(1)}' if _var_var_12.group(1) else ''
                self.audio_encode = f'DDP{_var_var_10}'
        if not self.audio_encode:
            _var_var_13 = re.search('(?<![A-Za-z])DD(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)?', _var_var_1, re.I)
            if _var_var_13:
                _var_var_10 = f'.{_var_var_13.group(1)}' if _var_var_13.group(1) else ''
                self.audio_encode = f'DD{_var_var_10}'
        if not self.audio_encode:
            _var_var_14 = re.search('(?<![A-Za-z])EAC3(?:\\.|\\s)?(5\\.1|7\\.1|2\\.0)?', _var_var_1, re.I)
            if _var_var_14:
                _var_var_10 = f'.{_var_var_14.group(1)}' if _var_var_14.group(1) else ''
                self.audio_encode = f'EAC3{_var_var_10}'
        if not self.audio_encode:
            _var_var_6 = re.search('(?<![A-Za-z])(AC3|AAC|FLAC)', _var_var_1, re.I)
            if _var_var_6:
                self.audio_encode = _var_var_6.group(1)
        _var_var_6 = re.search('(\\d+)Audio', _var_var_1, re.I)
        if _var_var_6:
            if self.audio_encode:
                self.audio_encode += f'.{_var_var_6.group(1)}Audios'
            else:
                self.audio_encode = f'{_var_var_6.group(1)}Audios'
        self.resource_team = TeamMatcher().match(title=self.original_name) or None
        if not self.resource_team:
            self.resource_team = TeamMatcher().match(title=self.format_name) or None
        _var_var_15 = [
            ('blu\\.?ray', 'BluRay'),
            ('web\\.?dl|webrip', 'WEB-DL'),
            ('MiniBD', 'MiniBD'),
            ('hdtv', 'HDTV'),
            ('DVDRIP', 'DVDRip'),
            ('BDRIP', 'BDRip'),
            ('HDRip', 'HDRip'),
        ]
        for _var_var_16, _var_var_17 in _var_var_15:
            _var_var_18 = re.search(_var_var_16, _var_var_1, re.I)
            if not _var_var_18:
                continue
            self.resource_type = _var_var_17(_var_var_18) if callable(_var_var_17) else _var_var_17
            break
        _var_var_19 = {
            '\\.NF\\.|Netflix|奈飞': 'NF',
            '\\.DSNP\\.': 'DSNP',
            '\\.Amazon\\.|\\.AMZN\\.|亚马逊': 'AMZN',
            '\\.Apple\\.TV\\.': 'Apple.TV',
            '\\.iTunes\\.': 'iTunes',
            '\\.IQ\\.|IQIYI|爱奇艺': 'IQIYI',
            '\\.Bilibili\\.|哔哩哔哩': 'Bilibili',
            '\\.YOUKU\\.|优酷': 'YOUKU',
            '\\.baha\\.|巴哈姆特': 'BAHA',
            '\\.CR\\.|Crunchyroll': 'CR',
            '\\.Mytvs\\.|Mytvsuper': 'Mytvs',
            '\\.MyVideo\\.': 'MyVideo',
            '\\.Hami\\.': 'Hami',
            '\\.Hulu\\.': 'Hulu',
            '\\.AnyWhere\\+\\.': 'AnyWhere+',
            '(?<![a-zA-Z])(USA|JPN|FRA|KOR|GBR|GER|EUR|HKG|TWN|ITA|CAN|AUS|ESP|NLD|SWE|NOR|DNK|RUS|BRA|MEX)(?:\\.UHD)?(?![a-zA-Z])': lambda m: f'{m.group(1)}.UHD' if m.group(0).endswith('.UHD') else m.group(1),
        }
        for _var_var_16, _var_var_20 in _var_var_19.items():
            _var_var_18 = re.search(_var_var_16, _var_var_1, re.I)
            if not _var_var_18:
                continue
            self.resource_source = _var_var_20(_var_var_18) if callable(_var_var_20) else _var_var_20
            break
        _var_var_21 = []
        if re.search('\\.imax', _var_var_1, re.I):
            _var_var_21.append('IMAX')
        if re.search('\\.Criterion\\.Collection|\\.CC\\.', _var_var_1, re.I):
            _var_var_21.append('CC')
        if re.search('\\.3D', _var_var_1, re.I):
            _var_var_21.append('3D')
        if re.search('repack|重置版', _var_var_1, re.I):
            _var_var_21.append('REPACK')
        if re.search('\\.dc|导演剪辑版', _var_var_1, re.I):
            _var_var_21.append('DC')
        if re.search('Extended', _var_var_1, re.I):
            _var_var_21.append('Extended')
        if re.search('\\.HQ|\\.高码', _var_var_1, re.I):
            _var_var_21.append('HQ')
        if re.search('2K\\.REMASTERED', _var_var_1, re.I):
            _var_var_21.append('2K.REMASTERED')
        if _var_var_21:
            self.resource_version = '.'.join(_var_var_21)
        self.build_fps(_var_var_1)
        self.build_disc_num(_var_var_1)
        self.build_episode_num_final()
        self.build_custom_match(_var_var_1)
    def build_custom_match(self, name):
        if not name or configEnv.custom_regex_match:
            return None
        return None
        _var_var_22 = re.search(configEnv.custom_regex_match, name, re.I)
        if _var_var_22:
            self.custom_regex_match = _var_var_22.group(0)
        return None
        return None

    
    def del_other_name(self, name):
        if not name:
            return None
        return None
        name = re.sub('第[一二三四五六七八九十百千万\\d]+[集话話]', '', name)
        name = re.sub('第[一二三四五六七八九十百千万\\d]+季', '', name)
        name = re.sub('[Ss]\\d{1,3}[Ee]\\d{1,3}|[Ee][Pp]?\\d{1,3}', '', name)
        name = re.sub('\\d{3,4}[ip]|4k|8k|16k', '', name, flags = re.I)
        name = re.sub('Blu-?Ray|WEB-?DL|WEB-?RIP|HDTV|\\.DVD|\\.BD|\\.UHD|\\.REMUX|\\.ENCODE', '', name, flags = re.I)
        name = re.sub('\\.IMAX|Criterion\\.Collection|\\.CC|\\.3D|\\.REPACK|重置版|\\.DC|导演剪辑版|Extended|\\.HQ|高码', '', name, flags = re.I)
        name = re.sub('\\.+', '.', name)
        return name.strip()
        return None

    
    def build_name(self):
        _var_var_23 = self.del_other_name(self.format_name)
        _var_var_2 = self.del_other_name(self._VideoInfo__p_name)
        _var_var_3 = self.del_other_name(self._VideoInfo__pp_name)
        self.build_name_year_2(_var_var_23)
        self.build_name_year_1(_var_var_2)
        self.build_name_year_1(_var_var_3)
        self.build_name_year_2(_var_var_2)
        self.build_name_year_2(_var_var_3)
        self.build_name_year_3(_var_var_23)
        self.build_name_year_3(_var_var_2)
        self.build_name_year_3(_var_var_3)
        self.build_name_year_4(self.format_name)
        self.build_name_year_5(_var_var_23)
        if not self.name:
            self.build_cn_name(_var_var_2)
        if not self.name:
            self.build_cn_name(_var_var_3)
        if self.name:
            self.name = self.name.strip()
        if self.en_name:
            self.en_name = re.sub('[.：:]|S\\d+E\\d+|E\\d+|EP\\d+', ' ', self.en_name).strip()
        self.build_name_aliases(_var_var_23)
        return None
        return None

    
    def build_cn_name(self, name):
        if not name:
            return None
        return None
        if re.search('整理|刮削', name, re.I):
            return None
        return None
        if re.match(f'''^{self.re_cn_name}$''', name):
            self.name = name
        return None
        return None

    
    def build_season_num(self, name):
        if not name or self.season_num is not None:
            return
        _var_var_24 = re.search('Season\\s*(\\d{1,3})', name, re.I)
        if _var_var_24:
            self.season_num = int(_var_var_24.group(1))
            self.type = 'tv'
            return
        _var_var_25 = re.search('S(\\d{1,3})E\\d+|S(\\d{1,3})EP\\d+', name, re.I)
        if _var_var_25:
            _var_var_26 = _var_var_25.group(1) or _var_var_25.group(2)
            self.season_num = int(_var_var_26)
            self.type = 'tv'
            return
        _var_var_27 = re.search('\\.S(\\d{1,3})\\.', name, re.I)
        if _var_var_27:
            self.season_num = int(_var_var_27.group(1))
            self.type = 'tv'
            return
        _var_var_28 = re.search('第([一二三四五六七八九十百零\\d]{1,3})季', name)
        if _var_var_28:
            self.season_num = self.convert_cn_num(_var_var_28.group(1))
            self.type = 'tv'
            return
    def build_episode_num_final(self):
        if self.type == 'tv' and self.season_num is None:
            self.season_num = 1
    def build_episode_num(self, name):
        if not name or self.episode_num is not None:
            return
        _var_var_29 = re.search('episode(?:\\s*|\\.*)(\\d{1,3})', name, re.I)
        if _var_var_29:
            self.episode_num = int(_var_var_29.group(1))
            self.type = 'tv'
            return
        _var_var_25 = re.search('S\\d{1,3}E(\\d+)|S\\d{1,3}EP(\\d+)', name, re.I)
        if _var_var_25:
            _var_var_30 = _var_var_25.group(1) or _var_var_25.group(2)
            self.episode_num = int(_var_var_30)
            self.type = 'tv'
            return
        _var_var_27 = re.search('\\.(?:E|EP|episode)(\\d{1,3})\\.', name, re.I)
        if _var_var_27:
            self.episode_num = int(_var_var_27.group(1))
            self.type = 'tv'
            return
        _var_var_28 = re.search('第([一二三四五六七八九十百零\\d]{1,5})[集话話]', name)
        if _var_var_28:
            self.episode_num = self.convert_cn_num(_var_var_28.group(1))
            self.type = 'tv'
            return
        if self.episode_num is None:
            _var_var_31 = re.search('(19|20)\\d{2}', name)
            if _var_var_31:
                _var_var_32 = _var_var_31.end()
                _var_var_33 = name[_var_var_32:]
            else:
                _var_var_33 = name
            _var_var_34 = self.del_char(_var_var_33)
            if _var_var_34.isdigit():
                self.episode_num = int(_var_var_34)
                self.type = 'tv'
                return
    def del_char(self, name):
        if not name:
            return None
        return None
        name = re.sub('(?i)(x|h)[.]?26[456]', '', name)
        name = re.sub('(?i)mpeg[-.]?[24]', '', name)
        name = re.sub('(?i)[ac|vc|av]+[-.]?1', '', name)
        name = re.sub('(?i)[ac]+[-.]?3', '', name)
        name = re.sub('(?i)vp[-.]?9', '', name)
        name = re.sub('(?i)hdr[.]?10', '', name)
        name = re.sub('(?i)10[ .]?bit', '', name)
        name = re.sub('(?i)8[ .]?bit', '', name)
        name = re.sub('(?:7|5|3|2|1)\\.[01]\\.', '', name)
        name = re.sub('\\d{3,4}[ip]|4k|8k|16k', '', name, flags = re.I)
        name = re.sub('Blu-?Ray|WEB-?DL|WEB-?RIP|HDTV|\\.DVD|\\.BD|\\.UHD|\\.REMUX|\\.ENCODE', '', name, flags = re.I)
        name = re.sub('\\.+', '.', name)
        name = name.lstrip('.')
        name = os.path.splitext(name)[0]
        return name.strip()
        return None

    
    def del_encode(self, name):
        if not name:
            return None
        return None
        name = re.sub('(?i)(x|h)[.]?26[456]', '', name)
        name = re.sub('(?i)mpeg[-.]?[24]', '', name)
        name = re.sub('(?i)[ac|vc|av]+[-.]?1', '', name)
        name = re.sub('(?i)[ac]+[-.]?3', '', name)
        name = re.sub('(?i)vp[-.]?9', '', name)
        name = re.sub('(?i)hdr[.]?10', '', name)
        name = re.sub('(?i)10[ .]?bit', '', name)
        name = re.sub('(?i)8[ .]?bit', '', name)
        name = re.sub('(?:7|5|3|2)\\.[01]\\.', '', name)
        name = re.sub('\\.+', '.', name)
        return name.strip()
        return None

    
    def build_part_num(self, name):
        if self.episode_num is not None:
            return
        _var_var_35 = re.search('Part\\.?(\\d+)', name, re.IGNORECASE)
        if _var_var_35:
            if self.season_num is None:
                self.episode_num = int(_var_var_35.group(1))
                self.type = 'tv'
            if self.season_num is None:
                self.season_num = 1
    def build_season_episode(self):
        if self.season_num is not None and self.episode_num is not None:
            if self.season_num < 10:
                _var_var_36 = f'0{self.season_num}'
            else:
                _var_var_36 = str(self.season_num)
            if self.episode_num < 10:
                _var_var_37 = f'0{self.episode_num}'
            else:
                _var_var_37 = str(self.episode_num)
            self.season_episode = f'S{_var_var_36}E{_var_var_37}'
    def build_fps(self, name):
        _var_var_16 = '\\d+(?:FPS|帧)'
        _var_var_18 = re.search(_var_var_16, name, re.IGNORECASE)
        if _var_var_18:
            self.fps = _var_var_18.group()
        return None
        return None

    
    def build_disc_num(self, name):
        _var_var_16 = 'DISC(\\d+)|CD(\\d+)'
        _var_var_18 = re.search(_var_var_16, name, re.IGNORECASE)
        if _var_var_18:
            self.disc_num = int(_var_var_18.group(1)) if _var_var_18.group(1) else int(_var_var_18.group(2))
        return None
        return None

    
    def to_json(self):
        return json.dumps(self, default = (lambda o: o.__dict__), ensure_ascii = False)
        return None

    
    def to_dict(self):
        return self.__dict__
        return None

    
    def convert_cn_num(self, cn_num):
        if cn_num.isdigit():
            return int(cn_num)
        _cn_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '零': 0}
        val = 0
        i = 0
        while i < len(cn_num):
            c = cn_num[i]
            if i + 1 < len(cn_num) and cn_num[i+1] == '十':
                val += _cn_map.get(c, 1) * 10
                i += 2
                if i < len(cn_num):
                    val += _cn_map.get(cn_num[i], 0)
                    i += 1
            elif c == '十':
                val += 10
                i += 1
                if i < len(cn_num):
                    val += _cn_map.get(cn_num[i], 0)
                    i += 1
            elif i + 1 < len(cn_num) and cn_num[i+1] == '百':
                val += _cn_map.get(c, 1) * 100
                i += 2
                if i < len(cn_num):
                    val += _cn_map.get(cn_num[i], 0)
                    i += 1
            else:
                val += _cn_map.get(c, 0)
                i += 1
        return val

    
    def format_filename(self, filename):
        filename = Mutil.remove_zero_width_chars(filename)
        _var_var_42 = configEnv.custom_words_replace
        for _var_var_43 in _var_var_42:
            filename = re.sub(_var_var_43['old'], _var_var_43['new'], filename)
        _var_var_44 = load_words_replace_from_env()
        for _var_var_43 in _var_var_44:
            filename = re.sub(_var_var_43['old'], _var_var_43['new'], filename)
        filename = re.sub(self.del_separators, '.', filename)
        filename = re.sub('\\.+', '.', filename)
        filename = re.sub('([：:])\\.', '\\1', filename)
        filename = filename.strip('.')
        filename = self.reformat_season_year(filename)
        self.format_name = filename
        return None
        return None

    
    def reformat_season_year(self, filename):
        _var_var_16 = '(.*?)(S\\d+\\.?E[P]?\\d+|E[P]?\\d+)\\.(\\d{4})\\.(.*)'
        _var_var_18 = re.search(_var_var_16, filename, re.IGNORECASE)
        if _var_var_18:
            _var_var_45 = _var_var_18.group(1).rstrip('.')
            _var_var_46 = _var_var_18.group(2)
            _var_var_47 = _var_var_18.group(3)
            _var_var_48 = _var_var_18.group(4)
            return f'''{_var_var_45}.{_var_var_47}.{_var_var_46}.{_var_var_48}'''
        return None
        return filename
        return None

    
    def build_name_year_1(self, name):
        if not name:
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_cn_name})[.\\-\\s]*[（(]({self.re_year_num})[)）]''', name)
        if _var_var_49:
            if not self.name:
                self.name = _var_var_49.group(1)
            if not self.year:
                self.year = _var_var_49.group(2)
            else:
                _var_var_49 = re.search(f'''({self.re_en_name})[.\\-\\s]*[（(]({self.re_year_num})[)）]''', name)
                if _var_var_49:
                    if not self.en_name:
                        self.en_name = _var_var_49.group(1)
                    if not self.year:
                        self.year = _var_var_49.group(2)
        return None
        return None

    
    def build_name_year_2(self, name):
        if not name:
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_cn_name})[.\\-\\s]+({self.re_en_name})[.\\-\\s]+({self.re_year_num})(?![a-zA-Z0-9])''', name)
        if _var_var_49:
            if not self.name:
                self.name = _var_var_49.group(1)
            if not self.en_name:
                self.en_name = _var_var_49.group(2)
            if not self.year:
                self.year = _var_var_49.group(3)
            else:
                _var_var_49 = re.search(f'''({self.re_cn_name})[.\\-\\s]+({self.re_year_num})(?![a-zA-Z0-9])''', name)
                if _var_var_49:
                    if not self.name:
                        self.name = _var_var_49.group(1)
                    if not self.year:
                        self.year = _var_var_49.group(2)
        return None
        return None

    
    def build_name_year_3(self, name):
        if not name:
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_en_name})[.\\-\\s]+({self.re_year_num})(?![a-zA-Z0-9])''', name)
        if _var_var_49:
            if not self.en_name:
                self.en_name = _var_var_49.group(1)
            if not self.year:
                self.year = _var_var_49.group(2)
        return None
        return None

    
    def build_name_year_4(self, name):
        if not name:
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_cn_name})[.\\-\\s]+(s\\d+e\\d+|s\\d+ep\\d+|e\\d+|ep\\d+)''', name, re.IGNORECASE)
        if not _var_var_49 and self.name:
            self.name = _var_var_49.group(1)
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_en_name})[.\\-\\s]+(s\\d+e\\d+|s\\d+ep\\d+|e\\d+|ep\\d+)''', name, re.IGNORECASE)
        if not _var_var_49 and self.en_name:
            _var_var_50 = _var_var_49.group(1)
            _var_var_50 = re.sub('[.\\-\\s]*(\\d{3,4}[ip]|4k|8k|16k)$', '', _var_var_50, flags = re.I)
            self.en_name = _var_var_50
            return None
        return None
        _var_var_49 = re.search(f'''({self.re_en_name})[.\\-\\s]+(\\d{{3,4}}[ip]|4k|8k|16k)''', name, re.IGNORECASE)
        if not _var_var_49 and self.en_name:
            _var_var_50 = _var_var_49.group(1)
            self.en_name = _var_var_50
        return None
        return None

    
    def build_name_year_5(self, name):
        if name and self.name or self.en_name:
            return None
        return None
        if re.match('^[\\u4e00-\\u9fff]', name):
            _var_var_28 = re.search(f'''^{self.re_cn_name}''', name)
            if _var_var_28:
                self.name = _var_var_28.group(0)
        return None
        return None

    
    def build_name_aliases(self, name):
        """
        从字符串中匹配出多个中文名称
        例如: 张三.李四.王五 会匹配出 ['张三','李四','王五']
        """
        if not name:
            return None
        return None
        _var_var_51 = re.findall(f'''{self.re_cn_name}''', name)
        if _var_var_51:
            self.name_aliases = _var_var_51
        return None
        return None

    
    def build_year(self):
        if self.year:
            return None
        return None
        _var_var_31 = re.search(f'''({self.re_year_x})''', self.format_name)
        if not _var_var_31:
            _var_var_31 = re.search(f'''({self.re_year_x})''', self._VideoInfo__p_name)
        if not _var_var_31:
            _var_var_31 = re.search(f'''({self.re_year_x})''', self._VideoInfo__pp_name)
        if _var_var_31:
            self.year = _var_var_31.group()
        return None
        return None

    
    def build_tmdb_id(self):
        self.build_tmdb_id_impl(self.format_name)
        self.build_tmdb_id_impl(self._VideoInfo__p_name)
        self.build_tmdb_id_impl(self._VideoInfo__pp_name)
        return None
        return None

    
    def build_tmdb_id_impl(self, name):
        if self.tmdb_id:
            return None
        return None
        _var_var_52 = re.search('(?:tmdb_?id[-=.]|tmdb[-=.])(\\d+)', name, re.I)
        if not _var_var_52 and self.tmdb_id:
            self.tmdb_id = _var_var_52.group(1)
        return None
        return None

    
    def get_season_num(self, name):
        _var_var_24 = re.search('[Ss](\\d{1,2})(?:[Ee]|\\.|$)|第([一二三四五六七八九十百零\\d]{1,3})季', name)
        if _var_var_24:
            return int(_var_var_24.group(1)) if _var_var_24.group(1) else self.convert_cn_num(_var_var_24.group(2))
        return None
        return None
        return None


if __name__ == '__main__':
    media_info = VideoInfo('/OBSOLETE(2019)/Season 1/OBSOLETE - 06 [WebRip 1080p HEVC-10bit AAC SRTx2].mkv')
    print(media_info.to_json())
    print(media_info.name + '|' + media_info.en_name + '|' + media_info.year)
    media_info = VideoInfo('/海贼王.1996.S22E132.1080p-DISC2.CR-.mkv')
    media_info.build_year()
    media_info.build_name_year_4('Youthful.Glory.S01E06.1080p.NF.WEB-DL.DDP5.1.H.264-MWeb.mkv')
    print(media_info.to_json())

