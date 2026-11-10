from typing import List
from aligo import Aligo, BatchRequest, BatchSubRequest, set_config_folder

class CustomAligo(Aligo):
    '''自定义 aligo '''
    V3_FILE_DELETE = '/v3/file/delete'
    
    def delete_file(self, file_id, drive_id):
        '''删除文件'''
        if not drive_id:
            drive_id
        drive_id = self.default_drive_id
        _var_var_0 = self.post(self.V3_FILE_DELETE, body = {
            'drive_id': drive_id,
            'file_id': file_id })
        return _var_var_0.status_code == 204
        return None

    
    def batch_delete_files(self, file_id_list, drive_id):
        '''批量删除文件'''
        if not drive_id:
            drive_id
        drive_id = self.default_drive_id

    
    def clear_recyclebin(self, drive_id):
        '''清空回收站'''
        if not drive_id:
            drive_id
        drive_id = self.default_drive_id
        _var_var_0 = self.post('/v2/recyclebin/clear', body = {
            'drive_id': drive_id })
        return _var_var_0.status_code == 202
        return None



