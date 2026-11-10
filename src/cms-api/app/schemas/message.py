from pydantic import BaseModel
from app.schemas.types import MessageChannel

class CommonMessage(BaseModel):
    '''外来消息'''
    userid: str | int | None = None
    username: str = None
    channel: MessageChannel | None = None
    text: str = None
    date: int = None
    action: int = 0
    
    def to_dict(self):
        """转换为字典"""
        return {
            _var_var_0: (
                _var_var_1.value
                if isinstance(_var_var_1, MessageChannel)
                else _var_var_1
            )
            for _var_var_0, _var_var_1 in self.dict().items()
        }

