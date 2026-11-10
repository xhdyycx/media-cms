from enum import Enum

class ActionEnum(Enum):
    SYNC = '同步'
    DOWN = '下载'
    STRM = '创建strm文件'
    IMG = '图片'
    DIR = '文件夹'
    RENAME = '重命名'
    MOVE = '移动'
    DEL = '删除'
    UPLOAD = '上传'
    UNKNOWN = '未知'


class StatusEnum(Enum):
    INIT = 0
    SUCCESS = 1
    FAIL = 2


class NotificationType(Enum):
    Download = '资源下载'
    Organize = '整理入库'
    Subscribe = '订阅'
    SiteMessage = '站点消息'
    MediaServer = '媒体服务器通知'
    Manual = '手动处理通知'
    Plugin = '插件消息'


class MessageChannel(Enum):
    '''
    消息渠道
    '''
    Wechat = '微信'
    Telegram = 'Telegram'


class EventType(Enum):
    CmdExec = 'cmd_exec'
    ShareDown = 'share_down'


class TidyUpRule(Enum):
    SKIP = '跳过'
    REPLACE = '替换'
    COEXIST = '共存'
    SAVE_ONE = '留一个'


class TidyUpType(Enum):
    EXITS = '已存在'
    ADD = '替换'
    COEXIST = '共存'
    SAVE_ONE = '留一个'


class ConfigType(Enum):
    SERVICE_CONFIG = '服务配置'
    TG_BOT_CONFIG = 'TG机器人配置'
    core = '核心配置'
    auto_organize = '自动整理配置'
    share_down = '分享下载配置'


