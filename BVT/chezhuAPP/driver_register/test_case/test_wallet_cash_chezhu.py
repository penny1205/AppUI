#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.driver.driver_operation import DriverOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_cash_chezhu import WalletCashCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_common.wallet_password_chezhu import WalletPasswordCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_main_chezhu import WalletMainCheZhu
from BVT.common.waybillPay import PayForDriver
from util.driver.driver import AppUiDriver


class TestWalletCash(unittest.TestCase):
    """凯京车主APP 提现"""

    def setUp(self):
        """前置条件准备"""
        self.logger.info('########################### TestWalletCash START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.mobile = config['mobile_register']
        self.wallet_pwd = config['wallet_pwd_register']
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        self.driver_tools = DriverOperation(self.driver)
        PayForDriver(self.mobile).pay_for_driver()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestWalletCash END ###########################')
        pass

    def test_bvt_wallet_cash(self):
        """钱包提现"""
        wallet = WalletMainCheZhu(self.driver)
        wallet_cash = WalletCashCheZhu(self.driver)
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_user_wallet()
        self.driver_tools.getScreenShot('wallet_cash')
        wallet.go_to_cash()
        wallet_cash.wallet_cash()
        WalletPasswordCheZhu(self.driver).send_password(self.wallet_pwd)
        wallet_cash.cash_confirm()
        self.driver_tools.getScreenShot('wallet_cash')
        wait_page = MainTabCheZhu(self.driver).wait_main_page()
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        wallet_balance = int(wallet.get_wallet_balance())
        self.assertEqual(wallet_balance, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
