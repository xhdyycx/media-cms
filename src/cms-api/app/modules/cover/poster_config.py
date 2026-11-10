import os
import json
from app.core.env import novaEnv
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
POSTER_FOLDER = os.path.join(novaEnv.COVER_PATH, 'poster')
TEMPLATE_FOLDER = os.path.join(novaEnv.COVER_PATH, 'template')
OUTPUT_FOLDER = os.path.join(novaEnv.COVER_PATH, 'output')
POSTER_GEN_CONFIG = {
    'ROWS': 3,
    'COLS': 3,
    'MARGIN': 22,
    'CORNER_RADIUS': 46.1,
    'ROTATION_ANGLE': -15.8,
    'START_X': 835,
    'START_Y': -362,
    'COLUMN_SPACING': 100,
    'SAVE_COLUMNS': True,
    'CELL_WIDTH': 410,
    'CELL_HEIGHT': 610 }
POSTER_DOWNLOAD_CONFIG = {
    'POSTER_COUNT': 9,
    'POSTER_DIR': POSTER_FOLDER }

