from typing import TypeVar
from datclass import get_datclass
DatClass = get_datclass(log = False)
DataType = TypeVar('DataType', bound = DatClass)

