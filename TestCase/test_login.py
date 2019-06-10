# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 5:08 PM
# @Author  : XuChen
# @File    : test_login.py

from __future__ import absolute_import

import sys
import time
from os import path

import pytest

from Common import assert_module, Consts
from Common import request_module, mysql_module
from Params.Params import exp_results

test = assert_module.AssertModule()
req = request_module.RequestModule()
mysql_opt = mysql_module.MySqlModule()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# 准备测试数据


class TestLogin:
    @pytest.allure.feature("Login", "登录")
    @pytest.allure.severity('blocker')
    def test_login(self, data_operation, make_username):
        """
        登录验证获取授权
        """
        with pytest.allure.step("登录"):
            # response_dicts = req.start_request("login", username=make_username)
            response_dicts = req.login_request(username=make_username)
            print(response_dicts)
        # with pytest.allure.step("登录"):
        #     response_dicts = req.start_request("login", username=make_username)
        # with pytest.allure.step("获取用户授权"):
        #     global authorization  # 获取登录授权
        #
        #     authorization = response_dicts['token_type'].capitalize() + ' ' + response_dicts['access_token']
        #
        # with pytest.allure.step("预期结果:" + str(exp_results('login')['scope']) + "与实际结果"
        #                         + str(response_dicts['scope']) + "做对比"):
        #     assert response_dicts['scope'] == exp_results('login')['scope']
        #
        # with pytest.allure.step("预期结果:" + str(exp_results('login')['license']) + "与实际结果"
        #                         + str(response_dicts['license']) + "做对比"):
        #     assert response_dicts['license'] == exp_results('login')['license']

        Consts.RESULT_LIST.append('True')
