from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, update, delete

class SubMedia(Base):
    '''
    订阅媒体
    '''
    __tablename__ = 'sub_media1'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    title = Column(String(255), nullable=True, comment='标题')
    year = Column(String(255), nullable=True, comment='年份')
    tmdb_id = Column(String(255), nullable=True, comment='tmdb_id')
    type = Column(String(255), nullable=True, comment='类型')
    sub_type = Column(String(255), nullable=True, comment='订阅类型 NORMAL REMASTER')
    season_info = Column(String(255), nullable=True, comment='季信息')
    max_season = Column(Integer, nullable=True, comment='最大季数')
    max_season_episodes = Column(Integer, nullable=True, comment='最大季集数')
    poster_path = Column(String(255), nullable=True, comment='海报路径')
    backdrop_path = Column(String(255), nullable=True, comment='背景图路径')
    status = Column(Integer, nullable=False, default=0, comment='状态 0-暂停订阅 1订阅中 2-完成订阅 3-洗版中')

    @staticmethod
    @db_query
    def get_tmdb_id(db: Session, tmdb_id):
        return db.query(SubMedia).filter_by(tmdb_id=tmdb_id).first()

    @staticmethod
    @db_query
    def get_type_status(db: Session, type, status):
        return db.query(SubMedia).filter_by(type=type, status=status).all()

    @staticmethod
    @db_query
    def list_page(db: Session, type, status, page, page_size):
        _var_var_0 = db.query(SubMedia).order_by(SubMedia.status.asc()).order_by(SubMedia.id.desc())
        if type:
            _var_var_0 = _var_var_0.filter_by(type=type)
        if status is not None:
            _var_var_0 = _var_var_0.filter_by(status=status)
        _var_var_1 = (page - 1) * page_size
        _var_var_2 = _var_var_0.count()
        return {'data': _var_var_0.offset(_var_var_1).limit(page_size).all(), 'total': _var_var_2, 'page': page, 'page_size': page_size}

    @staticmethod
    @db_query
    def get_status(db: Session, status):
        return db.query(SubMedia).filter_by(status=status).all()

    @staticmethod
    @db_update
    def update_all_status(db: Session, ids, status):
        _var_var_3 = update(SubMedia).where(SubMedia.id.in_(ids)).values(status=status)
        db.execute(_var_var_3)

    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_3 = delete(SubMedia).where(SubMedia.id.in_(ids))
        db.execute(_var_var_3)
