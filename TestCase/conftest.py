# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 4:11 PM
# @Author  : XuChen
# @File    : conftest.py
import time
import pytest

from Common import Consts, request_module
from Common import mysql_module

mysql_opt = mysql_module.MySqlModule()
req = request_module.RequestModule()
username = [
    "xiaohuang", "xiaohong", "xiaolv", "xiaozi", "xiaohei", "xiaobai",
    "xiaocheng"
]
phone_num = [
    "13922290999", "13933390999", "13944490999", "13955590999", "13966690999",
    "13977790999", "13988890999"
]

type_name = [
    "monetary_unit", "rule_symbol", "transaction_state", "surplus_quota",
    "risk_level", "deposit_type", "interest_mode", "pay_time"
]


@pytest.fixture(params=type_name)
def get_type_name(request):
    return request.param


@pytest.fixture(params=username)
def make_username(request):
    return request.param


@pytest.fixture(params=phone_num)
def make_phone_num(request):
    return request.param


@pytest.fixture(scope='module')
def data_operation():
    """
    预制测试数据/预制数据销毁
    """
    with pytest.allure.step("预制测试数据"):
        for i in range(username.__len__()):
            sql_insert = "INSERT INTO sys_user VALUES ( 0, '%s', '{bcrypt}$2a$10$XQgkulIVN0UdDRQXGNISfOBQmxwBBv.XQ75Fq8NPVmBePYIbqxu4W', NULL, '%s', NULL, 3, '2018-08-06 14:44:42', '2018-12-29 10:18:09', '0' )" % (
                str(username[i]), str(phone_num[i]))
            mysql_opt.data_write(sql_insert)
    yield
    with pytest.allure.step("预制数据销毁"):
        for i in range(username.__len__()):
            sql_del = "DELETE FROM sys_user WHERE username = '%s' ;" % username[
                i]
            mysql_opt.data_write(sql_del)


@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    """
    统计运行case数
    :param request:
    :return:
    """
    Consts.TEST_LIST.append('Test')
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')


@pytest.fixture(scope='module')
def login():
    """
    预制登录数据
    """
    with pytest.allure.step("预制登录数据获取授权"):
        response_dicts = req.start_request("login")
        authorization = response_dicts['token_type'].capitalize(
        ) + ' ' + response_dicts['access_token']
        return authorization


@pytest.fixture()
def delete_data():
    """
    数据销毁
    """
    yield
    with pytest.allure.step("数据回收"):

        mysql_opt.data_write("DELETE FROM sys_menu WHERE menu_id = '%s' ;" %
                             menu_id)

        mysql_opt.data_write("DELETE FROM sys_user WHERE user_id = '%s' ;" %
                             user_id)

        mysql_opt.data_write("DELETE FROM sys_role WHERE role_id = '%s' ;" %
                             role_id)

        mysql_opt.data_write("DELETE FROM sys_dict WHERE id = '%s' ;" %
                             dict_id)

        mysql_opt.data_write("DELETE FROM sys_dept WHERE dept_id = '%s' ;" %
                             dept_id)
