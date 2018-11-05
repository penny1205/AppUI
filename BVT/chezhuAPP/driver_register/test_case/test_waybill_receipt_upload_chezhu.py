#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_waybill.waybill_receipt_upload_chezhu import WaybillReceiptUploadCheZhu
from page_object.chezhu.chezhu_waybill.waybill_main_chezhu import WaybillMainCheZhu
from BVT.common.db_operation import DbOperation
from BVT.common.createWayBill import CreateWayBill
from util.driver.driver import AppUiDriver


class TestWaybillReceiptUpload(unittest.TestCase):
    """凯京车主APP 回单上传"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppDriver().set_driver(appPackage=app_package, appActivity=app_activity)
        self.logger = Log()
        self.mobile = config['mobile_register']
        self.driver = AppUiDriver(app_package, app_activity).get_driver()
        CreateWayBill(self.mobile).arrive_confirm()
        self.logger.info('########################### TestWaybillConfirm START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(self.mobile)
        self.logger.info('########################### TestWaybillConfirm END ###########################')
        pass

    def test_bvt_waybill_receipt_upload(self):
        """回单上传操作"""
        upload_receipt = WaybillReceiptUploadCheZhu(self.driver)
        self.driver.getScreenShot('waybill_receipt_upload')
        WaybillMainCheZhu(self.driver).go_to_waybill_detail()
        upload_receipt.add_receipt_image()
        upload_receipt.add_receipt_info()
        upload_receipt.upload_receipt()
        wait_page = MainTabCheZhu(self.driver).wait_main_page()
        self.driver.getScreenShot('waybill_receipt_upload')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        waybill_state = DbOperation().select_waybill_state(self.mobile)
        self.assertEqual(waybill_state, 'Y')

if __name__ == '__main__':
    unittest.main(verbosity=2)