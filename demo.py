#! /usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import requests
from common.login import cookie

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('116.63.11.59',port=22,username='root', password='Huawei@123', timeout=120,
            look_for_keys=True,allow_agent=False,key_filename=None,pkey=None)
cmd = "ifconfig | grep inet | awk 'NR==1{print $2}'"
cmd1 = "date | awk '{print $4}'"
stdin, stdout, stderr = ssh.exec_command(cmd)
stdin1, stdout1, stderr1 = ssh.exec_command(cmd1)
# print(stdout.readline())
# print(stdout.read())
print(stdout.read().decode("utf-8"))
print(stdout1.readline())

url = "http://116.63.11.59:9000/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
res = requests.get(url=url, cookies=cookie())
print(res, res.json())
course = res.json()["retlist"]
print(len(course),course)