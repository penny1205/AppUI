#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest

from page_object.wuliuyun.login_wuliuyun import LoginWuLiuYun
from page_object.wuliuyun.wuliuyun_common.notification_wuliuyun import NotificationWuLiuYun
from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestLogin(unittest.TestCase):
    # 物流云APP 货主登录
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestLogin START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

        self.user = config['username_wuliuyun']
        self.password = config['password_wuliuyun']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        self.driver.reset()
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestLogin END ###########################')
        pass

    def test_login(self):
        login = LoginWuLiuYun(self.driver)
        self.driver_tool.getScreenShot('login_wuliuyun')
        NotificationWuLiuYun(self.driver).guide_page()
        self.driver_tool.getScreenShot('login_wuliuyun')
        login_page = login.wait_login_page()
        self.assertTrue(login_page)
        login.user_login(user=self.user, pwd=self.password)
        self.driver_tool.getScreenShot('login_wuliuyun')
        main_page = WuLiuYunWaybillTab(self.driver).wait_main_page()
        self.assertTrue(main_page)





