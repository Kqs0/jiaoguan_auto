#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/8 22:39
# @Author : kouqingshan

import logging
import requests
from conf import GET_URL, POST_URL, PUT_URL, DELETE_URL, HEADERS_JSON, HEADERS_DATA, COOKIE_URL, ADMIN_USERNAME, \
    ADMIN_PASSWD

# 创建log对象
logger = logging.getLogger(__name__)


class HttpRequest(object):

    def __init__(self):
        params = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWD}
        resp = requests.post(url=COOKIE_URL, data=params)
        self.cookies = resp.cookies

    def list_course(self, **kwargs):
        resp = requests.get(url=GET_URL, headers=None, json=None, cookies=self.cookies)
        logger.info(resp.json())
        return resp, resp.json()

    def post_course(self, json, **kwargs):
        resp = requests.post(url=POST_URL, headers=HEADERS_JSON, json=json, cookies=self.cookies)
        logger.info(resp.json())
        return resp, resp.json()

    def put_course(self, json, **kwargs):
        resp = requests.put(url=PUT_URL, headers=HEADERS_JSON, json=json, cookies=self.cookies)
        logger.info(resp.json())
        return resp, resp.json()

    def delete_course(self, data, **kwargs):
        resp = requests.delete(url=DELETE_URL, headers=HEADERS_DATA, data=data, cookies=self.cookies)
        logger.info(resp.json())
        return resp, resp.json()

if __name__ == '__main__':
    print(HttpRequest.list_course)