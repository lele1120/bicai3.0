# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 11:14 AM
# @Author  : XuChen
# @File    : test_product_service.py

from __future__ import absolute_import

import operator
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


@pytest.allure.feature('Admin_Product_Service', "获取数据字典信息")
@pytest.allure.severity('blocker')
def test_get_admin_dict_info_01(get_type_name):
    """
    获取数据字典信息
    :param
    :return:
    """
    with pytest.allure.step("取用户权限列表"):
        response_dicts = req.get_request("get_dict_type", get_type_name)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_dict_type')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')
