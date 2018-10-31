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
from page_object.chezhu.chezhu_userCenter.certification_chezhu import CertificationCheZhu
from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu
from page_object.chezhu.chezhu_userCenter.car_certificate_chezhu import CarCertificateCheZhu
from util.driver.driver import AppUiDriver


class TestCertification(unittest.TestCase):
    """凯京车主APP 身份认证"""

    def setUp(self):
        """前置条件准备"""
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
        self.logger = Log()
        self.db = DbOperation()
        self.driver = AppUiDriver(appPackage=app_package, appActivity=app_activity).get_driver()
        self.mobile = config['mobile_unregister']
        self.name = config['name_unregister']
        self.idNo = config['idNo_unregister']
        self.db.initialize_driver_info(self.mobile)
        self.driver.start_activity(app_activity=app_activity, app_package=app_package)
        self.logger.info('########################### TestCertification START ###########################')
        pass

    def tearDown(self):
        """测试环境重置"""
        self.db.initialize_driver_info(self.mobile)
        self.logger.info('########################### TestCertification END ###########################')
        pass

    def test_bvt_certification(self):
        """身份认证"""
        certificate = CertificationCheZhu(self.driver)
        choosePhoto = ChoosePhotoCheZhu(self.driver)
        MainTabCheZhu(self.driver).goto_person_center()
        PersonCenterCheZhu(self.driver).goto_certification_page()
        certificate.upload_card_front()
        choosePhoto.choose_id_card_front()
        certificate.upload_card_back()
        choosePhoto.choose_id_card_back()
        certificate.input_id_card_info(self.name, self.idNo)
        certificate.submit_id_card_info()
        CarCertificateCheZhu(self.driver).wait_page()
        driver_info = self.db.select_driver_info(self.mobile)
        self.assertEqual(self.name, driver_info['name'])
        self.assertEqual(str(self.idNo), str(driver_info['idNo']))
        self.assertEqual('Y', driver_info['isCertifacate'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
