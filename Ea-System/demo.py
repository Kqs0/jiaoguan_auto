#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import requests
import login
import logging
from pytest import mark as MARK
from conf import GET_URL, POST_URL, PUT_URL, DELETE_URL

import urllib3

from client.request import list_course

logging.getLogger("requests").setLevel((logging.WARNING))

# urllib3.disable_warnings()



class TestApi:

    @classmethod
    def setup_class(self):
        self.cookie = login.cookie()

    @classmethod
    def teardown_class(self):
        pass

    @classmethod
    def setup_method(self):
        pass

    @classmethod
    def teardown_method(self):
        pass

    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_get_api_001"])
    def test_get_courser(self, id, code):
        # resp = requests.get(url=GET_URL, cookies=self.cookie)
        # log.info(resp.json())
        resp, body = list_course()
        logging.info(body)
        assert resp.status_code == code, "get course failed"

    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_post_api_001"])
    def test_post_course(self, id, code):
        params = {"action" : "add_course_json","data": {"name":"初中化学3","desc":"初中化学课程","display_idx":"4"}}
        headers = {"Content-Type":"application/json"}
        resp = requests.post(url=POST_URL, headers=headers, json=params, cookies=self.cookie)
        assert resp.status_code == code, "post course failed"


    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_put_api_001"])
    def test_put_course(self, id, code):
        params = {"action":"modify_course","id":"5827","newdata":{"name":"初中化学2","desc":"初中化学课程","display_idx":"4"}}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.put(url=PUT_URL, json=params, headers=headers, cookies=self.cookie)
        assert resp.status_code == code, "put course failed"

    @MARK.parametrize("code", [200])
    @MARK.parametrize("id", ["Test_delete_api_001"])
    def test_delete_course(self, id, code):
        params = {"action":"delete_course","id":"5823"}
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        resp = requests.delete(url=DELETE_URL, data=params, headers=headers, cookies=self.cookie)
        assert resp.status_code == code, "delete course failed"


    




