#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.driver.driver_operation import DriverOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_common.wallet_password_chezhu import WalletPasswordCheZhu
from page_object.chezhu.chezhu_userCenter.bankcard_main_chezhu import BankCardMainCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from BVT.common.db_operation import DbOperation
from util.driver.driver import AppUiDriver


class TestBankCardDelete(unittest.TestCase):
    """凯京车主APP 提现银行卡解绑 """
# 暂时无法测试，提现卡绑定状态记录在支付网关无法主动修改
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestBankCardDelete START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()  # 获取配置文件
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.mobile = config['mobile_register']
        self.wallet_pwd = config['wallet_pwd_register']  # 钱包密码
        self.driver = AppUiDriver(app_package, app_activity).get_driver()  # 获取appium driver
        self.driver_tools = DriverOperation(self.driver)
        DbOperation().update_wallet_card_state(self.mobile)  # 更新提现卡状态
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().update_wallet_card_state(self.mobile)
        self.logger.info('########################### TestBankCardDelete END ###########################')
        pass

    @unittest.skip('提现卡绑定状态记录在支付网关无法主动修改')
    def test_bvt_bankcard_delete(self):
        """提现银行卡解绑"""
        bankcard = BankCardMainCheZhu(self.driver)
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_account_bankcard()
        self.driver_tools.getScreenShot('bankcard_delete')
        bankcard.untie_cash_card()
        WalletPasswordCheZhu(self.driver).send_password(self.wallet_pwd)
        WalletPasswordCheZhu(self.driver).confirm_pwd()
        self.driver_tools.getScreenShot('bankcard_delete')
        cash_card = bankcard.find_cash_card()
        self.assertEqual(cash_card, False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
