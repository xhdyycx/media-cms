# -*- coding: utf-8 -*-
import abc
import time

class Singleton(abc.ABCMeta):
    '''类单例模式'''
    _instances: dict = {}
    _instance_created_time: dict = {}
    _class_expiration_seconds: dict = {}
    _default_expiration_seconds: int = 86400

    def __call__(cls, *args, **kwargs):
        key = (cls, args, frozenset(kwargs.items()))
        now = time.time()
        exp = cls._class_expiration_seconds.get(cls, cls._default_expiration_seconds)
        if key not in cls._instances or key not in cls._instance_created_time or now - cls._instance_created_time[key] > exp:
            cls._instances[key] = super().__call__(*args, **kwargs)
            cls._instance_created_time[key] = now
        return cls._instances[key]

class ExpiredSingleton(abc.ABCMeta):
    '''可过期类单例模式'''
    _instances: dict = {}
    _instance_created_time: dict = {}
    _class_expiration_seconds: dict = {}
    _default_expiration_seconds: int = 86400

    def __call__(cls, *args, **kwargs):
        key = (cls, args, frozenset(kwargs.items()))
        now = time.time()
        exp = cls._class_expiration_seconds.get(cls, cls._default_expiration_seconds)
        if key not in cls._instances or key not in cls._instance_created_time or now - cls._instance_created_time[key] > exp:
            cls._instances[key] = super().__call__(*args, **kwargs)
            cls._instance_created_time[key] = now
        return cls._instances[key]

    @classmethod
    def set_expiration_time(cls, hours=24):
        if cls is ExpiredSingleton:
            cls._default_expiration_seconds = hours * 3600
        else:
            cls._class_expiration_seconds[cls] = hours * 3600

    @classmethod
    def get_expiration_time(cls):
        if cls is ExpiredSingleton:
            return cls._default_expiration_seconds / 3600
        return cls._class_expiration_seconds.get(cls, cls._default_expiration_seconds) / 3600

class AbstractSingleton(abc.ABC, metaclass=Singleton):
    '''抽象类单例模式'''
    pass