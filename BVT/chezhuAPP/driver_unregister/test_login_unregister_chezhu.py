#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.db.dbutil import RedisDb
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_login.login_chezhu import LoginCheZhu
from util.driver.driver_operation import DriverOperation
from util.driver.driver import AppUiDriver
from page_object.chezhu.chezhu_common.notification_chezhu import NotificationCheZhu


class TestLoginUnregister(unittest.TestCase):
    """凯京车主APP 未认证司机登录"""

    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestLoginUnregister START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

        self.mobile = config['mobile_unregister']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        RedisDb().del_key(name='CHK_ONE_DAY_LOGIN', key='all')  # 清除当日APP登录设备记录
        self.driver.reset()
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestLoginUnregister END ###########################')
        pass

    def test_bvt_login_unregister(self):
        """未认证司机登录"""
        NotificationCheZhu(self.driver).guide_page()
        self.driver_tool.getScreenShot('login_unregister_chezhu')
        LoginCheZhu(self.driver).user_login(self.mobile)
        self.driver_tool.getScreenShot('login_unregister_chezhu')
        activity = MainTabCheZhu(self.driver).wait_main_page()
        self.assertTrue(activity)  # 检查登录操作后页面activity是否切换为主列表页


if __name__ == '__main__':
    unittest.main(verbosity=2)
