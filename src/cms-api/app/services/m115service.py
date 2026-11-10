import time
from datetime import datetime
from p115client import P115Client
from p115client.tool import wish_answer, wish_adopt, wish_info
from app.db import get_db
from app.db.account_op import Account115Op
from app.db.models.account import Account115
from app.db.wishlog_op import WishLogOp
from app.log import logger
from app.services.message_service import MessageService
from app.utils.ko_util import random_delay
from app.utils.mjson import JsonUtils

class M115Service:
    
    def __init__(self):
        self._message_service = MessageService()
        self._account_115_op = Account115Op()
        self._wish_log_op = WishLogOp()
        return None
        return None

    
    def sign(self, data):
        _var_var_0 = 0
        _var_var_1 = 0
        _var_var_2 = ''
        _var_var_3 = ''
        try:
            random_delay(data.get('random_delay'))
            with get_db() as _var_var_4:
                _var_var_5 = Account115.get_all(db=_var_var_4, type=2, status=1)
            if not _var_var_5:
                return None
            for _var_var_6 in _var_var_5:
                try:
                    logger.info(f'账号-{_var_var_6.username}-开始签到...')
                    _var_var_7 = P115Client(_var_var_6.cookie, check_for_relogin=False, app='qandroid')
                    _var_var_8 = _var_var_7.user_points_sign_post()
                    logger.info(f'签到响应-{JsonUtils.to_str(_var_var_8)}')
                    if _var_var_8['state']:
                        _var_var_3 += f'{_var_var_6.username} '
                        _var_var_0 += 1
                        logger.info(f'账号-{_var_var_6.username}-签到成功')
                    else:
                        _var_var_1 += 1
                        _var_var_3 += f'{_var_var_6.username} '
                        logger.info(f'账号-{_var_var_6.username}-签到失败-{_var_var_8["message"]}')
                except Exception as _var_var_9:
                    _var_var_1 += 1
                    _var_var_3 += f'{_var_var_6.username} '
                    logger.info(f'账号-{_var_var_6.username}-签到异常-{_var_var_9}')
                finally:
                    logger.info('暂停1s...')
                    time.sleep(1)
        except Exception as _var_var_9:
            _var_var_1 += 1
            _var_var_2 += '签到异常 ✴️\n'
            logger.info(f'签到发生异常: {_var_var_9}')
        _var_var_10 = f'签到日期 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        _var_var_10 += f'签到成功 {_var_var_0} 个\n'
        _var_var_10 += f'{_var_var_3}\n'
        if _var_var_1 > 0:
            _var_var_10 += f'签到失败 {_var_var_1} 个 ✴️\n'
        if _var_var_2:
            _var_var_10 += _var_var_2
        if _var_var_10.endswith('\n'):
            _var_var_10 = _var_var_10[:-1]
        self._message_service.send_msg(title='🏷︎ 115签到 ✅', text=_var_var_10, userid=data.get('userid'), source=data.get('source'))
        logger.info(_var_var_10)
        return None
    def wish_answer(self, data):
        try:
            _var_var_0 = 0
            _var_var_11 = 0
            _var_var_1 = 0
            _var_var_2 = ''
            _var_var_12 = datetime.now().strftime('%Y%m%d')
            random_delay(data.get('random_delay'))
            _var_var_6 = self._account_115_op.get_by_username(data['username'])
            _var_var_7 = P115Client(cookies = _var_var_6.cookie)
            _var_var_13 = _var_var_7.act_xys_get_act_info()
            _var_var_14 = int(_var_var_13['data']['leaving_aid_num'])
            if _var_var_14 == 0:
                logger.info('今日助愿次数已用完')
                self._message_service.send_msg(title = '🏷︎ 115助愿 ✅', text = '今日助愿次数已用完', userid = data.get('userid'), source = data.get('source'))
                return None
            logger.info(f'''账号：{data['username']}-助愿次数：{_var_var_14}''')
            _var_var_15 = self._wish_log_op.get_new_wish(_var_var_14)
            for _var_var_16 in _var_var_15:
                _var_var_17 = f'''助愿-{_var_var_16.wish_username}-{_var_var_16.wish_date}-{_var_var_16.wish_id}'''
                logger.info(f'''开始助愿-{_var_var_16.wish_username}-{_var_var_16.wish_date}-{_var_var_16.wish_id}''')
                _var_var_18 = f'''祝你愿望成功 {_var_var_12}'''
                _var_var_19 = wish_info(_var_var_7, str(_var_var_16.wish_id))
                time.sleep(2)
                _var_var_20 = wish_answer(_var_var_7, str(_var_var_16.wish_id), _var_var_18)
                time.sleep(10)
                logger.info('暂停10s...')
            _var_var_10 = f'''助愿账号 {data['username']}\n助愿日期 {datetime.now().strftime('%Y-%m-%d')}\n'''
            _var_var_10 += f'''助愿成功 {_var_var_0} 个\n预计收益 {int(_var_var_11 * 0.8)}G 空间\n'''
            if _var_var_1 > 0:
                _var_var_10 += f'''助愿失败 {_var_var_1} 个\n{_var_var_2}'''
            if _var_var_10.endswith('\n'):
                _var_var_10 = _var_var_10[:-1]
            self._message_service.send_msg(title = '🏷︎ 115助愿 ✅', text = _var_var_10, userid = data.get('userid'), source = data.get('source'))
            logger.info(_var_var_10)
        except Exception as _var_var_9:
            logger.error(f'助愿异常: {_var_var_9}')

    def wish_adopt(self, data):
        try:
            _var_var_10 = '115采纳助愿完成'
            self._message_service.send_msg(title='🏷︎ 115采纳助愿 ✅', text=_var_var_10, userid=data.get('userid'), source=data.get('source'))
            logger.info(_var_var_10)
        except Exception as _var_var_9:
            logger.info(f'采纳助愿发生异常: {_var_var_9}')

    def test(self):
        self._message_service.send_msg(title = '海贼王1001-1003整理成功', text = '海贼王1001-1003整理成功', image = 'https://image.tmdb.org/t/p/h632/y7IozUi2dwICMl8aGvLxjTmJDYZ.jpg')
        return None
        return None


if __name__ == '__main__':
    logger.info('start...')
    M115Service().wish_adopt({
        'username': "demo" })

