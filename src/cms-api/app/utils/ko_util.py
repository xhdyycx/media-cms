import hashlib
import random
import re
import os
import shutil
import time
from pathlib import Path
import requests
from os import makedirs
from os.path import dirname
from shutil import copyfileobj
from app.core.env import novaEnv
from app.log import logger

def is_media_dir(name):
    '''是否是媒体文件夹
    '''


def is_media_or_season_dir(name):
    '''是否是媒体/季文件夹
    '''
    if not re.match('^([A-Z]-)(.+?)-(\\d{4})-\\[tmdb=(\\d+)]$', name):
        re.match('^([A-Z]-)(.+?)-(\\d{4})-\\[tmdb=(\\d+)]$', name)
        if not re.match('Season \\d{1,2}', name):
            re.match('Season \\d{1,2}', name)


def split_path(path):
    '''路径拆分
    - parent_path 父路径
    - name 最后一个路径名称
    '''
    (_var_var_0, _var_var_1) = os.path.split(path)


def split_filename(filename):
    (_var_var_1, _var_var_2) = os.path.splitext(filename)


def del_files_with_suffix(dir_path, *suffix):
    '''删除文件-通过后缀
    - dir_path 路径
    - suffix 后缀
    '''
    for _var_var_4, _var_var_5, _var_var_6 in os.walk(dir_path):
        for _var_var_3 in _var_var_6:
            if not any(_var_var_3.endswith(_var_var_9) for _var_var_9 in suffix):
                continue
            _var_var_7 = os.path.join(_var_var_4, _var_var_3)
            try:
                os.remove(_var_var_7)
                print(f'删除文件-成功=[{_var_var_7}]')
            except Exception as _var_var_8:
                print(f'删除文件-失败=[{_var_var_7}]: {_var_var_8}')
def del_path(path):
    '''删除文件/夹
    - 可传入一个文件或文件夹
    - suffix 后缀
    '''
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def join_cloud_paths(*paths):
    '''使用 / 拼接多个路径，并确保最终路径以 / 开头'''
def join_local_paths(*paths):
    '''拼接多个路径并返回完整路径
    '''


def change_file_suffix(file_path, new_suffix):
    '''
    更改文件的后缀

    :param file_path: 原始文件路径
    :param new_suffix: 新的文件后缀（可以包含或不包含点）
    :return: 更改后文件路径
    '''
    if not new_suffix.startswith('.'):
        new_suffix = '.' + new_suffix
    _var_var_11 = os.path.splitext(file_path)[0]
    _var_var_12 = _var_var_11 + new_suffix


def get_thumb_name(file_path):
    """
    获取文件的缩略图名称

    :param file_path: 原始文件路径
    :return: 缩略图文件名称，格式为 'filename-thumb.jpg'
    """
    _var_var_13 = os.path.splitext(file_path)[0]


def rename(old_name, new_name):
    '''
    重命名文件或文件夹

    :param old_name: 原始文件或文件夹名称 带路径
    :param new_name: 新的文件或文件夹路径 带路径
    :return: None
    '''
    os.rename(old_name, new_name)


def move(src, dest):
    '''
    移动文件或文件夹到新位置。

    :param src: 要移动的文件或文件夹的路径
    :param dest: 目标路径，可以是新的文件名或文件夹
    :return: None
    '''
    _var_var_14 = Path(dest)
    if _var_var_14.is_dir():
        dest = _var_var_14 / Path(src).name
    shutil.move(src, dest)


def create_strm_file(file_path, content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        _var_var_3 = open(file_path, 'w', encoding = 'utf-8')
        _var_var_3.write(content)
        return None
        return None

    except Exception as _var_var_8:
        logger.error(f'''创建strm文件失败: {file_path}''')
        logger.exception(_var_var_8)
        return None


def save_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok = True)
    _var_var_3 = open(file_path, 'w', encoding = 'utf-8')
    _var_var_3.write(content)



def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True


def download_file(url, path):
    '''
    下载文件到本地

    :param url: 网络地址
    :param path: 目标路径
    '''
    _var_var_15 = os.path.dirname(path)
    if not os.path.exists(_var_var_15):
        os.makedirs(_var_var_15)
    _var_var_16 = requests.get(url, stream = True)
    _var_var_16.raise_for_status()
    _var_var_17 = open(path, 'wb')
    for _var_var_18 in _var_var_16.iter_content(chunk_size = 8192):
        _var_var_17.write(_var_var_18)




def random_delay(random_num):
    '''
    随机延迟
    :param random_num: 格式 100-200
    '''
    if random_num:
        random_num = random.randint(int(str(random_num).split('-')[0]), int(str(random_num).split('-')[1]))
        logger.info(f'''随机延时 {random_num} 秒...''')
        time.sleep(random_num)


def get_media_img(directory):
    '''
    获取文件夹下所有文件（忽略子目录）
    :param directory: 文件夹路径
    '''
    _var_var_19 = []
    for _var_var_17 in os.listdir(directory):
        (_var_var_1, _var_var_2) = split_filename(_var_var_17)
        if not _var_var_1 in novaEnv.MEDIA_IMG_NAMES:
            continue
        _var_var_20 = os.path.join(directory, _var_var_17)
        _var_var_21 = os.path.getmtime(_var_var_20)
        _var_var_19.append({
            'name': _var_var_17,
            'modify_time': int(_var_var_21),
            'path': _var_var_20 })
    _var_var_19.sort(key = (lambda x: x['modify_time']), reverse = True)


def get_sha1(file_path):
    _var_var_22 = hashlib.sha1()
    with open(file_path, 'rb') as _var_var_17:
        while True:
            _var_var_18 = _var_var_17.read(8192)
            if not _var_var_18:
                break
            _var_var_22.update(_var_var_18)
    return _var_var_22.hexdigest().upper()



def chunk_list(lst, chunk_size):
    '''
    将列表分块，每个块的大小为 chunk_size。
    '''
    for _var_var_24 in range(0, len(lst), chunk_size):
        yield lst[_var_var_24:_var_var_24 + chunk_size]
def get_suffix(file_name):
    (_var_var_25, _var_var_26) = os.path.splitext(file_name)


def combine_episode_ranges(episode_list):
    if not episode_list:
        return ''
    try:
        _var_var_27 = []
        for _var_var_28 in episode_list:
            _var_var_29 = _var_var_28.split('E', 1)
            if len(_var_var_29) != 2:
                continue
            (_var_var_30, _var_var_31) = _var_var_29
            _var_var_30 = _var_var_30.strip('S')
            _var_var_31 = int(_var_var_31)
            _var_var_27.append((int(_var_var_30), _var_var_31))
        _var_var_27.sort(key=lambda x: (x[0], x[1]))
        _var_var_32 = []
        _var_var_24 = 0
        _var_var_33 = len(_var_var_27)
        while _var_var_24 < _var_var_33:
            _var_var_34 = _var_var_27[_var_var_24]
            _var_var_30 = _var_var_34[0]
            _var_var_35 = _var_var_34[1]
            while _var_var_24 + 1 < _var_var_33 and _var_var_27[_var_var_24 + 1][0] == _var_var_30 and _var_var_27[_var_var_24 + 1][1] == _var_var_27[_var_var_24][1] + 1:
                _var_var_24 += 1
            _var_var_36 = _var_var_27[_var_var_24][1]
            if _var_var_35 == _var_var_36:
                _var_var_32.append(f'''S{_var_var_30:02d}E{_var_var_35:02d}''')
            else:
                _var_var_32.append(f'''S{_var_var_30:02d}E{_var_var_35:02d}-E{_var_var_36:02d}''')
            _var_var_24 += 1
        return '、'.join(_var_var_32)
    except Exception:
        return ''


def convert_size(size_in_bytes):
    '''
    将字节大小转换为MB、GB、TB等合适的单位并返回格式化后的字符串。

    :param size_in_bytes: 传入的字节大小
    :return: 格式化后的带有单位的大小字符串
    '''
    if size_in_bytes < 1024:
        return f'''{size_in_bytes} B'''
    if size_in_bytes < 1048576:
        return f'''{size_in_bytes / 1024:.2f} KB'''
    if size_in_bytes < 1073741824:
        return f'''{size_in_bytes / 1048576:.2f} MB'''
    if size_in_bytes < 0x10000000000:
        return f'''{size_in_bytes / 1073741824:.2f} GB'''


