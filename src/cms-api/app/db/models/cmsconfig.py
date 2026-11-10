from typing import Optional
from sqlalchemy.orm import Session
from app.db import Base, db_query
from sqlalchemy import Column, Integer, String, Text

class NovaConfig(Base):
    '''
    配置
    '''
    __tablename__ = 'nova_config'
    id = Column(Integer, primary_key = True, autoincrement = True)
    key = Column(String(255), nullable = True, comment = '配置key')
    config_json = Column(Text, nullable = True, comment = '配置信息')
    @staticmethod
    @db_query
    def get_by_key(db: Session, key) -> Optional["NovaConfig"]:
        return db.query(NovaConfig).filter_by(key=key).first()
    db_query


