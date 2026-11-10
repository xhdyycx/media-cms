# File: log.py (Accurately restored from bytecode)
import logging
from logging.handlers import RotatingFileHandler
import click
from version import APP_VERSION_CODE
from app.core.env import novaEnv

logger = logging.getLogger('novamedia')
logger.setLevel(logging.INFO)

apscheduler_log = logging.getLogger('apscheduler')
apscheduler_log.setLevel(logging.ERROR)

aligo_logger = logging.getLogger('aliyun')

level_name_colors = {
    logging.DEBUG: (lambda level_name: click.style(str(level_name), fg='cyan')),
    logging.INFO: (lambda level_name: click.style(str(level_name), fg='green')),
    logging.WARNING: (lambda level_name: click.style(str(level_name), fg='yellow')),
    logging.ERROR: (lambda level_name: click.style(str(level_name), fg='red')),
    logging.CRITICAL: (lambda level_name: click.style(str(level_name), fg='bright_red'))
}

def _process_message_content(message):
    """
    处理日志消息内容，检测并替换特定关键字
    """
    msg_str = str(message)
    if 'Max retries exceeded with url' in msg_str:
        if '请求当前地址失败' not in msg_str:
            return f"请求当前地址失败 - {message}"
    elif '401 Client Error: Unauthorized for url' in msg_str:
        if 'EMBY_API_KEY配置错误' not in msg_str:
            return f"EMBY_API_KEY配置错误 - {message}"
    return message


class CustomFormatter(logging.Formatter):
    """
    定义日志输出格式
    """
    def format(self, record):
        pad = ' ' * (6 - len(record.levelname))
        record.leveltext = record.levelname + f': {APP_VERSION_CODE}' + pad
        if record.filename.startswith('<frozen app.'):
            fname = record.filename.split('.')[-1].rstrip('>')
        else:
            fname = record.filename.split('/')[-1].split('.')[0]
        if len(fname) > 10:
            record.filename = fname[:10]
        else:
            record.filename = fname.ljust(10)
            
        raw_msg = record.getMessage()
        proc_msg = _process_message_content(raw_msg)
        record.msg = proc_msg
        record.args = None
        return super().format(record)


class CustomColorFormatter(logging.Formatter):
    """
    定义日志输出格式
    """
    def format(self, record):
        pad = ' ' * (6 - len(record.levelname))
        record.leveltext = record.levelname + f': {APP_VERSION_CODE}' + pad
        if record.filename.startswith('<frozen app.'):
            fname = record.filename.split('.')[-1].rstrip('>')
        else:
            fname = record.filename.split('/')[-1].split('.')[0]
        if len(fname) > 10:
            record.filename = fname[:10]
        else:
            record.filename = fname.ljust(10)
            
        raw_msg = record.getMessage()
        proc_msg = _process_message_content(raw_msg)
        record.msg = proc_msg
        record.args = None
        formatted = super().format(record)
        return level_name_colors[record.levelno](formatted)


file_formatter = CustomFormatter('%(leveltext)s %(asctime)s - %(filename)s:%(lineno)4d ➜ %(message)s')

file_handler = RotatingFileHandler(
    novaEnv.LOG_PATH + '/novamedia.log',
    maxBytes=10485760,
    backupCount=7,
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
apscheduler_log.addHandler(file_handler)
aligo_logger.addHandler(file_handler)

console_formatter = CustomColorFormatter('%(leveltext)s %(asctime)s - %(filename)s:%(lineno)4d ➜ %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

if novaEnv.RUN_ENV == 'online':
    console_handler.setFormatter(file_formatter)
else:
    console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)
apscheduler_log.addHandler(console_handler)
aligo_logger.addHandler(console_handler)