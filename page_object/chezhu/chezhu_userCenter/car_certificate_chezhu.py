#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class CarCertificateCheZhu(CheZhu):
    car_certificate_activity = '.account.MyCarActivity'
    __car_img_first = {'identifyBy': 'id', 'path': 'com.mustang:id/car_info_first_pic'}
    __car_img_second = {'identifyBy': 'id', 'path': 'com.mustang:id/car_info_second_pic'}
    __is_owner = {'identifyBy': 'id', 'path': 'com.mustang:id/rb_isDriver'}
    __not_is_owner = {'identifyBy': 'id', 'path': 'com.mustang:id/rb_nonDriver'}
    # -*- 车牌号省份选择 -*-
    __car_number_province = {'identifyBy': 'id', 'path': 'com.mustang:id/tv_car_number'}
    __choose_province = {'identifyBy': 'ids', 'path': ['com.mustang:id/item_text', 0]}
    __confirm_choose = {'identifyBy': 'id', 'path': 'com.mustang:id/gv_ok'}

    __car_number_input = {'identifyBy': 'id', 'path': 'com.mustang:id/editview_et'}
    # -*- 车辆类型选择 -*-
    __car_model_choose = {'identifyBy': 'id', 'path': 'com.mustang:id/et_car_model'}
    car_model_activity = '.account.CarFilterActivity'
    __car_model = {'identifyBy': 'ids', 'path': ['com.mustang:id/adapter_one_text', 0]}
    # -*- 车辆长度选择 -*-
    __car_length_choose = {'identifyBy': 'id', 'path': 'com.mustang:id/et_car_length'}
    car_length_activity = '.account.CarFilterActivity'
    __car_length = {'identifyBy': 'ids', 'path': ['com.mustang:id/adapter_one_text', 0]}

    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/btn_car_info_save'}

    # -*-上传图片弹窗-*-
    __choose_photos = {'identifyBy': 'id', 'path': 'com.mustang:id/select_from_album'}
    __take_photos = {'identifyBy': 'id', 'path': 'com.mustang:id/image_direct_scan'}
    __cancel_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/image_cancel_btn'}

    @catch_exception
    def wait_page(self):
        self.driver.wait_activity(self.car_certificate_activity)

    @catch_exception
    def upload_car_img_first(self):
        self.driver.click_element(self.__car_img_first)
        self.driver.click_element(self.__choose_photos)

    @catch_exception
    def upload_car_img_second(self):
        self.driver.click_element(self.__car_img_second)
        self.driver.click_element(self.__choose_photos)

    @catch_exception
    def input_car_number(self, carNo='A123456'):
        self.driver.click_element(self.__car_number_province)
        self.driver.click_element(self.__choose_province)
        self.driver.click_element(self.__confirm_choose)
        self.__car_number_input['keys'] = carNo
        self.driver.send_keys(self.__car_number_input)

    @catch_exception
    def choose_car_info(self):
        self.driver.click_element(self.__car_model_choose)
        self.driver.click_element(self.__car_model)
        self.driver.click_element(self.__car_length_choose)
        self.driver.click_element(self.__car_length)

    @catch_exception
    def submit_car_info(self):
        self.driver.click_element(self.__confirm_btn)
