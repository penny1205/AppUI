#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.driver.driver import AppUiDriver
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver_operation import DriverOperation
from page_object.wuliuyun.waybill_detail_wuliuyun import WuLiuYunWaybillDetail
from page_object.wuliuyun.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.createWayBill import CreateWayBill
from BVT.common.db_operation import DbOperation


class TestCancelWaybill(unittest.TestCase):
    # 物流云APP 取消运单
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestCancelWaybill START ###########################')
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
        self.logger.info('########################### TestCancelWaybill END ###########################')
        pass

    def test_cancel_waybill(self):
        # 取消运单
        WuLiuYunWaybillTab(self.driver).go_to_waybill_detail()
        self.driver_tool.getScreenShot('test_cancel_waybill')
        WuLiuYunWaybillDetail(self.driver).cancel_waybill()
        self.driver_tool.getScreenShot('test_cancel_waybill')
        main_page = WuLiuYunWaybillTab(self.driver).wait_main_page()
        self.assertTrue(main_page)
        waybill = DbOperation().select_waybill_state(self.driver_mobile)[0]
        self.assertEqual(waybill, 'Q')
