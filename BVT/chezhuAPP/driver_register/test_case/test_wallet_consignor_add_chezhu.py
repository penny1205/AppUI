#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.driver.driver_operation import DriverOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_consignor_chezhu import WalletConsignorCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_common.wallet_password_chezhu import WalletPasswordCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_main_chezhu import WalletMainCheZhu
from BVT.common.db_operation import DbOperation
from util.driver.driver import AppUiDriver


class TestWalletConsignorAdd(unittest.TestCase):
    """凯京车主APP 新增委托代收人"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.mobile = config['mobile_register']
        self.consignor_name = config['consignor_name']
        self.consignor_idNo = config['consignor_idNo']
        self.consignor_mobile = config['consignor_mobile']
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        self.driver_tools = DriverOperation(self.driver)
        DbOperation().delete_wallet_consignor(self.mobile)
        self.logger.info('########################### TestWalletConsignorAdd START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_wallet_consignor(self.mobile)
        self.logger.info('########################### TestWalletConsignorAdd END ###########################')
        pass

    def test_bvt_wallet_consignor_add(self):
        """新增委托代收人"""
        wallet_consignor = WalletConsignorCheZhu(self.driver)
        self.driver_tools.getScreenShot('wallet_consignor_add')
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_user_wallet()
        WalletMainCheZhu(self.driver).go_to_consignor()
        WalletPasswordCheZhu(self.driver).send_password('123321')
        wallet_consignor.go_to_add_consignor()
        wallet_consignor.add_consignor(name=self.consignor_name, idNo=self.consignor_idNo, mobile=self.consignor_mobile)
        wait_page = wallet_consignor.wait_consignor_page()
        self.driver_tools.getScreenShot('wallet_consignor_add')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        consignor_state = wallet_consignor.find_consignor()
        self.assertTrue(consignor_state)

if __name__ == '__main__':
    unittest.main(verbosity=2)
