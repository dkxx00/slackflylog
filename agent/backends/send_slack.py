# -*- coding: utf-8 -*-

from urllib2 import urlopen

import copy
import random
# import telegramlog.constants
from ..log import logger

# logger = logging.getLogger(telegramlog.constants.AGENT_LOGGER_NAME)
#
# MULTIPLE_CHANNEL_BOT_API = '1944182514:AAFeRKSO6S3TBRmPBxTZTO6JX-xh6BAWE5Y'
# MULTIPLE_CHANNEL_USER_API = '@server_error_log'


class TelegramBackend(object):
    """
    发送tele
    """

    def __init__(self, sender_list):
        """
        初始化
        sender_list可以保证只要发送失败就尝试下一个
        """
        self.sender_list = sender_list

    def emit(self, title, content, receiver_list):
        """
        发送
        """

        sender_list = copy.deepcopy(self.sender_list)
        logger.error("sender_list %s", sender_list)

        while sender_list:
            random.shuffle(sender_list)

            # 取出最后一个
            params = sender_list.pop()

            try:
                logger.error("params %s", params)
                bot_api = params['bot_api']
                user_api = params['user_api']
                self._send_msg_to_telegram(bot_api, user_api, content, title)
                return True
            except:
                logger.error('exc occur. params: %s', params, exc_info=True)
        else:
            # 就是循环完了，也没发送成功
            return False

    def _send_msg_to_telegram(self, bot_api, user_api, send_msg, title):
        """
        :param bot_api: 机器人密钥
        :param user_api: 频道link
        :param send_msg: 发送内容
        :return:
        """
        import urllib

        if not send_msg:
            return False

        full_content = '\n\n'.join([title, send_msg])
        logger.error("full_content [[[[[[[%s]]]]]]]", urllib.quote(full_content))

        url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(bot_api, user_api, urllib.quote(full_content))
        logger.error("url %s", url)
        urlopen(url).close()
        return True
