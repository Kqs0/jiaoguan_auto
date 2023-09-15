#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/8 22:39
# @Author : kouqingshan
import logging
import paramiko
import requests
from conf import ADMIN_USERNAME, ADMIN_PASSWD, COOKIE_URL, HOST, HOST_USERNAME, HOST_PASSWORD
logger = logging.getLogger(__name__)


# 定义一个方法,用于获取cookies
def cookie():
    params = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWD}
    res = requests.post(url=COOKIE_URL, data=params)
    cookie = res.cookies
    return cookie

# 定义一个方法远程执行shell命令
def ssh_cmd(cmd):
    # 创建一个ssh对象
    client = paramiko.SSHClient()
    # 如果之前没有，连接过的ip，会出现选择yes或者no的操作
    # 自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    client.connect(hostname=HOST,
                   port=22,
                   username=HOST_USERNAME,
                   password=HOST_PASSWORD)
    # 执行操作
    stdin, stdout, stderr = client.exec_command(cmd)
    # 获取命令执行的结果
    result = stdout.read().decode('utf-8')
    # 关闭连接
    client.close()
    logger.debug(result)
    return result



if __name__ == '__main__':
    ssh_cmd("ifconfig")


