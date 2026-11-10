import colorsys
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import math


import random
from app.modules.cover import poster_config
from app.core.env import configEnv, novaEnv
from app.core.env2 import config2Env
from app.log import logger

def create_gradient_background(width, height, color1, color2):
    '''
    创建一个从左到右、由深到浅的渐变背景
    增加多种色系选择，大幅提高颜色组合数量

    参数:
        width: 背景宽度
        height: 背景高度
        color1: 左侧颜色(深色)，如果为None则随机生成
        color2: 右侧颜色(浅色)，如果为None则随机生成

    返回:
        渐变背景图像
    '''
    if color1 is None:
        _var_var_0 = random.randint(0, 25)
        if _var_var_0 == 0:
            color1 = (random.randint(80, 150), random.randint(20, 70), random.randint(20, 70))
        elif _var_var_0 == 1:
            color1 = (random.randint(80, 150), random.randint(50, 100), random.randint(20, 50))
        elif _var_var_0 == 2:
            color1 = (random.randint(80, 150), random.randint(70, 140), random.randint(20, 50))
        elif _var_var_0 == 3:
            color1 = (random.randint(20, 70), random.randint(80, 150), random.randint(40, 90))
        elif _var_var_0 == 4:
            color1 = (random.randint(20, 70), random.randint(50, 100), random.randint(80, 150))
        elif _var_var_0 == 5:
            color1 = (random.randint(60, 120), random.randint(20, 80), random.randint(80, 150))
        elif _var_var_0 == 6:
            color1 = (random.randint(60, 100), random.randint(10, 30), random.randint(10, 30))
        elif _var_var_0 == 7:
            color1 = (random.randint(70, 120), random.randint(10, 40), random.randint(30, 70))
        elif _var_var_0 == 8:
            color1 = (random.randint(70, 120), random.randint(30, 70), random.randint(10, 40))
        elif _var_var_0 == 9:
            color1 = (random.randint(70, 130), random.randint(40, 80), random.randint(0, 30))
        elif _var_var_0 == 10:
            color1 = (random.randint(70, 130), random.randint(60, 110), random.randint(0, 30))
        elif _var_var_0 == 11:
            color1 = (random.randint(50, 100), random.randint(60, 110), random.randint(0, 40))
        elif _var_var_0 == 12:
            color1 = (random.randint(0, 50), random.randint(60, 110), random.randint(0, 50))
        elif _var_var_0 == 13:
            color1 = (random.randint(20, 60), random.randint(50, 100), random.randint(30, 80))
        elif _var_var_0 == 14:
            color1 = (random.randint(0, 50), random.randint(60, 110), random.randint(60, 110))
        elif _var_var_0 == 15:
            color1 = (random.randint(0, 50), random.randint(50, 100), random.randint(70, 120))
        elif _var_var_0 == 16:
            color1 = (random.randint(0, 40), random.randint(0, 50), random.randint(70, 120))
        elif _var_var_0 == 17:
            color1 = (random.randint(20, 60), random.randint(0, 40), random.randint(70, 130))
        elif _var_var_0 == 18:
            color1 = (random.randint(40, 90), random.randint(0, 40), random.randint(70, 130))
        elif _var_var_0 == 19:
            color1 = (random.randint(70, 120), random.randint(0, 40), random.randint(70, 120))
        elif _var_var_0 == 20:
            _var_var_1 = random.randint(40, 80)
            color1 = (_var_var_1, _var_var_1, _var_var_1)
        elif _var_var_0 == 21:
            _var_var_1 = random.randint(40, 80)
            color1 = (_var_var_1, _var_var_1 + random.randint(10, 30), _var_var_1 - random.randint(5, 15))
        elif _var_var_0 == 22:
            _var_var_1 = random.randint(40, 80)
            color1 = (_var_var_1, _var_var_1 - random.randint(5, 15), _var_var_1 + random.randint(10, 30))
        elif _var_var_0 == 23:
            color1 = (random.randint(60, 100), random.randint(40, 80), random.randint(20, 50))
        elif _var_var_0 == 24:
            color1 = (random.randint(80, 120), random.randint(60, 100), random.randint(10, 40))
        else:
            color1 = (random.randint(50, 90), random.randint(60, 100), random.randint(30, 70))
    if color2 is None:
        _var_var_0 = random.randint(0, 25)
        if _var_var_0 == 0:
            color2 = (random.randint(180, 255), random.randint(100, 180), random.randint(100, 180))
        elif _var_var_0 == 1:
            color2 = (random.randint(200, 255), random.randint(150, 220), random.randint(70, 150))
        elif _var_var_0 == 2:
            color2 = (random.randint(200, 255), random.randint(180, 255), random.randint(70, 150))
        elif _var_var_0 == 3:
            color2 = (random.randint(100, 180), random.randint(180, 255), random.randint(120, 200))
        elif _var_var_0 == 4:
            color2 = (random.randint(100, 180), random.randint(150, 220), random.randint(180, 255))
        elif _var_var_0 == 5:
            color2 = (random.randint(150, 220), random.randint(100, 170), random.randint(180, 255))
        elif _var_var_0 == 6:
            color2 = (random.randint(220, 255), random.randint(50, 100), random.randint(50, 100))
        elif _var_var_0 == 7:
            color2 = (random.randint(220, 255), random.randint(100, 160), random.randint(130, 190))
        elif _var_var_0 == 8:
            color2 = (random.randint(230, 255), random.randint(130, 200), random.randint(30, 90))
        elif _var_var_0 == 9:
            color2 = (random.randint(230, 255), random.randint(110, 170), random.randint(100, 160))
        elif _var_var_0 == 10:
            color2 = (random.randint(230, 255), random.randint(200, 255), random.randint(100, 160))
        elif _var_var_0 == 11:
            color2 = (random.randint(200, 255), random.randint(230, 255), random.randint(50, 130))
        elif _var_var_0 == 12:
            color2 = (random.randint(130, 190), random.randint(230, 255), random.randint(100, 160))
        elif _var_var_0 == 13:
            color2 = (random.randint(50, 110), random.randint(220, 255), random.randint(50, 130))
        elif _var_var_0 == 14:
            color2 = (random.randint(50, 110), random.randint(200, 255), random.randint(200, 255))
        elif _var_var_0 == 15:
            color2 = (random.randint(100, 160), random.randint(180, 230), random.randint(230, 255))
        elif _var_var_0 == 16:
            color2 = (random.randint(50, 130), random.randint(130, 190), random.randint(230, 255))
        elif _var_var_0 == 17:
            color2 = (random.randint(150, 210), random.randint(100, 160), random.randint(230, 255))
        elif _var_var_0 == 18:
            color2 = (random.randint(180, 230), random.randint(130, 190), random.randint(220, 255))
        elif _var_var_0 == 19:
            color2 = (random.randint(230, 255), random.randint(130, 190), random.randint(200, 255))
        elif _var_var_0 == 20:
            _var_var_1 = random.randint(200, 240)
            color2 = (_var_var_1, _var_var_1, _var_var_1)
        elif _var_var_0 == 21:
            color2 = (random.randint(220, 255), random.randint(180, 230), random.randint(80, 140))
        elif _var_var_0 == 22:
            color2 = (random.randint(220, 255), random.randint(210, 245), random.randint(170, 220))
        elif _var_var_0 == 23:
            color2 = (random.randint(180, 230), random.randint(140, 190), random.randint(100, 160))
        elif _var_var_0 == 24:
            color2 = (random.randint(150, 200), random.randint(220, 255), random.randint(180, 230))
        else:
            color2 = (random.randint(220, 255), random.randint(220, 255), random.randint(220, 255))
    _var_var_2 = Image.new('RGBA', (width, height), color1)
    _var_var_3 = ImageDraw.Draw(_var_var_2)
    for _var_var_4 in range(width):
        _var_var_5 = int(color1[0] + (color2[0] - color1[0]) * _var_var_4 / width)
        _var_var_6 = int(color1[1] + (color2[1] - color1[1]) * _var_var_4 / width)
        _var_var_7 = int(color1[2] + (color2[2] - color1[2]) * _var_var_4 / width)
        _var_var_3.line([(_var_var_4, 0), (_var_var_4, height)], fill=(_var_var_5, _var_var_6, _var_var_7, 255))
def create_gradient_background_v2(width, height, name, color):
    '''
    创建一个从左到右的渐变背景，使用遮罩技术实现渐变效果
    左侧颜色更深，右侧颜色适中，提供更明显的渐变效果

    参数:
        width: 背景宽度
        height: 背景高度
        color: 颜色数组或单个颜色，如果为None则随机生成
              如果是数组，会依次尝试每个颜色，跳过太黑或太淡的颜色

    返回:
        渐变背景图像
    '''
    
    def _var_var_8(input_rgb):
        '''
        将各种可能的输入格式，统一提取成 (r, g, b) 三元组。
        支持：
        - (r, g, b)
        - (r, g, b, a)
        - ((r, g, b), idx) or ((r, g, b, a), idx)
        '''
        if isinstance(input_rgb, tuple):
            if len(input_rgb) == 2 and isinstance(input_rgb[0], tuple):
                return _var_var_8(input_rgb[0])
            return None
        if len(input_rgb) == 4 and all(isinstance(x, (int, float)) for x in input_rgb):
            return input_rgb[:3]
        if len(input_rgb) == 3 and all(isinstance(x, (int, float)) for x in input_rgb):
            return input_rgb
        raise ValueError(f'无法识别的颜色格式: {input_rgb!r}')

    
    def _var_var_9(input_rgb, min_lum, max_lum):
        '''
        基于相对亮度判断：不过暗（>=min_lum）也不过白（<=max_lum）。
        input_rgb 可为多种格式，函数内部会 normalize。
        '''
        (_var_var_5, _var_var_6, _var_var_7) = _var_var_8(input_rgb)
        _var_var_22 = 0.299 * _var_var_5 + 0.587 * _var_var_6 + 0.114 * _var_var_7
        return min_lum <= _var_var_22 <= max_lum
        return None

    
    def _var_var_10(input_rgb, min_l, max_l):
        '''
        基于 HSL Lightness 判断。Lightness 在 [0,1]。
        '''
        (_var_var_5, _var_var_6, _var_var_7) = _var_var_8(input_rgb)
        _var_var_25 = _var_var_7 / 255
        _var_var_24 = _var_var_6 / 255
        _var_var_23 = _var_var_5 / 255
        (_var_var_26, _var_var_27, _var_var_28) = colorsys.rgb_to_hls(_var_var_23, _var_var_24, _var_var_25)
        return min_l <= _var_var_27 <= max_l
        return None

    _var_var_11 = None
    if isinstance(color, list) and len(color) > 0:
        for _var_var_12 in range(min(10, len(color))):
            if _var_var_10(color[_var_var_12]):
                logger.info(f'''{name} 海报主题色:[{_var_var_11}]适合做背景''')
                None if isinstance(color[_var_var_12], tuple) and len(color[_var_var_12]) == 2 and isinstance(color[_var_var_12][0], tuple) else range(min(10, len(color)))
            else:
                logger.info(f'''{name} 海报主题色:[{color[_var_var_12]}]不适合做背景,尝试取下一个海报的颜色''')


def get_poster_primary_color(image_path):
    '''
    分析图片并提取主色调

    参数:
        image_path: 图片文件路径

    返回:
        主色调颜色，RGBA格式
    '''
    try:
        from collections import Counter as _var_var_29
        _var_var_30 = Image.open(image_path)
        _var_var_30 = _var_var_30.resize((100, 150), Image.LANCZOS)
        if _var_var_30.mode != 'RGBA':
            _var_var_30 = _var_var_30.convert('RGBA')
        _var_var_31 = list(_var_var_30.getdata())
        _var_var_32 = []
        for _var_var_33 in _var_var_31:
            _var_var_5, _var_var_6, _var_var_7, _var_var_34 = _var_var_33
            if _var_var_34 < 200:
                continue
            _var_var_35 = (_var_var_5 + _var_var_6 + _var_var_7) / 3
            if _var_var_35 < 30 or _var_var_35 > 220:
                continue
            _var_var_32.append((_var_var_5, _var_var_6, _var_var_7, 255))
        if not _var_var_32:
            _var_var_32 = [(_var_var_36[0], _var_var_36[1], _var_var_36[2], 255) for _var_var_36 in _var_var_31 if _var_var_36[3] > 100]
        if not _var_var_32:
            return (150, 100, 50, 255)
        _var_var_37 = _var_var_29(_var_var_32)
        _var_var_38 = _var_var_37.most_common(10)
        if _var_var_38:
            return _var_var_38
        _var_var_39 = sum(_var_var_36[0] for _var_var_36 in _var_var_32) // len(_var_var_32)
        _var_var_40 = sum(_var_var_36[1] for _var_var_36 in _var_var_32) // len(_var_var_32)
        _var_var_41 = sum(_var_var_36[2] for _var_var_36 in _var_var_32) // len(_var_var_32)
        return [(_var_var_39, _var_var_40, _var_var_41, 255)]
    except Exception as _var_var_42:
        logger.error(f'获取图片主色调时出错: {_var_var_42}')
        return [(150, 100, 50, 255)]