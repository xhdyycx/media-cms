from typing import Optional, Type
from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, DateTime, func, delete

class Account115(Base):
    '''
    115账号库
    '''
    __tablename__ = 'account_115'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True, comment='账号id')
    username = Column(String(255), nullable=True, comment='账号昵称')
    cookie_type = Column(String(255), nullable=True, comment='cookie类型')
    cookie = Column(String(2000), nullable=True, comment='cookie')
    type = Column(Integer, nullable=False, default=2, comment='账号类型 1祝愿账号 2许愿账号 3小号')
    status = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False, server_default=func.now(), comment='创建时间')
    last_update_time = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='最后更新时间')

    @staticmethod
    @db_query
    def get_by_username(db: Session, username):
        return db.query(Account115).filter(Account115.username == username).first()

    @staticmethod
    @db_query
    def get_all(db: Session, type, status):
        return db.query(Account115).filter(Account115.type == type, Account115.status == status).all()

    @staticmethod
    @db_query
    def list_page(db: Session, username, type, status, page, page_size):
        _var_var_0 = db.query(Account115).order_by(Account115.id.desc())
        if username:
            _var_var_0 = _var_var_0.filter(Account115.username.like(f'%{username}%'))
        if type is not None:
            _var_var_0 = _var_var_0.filter(Account115.type == type)
        if status is not None:
            _var_var_0 = _var_var_0.filter(Account115.status == status)
        _var_var_1 = (page - 1) * page_size
        _var_var_2 = _var_var_0.count()
        return {
            'data': _var_var_0.offset(_var_var_1).limit(page_size).all(),
            'total': _var_var_2,
            'page': page,
            'page_size': page_size
        }

    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_3 = delete(Account115).where(Account115.id.in_(ids))
        db.execute(_var_var_3)
