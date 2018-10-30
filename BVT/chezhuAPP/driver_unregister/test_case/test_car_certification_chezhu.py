#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from BVT.common.db_operation import DbOperation
from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu
from page_object.chezhu.chezhu_userCenter.car_certificate_chezhu import CarCertificateCheZhu
from page_object.chezhu.chezhu_userCenter.wallet_open_chezhu import WalletOpenCheZhu
from util.driver.driver import AppUiDriver


class TestCarCertification(unittest.TestCase):
    """凯京车主APP 车辆认证"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.db = DbOperation()
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.db.update_driver_info()
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        self.logger.info('########################### TestCarCertification START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        self.db.initialize_driver_info(self.mobile)
        self.logger.info('########################### TestCarCertification END ###########################')
        pass

    def test_bvt_car_certification(self):
        """车辆认证"""
        car_certificate = CarCertificateCheZhu(self.driver)
        choosePhoto = ChoosePhotoCheZhu(self.driver)
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_certification_page()
        car_certificate.upload_car_img_first()
        choosePhoto.choose_driving_license_front()
        car_certificate.upload_car_img_second()
        choosePhoto.choose_id_card_back()
        car_certificate.input_car_number()
        car_certificate.choose_car_info()
        car_certificate.submit_car_info()
        WalletOpenCheZhu(self.driver).wait_page()
        driver_info = self.db.select_driver_info(self.mobile)
        self.assertEqual('Y', driver_info['isCarCertifacate'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
