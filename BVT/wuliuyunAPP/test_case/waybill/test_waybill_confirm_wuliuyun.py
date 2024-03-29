#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.createWayBill import CreateWayBill
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_waybill.waybill_confirm_wuliuyun import WaybillConfirmWuliuyun
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestConfirmWaybill(unittest.TestCase):
    # 物流云APP 运单确认发车
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestConfirmWaybill START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.driver_mobile = config['employ_driver_mobile']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        CreateWayBill(self.driver_mobile).saveWayBill()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(mobile=self.driver_mobile)
        self.logger.info('########################### TestConfirmWaybill END ###########################')
        pass

    def test_confirm_waybill(self):
        # 运单 确认发车
        WuLiuYunWaybillTab(self.driver).go_to_waybill_detail()
        self.driver_tool.getScreenShot('test_confirm_waybill')
        WaybillConfirmWuliuyun(self.driver).confirm_waybill(type=1)
        self.driver_tool.getScreenShot('test_confirm_waybill')
        main_page = WuLiuYunWaybillTab(self.driver).wait_main_page()
        self.assertTrue(main_page)
        waybill = DbOperation().select_waybill_state(self.driver_mobile)[0]
        self.assertEqual(waybill, 'X')
