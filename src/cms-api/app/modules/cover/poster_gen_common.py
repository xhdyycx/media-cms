from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os


import random
from app.modules.cover import poster_config
from app.core.env import novaEnv
from app.core.env2 import config2Env
from app.log import logger
from app.modules.cover.poster_gen_gradients import get_poster_primary_color
import colorsys
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import math


import random
from app.modules.cover import poster_config
from app.core.env import configEnv, novaEnv
from app.core.env2 import config2Env
from app.log import logger

def add_shadow(img, offset, shadow_color, blur_radius):
    '''
    给图片添加右侧和底部阴影

    参数:
        img: 原始图片（PIL.Image对象）
        offset: 阴影偏移量，(x, y)格式
        shadow_color: 阴影颜色，RGBA格式
        blur_radius: 阴影模糊半径

    返回:
        添加了阴影的新图片
    '''
    _var_var_0 = img.width + offset[0] + blur_radius * 2
    _var_var_1 = img.height + offset[1] + blur_radius * 2
    _var_var_2 = Image.new('RGBA', (_var_var_0, _var_var_1), (0, 0, 0, 0))
    _var_var_3 = Image.new('RGBA', img.size, shadow_color)
    _var_var_2.paste(_var_var_3, (blur_radius + offset[0], blur_radius + offset[1]))
    _var_var_2 = _var_var_2.filter(ImageFilter.GaussianBlur(blur_radius))
    _var_var_4 = Image.new('RGBA', _var_var_2.size, (0, 0, 0, 0))
    _var_var_4.paste(img, (blur_radius, blur_radius), img if img.mode == 'RGBA' else None)
    _var_var_5 = Image.alpha_composite(_var_var_2, _var_var_4)


def draw_text_on_image(image, text, position, font_path, font_size, fill_color):
    '''
    在图像上绘制文字

    参数:
        image: PIL.Image对象
        text: 要绘制的文字
        position: 文字位置 (x, y)
        font_path: 字体文件路径
        font_size: 字体大小
        fill_color: 文字颜色，RGBA格式

    返回:
        添加了文字的图像
    '''
    _var_var_6 = image.copy()
    _var_var_7 = ImageDraw.Draw(_var_var_6)
    font_path = os.path.join(poster_config.CURRENT_DIR, font_path)
    _var_var_8 = ImageFont.truetype(font_path, font_size)
    _var_var_7.text(position, text, font = _var_var_8, fill = fill_color)


def draw_multiline_text_on_image(image, text, position, font_path, font_size, line_spacing, fill_color):
    '''
    在图像上绘制多行文字，根据空格自动换行

    参数:
        image: PIL.Image对象
        text: 要绘制的文字
        position: 第一行文字位置 (x, y)
        font_path: 字体文件路径
        font_size: 字体大小
        line_spacing: 行间距
        fill_color: 文字颜色，RGBA格式

    返回:
        添加了文字的图像和行数
    '''
    _var_var_6 = image.copy()
    _var_var_7 = ImageDraw.Draw(_var_var_6)
    font_path = os.path.join(poster_config.CURRENT_DIR, font_path)
    _var_var_8 = ImageFont.truetype(font_path, font_size)
    _var_var_9 = text.split(' ')
    if len(_var_var_9) <= 1:
        _var_var_7.text(position, text, font = _var_var_8, fill = fill_color)
        return (_var_var_6, 1)
    (_var_var_10, _var_var_11) = position
    for _var_var_12, _var_var_13 in enumerate(_var_var_9):
        _var_var_14 = _var_var_11 + _var_var_12 * (font_size + line_spacing)
        _var_var_7.text((_var_var_10, _var_var_14), _var_var_13, font = _var_var_8, fill = fill_color)


def get_random_color(image_path):
    '''
    获取图片随机位置的颜色

    参数:
        image_path: 图片文件路径

    返回:
        随机点颜色，RGBA格式
    '''
    try:
        _var_var_15 = Image.open(image_path)
        (_var_var_16, _var_var_17) = _var_var_15.size
        _var_var_18 = random.randint(int(_var_var_16 * 0.5), int(_var_var_16 * 0.8))
        _var_var_19 = random.randint(int(_var_var_17 * 0.5), int(_var_var_17 * 0.8))
        if _var_var_15.mode == 'RGBA':
            (_var_var_20, _var_var_21, _var_var_22, _var_var_23) = _var_var_15.getpixel((_var_var_18, _var_var_19))
            return (_var_var_20, _var_var_21, _var_var_22, _var_var_23)
        if _var_var_15.mode == 'RGB':
            (_var_var_20, _var_var_21, _var_var_22) = _var_var_15.getpixel((_var_var_18, _var_var_19))
            return (_var_var_20 + 100, _var_var_21 + 50, _var_var_22, 255)
        _var_var_15 = _var_var_15.convert('RGBA')
        (_var_var_20, _var_var_21, _var_var_22, _var_var_23) = _var_var_15.getpixel((_var_var_18, _var_var_19))
        return (_var_var_20, _var_var_21, _var_var_22, _var_var_23)
    except Exception as _var_var_24:
        logger.info(f'获取图片颜色时出错: {_var_var_24}')
        return None


def draw_color_block(image, position, size, color):
    '''
    在图像上绘制色块

    参数:
        image: PIL.Image对象
        position: 色块位置 (x, y)
        size: 色块大小 (width, height)
        color: 色块颜色，RGBA格式

    返回:
        添加了色块的图像
    '''
    _var_var_6 = image.copy()
    _var_var_7 = ImageDraw.Draw(_var_var_6)
    _var_var_7.rectangle([
        position,
        (position[0] + size[0], position[1] + size[1])], fill = color)


def _parse_rgb_config(value):
    if not value:
        return None
    try:
        return tuple(map(int, value.split(',')))
    except Exception:
        return None


def _get_matched_template(name):
    _var_var_25 = { }
    _var_var_26 = config2Env.e_cover_gen_template_mapping
    _var_var_27 = _var_var_26.get('template_mapping', [])
    for _var_var_28 in _var_var_27:
        if not _var_var_28.get('library_name') == name:
            continue
        _var_var_25 = _var_var_28
        _var_var_27


def _get_library_names(name, matched_template):
    _var_var_29 = name
    _var_var_30 = ''
    if matched_template:
        _var_var_29 = matched_template.get('library_ch_name', _var_var_29)
        _var_var_30 = matched_template.get('library_eng_name', _var_var_30)


def _get_font_path(font_name, default_font_name):
    if font_name:
        return os.path.join(novaEnv.CONFIG_PATH, font_name)


def _get_primary_color_value(image_path, default):
    _var_var_31 = get_poster_primary_color(image_path)
    if not _var_var_31:
        return default
    _var_var_32 = _var_var_31[0]
    if isinstance(_var_var_32, tuple) and len(_var_var_32) == 2 and isinstance(_var_var_32[0], tuple):
        return _var_var_32[0]
    if isinstance(_var_var_32, tuple) and len(_var_var_32) >= 3:
        return _var_var_32


def _get_ordered_poster_files(poster_folder, template_mapping_config, limit, default_order):
    _var_var_34 = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    _var_var_35 = template_mapping_config.get('poster_position', default_order)


def _get_first_image_file(folder):
    _var_var_34 = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    if not os.path.exists(folder):
        return None


def _resize_crop(image, size):
    (_var_var_41, _var_var_42) = size
    _var_var_43 = _var_var_41 / image.width
    _var_var_44 = _var_var_42 / image.height
    _var_var_45 = max(_var_var_43, _var_var_44)
    _var_var_46 = int(image.width * _var_var_45)
    _var_var_47 = int(image.height * _var_var_45)
    _var_var_48 = image.resize((_var_var_46, _var_var_47), Image.LANCZOS)
    _var_var_49 = (_var_var_46 - _var_var_41) // 2
    _var_var_50 = (_var_var_47 - _var_var_42) // 2


def _rounded_image(image, radius):
    if radius <= 0:
        return image.convert('RGBA')
    image = image.convert('RGBA')
    _var_var_51 = Image.new('L', image.size, 0)
    _var_var_7 = ImageDraw.Draw(_var_var_51)
    _var_var_7.rounded_rectangle([
        (0, 0),
        image.size], radius = radius, fill = 255)
    _var_var_4 = Image.new('RGBA', image.size, (0, 0, 0, 0))
    _var_var_4.paste(image, (0, 0), _var_var_51)


def _draw_text_fit(draw, text, position, font_path, max_font_size, max_width, fill, min_font_size):
    _var_var_52 = max_font_size
    while _var_var_52 > min_font_size:
        _var_var_8 = ImageFont.truetype(font_path, _var_var_52)
        _var_var_53 = draw.textbbox(position, text, font = _var_var_8)
        if _var_var_53[2] - _var_var_53[0] <= max_width:
            return _var_var_8
        _var_var_52 -= 4
    return ImageFont.truetype(font_path, min_font_size)


def _relative_luminance(color):
    
    def _var_var_54(channel):
        channel = channel / 255
        if channel <= 0.03928:
            return channel / 12.92
        return None
        return ((channel + 0.055) / 1.055) ** 2.4
        return None

    (_var_var_20, _var_var_21, _var_var_22) = color[:3]


def _contrast_ratio(color1, color2):
    _var_var_55 = _relative_luminance(color1)
    _var_var_56 = _relative_luminance(color2)
    _var_var_57 = max(_var_var_55, _var_var_56)
    _var_var_58 = min(_var_var_55, _var_var_56)


def _sample_average_color(image, box):
    (_var_var_16, _var_var_17) = image.size
    (_var_var_49, _var_var_50, _var_var_59, _var_var_60) = box
    _var_var_49 = max(0, min(_var_var_16, int(_var_var_49)))
    _var_var_50 = max(0, min(_var_var_17, int(_var_var_50)))
    _var_var_59 = max(_var_var_49 + 1, min(_var_var_16, int(_var_var_59)))
    _var_var_60 = max(_var_var_50 + 1, min(_var_var_17, int(_var_var_60)))
    _var_var_61 = image.crop((_var_var_49, _var_var_50, _var_var_59, _var_var_60)).resize((1, 1), Image.LANCZOS).convert('RGB')


def _mix_color(color, target, ratio):
    return tuple(int(c * (1 - ratio) + t * ratio) for c, t in zip(color[:3], target[:3]))


def _fit_text_color(base_color, background_color, min_contrast):
    _var_var_62 = tuple(base_color[:3])
    if _contrast_ratio(_var_var_62, background_color) >= min_contrast:
        return _var_var_62
    _var_var_63 = _mix_color(_var_var_62, (255, 255, 255), 0.62)
    _var_var_64 = _mix_color(_var_var_62, (0, 0, 0), 0.62)
    if _contrast_ratio(_var_var_63, background_color) >= _contrast_ratio(_var_var_64, background_color):
        return _var_var_63


