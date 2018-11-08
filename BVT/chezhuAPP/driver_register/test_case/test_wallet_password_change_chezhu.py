#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.driver.driver_operation import DriverOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_main_chezhu import WalletMainCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_change_pwd_chezhu import WalletChangePwdCheZhu
from util.driver.driver import AppUiDriver


class TestWalletPasswordChange(unittest.TestCase):
    """凯京车主APP 修改钱包密码"""

    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestWalletPasswordChange START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.pwd = config['wallet_pwd_register']
        self.newpwd = '147369'
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        self.driver_tools = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)

        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestWalletPasswordChange END ###########################')
        pass

    def test_bvt_wallet_password_change(self):
        """ 修改钱包密码 """
        wallet_pwd = WalletChangePwdCheZhu(self.driver)
        self.driver_tools.getScreenShot('wallet_password_change')
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_user_wallet()
        WalletMainCheZhu(self.driver).go_to_change_pwd()
        wallet_pwd.change_pwd(oldpwd=self.pwd, newpwd=self.newpwd)
        wallet_pwd.confirm_change_pwd()
        wait_page = WalletMainCheZhu(self.driver).wait_wallet_page()
        self.driver_tools.getScreenShot('wallet_password_change')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为钱包主页面
        WalletMainCheZhu(self.driver).go_to_change_pwd()
        wallet_pwd.change_pwd(oldpwd=self.newpwd, newpwd=self.pwd)
        wallet_pwd.confirm_change_pwd()


if __name__ == '__main__':
    unittest.main(verbosity=2)
