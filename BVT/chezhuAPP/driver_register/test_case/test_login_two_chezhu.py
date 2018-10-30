#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from page_object.chezhu.chezhu_login.login_chezhu import LoginCheZhu
from BVT.common.app_driver import AppDriver


class TestLoginRegister(unittest.TestCase):
    """凯京车主APP 已认证司机登录"""

    def setUp(self):
        """前置条件准备"""
        # config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # app_package = config['appPackage_chezhu']
        # app_activity = config['appActivity_chezhu']
        # AppDriver().set_driver(appPackage=app_package, appActivity=app_activity)
        self.logger = Log()
        self.mobile = '18655148783'
        self.driver = AppDriver().get_driver()
        self.logger.info('########################### TestLoginRegister START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestLoginRegister END ###########################')
        pass

    def test_bvt_login_register(self):
        """认证司机登录"""
        print(self.mobile)
        print(type(self.driver))
        LoginCheZhu(self.driver).user_login(self.mobile)


if __name__ == '__main__':
    unittest.main(verbosity=2)