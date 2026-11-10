from typing import Optional, List, Type
from blacksheep import text
from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import BigInteger, Column, Integer, String, cast

class LiftList(Base):
    '''
    生活数据表
    '''
    __tablename__ = 'lift_list'
    id = Column(Integer, primary_key = True, autoincrement = True, comment = '主键')
    lid = Column(String(255), nullable = True, comment = '最近id')
    behavior_type = Column(String(255), nullable = True, comment = '类型')
    start_time = Column(Integer, nullable = True, comment = '开始时间')
    end_time = Column(Integer, nullable = True, comment = '结束时间')
    item_json = Column(String(5000), nullable = True, comment = 'item数据')
    status = Column(Integer, nullable = False, default = 0, comment = '状态 0-待处理 1-处理成功 2-处理失败')
    desc = Column(String(255), nullable = True, comment = '备注')
    @staticmethod
    @db_query
    def get_by_status(db: Session, status) -> list[Type["LiftList"]]:
        return db.query(LiftList).filter(LiftList.status == status).order_by(LiftList.lid.asc()).all()
    @staticmethod
    @db_query
    def get_by_lid(db: Session, lid) -> Optional["LiftList"]:
        return db.query(LiftList).filter(LiftList.lid == lid).first()
    @staticmethod
    @db_query
    def get_last(db: Session) -> Optional["LiftList"]:
        return db.query(LiftList).order_by(LiftList.id.desc()).limit(1).offset(0).first()
    @staticmethod
    @db_query
    def get_max_lid(db: Session) -> Optional["LiftList"]:
        return db.query(LiftList).order_by(LiftList.lid.desc()).limit(1).offset(0).first()
    @staticmethod
    @db_update
    def clear(db: Session):
        db.query(LiftList).delete(synchronize_session=False)
    @staticmethod
    @db_update
    def del_by_status_and_lid(db: Session, status, lid):
        db.query(LiftList).filter(LiftList.status == status, LiftList.lid < lid).delete(synchronize_session=False)
    db_update


