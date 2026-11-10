from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, update, delete, BigInteger, Text

class ShareDown(Base):
    '''
    分享下载记录
    '''
    __tablename__ = 'share_down'
    id = Column(Integer, primary_key = True, autoincrement = True, comment = '主键')
    type = Column(String(255), nullable = True, comment = '类型 share_115/magnet/share_aliyun')
    share_id = Column(String(255), nullable = True, comment = '分享id')
    share_pwd = Column(String(255), nullable = True, comment = '分享密码')
    share_name = Column(String(255), nullable = True, comment = '分享名称')
    f_id = Column(String(255), nullable = True, comment = '文件id')
    f_name = Column(String(255), nullable = True, comment = '文件名')
    async_task_id = Column(String(255), nullable = True, comment = '异步任务id')
    status = Column(Integer, nullable = False, default = 0, comment = '状态 0-处理中 1-保存成功 2-保存失败 200-秒传成功 201-秒传失败')
    remark = Column(String(255), nullable = True, comment = '备注')
    @staticmethod
    @db_query
    def get_by_share_id(db, share_id):
        return db.query(ShareDown).filter_by(share_id=share_id).first()
    @staticmethod
    @db_query
    def get_type_status(db, type, status):
        return db.query(ShareDown).filter_by(type=type, status=status).all()
    @staticmethod
    @db_query
    def get_status(db, status):
        return db.query(ShareDown).filter_by(status=status).all()
    @staticmethod
    @db_query
    def get_share_id(db, share_id):
        return db.query(ShareDown).filter_by(share_id=share_id).first()
    @staticmethod
    @db_query
    def get_by_fid(db, fid):
        return db.query(ShareDown).filter_by(f_id=fid).first()
    @staticmethod
    @db_query
    def update_all_status(db, ids, status):
        _var_var_0 = update(ShareDown).where(ShareDown.id.in_(ids)).values(status=status)
        db.execute(_var_var_0)
        return None
    @staticmethod
    @db_query
    def delete_by_ids(db, ids):
        _var_var_0 = delete(ShareDown).where(ShareDown.id.in_(ids))
        db.execute(_var_var_0)
        return None
    @staticmethod
    @db_query
    def clear(db):
        """清空"""
        return db.query(ShareDown).delete(synchronize_session=False)
    @staticmethod
    @db_query
    def list_page(
        db: Session,
        type: str = None,
        status: int = None,
        page: int = 1,
        page_size: int = 10,
    ):
        _var_var_1 = db.query(ShareDown).order_by(ShareDown.id.desc())
        if type:
            _var_var_1 = _var_var_1.filter_by(type=type)
        if status is not None:
            _var_var_1 = _var_var_1.filter_by(status=status)
        _var_var_2 = (page - 1) * page_size
        _var_var_3 = _var_var_1.count()
        return {
            'data': _var_var_1.offset(_var_var_2).limit(page_size).all(),
            'total': _var_var_3,
            'page': page,
            'page_size': page_size,
        }
    db_query


