from typing import Optional
from blacksheep import Request
from blacksheep.server.authentication import AuthenticationHandler
from guardpost import Identity
from app.core.auth import verify_token

class JWTAuthenticationHandler(AuthenticationHandler):
    '''JWT认证处理器'''
    
    def __init__(self):
        super().__init__()
    async def authenticate(self, request: Request) -> Optional[dict]:
        '''验证请求的认证信息'''
        _var_var_0 = request.get_first_header(b'Authorization')
        if not _var_var_0:
            request.identity = None
            return request.identity
        if not _var_var_0.startswith(b'Bearer '):
            request.identity = None
            return request.identity
        _var_var_1 = _var_var_0.split(b' ')
        if not _var_var_1 or len(_var_var_1) != 2:
            request.identity = None
            return request.identity
        _var_var_2 = _var_var_1[1]
        _var_var_3 = verify_token(_var_var_2.decode())
        if _var_var_3:
            request.identity = Identity({'id': _var_var_3['id'], 'username': _var_var_3['username']}, 'login')
        else:
            request.identity = None
        return request.identity

