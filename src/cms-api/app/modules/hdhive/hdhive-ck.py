from app.modules.hdhive.hdhive_web import HDHiveWebClient
from app.utils.mjson import JsonUtils
if __name__ == '__main__':
    client = HDHiveWebClient()
    print('HDHiveWebClient loaded:', client.base_url)
    login_next_action = client.get_login_next_action()
    print('HDHiveWebClient login_next_action:', login_next_action)
    token = '<TOKEN>'
    token = ''
    ck = f'''token={token}'''
    ret = client.decode_jwt(token)
    print(JsonUtils.to_str(ret))
    client.set_cookies(ck)
    ret = client.get_account_next_action()
    print('HDHiveWebClient get_account_next_action:', JsonUtils.to_str(ret))

