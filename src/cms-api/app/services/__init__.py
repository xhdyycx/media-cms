# File: __init__.py (Cleaned & Decompiled)
from abc import ABCMeta
from typing import Any
from app.core.mconfig import ServiceConfig
from app.core.obj_factory import ObjFactory

class BaseService(metaclass=ABCMeta):
    def __init__(self):
        pass

    @property
    def get_config(self) -> ServiceConfig:
        return ObjFactory.get_instance(ServiceConfig)

    def is_enable(self, config_type: str):
        return self.get_config.get(config_type)