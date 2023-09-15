#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/8 22:39
# @Author : kouqingshan

import os.path
import yaml


current_dir = os.path.dirname(os.path.realpath(__file__))
yaml_file = os.path.join(current_dir, 'test.yaml')

try:
    with open(yaml_file, "r") as f:
        # yaml_file1 =f.read()
        CONF = yaml.safe_load(f)
except Exception as e:
    raise e


# 定义用例所需的变量
URL = CONF.get("url", {})
COOKIE_URL = URL.get("cookie", None)
GET_URL = URL.get("get",None)
POST_URL = URL.get("post",None)
PUT_URL = URL.get("put",None)
DELETE_URL = URL.get("delete",None)

ADMIN = CONF.get("admin", {})
ADMIN_USERNAME = ADMIN.get("username", None)
ADMIN_PASSWD = ADMIN.get("password", None)

HEADERS_JSON = {"Content-Type":"application/json"}
HEADERS_DATA = {"Content-Type": "application/x-www-form-urlencoded"}

HOST_INFO = CONF.get("host_info", {})
HOST = HOST_INFO.get("host", None)
HOST_USERNAME = HOST_INFO.get("username", None)
HOST_PASSWORD = HOST_INFO.get("password", None)
