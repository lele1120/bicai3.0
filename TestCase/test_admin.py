# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 2:34 PM
# @Author  : XuChen
# @File    : test_admin.py

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
Consts.MYSQL_ENVIRONMENT = 'bicai_admin'


@pytest.allure.feature('Admin_User', "获取用户权限列表")
@pytest.allure.severity('blocker')
def test_get_admin_user_info_01():
    """
    获取用户权限列表
    :param login: 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("取用户权限列表"):
        response_dicts = req.start_request("get_admin_user_info")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_admin_user_info')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "获取用户管理页面")
@pytest.allure.severity('blocker')
def test_get_admin_user_page_02():
    """
    获取用户管理页面信息
    :param login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("获取用户管理页面"):
        response_dicts = req.start_request("get_admin_user_userPage")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_admin_user_info')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "添加新用户")
@pytest.allure.severity('blocker')
def test_post_add_admin_user_03():
    """
    添加新用户
    :param login: login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("获取用户管理页面"):
        response_dicts = req.start_request("add_admin_user")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('add_admin_user')['success'], response_dicts['success'])
    with pytest.allure.step("添加用户后查询数据库,断言是否查询出数据，是否del——flag为:0"):
        user_add_info = mysql_opt.data_read("SELECT user_id,del_flag,phone FROM sys_user WHERE username = 'test1';", "bicai_admin")
        global user_id  # 新添加用户ID
        global phone  # 新添加用户ID
        global del_flag
        user_id = user_add_info[0]
        del_flag = user_add_info[1]
        phone = user_add_info[2]
        test.assert_text(user_add_info[1], '0')
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "添加已有用户")
@pytest.allure.severity('blocker')
def test_post_add_admin_user_again_04():
    """
    添加重复用户
    :param login: login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("获取用户管理页面"):
        response_dicts = req.start_request("add_admin_user")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('add_admin_user')['success1'], response_dicts['success'])
    with pytest.allure.step("断言code对比"):
        test.assert_text(exp_results('add_admin_user')['code'], response_dicts['code'])
    with pytest.allure.step("断言message对比"):
        test.assert_text(exp_results('add_admin_user')['message'], response_dicts['message'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "根据新创建用户test1查询用户管理页面")
@pytest.allure.severity('blocker')
def test_get_admin_user_page_by_username_05():
    """
    根据username获取用户管理页面信息
    :param login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("根据新创建用户test1查询用户管理页面"):
        response_dicts = req.start_request("get_admin_user_userPage_by_username", username="test1")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_admin_user_userPage_by_username')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "修改用户test1手机号并查询数据库")
@pytest.allure.severity('blocker')
def test_put_admin_user_modify_phone_06():
    """
    修改用户test1手机号并查询数据库
    :param login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("根据新创建用户test1查询用户管理页面"):
        response_dicts = req.start_request("modify_user_phone", userId=user_id, phone='13922222222')
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('modify_user_phone')['success'], response_dicts['success'])
    with pytest.allure.step("修改手机号后查询数据库,断言是否修改成功"):
        modify_phone = mysql_opt.data_read("SELECT phone FROM sys_user WHERE user_id ='%s';" % user_id, "bicai_admin")[0]
        test.assert_not_in_results(modify_phone, phone)
        test.assert_in_results(modify_phone, '13922222222')
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "修改用户test1密码")
@pytest.allure.severity('blocker')
def test_put_admin_user_modify_userinfo_07():
    """
    修改用户test1手机号并查询数据库
    :param login 预制登录信息 获取授权authorization:
    :return:
    """
    with pytest.allure.step("修改用户test1密码"):
        response_dicts = req.start_request("modify_user_userinfo", userId=user_id,
                                           newpassword1='999999', newpassword2='999999')
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('modify_user_userinfo')['success'], response_dicts['success'])

    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "根据部门获取角色列表")
@pytest.allure.severity('blocker')
def test_get_role_list_08():
    """
    根据部门获取角色列表
    :param login:
    :return:
    """
    with pytest.allure.step("根据部门获取角色列表"):
        response_dicts = req.get_request("get_role_roleList", '1')
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_role_roleList')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Menu', "获取查看菜单树")
@pytest.allure.severity('blocker')
def test_get_admin_menu_all_tree_09():
    """
    获取查看菜单
    :param login:
    :return:
    """
    with pytest.allure.step("获取查看菜单树"):
        response_dicts = req.start_request("get_menu_allTree")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_menu_allTree')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Menu', "添加菜单")
@pytest.allure.severity('blocker')
def test_post_add_menu_10():
    """
    添加菜单
    :param login:
    :return:
    """
    with pytest.allure.step("添加菜单"):
        response_dicts = req.start_request("add_menu")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('add_menu')['success'], response_dicts['success'])
    with pytest.allure.step("添加菜单后查询数据库,断言是否查询出数据，是否del——flag为:0"):
        menu_add_info = mysql_opt.data_read("SELECT menu_id,del_flag,parent_id FROM sys_menu WHERE name = '自动化测试';", "bicai_admin")
        global menu_id  # 新添加菜单id
        global menu_del_flag  # 新添加菜单删除标记
        global menu_parent_id  # 新添加菜单父菜单ID
        menu_id = menu_add_info[0]
        menu_del_flag = menu_add_info[1]
        menu_parent_id = menu_add_info[2]
        test.assert_text(menu_del_flag, '0')
    with pytest.allure.step("查询数据库结果:"):
        with pytest.allure.step("menu_id:" + str(menu_id)):
            pass
        with pytest.allure.step("menu_del_flag:" + str(menu_del_flag)):
            pass
        with pytest.allure.step("menu_parent_id:" + str(menu_parent_id)):
            pass
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Menu', "获取查看菜单")
@pytest.allure.severity('blocker')
def test_get_admin_menu_by_id_11():
    """
    根据menu_id获取查看菜单
    :param login:
    :return:
    """
    with pytest.allure.step("获取查看菜单"):
        response_dicts = req.get_request("get_menu_by_menuId", str(menu_id))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_menu_by_menuId')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Menu', "修改菜单")
@pytest.allure.severity('blocker')
def test_put_modify_menu_12():
    """
    修改菜单
    :param login:
    :return:
    """
    with pytest.allure.step("修改菜单"):
        response_dicts = req.start_request("modify_menu", menuId=menu_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('modify_menu')['success'], response_dicts['success'])
    with pytest.allure.step("修改菜单后查询数据库,断言是否查询出数据"):
        menu_modify_name = mysql_opt.data_read("SELECT name FROM sys_menu WHERE menu_id = '%s';"% menu_id, "bicai_admin")[0]
    test.assert_text(menu_modify_name, '自动化测试123')
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Menu', "删除菜单")
@pytest.allure.severity('blocker')
def test_delete_del_menu_13():
    """
    删除菜单
    :param login:
    :return:
    """
    with pytest.allure.step("删除菜单"):
        response_dicts = req.del_request("del_menu", str(menu_id))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('del_menu')['success'], response_dicts['success'])
    with pytest.allure.step("修改菜单后查询数据库,断言del_flag是否正确"):
        menu_del_flag = mysql_opt.data_read("SELECT del_flag FROM sys_menu WHERE menu_id = '%s';"% menu_id, "bicai_admin")[0]
        test.assert_text(menu_del_flag, '1')
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "添加角色")
@pytest.allure.severity('blocker')
def test_post_add_role_14():
    """
    添加角色
    :param login:
    :return:
    """
    with pytest.allure.step("添加角色"):
        response_dicts = req.start_request("add_role")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('add_role')['success'], response_dicts['success'])
    with pytest.allure.step("添加菜单后查询数据库,断言是否查询出数据，是否del——flag为:0"):
        role_add_info = mysql_opt.data_read("SELECT role_id,del_flag FROM sys_role WHERE role_name = '我的自动化测试';", "bicai_admin")
        global role_id  # 新添加角色id
        global role_del_flag  # 新添加角色删除标记
        role_id = role_add_info[0]
        role_del_flag = role_add_info[1]
        test.assert_text(role_del_flag, '0')
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "获取角色列表")
@pytest.allure.severity('blocker')
def test_get_role_role_page_15():
    """
    添加角色
    :param login:
    :return:
    """
    with pytest.allure.step("获取角色列表"):
        response_dicts = req.start_request("get_role_rolePage")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_role_rolePage')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "修改角色信息")
@pytest.allure.severity('blocker')
def test_put_modify_role_16():

    """
    修改角色信息
    :param login:
    :return:
    """
    with pytest.allure.step("修改角色信息"):
        response_dicts = req.start_request("modify_role", roleId=role_id)

    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('modify_role')['success'], response_dicts['success'])
    with pytest.allure.step("修改角色后查询数据库,断言是否查询出数据，是否del——flag为:0"):
        role_modify_info = mysql_opt.data_read("SELECT role_name,role_code,role_desc,del_flag FROM sys_role WHERE role_id = '% s';" % role_id, "bicai_admin")
        role_modify_name = role_modify_info[0]  # 修改后role_name
        global role_modify_code   # 修改后role_code
        role_modify_code = role_modify_info[1]
        role_modify_desc = role_modify_info[2]  # 修改后role_desc
        role_del_flag = role_modify_info[3]  # 修改后del_flag
    test.assert_text(exp_results('modify_role')['role_name'], role_modify_name)
    test.assert_text(exp_results('modify_role')['role_code'], role_modify_code)
    test.assert_text(exp_results('modify_role')['role_desc'], role_modify_desc)
    test.assert_text(exp_results('modify_role')['del_flag'], str(role_del_flag))
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "根据角色获取权限")
@pytest.allure.severity('blocker')
def test_get_role_tree_17():
    """
    根据角色获取权限
    :param login:
    :return:
    """
    with pytest.allure.step("根据角色获取权限"):
        response_dicts = req.get_request("get_role_tree", str(role_modify_code))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_role_tree')['success'], response_dicts['success'])
    with pytest.allure.step("查询数据库sys_role_menu,断言是否查询对应role_id:"+str(role_id)+"的权限数据数据"):
        menu_ids = mysql_opt.data_read("SELECT menu_id FROM sys_role_menu WHERE role_id = '%s';" % role_id, "bicai_admin")
        assert menu_ids is None
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "更新角色权限")
@pytest.allure.severity('blocker')
def test_put_role_menu_18():
    """
    更新角色权限
    :param login:
    :return:
    """
    with pytest.allure.step("更新角色权限"):
        response_dicts = req.put_request("put_role_menu", roleId=role_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_role_menu')['success'], response_dicts['success'])
    # with pytest.allure.step("查询数据库sys_role_menu,断言是否查询对应role_id:"+str(role_id)+"的权限数据数据"):
    #     menu_ids = mysql_opt.data_read_all("SELECT menu_id FROM sys_role_menu WHERE role_id = '%s';" % role_id)
        # global menu_ids_list  # 修改后角色权限
        # menu_ids_list = [x[0] for x in menu_ids]  # 循环取出查询结果二维数组中每个数组中的第一个值
        # assert menu_ids_list is not None
        # for i in range(0, menu_ids_list.__len__()):
        #     assert menu_ids_list[i] == exp_results('put_role_menu')['menu_ids'][i]
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "根据角色获取权限")
@pytest.allure.severity('blocker')
def test_get_role_tree_again_19():
    """
    修改权限后再次根据角色获取权限
    :param login:
    :return:
    """
    with pytest.allure.step("根据角色获取权限"):
        response_dicts = req.get_request("get_role_tree", str(role_modify_code))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_role_tree')['success'], response_dicts['success'])
    # with pytest.allure.step("查询数据库sys_role_menu,断言是否查询对应role_id:"+str(role_id)+"的权限数据数据"):
    #     act_menu_ids = list(response_dicts['data'])
    #     act_menu_ids.sort()
    #     menu_ids_list.sort()
    #     for i in range(0, menu_ids_list.__len__()):
    #         assert menu_ids_list[i] == act_menu_ids[i]
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Role', "删除角色信息")
@pytest.allure.severity('blocker')
def test_delete_role_20():
    """
    删除角色信息
    :param login:
    :return:
    """
    with pytest.allure.step("删除角色信息"):
        response_dicts = req.del_request("delete_role", str(role_id))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('delete_role')['success'], response_dicts['success'])
    with pytest.allure.step("删除角色后查询数据库,断言是否查询出数据，是否del——flag为:1"):
        role_del_info = mysql_opt.data_read("SELECT role_name,role_code,role_desc,del_flag FROM sys_role WHERE role_id = '% s';" % role_id, "bicai_admin")
        role_del_flag = role_del_info[3]  # 删除后del_flag
    test.assert_text(exp_results('delete_role')['del_flag'], str(role_del_flag))
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dept', "获取部门树")
@pytest.allure.severity('blocker')
def test_get_dept_tree_21():
    """
    获取部门树
    :param login:
    :return:
    """
    with pytest.allure.step("获取部门树"):
        response_dicts = req.start_request("get_dept_tree")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_dept_tree')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dept', "添加部门")
@pytest.allure.severity('blocker')
def test_post_dept_22():
    """
    添加新部门
    :param login:
    :return:
    """
    with pytest.allure.step("添加部门"):
        response_dicts = req.start_request("post_dept")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_dept')['success'], response_dicts['success'])
    with pytest.allure.step("删除角色后查询数据库,断言是否查询出数据，是否del——flag为:0"):
        dept_info = mysql_opt.data_read(
            "SELECT dept_id,code,del_flag FROM sys_dept WHERE name = '自动化测试';", "bicai_admin")
        global dept_id  # 部门id
        dept_id = dept_info[0]
        dept_code = dept_info[1]
        dept_del_flag = dept_info[2]
        test.assert_text(exp_results('post_dept')['code'], dept_code)
        test.assert_text(exp_results('post_dept')['del_flag'], dept_del_flag)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dept', "修改部门信息")
@pytest.allure.severity('blocker')
def test_put_dept_23():
    """
    修改部门信息
    :param login:
    :return:
    """
    with pytest.allure.step("修改部门信息"):
        response_dicts = req.start_request("put_dept", deptId=dept_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_dept')['success'], response_dicts['success'])
        put_dept_info = mysql_opt.data_read(
            "SELECT name,code,del_flag FROM sys_dept WHERE dept_id = '%s';" % dept_id, "bicai_admin")
        put_dept_name = put_dept_info[0]
        put_dept_code = put_dept_info[1]
        put_dept_del_flag = put_dept_info[2]
        test.assert_text(exp_results('put_dept')['name'], put_dept_name)
        test.assert_text(exp_results('put_dept')['code'], put_dept_code)
        test.assert_text(exp_results('put_dept')['del_flag'], put_dept_del_flag)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dept', "删除部门")
@pytest.allure.severity('blocker')
def test_del_dept_24():
    """
    删除部门
    :param login:
    :return:
    """
    with pytest.allure.step("修改部门信息"):
        response_dicts = req.del_request("del_dept", str(dept_id))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('del_dept')['success'], response_dicts['success'])
        del_dept_info = mysql_opt.data_read(
            "SELECT name,code,del_flag FROM sys_dept WHERE dept_id = '%s';" % dept_id, "bicai_admin")
        del_dept_del_flag = del_dept_info[2]
        test.assert_text(exp_results('del_dept')['del_flag'], del_dept_del_flag)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dict', "获取字典列表")
@pytest.allure.severity('blocker')
def test_get_dict_page_25():
    """
    获取字典列表
    :param login:
    :return:
    """
    with pytest.allure.step("获取字典列表"):
        response_dicts = req.start_request("get_dict_page")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('get_dict_page')['success'], response_dicts['success'])
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dict', "添加字典")
@pytest.allure.severity('blocker')
def test_post_dict_26():
    """
    添加字典
    :param login:
    :return:
    """
    with pytest.allure.step("添加字典"):
        response_dicts = req.start_request("post_dict")
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('post_dict')['success'], response_dicts['success'])
    with pytest.allure.step("添加字典后查询数据库,断言是否查询出数据"):
        dict_add_info = mysql_opt.data_read("SELECT id,type,del_flag FROM sys_dict WHERE remarks = '自动化测试123';", "bicai_admin")
        global dict_id  # 新添加字典id
        global dict_del_flag  # 新添加字典删除标记
        global dict_type  # 新添加字典类型
        dict_id = dict_add_info[0]
        dict_type = dict_add_info[1]
        dict_del_flag = dict_add_info[2]
        test.assert_text(exp_results('post_dict')['type'], dict_type)
        test.assert_text(exp_results('post_dict')['del_flag'], dict_del_flag)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dict', "修改字典")
@pytest.allure.severity('blocker')
def test_put_dict_27():
    """
    修改字典
    :param login:
    :return:
    """
    with pytest.allure.step("修改字典"):
        response_dicts = req.start_request("put_dict", id=dict_id)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('put_dict')['success'], response_dicts['success'])
    with pytest.allure.step("修改字典后查询数据库,断言是否查询出数据"):
        dict_put_info = mysql_opt.data_read("SELECT type,del_flag,remarks FROM sys_dict WHERE id = '% s';" % dict_id, "bicai_admin")
        global put_dict_id  # 修改后字典id
        global put_dict_del_flag  # 修改字典后删除标记
        global put_dict_type # 修改后字典类型
        put_dict_type = dict_put_info[0]
        put_dict_del_flag = dict_put_info[1]
        put_dict_remarks = dict_put_info[2]
        test.assert_text(exp_results('put_dict')['type'], put_dict_type)
        test.assert_text(exp_results('put_dict')['del_flag'], put_dict_del_flag)
        # test.assert_text(exp_results('put_dict')['remarks'], put_dict_remarks)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_Dict', "删除字典")
@pytest.allure.severity('blocker')
def test_del_dict_28():
    """
    删除字典
    :param login:
    :return:
    """
    with pytest.allure.step("删除字典"):
        response_dicts = req.del_request("del_dict", str(dict_id), put_dict_type)
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('del_dict')['success'], response_dicts['success'])
    with pytest.allure.step("删除字典后查询数据库,断言是否查询出数据"):
        dict_del_info = mysql_opt.data_read("SELECT del_flag FROM sys_dict WHERE id = '% s';" % dict_id, "bicai_admin")
        del_flag = dict_del_info[0]  # 新添加角色删除标记
        test.assert_text(exp_results('del_dict')['del_flag'], del_flag)
    Consts.RESULT_LIST.append('True')


@pytest.allure.feature('Admin_User', "根据user_id删除用户")
@pytest.allure.severity('blocker')
def test_get_admin_user_delete():
    """
    根据user_id删除用户
    :param login:
    :return:
    """
    with pytest.allure.step("根据user_id删除用户"):
        response_dicts = req.del_request("delete_user_by_userid", str(user_id))
    with pytest.allure.step("断言success对比"):
        test.assert_text(exp_results('delete_user_by_userid')['success'], response_dicts['success'])
    with pytest.allure.step("添加用户后查询数据库,断言是否查询出数据，是否del——flag为:1"):
        delde_flag = mysql_opt.data_read("SELECT del_flag FROM sys_user WHERE user_id ='%s';" % user_id, "bicai_admin")[0]
        del_data()  # 数据回收
        with pytest.allure.step("删除后del_flag更改"):
            test.assert_not_in_results(del_flag, delde_flag)
        with pytest.allure.step("删除后del_flag变为1"):
            test.assert_in_results(delde_flag, '1')
    Consts.RESULT_LIST.append('True')


def del_data():
    with pytest.allure.step("数据回收"):
        mysql_opt.data_write("DELETE FROM sys_menu WHERE menu_id = '%s' ;" % menu_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_user WHERE user_id = '%s' ;" % user_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_role WHERE role_id = '%s' ;" % role_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_role_dept WHERE role_id = '%s' ;" % role_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_user_role WHERE role_id = '%s' ;" % role_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_role_menu WHERE role_id = '%s' ;" % role_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_dict WHERE id = '%s' ;" % dict_id, "bicai_admin")

        mysql_opt.data_write("DELETE FROM sys_dept WHERE dept_id = '%s' ;" % dept_id, "bicai_admin")



