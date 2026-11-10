# app.modules.cover.poster_gen_styles
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from app.modules.cover import poster_config
from app.core.env import novaEnv
from app.log import logger
from app.modules.cover.poster_gen_common import (
    _draw_text_fit, _fit_text_color, _get_first_image_file, _get_font_path,
    _get_library_names, _get_matched_template, _get_ordered_poster_files,
    _get_primary_color_value, _parse_rgb_config, _resize_crop, _rounded_image,
    _sample_average_color, add_shadow
)
from app.modules.cover.poster_gen_gradients import create_gradient_background
from app.modules.cover.poster_gen_grid import gen_poster_workflow

def gen_poster_workflow2(name):
    '''
    生成横版媒体库封面：上方背景和左侧标题，底部横向排列 5 张圆角海报。
    '''
    try:
        matched = _get_matched_template(name)
        folder = os.path.join(poster_config.POSTER_FOLDER, name)
        output_path = os.path.join(poster_config.OUTPUT_FOLDER, f"{name}_2.png")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        files = _get_ordered_poster_files(folder, limit=5, default_order='123456')
        if not files:
            logger.info(f"在 {folder} 中没有找到支持的图片文件")
            return gen_poster_workflow(name)
        return gen_poster_workflow(name)
    except Exception as e:
        logger.exception(f"gen_poster_workflow2 error: {e}")
        return gen_poster_workflow(name)

def gen_poster_workflow3(name):
    '''
    生成参考 3-1/3-2 风格的横版媒体库封面：
    右侧影视背景，左侧颗粒质感色块，斜切分割，大号中文标题。
    '''
    try:
        matched = _get_matched_template(name)
        folder = os.path.join(poster_config.POSTER_FOLDER, name)
        output_path = os.path.join(poster_config.OUTPUT_FOLDER, f"{name}_3.png")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        return gen_poster_workflow(name)
    except Exception as e:
        logger.exception(f"gen_poster_workflow3 error: {e}")
        return gen_poster_workflow(name)
