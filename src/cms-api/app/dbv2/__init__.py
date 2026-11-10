import sqlite_utils
from app.core.env import novaEnv
db_config_path = novaEnv.CONFIG_PATH / 'novamedia-config.db'
db_cloud123_path = novaEnv.CONFIG_PATH / 'novamedia-cloud123.db'
table_account = 'account'
table_cloud123 = 'cloud123'

def init_dbv2():
    _var_var_0 = sqlite_utils.Database(db_cloud123_path)


