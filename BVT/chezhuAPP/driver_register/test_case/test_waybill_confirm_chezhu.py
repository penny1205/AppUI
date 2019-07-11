#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_waybill.waybill_confirm_chezhu import WaybillConfirmCheZhu
from page_object.chezhu.chezhu_waybill.waybill_main_chezhu import WaybillMainCheZhu
from BVT.common.db_operation import DbOperation
from BVT.common.createWayBill import CreateWayBill
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation


class TestWaybillConfirm(unittest.TestCase):
    """凯京车主APP 确认发车"""

    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestWaybillConfirm START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()  # 获取配置文件
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.mobile = config['mobile_register']
        self.driver = AppUiDriver(app_package, app_activity).get_driver()  # 获取appium driver
        DbOperation().delete_waybill_driver(self.mobile)  # 删除已有运单
        CreateWayBill(self.mobile).saveWayBill()  # 创建运单
        self.driver_tools = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)  # 重启应用
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(self.mobile)  # 删除case中操作的运单
        self.logger.info('########################### TestWaybillConfirm END ###########################')
        pass

    def test_bvt_waybill_confirm(self):
        """确认发车操作"""
        MainTabCheZhu(self.driver).close_driver_loan_ads()
        self.driver_tools.getScreenShot('waybill_confirm')
        WaybillMainCheZhu(self.driver).go_to_waybill_detail()  # 进入运单详情页面 操作确认发车
        WaybillConfirmCheZhu(self.driver).upload_transport_img()  # 上传运输协议
        self.driver_tools.getScreenShot('waybill_confirm')
        WaybillConfirmCheZhu(self.driver).confirm_waybill()  # 确认发车
        wait_page = MainTabCheZhu(self.driver).wait_main_page()
        self.driver_tools.getScreenShot('waybill_confirm')
        self.assertTrue(wait_page)  # 检查操作完成后页面activity是否切换为主列表页
        waybill_state = DbOperation().select_waybill_state(self.mobile)[0]
        self.assertEqual(waybill_state, 'Y')  # 判断运单状态是否变为  Y司机已确认

if __name__ == '__main__':
    unittest.main(verbosity=2)
