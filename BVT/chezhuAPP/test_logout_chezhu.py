#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.db.dbutil import RedisDb
from util.driver.driver_operation import DriverOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_userCenter.setting_chezhu import SettingCheZhu
from page_object.chezhu.chezhu_login.login_chezhu import LoginCheZhu
from util.driver.driver import AppUiDriver


class TestLogout(unittest.TestCase):
    """凯京车主APP 退出登录"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        self.device = config[]
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_operation = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        self.login_page = LoginCheZhu(self.driver).activity
        self.logger.info('########################### TestLogout START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        RedisDb().del_key(name='CHK_ONE_DAY_LOGIN', key= 'all')
        self.logger.info('########################### TestLogout END ###########################')
        pass

    def test_bvt_logout(self):
        """用户退出登录"""
        self.driver_operation.getScreenShot('TestLogout')
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_setting_page()
        SettingCheZhu(self.driver).user_logout()
        self.driver_operation.getScreenShot('TestLogout')
        activity = self.driver_operation.get_activity()
        self.assertEqual(self.login_page, activity)


if __name__ == '__main__':
    unittest.main(verbosity=2)
