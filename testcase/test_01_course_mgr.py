#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/8 22:39
# @Author : kouqingshan
import logging

import pytest
from pytest import mark as MARK
from client.request import HttpRequest
from common.tool import ssh_cmd

# 创建log对象
logger = logging.getLogger(__name__)
# urllib3设置日志显示级别
logging.getLogger("urllib3").setLevel(logging.DEBUG)
logging.getLogger("paramiko").setLevel(logging.WARNING)


class TestApi:

    @classmethod
    def setup_class(cls):
        logger.info("--------------setup_class开始---------------------")
        cls.HttpRequest = HttpRequest()

    @classmethod
    def teardown_class(cls):
        logger.info("--------------teardown_class结束---------------------")
        pass

    @classmethod
    def setup_method(self, method):
        logger.info("--------------setup_method开始---------------------")
        pass

    @classmethod
    def teardown_method(self, method):
        logger.info("--------------teardown_method结束---------------------")
        pass

    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_get_api_001"])
    def test_get_courser(self, id, code):
        # resp = requests.get(url=GET_URL, cookies=self.cookie)
        # log.info(resp.json())
        resp, body = self.HttpRequest.list_course()
        assert resp.status_code == code, "get course failed"

    @MARK.level1
    @MARK.parametrize("code", [200])
    @MARK.parametrize("params", [pytest.param({"action": "add_course_json", "data":
                                     {"name": "初中化学4", "desc": "初中化学课程", "display_idx": "4"}}, id="01"),
                                 pytest.param({"action": "add_course_json", "data":
                                     {"name": "初中化学5", "desc": "初中化学课程", "display_idx": "4"}}, id="02")])
    @MARK.parametrize("id", ["Test_post_api_001"])
    def test_post_course(self, id, code, params):
        # params = {"action": "add_course_json",
        #           "data": {"name": "初中化学3", "desc": "初中化学课程", "display_idx": "4"}}
        # headers = {"Content-Type":"application/json"}
        # resp = requests.post(url=POST_URL, headers=headers, json=params, cookies=self.cookie)
        resp, body = self.HttpRequest.post_course(json=params)
        assert resp.status_code == code, "post course failed"

    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_put_api_001"])
    def test_put_course(self, id, code):
        params = {"action": "modify_course", "id": "5827",
                  "newdata": {"name": "初中化学2", "desc": "初中化学课程", "display_idx": "4"}}
        # headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # resp = requests.put(url=PUT_URL, json=params, headers=headers, cookies=self.cookie)
        resp, body = self.HttpRequest.put_course(json=params)
        assert resp.status_code == code, "put course failed"

    @MARK.level1
    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_delete_api_001"])
    def test_delete_course(self, id, code):
        params = {"action": "delete_course", "id": "5823"}
        # headers = {"Content-Type":"application/x-www-form-urlencoded"}
        # resp = requests.delete(url=DELETE_URL, data=params, headers=headers, cookies=self.cookie)
        resp, body = self.HttpRequest.delete_course(data=params)
        assert resp.status_code == code, "delete course failed"

    def test_check_process(self):
        resp = ssh_cmd("ps -ef | grep -v grep |grep jenkins")
        # print(resp)
        assert resp