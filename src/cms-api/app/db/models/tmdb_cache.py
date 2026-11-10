from sqlalchemy import Column, Integer, String, delete, UniqueConstraint, Index, Text
from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update

class TmdbCache(Base):
    '''
    tmdb_cache
    '''
    __tablename__ = 'tmdb_cache'
    id = Column(Integer, primary_key = True, autoincrement = True)
    type = Column(String(255), nullable = True, comment = 'movie/tv/season')
    tmdb_id = Column(String(255), nullable = True, comment = 'tmdb_id')
    title = Column(String(255), nullable = True, comment = '标题')
    year = Column(String(255), nullable = True, comment = '年份')
    season_num = Column(Integer, nullable = True, comment = '季号')
    poster_path = Column(String(255), nullable = True, comment = '海报路径')
    backdrop_path = Column(String(255), nullable = True, comment = '背景图路径')
    query_url = Column(String(255), nullable = True, unique = True, comment = '查询url')
    query_response = Column(Text, nullable = True, comment = '查询响应')
    status = Column(Integer, nullable = True, comment = '状态 0-禁用 1-启用')
    __table_args__ = (UniqueConstraint('query_url', name = 'uix_query_url'), Index('ix_tmdb_id', 'tmdb_id'))
    @staticmethod
    @db_query
    def get_by_query_url(db: Session, query_url: str):
        return db.query(TmdbCache).filter_by(query_url=query_url).first()
    @staticmethod
    @db_query
    def get_tmdb_cache(db: Session, type: str = None, tmdb_id: str = None, season_num: int = None):
        _var_var_0 = db.query(TmdbCache)
        if type:
            _var_var_0 = _var_var_0.filter_by(type=type)
        if tmdb_id:
            _var_var_0 = _var_var_0.filter_by(tmdb_id=tmdb_id)
        if season_num is not None:
            _var_var_0 = _var_var_0.filter_by(season_num=season_num)
        return _var_var_0.order_by(TmdbCache.id.desc()).first()
    @staticmethod
    @db_query
    def list_page(db: Session, type: str = None, status: int = None, title: str = None, tmdb_id: str = None, page: int = 1, page_size: int = 10):
        _var_var_0 = db.query(TmdbCache).order_by(TmdbCache.id.desc())
        if type:
            _var_var_0 = _var_var_0.filter_by(type=type)
        if status is not None:
            _var_var_0 = _var_var_0.filter_by(status=status)
        if title:
            _var_var_0 = _var_var_0.filter(TmdbCache.title.like(f'%{title}%'))
        if tmdb_id:
            _var_var_0 = _var_var_0.filter_by(tmdb_id=tmdb_id)
        _var_var_1 = (page - 1) * page_size
        _var_var_2 = _var_var_0.count()
        return {
            'data': _var_var_0.offset(_var_var_1).limit(page_size).all(),
            'total': _var_var_2,
            'page': page,
            'page_size': page_size,
        }
    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_3 = delete(TmdbCache).where(TmdbCache.id.in_(ids))
        db.execute(_var_var_3)



