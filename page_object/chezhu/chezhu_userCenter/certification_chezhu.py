#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class CertificationCheZhu(CheZhu):
    certification_activity = '.account.RealNameAuthActivity'
    # -*-实名认证页面-*-
    __card_front = {'identifyBy': 'id', 'path': 'com.mustang:id/name_auth_front'}
    __card_back = {'identifyBy': 'id', 'path': 'com.mustang:id/name_auth_back'}
    __card_name = {'identifyBy': 'id', 'path': 'com.mustang:id/name_auth_name'}
    __card_id = {'identifyBy': 'id', 'path': 'com.mustang:id/name_auth_id'}
    __card_type = {'identifyBy': 'id', 'path': 'com.mustang:id/id_card_type'}
    __info_del = {'identifyBy': 'id', 'path': 'com.mustang:id/editview_delete'}

    __next_step = {'identifyBy': 'id', 'path': 'com.mustang:id/name_auth_button'}
    # -*-上传图片弹窗-*-
    __choose_photos = {'identifyBy': 'id', 'path': 'com.mustang:id/select_from_album'}
    __take_photos = {'identifyBy': 'id', 'path': 'com.mustang:id/image_direct_scan'}
    __cancel_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/image_cancel_btn'}

    @catch_exception
    def upload_card_front(self):
        self.driver.click_element(self.__card_front)
        self.driver.click_element(self.__choose_photos)

    @catch_exception
    def upload_card_back(self):
        self.driver.click_element(self.__card_back)
        self.driver.click_element(self.__choose_photos)

    def input_id_card_info(self, name, idNo):
        self.__card_name['keys'] = name
        self.__card_id['keys'] = idNo
        self.driver.click_element(self.__card_name)
        self.driver.click_element(self.__info_del)
        self.driver.send_keys(self.__card_name)
        self.driver.click_element(self.__card_id)
        self.driver.click_element(self.__info_del)
        self.driver.send_keys(self.__card_id)

    @catch_exception
    def submit_id_card_info(self):
        self.driver.click_element(self.__next_step)

if __name__ == '__main__':
    import time
    from util.driver.driver import AppUiDriver
    from page_object.chezhu.chezhu_common.main_tab_chezhu import MainTabCheZhu
    from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import PersonCenterCheZhu
    from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu

    try:
        driver = AppUiDriver().app_ui_driver(appPackage='com.mustang', appActivity='.account.SplashActivity')
        main_tab = MainTabCheZhu(driver)
        person_center = PersonCenterCheZhu(driver)
        choose_img = ChoosePhotoCheZhu(driver)
        main_tab.goto_person_center()
        person_center.goto_certification_page()
        CertificationCheZhu(driver).upload_card_front()
        choose_img.choose_id_card_front()
        time.sleep(10)
    finally:
        driver.quit()
