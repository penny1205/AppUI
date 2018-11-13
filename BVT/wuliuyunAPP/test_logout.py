#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.driver.driver import AppUiDriver
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver_operation import DriverOperation
from page_object.wuliuyun.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from page_object.wuliuyun.user_main_wuliuyun import UserMainPageWuliuyun
from page_object.wuliuyun.user_setting_wuliuyun import UserSettingPageWuliuyun
from page_object.wuliuyun.login_wuliuyun import LoginWuLiuYun


class TestLogout(unittest.TestCase):
    # 物流云APP 货主退出登录
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestLogout START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestLogout END ###########################')
        pass

    def test_logout(self):
        # 货主退出登录
        WuLiuYunWaybillTab(self.driver).go_to_user_account()
        self.driver_tool.getScreenShot('test_logout')
        UserMainPageWuliuyun(self.driver).go_to_setting_page()
        UserSettingPageWuliuyun(self.driver).logout()
        self.driver_tool.getScreenShot('test_logout')
        login_page = LoginWuLiuYun(self.driver).wait_login_page()
        self.assertTrue(login_page)





