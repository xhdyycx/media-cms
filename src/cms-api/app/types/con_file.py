# File: con_file.py (Cleaned & Decompiled)
from dataclasses import dataclass
from app.modules.media.types.media_info import MediaInfo
from app.types.Type import DatClass

@dataclass
class ConFile(DatClass):
    is_dir: int = None
    fid: str = None
    pid: str = None
    name: str = None
    ext: str = None
    size: int = None
    s3_key_flag: str = None
    md5: str = None
    full_y_path: str = None
    p_name: str = None
    f_modify_time: str = None
    url: str = None
    local_name: str = None
    local_path: str = None
    sync_time: str = None
    desc: str = None
    status: str = None
    media_info: MediaInfo = None