import json
from contextlib import contextmanager
from typing import Any, Self, List, Tuple, Optional, Generator
from datetime import datetime

from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy import create_engine, QueuePool, Column, DateTime, func, inspect
from sqlalchemy.orm import declared_attr, sessionmaker, Session, scoped_session, as_declarative

from app.core.env import novaEnv
from app.log import logger

Engine = create_engine(
    novaEnv.DATABASE_SQL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionFactory = sessionmaker(bind=Engine, autocommit=False, autoflush=False)
ScopedSession = scoped_session(SessionFactory)

def init_db():
    Base.metadata.create_all(bind=Engine)

def update_db():
    try:
        _var_var_0 = novaEnv.ROOT_PATH / 'sql'
        _var_var_1 = Config()
        _var_var_1.set_main_option('script_location', str(_var_var_0))
        _var_var_1.set_main_option('sqlalchemy.url', novaEnv.DATABASE_SQL)
        upgrade(_var_var_1, 'head')
    except Exception as _var_var_2:
        logger.error(f'数据库表结构更新失败：{str(_var_var_2)}')

@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = ScopedSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def get_args_db(args: tuple, kwargs: dict) -> Optional[Session]:
    '''
    从参数中获取数据库Session对象
    '''
    db = None
    if args:
        for arg in args:
            if isinstance(arg, Session):
                db = arg
                break
    if kwargs and not db:
        for v in kwargs.values():
            if isinstance(v, Session):
                db = v
                break
    return db

def update_args_db(args: tuple, kwargs: dict, db: Session) -> Tuple[tuple, dict]:
    '''
    更新参数中的数据库Session对象，关键字传参时更新db的值，否则更新第1或第2个参数
    '''
    if kwargs and 'db' in kwargs:
        kwargs['db'] = db
    elif args:
        if args[0] is None:
            args = (db,) + args[1:]
        else:
            args = (args[0], db) + args[2:]
    return args, kwargs

def db_update(func):
    '''数据库更新类操作装饰器，第一个参数必须是数据库会话或存在db参数'''
    def wrapper(*args, **kwargs):
        is_new_session = False
        db = get_args_db(args, kwargs)
        if not db:
            db = ScopedSession()
            is_new_session = True
            args, kwargs = update_args_db(args, kwargs, db)
        try:
            res = func(*args, **kwargs)
            db.commit()
            return res
        except Exception as e:
            db.rollback()
            raise e
        finally:
            if is_new_session:
                db.close()
    return wrapper

def db_query(func):
    '''数据库查询操作装饰器，第一个参数必须是数据库会话或存在db参数'''
    def wrapper(*args, **kwargs):
        is_new_session = False
        db = get_args_db(args, kwargs)
        if not db:
            db = ScopedSession()
            is_new_session = True
            args, kwargs = update_args_db(args, kwargs, db)
        try:
            return func(*args, **kwargs)
        finally:
            if is_new_session:
                db.close()
    return wrapper

@as_declarative()
class Base:
    id: Any
    __name__: str

    create_time = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    last_update_time = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='最后更新时间')

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @db_update
    def create(self, db: Session = None):
        db.add(self)

    @classmethod
    @db_query
    def get(cls, db: Session, rid: int) -> Optional[Self]:
        return db.query(cls).filter(cls.id == rid).first()

    @db_update
    def update(self, db: Session, payload: dict):
        for k, v in payload.items():
            if hasattr(self, k):
                setattr(self, k, v)

    @staticmethod
    @db_update
    def delete_log(db: Session, db_log):
        db.delete(db_log)

    @classmethod
    @db_update
    def delete(cls, db: Session, rid: int):
        db.query(cls).filter(cls.id == rid).delete()

    @classmethod
    @db_update
    def truncate(cls, db: Session):
        db.query(cls).delete()

    @classmethod
    @db_query
    def list(cls, db: Session) -> List[Self]:
        return list(db.query(cls).all())

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, default=str)

class DbOp:
    '''数据库操作基类'''
    _db: Session = None

    def __init__(self, db: Session):
        self._db = db

    @property
    def db(self) -> Session:
        return self._db
