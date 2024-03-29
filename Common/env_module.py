# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 10:29 AM
# @Author  : XuChen
# @File    : env_module.py



"""
封装获取运行环境

"""
import sys

import pytest
import allure

from Common import request_module
from Conf import Config



class EnvModule:

    def __init__(self):
        self.config = Config.Config()
        # self.log = log_module.MyLog()
        # self.env = sys.argv[1]
        self.env = 'debug'
        # pytest.allure.environment(environment=self.env)

    def get_env_url(self):
        """
        获取环境url
        :param env: 环境变量
        :return:
        """
        if self.env == "debug":
            login_url = 'http://' + self.config.loginHost_debug
            return login_url

        elif self.env == "release":
            login_url = 'http://' + self.config.loginHost_release
            return login_url
        else:
            print("get url error")
            self.log.error('get url error, please checkout!!!')

    def get_env_mysql_para(self, data_db):
        """返回mysql参数"""
        # if data is None:
        #     if self.env == "debug":
        #         env_mysql = {"host": self.config.mysqlHost_debug,
        #                      "user": self.config.mysqlUser_debug,
        #                      "passwd": self.config.mysqlPassword_debug,
        #                      "port": int(self.config.mysqlPort_debug),
        #                      "db": self.config.mysqlDB_debug,
        #                      'charset': self.config.mysqlCharset_debug
        #                      }
        #         return env_mysql
        #     elif self.env == "release":
        #         env_mysql = {"host": self.config.mysqlHost_release,
        #                      "user": self.config.mysqlUser_release,
        #                      "passwd": self.config.mysqlPassword_release,
        #                      "port": int(self.config.mysqlPort_release),
        #                      "db": self.config.mysqlDB_release,
        #                      'charset': self.config.mysqlCharset_release
        #                      }
        #         return env_mysql
        # else:
        if self.env == "debug":
            env_mysql = {"host": self.config.mysqlHost_debug,
                         "user": self.config.mysqlUser_debug,
                         "passwd": self.config.mysqlPassword_debug,
                         "port": int(self.config.mysqlPort_debug),
                         "db": data_db,
                         'charset': self.config.mysqlCharset_debug
                         }
            return env_mysql
        elif self.env == "release":
            env_mysql = {"host": self.config.mysqlHost_release,
                         "user": self.config.mysqlUser_release,
                         "passwd": self.config.mysqlPassword_release,
                         "port": int(self.config.mysqlPort_release),
                         "db": data_db,
                         'charset': self.config.mysqlCharset_release
                         }
            return env_mysql


if __name__ == '__main__':
    # at = RequestModule().login_request()
    print(EnvModule().get_web_header())