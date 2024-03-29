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


class TestWalletConsignorDelete(unittest.TestCase):
    """凯京车主APP 删除委托代收人"""

    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestWalletConsignorDelete START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()  # 获取配置文件
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.mobile = config['mobile_register']
        self.consignor_mobile = config['consignor_mobile']  # 委托代收人手机号
        self.wallet_pwd = config['wallet_pwd_register']  # 钱包密码
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        self.driver_tools = DriverOperation(self.driver)
        DbOperation().add_wallet_consignor(self.mobile)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        self.logger.info('########################### TestWalletConsignorDelete END ###########################')
        pass

    def test_bvt_wallet_consignor_delete(self):
        """删除委托代收人"""
        wallet_consignor = WalletConsignorCheZhu(self.driver)
        self.driver_tools.getScreenShot('wallet_consignor_delete')
        MainTabCheZhu(self.driver).goto_person_center()  # 进入用户信息页面
        PersonCenterCheZhu(self.driver).goto_user_wallet()  # 进入钱包模块
        WalletMainCheZhu(self.driver).go_to_consignor()  # 进入委托代收人模块
        WalletPasswordCheZhu(self.driver).send_password(self.wallet_pwd)  # 输入钱包密码
        wallet_consignor.go_to_consignor_details()  # 进入委托代收人详情页面
        wallet_consignor.delete_consignor()  # 删除委托代收人
        wait_page = wallet_consignor.wait_consignor_page()
        self.driver_tools.getScreenShot('wallet_consignor_delete')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        consignor_state = wallet_consignor.find_consignor()
        self.assertFalse(consignor_state)

if __name__ == '__main__':
    unittest.main(verbosity=2)
