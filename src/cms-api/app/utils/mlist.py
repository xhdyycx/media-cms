class MListUtils:
    @staticmethod
    def split_list_by_size(lst, size):
        '''将列表分割成指定大小的子列表'''
        if size <= 0:
            raise ValueError('size必须大于0')
        return [lst[_var_var_0:_var_var_0 + size] for _var_var_0 in range(0, len(lst), size)]


