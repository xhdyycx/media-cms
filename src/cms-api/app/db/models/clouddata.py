from typing import Optional, Type, List
from sqlalchemy.orm import Session
from app.db import Base, db_query, db_update
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func, delete, text

class CloudData(Base):
    '''
    云盘数据
    '''
    __tablename__ = 'cloud_data'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    fid = Column(String(255), nullable=True, unique=True, comment='文件id')
    name = Column(String(500), nullable=True, comment='名称')
    f_modify_time = Column(BigInteger, nullable=True, comment='网盘修改时间')
    pid = Column(String(255), nullable=True, comment='父级id')
    p_name = Column(String(500), nullable=True, comment='父级名称')
    full_y_path = Column(String(1000), nullable=True, comment='网盘完整路径')
    pick_code = Column(String(255), nullable=True, comment='提取码')
    sha1 = Column(String(255), nullable=True, comment='sha1')
    size = Column(BigInteger, nullable=True, comment='大小')
    is_dir = Column(Integer, nullable=True, comment='是否目录 0-文件 1-目录')
    is_media_dir = Column(Integer, nullable=True, comment='是否媒体目录 0-否 1-是')
    suffix = Column(String(255), nullable=True, comment='后缀')
    thumb = Column(String(1000), nullable=True, comment='缩略图')
    local_name = Column(String(500), nullable=True, comment='本地名称')
    local_path = Column(String(1000), nullable=True, comment='本地路径')
    action = Column(String(255), nullable=True, comment='动作')
    status = Column(Integer, nullable=False, default=0, comment='状态')
    desc = Column(String(1000), nullable=True, comment='描述')
    sync_time = Column(DateTime, nullable=True, comment='同步时间')
    create_time = Column(DateTime, nullable=False, server_default=func.now(), comment='创建时间')
    last_update_time = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='最后更新时间')

    @staticmethod
    @db_query
    def get_by_fid(db: Session, fid):
        return db.query(CloudData).filter_by(fid=fid).first()

    @staticmethod
    @db_query
    def get_by_sha1(db: Session, sha1):
        return db.query(CloudData).filter_by(sha1=sha1).all()

    @staticmethod
    @db_query
    def get_by_pid(db: Session, pid):
        return db.query(CloudData).filter_by(pid=pid).all()

    @staticmethod
    @db_query
    def get_dirs_by_pid(db: Session, pid):
        return db.query(CloudData).filter_by(pid=pid, is_dir=1).all()

    @staticmethod
    @db_query
    def get_video_by_pid(db: Session, pid):
        return db.query(CloudData).filter_by(pid=pid, is_dir=0).all()

    @staticmethod
    @db_query
    def get_by_pick_code(db: Session, pick_code):
        return db.query(CloudData).filter_by(pick_code=pick_code).first()

    @staticmethod
    @db_update
    def delete_cloud(db: Session, fid):
        return db.query(CloudData).filter_by(fid=fid).delete()

    @staticmethod
    @db_update
    def delete_by_pid(db: Session, pid):
        return db.query(CloudData).filter_by(pid=pid).delete()

    @staticmethod
    @db_query
    def get_media_dir(db: Session, pageNum, pageSize):
        return db.query(CloudData).filter(CloudData.is_media_dir == 1).limit(pageSize).offset((pageNum - 1) * pageSize).all()

    @staticmethod
    @db_query
    def get_by_pid_and_name(db: Session, pid, name):
        return db.query(CloudData).filter(CloudData.pid == pid, CloudData.name == name).first()

    @staticmethod
    @db_query
    def get_by_local_path(db: Session, local_path, name):
        return db.query(CloudData).filter(CloudData.local_path == local_path, CloudData.name == name).first()

    @staticmethod
    @db_query
    def get_by_dir_name(db: Session, name):
        return db.query(CloudData).filter(CloudData.is_dir == 1, CloudData.name == name).first()

    @staticmethod
    @db_query
    def get_by_name_pid(db: Session, name, pid):
        return db.query(CloudData).filter(CloudData.is_dir == 1, CloudData.pid == pid, CloudData.name == name).first()

    @staticmethod
    @db_query
    def list_page(db: Session, params):
        _var_var_0 = params.get('page', 1)
        _var_var_1 = params.get('page_size', 10)
        _var_var_2 = params.get('order_by', 'name')
        _var_var_3 = params.get('order_type', 'asc')
        _var_var_4 = getattr(CloudData, _var_var_2)
        if _var_var_3 == 'desc':
            _var_var_4 = _var_var_4.desc()
        else:
            _var_var_4 = _var_var_4.asc()
        _var_var_5 = db.query(CloudData).order_by(_var_var_4)
        if params.get('fid'):
            _var_var_5 = _var_var_5.filter_by(fid=params['fid'])
        if params.get('action'):
            _var_var_5 = _var_var_5.filter_by(action=params['action'])
        if params.get('status') is not None:
            _var_var_5 = _var_var_5.filter_by(status=params['status'])
        if params.get('pid'):
            _var_var_5 = _var_var_5.filter_by(pid=params['pid'])
        if params.get('name'):
            _var_var_5 = _var_var_5.filter(CloudData.name.ilike(f"%{params['name']}%"))
        if 'is_dir' in params and params['is_dir'] is not None:
            _var_var_5 = _var_var_5.filter_by(is_dir=params['is_dir'])
        if 'is_media_dir' in params and params['is_media_dir'] is not None:
            _var_var_5 = _var_var_5.filter_by(is_media_dir=params['is_media_dir'])
        if params.get('suffix'):
            _var_var_5 = _var_var_5.filter_by(suffix=params['suffix'])
        _var_var_6 = (_var_var_0 - 1) * _var_var_1
        _var_var_7 = _var_var_5.count()
        return {
            'data': _var_var_5.offset(_var_var_6).limit(_var_var_1).all(),
            'total': _var_var_7,
            'page': _var_var_0,
            'page_size': _var_var_1
        }

    @staticmethod
    @db_update
    def clear(db: Session):
        '''清空云盘数据表'''
        db.query(CloudData).delete(synchronize_session=False)

    @staticmethod
    @db_update
    def delete_by_ids(db: Session, ids):
        _var_var_8 = delete(CloudData).where(CloudData.id.in_(ids))
        db.execute(_var_var_8)

    @staticmethod
    @db_query
    def get_by_ids(db: Session, ids):
        return db.query(CloudData).filter(CloudData.id.in_(ids)).all()

    @staticmethod
    @db_update
    def bulk_insert_file(db: Session, data_list):
        _var_var_5 = '''
        INSERT INTO cloud_data 
            (fid, name, f_modify_time, pid, p_name, full_y_path, pick_code, 
             sha1, size, is_dir, is_media_dir, suffix,thumb,local_name,local_path, action, status, 
             sync_time, create_time, last_update_time)
        VALUES 
            (:fid, :name, :f_modify_time, :pid, :p_name, :full_y_path, :pick_code,
             :sha1, :size, :is_dir, :is_media_dir, :suffix,:thumb, :local_name, :local_path, :action, :status,
             :sync_time, :create_time, :last_update_time)
        ON CONFLICT(fid) DO UPDATE SET
            name = excluded.name,
            f_modify_time = excluded.f_modify_time,
            pid = excluded.pid,
            p_name = excluded.p_name,
            full_y_path = excluded.full_y_path,
            pick_code = excluded.pick_code,
            sha1 = excluded.sha1,
            size = excluded.size,
            is_dir = excluded.is_dir,
            is_media_dir = excluded.is_media_dir,
            suffix = excluded.suffix,
            thumb = excluded.thumb,
            local_name = excluded.local_name,
            local_path = excluded.local_path,
            action = excluded.action,
            status = excluded.status,
            sync_time = excluded.sync_time,
            last_update_time = excluded.last_update_time
        WHERE cloud_data.status != 1
        '''
        db.execute(text(_var_var_5), data_list)

    @staticmethod
    @db_update
    def bulk_insert_dir(db: Session, data_list):
        _var_var_5 = '''
        INSERT INTO cloud_data 
            (fid, name, f_modify_time, pid, p_name, full_y_path, size, is_dir, 
             is_media_dir,local_name,local_path, action, status, sync_time, create_time, last_update_time)
        VALUES 
            (:fid, :name, :f_modify_time, :pid, :p_name, :full_y_path, :size, :is_dir,
             :is_media_dir, :local_name, :local_path, :action, :status, :sync_time, :create_time, :last_update_time)
        ON CONFLICT(fid) DO UPDATE SET
            name = excluded.name,
            f_modify_time = excluded.f_modify_time,
            pid = excluded.pid,
            p_name = excluded.p_name,
            full_y_path = excluded.full_y_path,
            size = excluded.size,
            is_dir = excluded.is_dir,
            is_media_dir = excluded.is_media_dir,
            local_name = excluded.local_name,
            local_path = excluded.local_path,
            action = excluded.action,
            status = excluded.status,
            sync_time = excluded.sync_time,
            last_update_time = excluded.last_update_time
        WHERE cloud_data.status != 1
        '''
        db.execute(text(_var_var_5), data_list)

    @staticmethod
    @db_update
    def bulk_update_cloud(db: Session, data_list):
        '''
        批量更新云盘数据
        :param db: 数据库会话
        :param data_list: 要更新的数据列表，每个数据必须包含id字段
        '''
        _var_var_5 = '''
        INSERT INTO cloud_data 
            (id, p_name, full_y_path, local_name, local_path,size,is_dir,is_media_dir,action,status, desc, sync_time,create_time,last_update_time)
        VALUES 
            (:id, :p_name, :full_y_path, :local_name, :local_path, :size, :is_dir, :is_media_dir, :action, :status, :desc, :sync_time, :create_time, :last_update_time)
        ON CONFLICT(id) DO UPDATE SET
            p_name = excluded.p_name,
            full_y_path = excluded.full_y_path,
            local_name = excluded.local_name,
            local_path = excluded.local_path,
            status = excluded.status,
            desc = excluded.desc,
            sync_time = excluded.sync_time
        '''
        db.execute(text(_var_var_5), [item.to_dict() for item in data_list])

    @staticmethod
    @db_query
    def get_by_pcs(db: Session, pcs):
        return db.query(CloudData).filter(CloudData.pick_code.in_(pcs)).all()

    @staticmethod
    @db_query
    def get_by_pids(db: Session, pids):
        return db.query(CloudData).filter(CloudData.pid.in_(pids)).all()
