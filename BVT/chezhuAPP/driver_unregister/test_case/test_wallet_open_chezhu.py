#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from BVT.common.db_operation import DbOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_open_chezhu import WalletOpenCheZhu
from util.driver.driver import AppUiDriver


class TestWalletOpen(unittest.TestCase):
    """凯京车主APP 开通钱包"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.db = DbOperation()
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.mobile = config['mobile_unregister']
        self.db.certificate_driver_info()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        self.logger.info('########################### TestWalletOpen START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        self.db.delete_wallet_driver()
        self.db.initialize_driver_info(self.mobile)
        self.logger.info('########################### TestWalletOpen END ###########################')
        pass

    def test_bvt_wallet_open(self):
        """开通司机钱包"""
        wallet = WalletOpenCheZhu(self.driver)
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_user_wallet()
        wallet.wallet_open()
        wallet.set_pwd()
        page_wait = MainTabCheZhu(self.driver).wait_main_page()
        self.assertTrue(page_wait)
        sql = 'select COUNT(*) FROM YD_APP_MYBANK_OPEN_ACCOUNT where mobile = \'{0}\' and accountOpened = 1'.format(
            self.mobile)
        wallet_type = self.db.update(sql)
        self.assertEqual('1', str(wallet_type))


if __name__ == '__main__':
    unittest.main(verbosity=2)
