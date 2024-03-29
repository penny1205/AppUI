#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.driver.driver import AppUiDriver
import unittest
from BVT.chezhuAPP.driver_register.test_login_register_chezhu import TestLoginRegister
from BVT.chezhuAPP.test_logout_chezhu import TestLogout
from util.unittest.unittestutil import UnitTestUtil


class RegisterDriverCaseSuite(object):
    # 已认证司机BVT自动化case集合
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

    def case_suite_register(self):
        test_suite = unittest.makeSuite(TestLoginRegister)
        test_suite.addTests(UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_register/test_case', 'test*.py'))
        test_suite.addTest(TestLogout('test_bvt_logout'))
        # test_suit = test_suit + UnitTestUtil().discover_pattern(
        #     FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_register/test_case', 'test*.py')
        return test_suite


if __name__ == '__main__':
    test_suite = RegisterDriverCaseSuite().case_suite_register()
    print(test_suite)
    print(type(test_suite))
    unittest.TextTestRunner().run(test_suite)
