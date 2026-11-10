from typing import Optional
from sqlalchemy.orm import Session
from app.db import Base, db_query
from sqlalchemy import Column, Integer, String

class NovaUser(Base):
    '''
    配置
    '''
    __tablename__ = 'nova_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    salt = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    status = Column(Integer, nullable=False, default=1, comment='状态 0-禁用 1-启用')

    @db_query
    @staticmethod
    def get_by_username(db: Session, username) -> Optional['NovaUser']:
        return db.query(NovaUser).filter_by(username=username).first()

    @db_query
    @staticmethod
    def get_by_role(db: Session, role) -> Optional['NovaUser']:
        return db.query(NovaUser).filter_by(role=role).first()
