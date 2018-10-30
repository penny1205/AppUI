#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_login.login_chezhu import LoginCheZhu
from util.driver.driver import AppUiDriver


class TestWaybillConfirm(unittest.TestCase):
    """凯京车主APP 确认发车"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppDriver().set_driver(appPackage=app_package, appActivity=app_activity)
        self.logger = Log()
        self.mobile = config['mobile_register']
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        self.main_page = MainTabCheZhu().activity
        self.logger.info('########################### TestWaybillConfirm START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestWaybillConfirm END ###########################')
        pass

    def test_bvt_waybill_confirm(self):
        """确认发车操作"""
        self.driver.getScreenShot('login_register_chezhu')
        LoginCheZhu(self.driver).user_login(self.mobile)
        activity = self.driver.get_activity
        self.driver.getScreenShot('login_register_chezhu')
        self.assertEqual(self.main_page, activity)  # 检查登录操作后页面activity是否切换为主列表页


if __name__ == '__main__':
    unittest.main(verbosity=2)