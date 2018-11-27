#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from page_object.wuliuyun.wuliuyun_waybill.waybill_create_wuliuyun import WaybillCreateWuLiuYun
from BVT.common.db_operation import DbOperation
from page_object.wuliuyun.wuliuyun_waybill.waybill_tab_wuliuyun import WuLiuYunWaybillTab
from util.config.yaml.readyaml import ReadYaml
from util.driver.driver import AppUiDriver
from util.driver.driver_operation import DriverOperation
from util.file.fileutil import FileUtil
from util.log.log import Log


class TestCreateWaybillEmploy(unittest.TestCase):
    # 物流云APP 新建外请车运单
    def setUp(self):
        """前置条件准备"""
        self.logger = Log()
        self.logger.info('########################### TestCreateWaybill START ###########################')
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_wuliuyun']
        app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()  # 单例测试 启动driver
        self.employ_driver = config['employ_driver_mobile']
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.driver_tool = DriverOperation(self.driver)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        DbOperation().delete_waybill_driver(mobile=self.employ_driver)
        pass

    def tearDown(self):
        """测试环境重置"""
        DbOperation().delete_waybill_driver(mobile=self.employ_driver)
        self.logger.info('########################### TestCreateWaybill END ###########################')
        pass

    def test_create_waybill_employ(self):
        # 新建外请车运单
        create_waybill = WaybillCreateWuLiuYun(self.driver)
        WuLiuYunWaybillTab(self.driver).wait_main_page()
        WuLiuYunWaybillTab(self.driver).go_to_create_waybill()
        self.driver_tool.getScreenShot('test_create_waybill_employ')
        create_waybill.input_basic_info(car_type='1')
        create_waybill.input_goods_info()
        create_waybill.input_driver_info(car_type='1', mobile=self.employ_driver)
        create_waybill.input_cost_info()
        create_waybill.commit_waybill_info()
        self.driver_tool.getScreenShot('test_create_waybill_employ')
        main_page = WuLiuYunWaybillTab(self.driver).wait_main_page()
        self.assertTrue(main_page)
        waybill = DbOperation().select_waybill_state(self.employ_driver)[0]
        self.assertEqual(waybill, 'W')


if __name__ == '__main__':
    unittest.main(verbosity=1)

