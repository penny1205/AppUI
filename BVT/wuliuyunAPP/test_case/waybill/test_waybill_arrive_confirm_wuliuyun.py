#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest

from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.createWayBill import CreateWayBill
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_waybill.waybill_arrive_confirm_wuliuyun import WaybillArriveConfirmWuliuyun
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestArriveConfirmWaybill(unittest.TestCase):
    # 物流云APP 运单确认到达
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestArriveConfirmWaybill START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.driver_mobile = config['employ_driver_mobile']
        self.confirm_amt = '0.8'
        self.confirm_info = '到达确认自动化备注'
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        CreateWayBill(self.driver_mobile).confirmWayBill()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(mobile=self.driver_mobile)
        self.logger.info('########################### TestArriveConfirmWaybill END ###########################')
        pass

    def test_arrive_confirm_waybill(self):
        # 运单 确认到达
        WuLiuYunWaybillTab(self.driver).go_to_waybill_ysz()
        WuLiuYunWaybillTab(self.driver).go_to_waybill_detail()
        self.driver_tool.getScreenShot('test_arrive_confirm_waybill')
        WaybillArriveConfirmWuliuyun(self.driver).go_to_confirm_waybill(type=1)
        WaybillArriveConfirmWuliuyun(self.driver).arrive_confirm_waybill(amt=self.confirm_amt, info=self.confirm_info)
        self.driver_tool.getScreenShot('test_arrive_confirm_waybill')
        main_page = WuLiuYunWaybillTab(self.driver).wait_main_page()
        self.assertTrue(main_page)
        waybill = DbOperation().select_waybill_state(self.driver_mobile)[0]
        self.assertEqual(waybill, 'D')
