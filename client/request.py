#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/8 22:39
# @Author : kouqingshan
import logging

import requests
import login
from conf import GET_URL


def list_course():
    resp = requests.get(url=GET_URL, headers=None, json=None, cookies=login.cookie())
    logging.info(resp.json())
    return resp, resp.json()

if __name__ == '__main__':
    print(list_course())