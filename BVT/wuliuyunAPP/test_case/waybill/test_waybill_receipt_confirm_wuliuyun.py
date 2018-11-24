#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest

from page_object.wuliuyun.wuliuyun_waybill.waybill_receipt_confirm_wuliuyun import WaybillReceiptConfirmWuliuyun
from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from BVT.common.createWayBill import CreateWayBill
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_waybill.waybill_detail_wuliuyun import WuLiuYunWaybillDetail
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestConfirmReceiptWaybill(unittest.TestCase):
    # 物流云APP 运单回单确认
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestConfirmReceiptWaybill START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()  # 单例测试 启动driver
        self.driver_mobile = config['employ_driver_mobile']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        CreateWayBill(self.driver_mobile).upload_receipt()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(mobile=self.driver_mobile)
        self.logger.info('########################### TestConfirmReceiptWaybill END ###########################')
        pass

    def test_confirm_receipt_waybill(self):
        # 运单 回单确认
        confirm_receipt = WaybillReceiptConfirmWuliuyun(self.driver)
        WuLiuYunWaybillTab(self.driver).go_to_waybill_ydd()
        WuLiuYunWaybillTab(self.driver).go_to_waybill_detail()
        self.driver_tool.getScreenShot('test_confirm_receipt_waybill')
        WuLiuYunWaybillDetail(self.driver).operating_waybill()
        confirm_receipt.add_receipt_image()
        confirm_receipt.del_receipt_image()
        confirm_receipt.add_confirm_info()
        confirm_receipt.confirm_receipt()
        self.driver_tool.getScreenShot('test_confirm_receipt_waybill')
        waybill = DbOperation().select_waybill_state(self.driver_mobile)[0]
        self.assertEqual(waybill, 'S')

if __name__ == '__main__':
    unittest.main(verbosity=1)
