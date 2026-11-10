# File: media_info.py (Cleaned & Decompiled)
from dataclasses import dataclass
from app.types.Type import DatClass

@dataclass
class MediaInfo(DatClass):
    type: str = None
    tidy_type: str = None
    name: str = None
    many_version_name: str = None
    dir_name: str = None
    season_name: str = None
    tmdb_id: str = None
    season_num: int = None
    episode_num: int = None
    poster_path: str = None
    backdrop_path: str = None
    video_info: dict = None
    tmdb_info: dict = None