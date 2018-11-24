#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.createWayBill import CreateWayBill
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_waybill.waybill_detail_wuliuyun import WuLiuYunWaybillDetail
from page_object.wuliuyun.wuliuyun_waybill.waybill_change_wuliuyun import WaybillChangeWuLiuYun
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestChangeWaybill(unittest.TestCase):
    # 物流云APP 运单修改运单
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestChangeWaybill START ###########################')
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
        self.logger.info('########################### TestChangeWaybill END ###########################')
        pass

    def test_change_waybill(self):
        # 运单 修改运单
        change_waybill = WaybillChangeWuLiuYun(self.driver)
        WuLiuYunWaybillTab(self.driver).go_to_waybill_detail()
        self.driver_tool.getScreenShot('test_confirm_waybill')
        WuLiuYunWaybillDetail(self.driver).go_to_change_page(type=0)
        change_waybill.change_waybill(totalAmt='66', preAmt='1', oilAmt='2', destAmt='3', lastAmt='4')
        change_waybill.commit_change()
        self.driver_tool.getScreenShot('test_confirm_waybill')
        page = WuLiuYunWaybillDetail(self.driver).wait_detail_page()
        self.assertTrue(page)


if __name__ == '__main__':
    unittest.main(verbosity=1)
