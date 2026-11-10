import math
import os
import random
from PIL import Image
from app.core.env import novaEnv
from app.core.env2 import config2Env
from app.modules.cover import poster_config
from app.modules.cover.poster_gen_common import add_shadow, draw_color_block, draw_multiline_text_on_image, draw_text_on_image, get_random_color
from app.modules.cover.poster_gen_gradients import create_gradient_background, create_gradient_background_v2, get_poster_primary_color
from app.log import logger

def gen_poster_workflow(name):
    """
    将多张电影海报排列成三列，每列三张，然后将每列作为整体旋转并放在渐变背景上
    不再依赖外部模板文件，直接生成渐变背景
    """
    _var_var_1 = {}
    _var_var_2 = config2Env.e_cover_gen_template_mapping
    _var_var_3 = _var_var_2.get('template_mapping', [])
    logger.info(f'模板配置: {_var_var_3}')
    for _var_var_4 in _var_var_3:
        if _var_var_4.get('library_name') == name:
            _var_var_1 = _var_var_4
            break
    _var_var_5 = os.path.join(poster_config.POSTER_FOLDER, name)
    _var_var_6 = os.path.join(poster_config.OUTPUT_FOLDER, f'{name}.png')
    _var_var_7 = poster_config.POSTER_GEN_CONFIG['ROWS']
    _var_var_8 = poster_config.POSTER_GEN_CONFIG['COLS']
    _var_var_9 = poster_config.POSTER_GEN_CONFIG['MARGIN']
    _var_var_10 = poster_config.POSTER_GEN_CONFIG['CORNER_RADIUS']
    _var_var_11 = poster_config.POSTER_GEN_CONFIG['ROTATION_ANGLE']
    _var_var_12 = poster_config.POSTER_GEN_CONFIG['START_X']
    _var_var_13 = poster_config.POSTER_GEN_CONFIG['START_Y']
    _var_var_14 = poster_config.POSTER_GEN_CONFIG['COLUMN_SPACING']
    _var_var_15 = poster_config.POSTER_GEN_CONFIG['SAVE_COLUMNS']
    _var_var_16 = 1920
    _var_var_17 = 1080
    _var_var_18 = _var_var_1.get('background_color_rgb_left') or _var_var_2.get('background_color_rgb_left')
    _var_var_19 = tuple(map(int, _var_var_18.split(','))) if _var_var_18 else None
    _var_var_20 = _var_var_1.get('background_color_rgb_right') or _var_var_2.get('background_color_rgb_right')
    _var_var_21 = tuple(map(int, _var_var_20.split(','))) if _var_var_20 else None
    if _var_var_19 is None and _var_var_21 is None:
        _var_var_22 = os.path.join(_var_var_5, '1.jpg')
        _var_var_23 = get_poster_primary_color(_var_var_22)
        _var_var_24 = create_gradient_background_v2(_var_var_16, _var_var_17, name, _var_var_23)
    else:
        _var_var_24 = create_gradient_background(_var_var_16, _var_var_17, _var_var_19, _var_var_21)
    _var_var_25 = _var_var_24.copy()
    _var_var_26 = os.path.dirname(_var_var_6)
    if not os.path.exists(_var_var_26):
        os.makedirs(_var_var_26)
    _var_var_27 = os.path.join(_var_var_26, 'columns')
    if _var_var_15 and not os.path.exists(_var_var_27):
        os.makedirs(_var_var_27)
    _var_var_28 = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    _var_var_29 = _var_var_2.get('poster_position', '315426987')
    _var_var_0 = {i: c for i, c in enumerate(_var_var_29)}
    _var_var_33 = sorted([os.path.join(_var_var_5, _var_var_32) for _var_var_32 in os.listdir(_var_var_5) if os.path.isfile(os.path.join(_var_var_5, _var_var_32)) and _var_var_32.lower().endswith(_var_var_28) and os.path.splitext(_var_var_32)[0] in _var_var_0], key=lambda x: _var_var_0[os.path.splitext(os.path.basename(x))[0]])
    if not _var_var_33:
        logger.info(f'错误: 在 {_var_var_5} 中没有找到支持的图片文件')
        return (False, None)
    _var_var_33 = _var_var_33[:_var_var_7 * _var_var_8]
    _var_var_34 = poster_config.POSTER_GEN_CONFIG['CELL_WIDTH']
    _var_var_35 = poster_config.POSTER_GEN_CONFIG['CELL_HEIGHT']
    _var_var_37 = [_var_var_33[_var_var_36:_var_var_36 + _var_var_7] for _var_var_36 in range(0, len(_var_var_33), _var_var_7)]
    try:
        for _var_var_38, _var_var_39 in enumerate(_var_var_37):
            if _var_var_38 >= _var_var_8:
                break
            _var_var_40 = _var_var_12 + _var_var_38 * _var_var_14
            _var_var_41 = _var_var_7 * _var_var_35 + (_var_var_7 - 1) * _var_var_9
            _var_var_42 = 60
            _var_var_43 = 60
            _var_var_44 = Image.new('RGBA', (_var_var_34 + _var_var_42, _var_var_41 + _var_var_43), (0, 0, 0, 0))
            for _var_var_45, _var_var_46 in enumerate(_var_var_39):
                try:
                    _var_var_47 = Image.open(_var_var_46)
                    _var_var_48 = _var_var_34 / _var_var_47.width
                    _var_var_49 = _var_var_35 / _var_var_47.height
                    _var_var_50 = max(_var_var_48, _var_var_49)
                    _var_var_51 = int(_var_var_47.width * _var_var_50)
                    _var_var_52 = int(_var_var_47.height * _var_var_50)
                    _var_var_53 = _var_var_47.resize((_var_var_51, _var_var_52), Image.LANCZOS)
                    _var_var_54 = (_var_var_51 - _var_var_34) // 2
                    _var_var_55 = (_var_var_52 - _var_var_35) // 2
                    _var_var_53 = _var_var_53.crop((_var_var_54, _var_var_55, _var_var_54 + _var_var_34, _var_var_55 + _var_var_35))
                    if _var_var_10 > 0:
                        from PIL import ImageDraw
                        _var_var_57 = Image.new('L', (_var_var_34, _var_var_35), 0)
                        _var_var_58 = ImageDraw.Draw(_var_var_57)
                        _var_var_58.rounded_rectangle([(0, 0), (_var_var_34, _var_var_35)], radius=_var_var_10, fill=255)
                        _var_var_59 = Image.new('RGBA', _var_var_53.size, (0, 0, 0, 0))
                        _var_var_59.paste(_var_var_53, (0, 0), _var_var_57)
                        _var_var_53 = _var_var_59
                    _var_var_60 = add_shadow(_var_var_53, offset=(20, 20), shadow_color=(0, 0, 0, 255), blur_radius=20)
                    _var_var_61 = _var_var_45 * (_var_var_35 + _var_var_9)
                    _var_var_44.paste(_var_var_60, (0, _var_var_61), _var_var_60)
                except Exception as _var_var_62:
                    logger.info(f'错误: 处理图片 {os.path.basename(_var_var_46)} 时出错: {_var_var_62}')
            if _var_var_15:
                _var_var_63 = os.path.join(_var_var_27, f'{name}_column_{_var_var_38 + 1}_original.png')
                _var_var_44.save(_var_var_63)
            _var_var_64 = int(math.sqrt((_var_var_34 + _var_var_42) ** 2 + (_var_var_41 + _var_var_43) ** 2) * 1.5)
            _var_var_65 = Image.new('RGBA', (_var_var_64, _var_var_64), (0, 0, 0, 0))
            _var_var_66 = (_var_var_64 - _var_var_34) // 2
            _var_var_67 = (_var_var_64 - _var_var_41) // 2
            _var_var_65.paste(_var_var_44, (_var_var_66, _var_var_67), _var_var_44)
            _var_var_68 = _var_var_65.rotate(_var_var_11, Image.BICUBIC, expand=True)
            if _var_var_15:
                _var_var_69 = os.path.join(_var_var_27, f'column_{_var_var_38 + 1}_rotated.png')
                _var_var_68.save(_var_var_69)
            _var_var_70 = _var_var_13 + _var_var_41 // 2
            _var_var_71 = _var_var_40
            if _var_var_38 == 1:
                _var_var_71 += _var_var_34 - 50
            elif _var_var_38 == 2:
                _var_var_70 += -155
                _var_var_71 += _var_var_34 * 2 - 40
            _var_var_72 = _var_var_71 - _var_var_68.width // 2 + _var_var_34 // 2
            _var_var_73 = _var_var_70 - _var_var_68.height // 2
            _var_var_25.paste(_var_var_68, (_var_var_72, _var_var_73), _var_var_68)
        _var_var_74 = _var_var_1.get('color_block_rgb') or _var_var_2.get('color_block_rgb')
        _var_var_75 = tuple(map(int, _var_var_74.split(','))) if _var_var_74 else None
        if _var_var_33:
            _var_var_22 = _var_var_33[0]
            _var_var_76 = _var_var_75 or get_random_color(_var_var_22)
        else:
            _var_var_76 = _var_var_75 or (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200), 255)
        _var_var_77 = name
        _var_var_78 = ''
        if _var_var_1:
            if 'library_ch_name' in _var_var_1:
                _var_var_77 = _var_var_1['library_ch_name']
            if 'library_eng_name' in _var_var_1:
                _var_var_78 = _var_var_1['library_eng_name']
        _var_var_79 = _var_var_2.get('ch_font_name', '')
        _var_var_80 = _var_var_2.get('ch_position', '73.32,427.34')
        _var_var_81 = tuple(map(float, _var_var_80.split(',')))
        if _var_var_79:
            _var_var_82 = os.path.join(novaEnv.CONFIG_PATH, _var_var_79)
        else:
            _var_var_82 = os.path.join(poster_config.CURRENT_DIR, 'font', 'ch.ttf')
        _var_var_83 = _var_var_2.get('ch_font_size', 180)
        _var_var_25 = draw_text_on_image(_var_var_25, _var_var_77, _var_var_81, _var_var_82, _var_var_83)
        if _var_var_78:
            _var_var_84 = _var_var_2.get('eng_font_size', 80)
            _var_var_85 = 5
            _var_var_86 = len(_var_var_78.split())
            _var_var_88 = max([len(_var_var_87) for _var_var_87 in _var_var_78.split()])
            if _var_var_88 > 10 or _var_var_86 > 3:
                _var_var_89 = _var_var_84 * (10 / max(_var_var_88, _var_var_86 * 3)) ** 0.8
                _var_var_89 = max(_var_var_89, 30)
            else:
                _var_var_89 = _var_var_84
            logger.info(f"英文名 '{_var_var_78}' 单词数量: {_var_var_86}, 最长单词长度: {_var_var_88}")
            logger.info(f'使用字体大小: {_var_var_89:.2f}')
            _var_var_90 = _var_var_2.get('eng_font_name', '')
            _var_var_91 = _var_var_2.get('eng_position', '124.68,635.55')
            _var_var_92 = tuple(map(float, _var_var_91.split(',')))
            if _var_var_90:
                _var_var_93 = os.path.join(novaEnv.CONFIG_PATH, _var_var_90)
            else:
                _var_var_93 = os.path.join(poster_config.CURRENT_DIR, 'font', 'en.ttf')
            _var_var_25, _var_var_94 = draw_multiline_text_on_image(_var_var_25, _var_var_78, _var_var_92, _var_var_93, int(_var_var_89), _var_var_85)
            _var_var_95 = _var_var_2.get('color_block_position', '84.38,620.06')
            _var_var_96 = tuple(map(float, _var_var_95.split(',')))
            _var_var_97 = _var_var_89 + 10 + (_var_var_94 - 1) * (int(_var_var_89) + _var_var_85)
            _var_var_98 = (21.51, _var_var_97)
            logger.info(f'色块高度调整为: {_var_var_97} (行数: {_var_var_94})')
            _var_var_25 = draw_color_block(_var_var_25, _var_var_96, _var_var_98, _var_var_76)
        _var_var_25.save(_var_var_6)
        logger.info(f'成功: 图片已保存到 {_var_var_6}')
        return (True, _var_var_6)
    except Exception as _var_var_62:
        logger.exception(_var_var_62)
        logger.info(f'错误: 创建九宫格图片时出错: {_var_var_62}')
        return (False, None)