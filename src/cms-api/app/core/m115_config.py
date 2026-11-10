import os
import secrets
from typing import Any, Dict, Final
from urllib3_future.util.timeout import Timeout

class M115Config:
    __module__ = __name__
    __qualname__ = 'M115Config'
    IOS_UA_2: Final = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 115wangpan_ios/36.2.20'
    IOS_UA: Final = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B956 115wangpan_ios/36.2.20'
    CHROME_UA: Final = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    CHROME_PLATFORMS: Final = ('Windows NT 10.0; Win64; x64', 'Macintosh; Intel Mac OS X 10_15_7', 'X11; Linux x86_64')
    REQUEST_TIMEOUT_SECONDS: Final = float(os.getenv('REQUEST_TIMEOUT_SECONDS', '30'))
    REQUEST_TIMEOUT: Final = Timeout(total = REQUEST_TIMEOUT_SECONDS, connect = REQUEST_TIMEOUT_SECONDS, read = REQUEST_TIMEOUT_SECONDS)


