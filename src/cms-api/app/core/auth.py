# File: auth.py (Cleaned & Decompiled)
from datetime import datetime, timedelta
from typing import Optional
import jwt
from blacksheep.server.authorization import Policy
from guardpost import AuthorizationContext, Requirement
from app.core.env import NovaEnv
from app.core.license import LicenseInfo

nova_env = NovaEnv()
if nova_env.RUN_ENV == 'dev':
    SECRET_KEY = f'{nova_env.RUN_ENV}-{nova_env.JWT_SECRET_KEY}'
else:
    SECRET_KEY = f'{nova_env.RUN_ENV}-{nova_env.JWT_SECRET_KEY}-{nova_env.APP_VERSION}-{LicenseInfo().get_type()}'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 10080

def create_access_token(data, expires_delta=None):
    """创建 JWT token"""
    _var_var_0 = data.copy()
    if expires_delta:
        _var_var_1 = datetime.utcnow() + expires_delta
    else:
        _var_var_1 = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    _var_var_0.update({'exp': _var_var_1})
    _var_var_2 = jwt.encode(_var_var_0, SECRET_KEY, algorithm=ALGORITHM)
    return _var_var_2

def verify_token(token):
    """验证 JWT token"""
    try:
        _var_var_3 = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return _var_var_3
    except jwt.PyJWTError:
        return None

class ProRequirement(Requirement):
    def handle(self, context: AuthorizationContext):
        _var_var_4 = context.identity
        if _var_var_4 is not None and LicenseInfo().get_type().lower() == 'pro':
            context.succeed(self)

class ProPolicy(Policy):
    def __init__(self):
        super().__init__('pro', ProRequirement())