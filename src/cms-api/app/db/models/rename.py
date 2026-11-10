from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, update, delete, BigInteger, Text

class RenameLog(Base):
    '''
    重命名记录
    '''
    __tablename__ = 'rename_log'
    id = Column(Integer, primary_key = True, autoincrement = True, comment = '主键')
    fid = Column(String(255), nullable = True, comment = '文件id')
    pid = Column(String(255), nullable = True, comment = '文件夹id')
    name = Column(String(255), nullable = True, comment = '文件名')
    p_name = Column(String(255), nullable = True, comment = '文件夹名')
    suffix = Column(String(255), nullable = True, comment = '后缀')
    sha1 = Column(String(255), nullable = True, comment = 'sha1')
    size = Column(BigInteger, nullable = False, default = 0, comment = '大小')
    f_modify_time = Column(Integer, nullable = True, comment = '修改时间')
    path = Column(String(5000), nullable = True, comment = '路径')
    type = Column(String(255), nullable = True, comment = '类型 movie/tv')
    new_name = Column(String(255), nullable = True, comment = '新文件名')
    new_dir_name = Column(String(255), nullable = True, comment = '新文件夹名')
    new_season_name = Column(String(255), nullable = True, comment = '新季文件夹名')
    tmdb_id = Column(String(255), nullable = True, comment = 'tmdb_id')
    season_num = Column(String(255), nullable = True, comment = 'season_num')
    episode_num = Column(String(255), nullable = True, comment = 'episode_num')
    poster_path = Column(String(255), nullable = True, comment = 'poster_path')
    backdrop_path = Column(String(255), nullable = True, comment = 'backdrop_path')
    video_info = Column(Text, nullable = True, comment = '视频信息')
    tmdb_info = Column(Text, nullable = True, comment = 'tmdb信息')
    ali_fid = Column(String(255), nullable = True, comment = '阿里云盘文件id')
    tidy_type = Column(String(255), nullable = True, comment = '整理类型 un/video/subtitle')
    status = Column(Integer, nullable = False, default = 0, comment = '状态 0-待处理 100-刮削成功 101-刮削失败 20-重命名成功 201-重命名失败')
    desc = Column(String(255), nullable = True, comment = '备注')
    @staticmethod
    @db_query
    def get_by_status(db: Session, status):
        return db.query(RenameLog).filter_by(status=status).all()
    @staticmethod
    @db_query
    def get_by_status_tidy_type(db: Session, status, tidy_type):
        return db.query(RenameLog).filter_by(status=status, tidy_type=tidy_type).all()
    @staticmethod
    @db_query
    def get_pid_by_status_tidy_type(db: Session, status, tidy_type):
        return db.query(RenameLog.pid).filter_by(status=status, tidy_type=tidy_type).group_by(RenameLog.pid).all()
    @staticmethod
    @db_query
    def get_type_status(db: Session, type, status):
        return db.query(RenameLog).filter_by(type=type, status=status).all()
    @staticmethod
    @db_query
    def get_by_pid(db: Session, pid):
        return db.query(RenameLog).filter_by(pid=pid).all()
    @staticmethod
    @db_query
    def get_by_fid(db: Session, fid):
        return db.query(RenameLog).filter_by(fid=fid).first()
    @staticmethod
    @db_query
    def get_by_sha1(db: Session, sha1):
        return db.query(RenameLog).filter_by(sha1=sha1).first()
    @staticmethod
    @db_query
    def get_by_sha1_status(db: Session, sha1, status):
        return db.query(RenameLog).filter_by(sha1=sha1, status=status).first()
    @staticmethod
    @db_update
    def update_all_status(db: Session, ids, status, desc):
        _var_var_0 = update(RenameLog).where(RenameLog.id.in_(ids)).values(status=status, desc=desc)
        db.execute(_var_var_0)
    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_0 = delete(RenameLog).where(RenameLog.id.in_(ids))
        db.execute(_var_var_0)
    @staticmethod
    @db_update
    def clear(db: Session):
        """
        清空
        """
        db.query(RenameLog).delete(synchronize_session=False)
    db_update


