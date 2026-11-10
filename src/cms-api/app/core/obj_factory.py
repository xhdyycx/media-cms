from typing import Dict, Any, Type, TypeVar
from app.core.env import configEnv
from app.core.m115 import M115
from app.core.m123 import M123
from app.core.mconfig import ServiceConfig, TmdbConfig, AutoOrganizeConfig
from app.db import get_db
from app.db.config_op import ConfigOp
from app.modules.hdhive.hdhive_proxy import HDHiveProxyClient
from app.schemas.types import ConfigType
T = TypeVar('T')

class ObjFactory:
    '''
    通用对象工厂类，用于管理不同类型的对象实例
    '''
    _instances: Dict[(str, Dict[(str, Any)])] = { }
    @classmethod
    def get_instance(cls, obj_type: Type[T], identifier: str = 'default') -> T:
        """
        获取指定类型和标识符的对象实例，如果不存在则创建

        Args:
            obj_type: 对象类型
            identifier: 实例标识符，默认为"default"
        """
        _var_var_0 = obj_type.__name__
        if _var_var_0 not in cls._instances:
            cls._instances[_var_var_0] = {}
        if identifier not in cls._instances[_var_var_0]:
            cls._instances[_var_var_0][identifier] = cls._create_instance(obj_type)
        return cls._instances[_var_var_0][identifier]
    @classmethod
    def _create_instance(cls, obj_type: Type[T]) -> T:
        """
        创建指定类型的实例

        Args:
            obj_type: 对象类型
        """
        if obj_type == M115:
            with get_db() as _var_var_1:
                _var_var_2 = ConfigOp(_var_var_1)
                _var_var_3 = _var_var_2.get_by_key('core')
                _var_var_4 = _var_var_3['basic']['COOKIE_FILE_PATH']
                _var_var_5 = _var_var_3['basic']['DEVICE_TYPE']
                return M115(_var_var_4, _var_var_5)
        if obj_type == M123:
            return M123()
        if obj_type == HDHiveProxyClient:
            return HDHiveProxyClient(proxy=configEnv.nova_proxy)
        if obj_type == AutoOrganizeConfig:
            with get_db() as _var_var_1:
                _var_var_2 = ConfigOp(_var_var_1)
                _var_var_3 = _var_var_2.get_by_key('auto_organize')
                return AutoOrganizeConfig(_var_var_3)
        if obj_type == ServiceConfig:
            with get_db() as _var_var_1:
                _var_var_2 = ConfigOp(_var_var_1)
                _var_var_3 = _var_var_2.get_by_key(ConfigType.SERVICE_CONFIG.name)
                return ServiceConfig(_var_var_3)
        if obj_type == TmdbConfig:
            with get_db() as _var_var_1:
                _var_var_2 = ConfigOp(_var_var_1)
                _var_var_3 = _var_var_2.get_by_key(ConfigType.core.name)
                return TmdbConfig(_var_var_3['tmdb'])
        raise ValueError(f'未支持的类型: {obj_type.__name__}')
    @classmethod
    def refresh_instance(cls, obj_type: Type[T], identifier: str = 'default') -> T:
        """
        刷新指定类型和标识符的对象实例

        Args:
            obj_type: 对象类型
            identifier: 实例标识符，默认为"default"
        """
        _var_var_0 = obj_type.__name__
        if _var_var_0 not in cls._instances:
            cls._instances[_var_var_0] = {}
        cls._instances[_var_var_0][identifier] = cls._create_instance(obj_type)
        return cls._instances[_var_var_0][identifier]
    @classmethod
    def remove_instance(cls, obj_type: Type[T], identifier: str) -> None:
        """
        移除指定类型和标识符的对象实例

        Args:
            obj_type: 对象类型
            identifier: 要移除的实例标识符
        """
        _var_var_0 = obj_type.__name__
        if _var_var_0 in cls._instances:
            cls._instances[_var_var_0].pop(identifier, None)
    @classmethod
    def get_all_instances(cls, obj_type: Type[T]) -> Dict[str, T]:
        """
        获取指定类型的所有对象实例

        Args:
            obj_type: 对象类型
        """
        _var_var_0 = obj_type.__name__
        return cls._instances.get(_var_var_0, {}).copy()


