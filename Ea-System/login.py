

import requests
from conf import ADMIN_USERNAME, ADMIN_PASSWD, COOKIE_URL


#定义一个方法,用于获取cookies

def cookie():
    params = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWD}
    res = requests.post(url=COOKIE_URL, data=params)
    cookie = res.cookies
    return cookie


if __name__ == '__main__':
    print(cookie())