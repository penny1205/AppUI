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
from util.driver.driver_operation import DriverOperation


class TestWaybillReceiptUpload(unittest.TestCase):
    """凯京车主APP 回单上传"""

    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestWaybillReceiptUpload START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()  # 读取配置文件
        app_package = config['appPackage_chezhu']  # APP 包名
        app_activity = config['appActivity_chezhu']  # APP 启动activity
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.mobile = config['mobile_register']   # 认证司机手机号
        self.driver = AppUiDriver(app_package, app_activity).get_driver()  # 获取appium driver
        CreateWayBill(self.mobile).arrive_confirm()  # 创建运单并确认发车及到达确认
        self.driver_tools = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)  # 重启APP 保证case从主页面开始执行
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(self.mobile)  # 删除case中操作的运单
        self.logger.info('########################### TestWaybillReceiptUpload END ###########################')
        pass

    def test_bvt_waybill_receipt_upload(self):
        """回单上传操作"""
        upload_receipt = WaybillReceiptUploadCheZhu(self.driver)
        MainTabCheZhu(self.driver).close_driver_loan_ads()
        self.driver_tools.getScreenShot('waybill_receipt_upload')
        WaybillMainCheZhu(self.driver).go_to_waybill_detail()  # 跳转运单回单上传操作页面
        self.driver_tools.getScreenShot('waybill_receipt_upload')
        upload_receipt.add_receipt_image()  # 添加回单照片
        upload_receipt.add_receipt_info('自动化回单异常')  # 添加回单异常信息
        upload_receipt.upload_receipt()  # 上传回单相关信息
        wait_page = MainTabCheZhu(self.driver).wait_main_page()
        self.driver_tools.getScreenShot('waybill_receipt_upload')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        waybill_state = DbOperation().select_waybill_state(self.mobile)[0]  # 判断运单状态是否变为  H回单已上传
        self.assertEqual(waybill_state, 'H')

if __name__ == '__main__':
    unittest.main(verbosity=2)
