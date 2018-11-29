#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
import unittest
from BVT.chezhuAPP.driver_unregister.test_login_unregister_chezhu import TestLoginUnregister
from BVT.chezhuAPP.test_logout_chezhu import TestLogout
from util.unittest.unittestutil import UnitTestUtil
from util.driver.driver import AppUiDriver


class UnregisterDriverCaseSuit(object):
    # 未认证司机BVT自动化case集合
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

    def case_suite_unregister(self):
        test_suite = unittest.makeSuite(TestLoginUnregister)
        test_suite.addTest(
            UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_unregister/test_case',
                                            'test*.py'))
        # test_suite.addTest(TestLoginRegister('test_bvt_login_register'))
        # test_suit = test_suit + UnitTestUtil().discover_pattern(
        #     FileUtil.getProjectObsPath() + '/BVT/chezhuAPP/driver_register/test_case', 'test*.py')
        return test_suite


if __name__ == '__main__':
    UnregisterDriverCaseSuit().case_suite_runner()
