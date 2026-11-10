from typing import Type, List, Self
from sqlalchemy.orm import Session
from app.db import Base, db_query
from sqlalchemy import Column, Integer, String

class WishLog(Base):
    '''
    许愿记录
    '''
    __tablename__ = 'wish_log'
    id = Column(Integer, primary_key = True, autoincrement = True)
    status = Column(Integer, nullable = True, comment = '状态 1-已许愿 2-已祝愿 3-已采纳')
    wish_username = Column(String(255), nullable = True, comment = '许愿昵称')
    wish_id = Column(String(255), nullable = True, comment = '许愿id')
    wish_date = Column(Integer, nullable = True, comment = '许愿日期 yyyyMMdd 格式')
    wish_content = Column(String(255), nullable = True, comment = '许愿内容')
    aid_username = Column(String(255), nullable = True, comment = '祝愿昵称')
    wish_size = Column(Integer, nullable = True, comment = '许愿大小 单位GB')
    aid_id = Column(String(255), nullable = True, comment = '祝愿id')
    aid_content = Column(String(255), nullable = True, comment = '祝愿内容')
    desc = Column(String(255), nullable = True, comment = '描述')
    sort_num = Column(Integer, nullable = True, comment = '排序 大的靠前')
    @staticmethod
    @db_query
    def get_new_wish(db: Session, size):
        return db.query(WishLog).filter_by(status=1).order_by(WishLog.wish_size.desc(), WishLog.sort_num.desc(), WishLog.wish_username.asc(), WishLog.wish_date.asc(), WishLog.id.asc()).limit(size).offset(0).all()
    @staticmethod
    @db_query
    def get_by_status(db: Session, status):
        return db.query(WishLog).filter_by(status=status).all()
    db_query


