# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 11:00 AM
# @Author  : XuChen
# @File    : test_member.py


from __future__ import absolute_import

import operator
import sys
import time
from os import path

import pytest

from Common import assert_module, Consts, json_module
from Common import request_module, mysql_module
from Params.Params import exp_results

test = assert_module.AssertModule()
req = request_module.RequestModule()
mysql_opt = mysql_module.MySqlModule()
act_res = json_module.JsonModule()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def add_member_data():
    """
    预制会员数据
    :param
    :return:
    """
    with pytest.allure.step("预制会员数据"):
        mysql_opt.data_write("INSERT INTO `member` VALUES (1, '1', 'test111', 'xuchen001', 1, '1986-06-01 15:54:53', 33, 1, 1, '110101198606011111', NULL, NULL, NULL, 1000, 1000, 1, 1, 0, 0, '2019-04-08 15:40:47', '2019-04-08 15:40:47');", "bicai_member")
        mysql_opt.data_write("INSERT INTO `member` VALUES (2, '2', 'test222', 'xuchen002', 1, '1986-06-01 15:54:53', 33, 1, 1, '110101198606011111', NULL, NULL, NULL, 1000, 1000, 1, 1, 0, 0, '2019-04-08 15:40:47', '2019-04-08 15:40:47');", "bicai_member")
        mysql_opt.data_write("INSERT INTO `member` VALUES (3, '3', 'test333', 'xuchen003', 1, '1986-06-01 15:54:53', 33, 1, 1, '110101198606011111', NULL, NULL, NULL, 1000, 1000, 1, 1, 0, 0, '2019-04-08 15:40:47', '2019-04-08 15:40:47');", "bicai_member")
        mysql_opt.data_write("INSERT INTO `member` VALUES (4, '4', 'test444', 'xuchen004', 1, '1986-06-01 15:54:53', 33, 1, 1, '110101198606011111', NULL, NULL, NULL, 1000, 1000, 1, 1, 0, 0, '2019-04-08 15:40:47', '2019-04-08 15:40:47');", "bicai_member")
        mysql_opt.data_write("INSERT INTO `member` VALUES (5, '5', 'test555', 'xuchen005', 1, '1986-06-01 15:54:53', 33, 1, 1, '110101198606011111', NULL, NULL, NULL, 1000, 1000, 1, 1, 0, 0, '2019-04-08 15:40:47', '2019-04-08 15:40:47');", "bicai_member")


def del_membe_data():
    with pytest.allure.step("数据回收"):
        mysql_opt.data_write("DELETE FROM member WHERE id = 1 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member WHERE id = 2 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member WHERE id = 3 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member WHERE id = 4 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member WHERE id = 5 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member_label WHERE member_id = 1 ;", "bicai_member")
        mysql_opt.data_write("DELETE FROM member_label WHERE member_id = 2 ;", "bicai_member")


@pytest.allure.feature('Admin_Member', "查询会员列表")
@pytest.allure.severity('blocker')
def test_post_member_select_01():
    """
    查询会员列表
    :param
    :return:
    """
    add_member_data()
    with pytest.allure.step("查询会员列表"):
        response_dicts = req.start_request("post_member_select")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_member_select')['success'], response_dicts['success'])
        test.assert_text(exp_results('post_member_select')['status'], response_dicts['data']['list'][0]['status'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "根据id查询会员")
@pytest.allure.severity('blocker')
def test_get_member_by_id_02():
    """
    查询会员列表
    :param
    :return:
    """
    with pytest.allure.step("根据id查询会员"):
        response_dicts = req.get_request("get_member_by_id", "1")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_member_by_id')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "变更会员状态")
@pytest.allure.severity('blocker')
def test_put_member_status_03():
    """
    变更会员状态
    :param
    :return:
    """
    with pytest.allure.step("变更会员状态"):
        response_dicts = req.start_request("put_member_status", id="1")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_member_status')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "单次给会员打标签")
@pytest.allure.severity('blocker')
def test_post_member_label_04():
    """
    单次给会员打标签
    :param
    :return:
    """
    with pytest.allure.step("单次给会员打标签"):
        response_dicts = req.start_request("post_member_label", memberId="1")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_member_label')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "批量给会员打标签")
@pytest.allure.severity('blocker')
def test_post_member_batch_05():
    """
    单次给会员打标签
    :param
    :return:
    """
    with pytest.allure.step("批量给会员打标签"):
        response_dicts = req.start_request("post_member_batch")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_member_batch')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "批量更新会员等级")
@pytest.allure.severity('blocker')
def test_post_member_batch_level_06():
    """
    批量更新会员等级
    :param
    :return:
    """
    with pytest.allure.step("批量更新会员等级"):
        response_dicts = req.start_request("post_member_batch_level", type="LEVEL")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_member_batch_level')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member', "批量更新会员状态")
@pytest.allure.severity('blocker')
def test_post_member_batch_status_07():
    """
    批量更新会员状态
    :param
    :return:
    """
    with pytest.allure.step("批量更新会员状态"):
        response_dicts = req.start_request("post_member_batch_status", type="STATUS", status="ENABLE")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_member_batch_status')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')
    del_membe_data()


@pytest.allure.feature('Admin_Member_Label1', "创建标签信息")
@pytest.allure.severity('blocker')
def test_post_manager_label_08():
    """
    创建标签信息
    :param
    :return:
    """
    with pytest.allure.step("创建标签信息"):
        response_dicts = req.start_request("post_manager_label", name="xuchen01")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_manager_label')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "查询标签列表")
@pytest.allure.severity('blocker')
def test_get_manager_label_09():
    """
    查询标签列表
    :param
    :return:
    """
    with pytest.allure.step("查询标签列表"):
        response_dicts = req.start_request("get_manager_label")
    with pytest.allure.step("断言success对比"):
        global bq_id  # 标签id
        test.assert_text(exp_results('get_manager_label')['success'], response_dicts['success'])
        # for i in range(0, response_dicts['data']['list'].__len__()):
        #     if response_dicts['data']['list'][i]['name'] == 'xc01':
        #         bq_id = response_dicts['data']['list'][i]['id']
        bq_id = act_res.get_act_value(response_dicts, "xc01")
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "查询标签详情")
@pytest.allure.severity('blocker')
def test_get_manager_label_by_id_10():
    """
    查询标签详情
    :param
    :return:
    """
    with pytest.allure.step("查询标签详情"):
        response_dicts = req.get_request("get_manager_label_by_id", bq_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_manager_label_by_id')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "更新标签信息")
@pytest.allure.severity('blocker')
def test_put_manager_label_11():
    """
    更新标签信息
    :param
    :return:
    """
    with pytest.allure.step("更新标签信息"):
        response_dicts = req.start_request("put_manager_label", id=bq_id, name="xc01")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_manager_label')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "删除标签信息(逻辑删除)")
@pytest.allure.severity('blocker')
def test_del_manager_label_by_id_12():
    """
    删除标签信息(逻辑删除)
    :param
    :return:
    """
    with pytest.allure.step("删除标签信息(逻辑删除)"):
        response_dicts = req.del_request("del_manager_label_by_id", bq_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('del_manager_label_by_id')['success'], response_dicts['success'])
        test.assert_text(exp_results('del_manager_label_by_id')['code'], response_dicts['code'])
        test.assert_text(exp_results('del_manager_label_by_id')['message'], response_dicts['message'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "变更标签状态")
@pytest.allure.severity('blocker')
def test_put_manager_label_status_13():
    """
    变更标签状态
    :param
    :return:
    """
    with pytest.allure.step("变更标签状态"):
        response_dicts = req.start_request("put_manager_label_status", id=bq_id, status="DISABLE")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_manager_label_status')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Label', "删除标签信息(逻辑删除)")
@pytest.allure.severity('blocker')
def test_del_manager_label_by_id_14():
    """
    删除标签信息(逻辑删除)
    :param
    :return:
    """
    with pytest.allure.step("删除标签信息(逻辑删除)"):
        response_dicts = req.del_request("del_manager_label_by_id", bq_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('del_manager_label_by_id')['success1'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Level', "查询等级列表接口")
@pytest.allure.severity('blocker')
def test_get_manager_level_15():
    """
    查询等级列表接口
    :param
    :return:
    """
    with pytest.allure.step("查询等级列表接口"):
        response_dicts = req.start_request("get_manager_level")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_manager_level')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Level', "创建等级信息")
@pytest.allure.severity('blocker')
def test_post_manager_level_16():
    """
    创建等级信息
    :param
    :return:
    """
    with pytest.allure.step("创建等级信息"):
        response_dicts = req.start_request("post_manager_level", name="自动化11测试22")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_manager_level')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Level1', "查询等级列表接口")
@pytest.allure.severity('blocker')
def test_get_manager_level_17():
    """
    查询等级列表接口
    :param
    :return:
    """
    with pytest.allure.step("查询等级列表接口"):
        response_dicts = req.start_request("get_manager_level")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_manager_level')['success'], response_dicts['success'])
        global level_id
        # for i in range(0, response_dicts['data']['list'].__len__()):
        #     if response_dicts['data']['list'][i]['name'] == 'xc01':
        #         bq_id = response_dicts['data']['list'][i]['id']
        level_id = act_res.get_act_value(response_dicts, "自动化11测试22")
        print("----------------------")
        print(level_id)
        print("----------------------")

    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Level1', "根据id查询等级详情接口")
@pytest.allure.severity('blocker')
def test_get_manager_level_by_id_18():
    """
    根据id查询等级详情接口
    :param
    :return:
    """
    with pytest.allure.step("根据id查询等级详情接口"):
        response_dicts = req.get_request("get_manager_level_by_id", level_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_manager_level_by_id')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Member_Level1', "更新等级信息")
@pytest.allure.severity('blocker')
def test_put_manager_level_19():
    """
    更新等级信息
    :param
    :return:
    """
    with pytest.allure.step("更新等级信息"):
        response_dicts = req.start_request("put_manager_level", id=level_id, name='自动化测试')
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_manager_level')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')