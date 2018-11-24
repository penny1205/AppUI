#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest

from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_user.user_bankcard_add_wuliuyun import UserBankcardAddWuliuyun
from page_object.wuliuyun.wuliuyun_user.user_bankcard_main_wuliuyun import UserBankcardMainWuliuyun
from page_object.wuliuyun.wuliuyun_user.user_main_wuliuyun import UserMainPageWuliuyun
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestAddBankcard(unittest.TestCase):
    # 物流云APP 添加银行卡
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestAddBankcard START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()  # 单例调试时启动driver
        self.shipper_mobile = config['shipper_mobile']
        self.shipper_card_mobile = config['shipper_card_mobile']
        self.shipper_card_number = config['shipper_card_no']
        self.shipper_card_bank_name = config['shipper_card_bank_name']
        self.shipper_card_bank_branch = config['shipper_card_bank_branch']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        DbOperation().shipper_bankcard_del(self.shipper_mobile)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        self.driver.close_app()
        DbOperation().shipper_bankcard_del(self.shipper_mobile)
        self.logger.info('########################### TestAddBankcard END ###########################')
        pass

    def test_add_bankcard(self):
        # 个人中心 添加银行卡
        add_card = UserBankcardAddWuliuyun(self.driver)
        WuLiuYunWaybillTab(self.driver).go_to_user_account()
        UserMainPageWuliuyun(self.driver).go_to_card_page()
        self.driver_tool.getScreenShot('test_add_bankcard')
        add_card.add_card_info(card_no=self.shipper_card_number, card_mobile=self.shipper_card_mobile,
                               bank_name=self.shipper_card_bank_name, bank_branch_name=self.shipper_card_bank_branch)
        add_card.choose_bank_city()
        add_card.submit_bankcard()
        add_card.add_card_confirm(self.shipper_card_mobile)
        bankcard_page = UserBankcardMainWuliuyun(self.driver).wait_bankcard_main_page()
        self.driver_tool.getScreenShot('test_add_bankcard')
        self.assertTrue(bankcard_page)
        card_state = UserBankcardMainWuliuyun(self.driver).find_bankcard()
        self.assertTrue(card_state)


if __name__ == '__main__':
    unittest.main(verbosity=1)
