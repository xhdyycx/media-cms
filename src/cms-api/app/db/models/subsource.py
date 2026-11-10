from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, update, delete

class SubSource(Base):
    '''
    订阅源
    '''
    __tablename__ = 'sub_source'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    name = Column(String(255), nullable=True, comment='名称')
    url = Column(String(1000), nullable=True, comment='链接')
    type = Column(String(255), nullable=True, comment='类型')
    status = Column(Integer, nullable=False, default=1, comment='状态 0-禁用 1-启用')
    level = Column(Integer, nullable=False, default=1, comment='优先级')
    fid = Column(String(255), nullable=True, comment='文件id')

    @staticmethod
    @db_query
    def get_type_status(db: Session, type, status):
        return db.query(SubSource).filter_by(type=type, status=status).all()

    @staticmethod
    @db_query
    def list(db: Session, type, status):
        _var_var_0 = db.query(SubSource)
        if type:
            _var_var_0 = _var_var_0.filter_by(type=type)
        if status is not None:
            _var_var_0 = _var_var_0.filter_by(status=status)
        return _var_var_0.order_by(SubSource.level.desc(), SubSource.id.desc()).all()

    @staticmethod
    @db_query
    def get_status(db: Session, status):
        return db.query(SubSource).filter_by(status=status).all()

    @staticmethod
    @db_query
    def get_by_fid(db: Session, fid):
        return db.query(SubSource).filter_by(fid=fid).first()

    @staticmethod
    @db_update
    def update_all_status(db: Session, ids, status):
        _var_var_3 = update(SubSource).where(SubSource.id.in_(ids)).values(status=status)
        db.execute(_var_var_3)

    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_3 = delete(SubSource).where(SubSource.id.in_(ids))
        db.execute(_var_var_3)
