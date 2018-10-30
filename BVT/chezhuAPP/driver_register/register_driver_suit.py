#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
import unittest
from BVT.chezhuAPP.driver_register.test_login_register_chezhu import TestLoginRegister
from util.unittest.unittestutil import UnitTestUtil


class RegisterDriverCaseSuite(object):
    # 已认证司机BVT自动化case集合
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # app_package = config['appPackage_chezhu']
        # app_activity = config['appActivity_chezhu']
        # AppDriver().set_driver(app_package, app_activity)

    def case_suite_runner(self):
        test_suite = unittest.makeSuite(TestLoginRegister)
        test_suite.addTest(UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_register/test_case', 'test*.py'))
        # test_suite.addTest(TestLoginRegister('test_bvt_login_register'))
        # test_suit = test_suit + UnitTestUtil().discover_pattern(
        #     FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_register/test_case', 'test*.py')
        print(test_suite)
        unittest.TextTestRunner().run(test_suite)


if __name__ == '__main__':
    RegisterDriverCaseSuite().case_suite_runner()
