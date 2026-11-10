# File: dom.py (Cleaned & Decompiled)
from typing import Union

class DomUtils:
    @staticmethod
    def tag_value(tag_item, tag_name: str, attname: str = '', default: Union[str, int] = None):
        """
        解析XML标签值
        """
        _var_var_0 = tag_item.getElementsByTagName(tag_name)
        if _var_var_0:
            if attname:
                _var_var_1 = _var_var_0[0].getAttribute(attname)
                if _var_var_1:
                    return _var_var_1
            _var_var_2 = _var_var_0[0].firstChild
            if _var_var_2:
                return _var_var_2.data
        return default

    @staticmethod
    def add_node(doc, parent, name: str, value: str = None):
        """
        添加一个DOM节点
        """
        _var_var_3 = doc.createElement(name)
        parent.appendChild(_var_var_3)
        if value is not None:
            _var_var_4 = doc.createTextNode(str(value))
            _var_var_3.appendChild(_var_var_4)
        return _var_var_3