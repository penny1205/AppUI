#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WaybillReceiptUploadCheZhu(CheZhu):
    # 回单上传页面
    receipt_upload_activity = '.account.ReceiptUploadActivity'
    __add_image = {'identifyBy': 'id', 'path': 'com.mustang:id/multi_select_item_image'}
    __delete_image = {'identifyBy': 'id', 'path': 'com.mustang:id/multi_select_item_close'}
    __add_info = {'identifyBy': 'id', 'path': 'com.mustang:id/receipt_upload_picture_check'}
    __info_1 = {'identifyBy': 'id', 'path': 'com.mustang:id/receipt_upload_picture_torn'}
    __info_2 = {'identifyBy': 'id', 'path': 'com.mustang:id/receipt_upload_picture_lose'}
    __info_input = {'identifyBy': 'id', 'path': 'com.mustang:id/receipt_upload_picture_input'}
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/receipt_upload_picture_submit'}

    @catch_exception
    def add_receipt_image(self):
        # 上传回单照片
        self.driver.click_element(self.__add_image)

    @catch_exception
    def delete_receipt_image(self):
        # 删除回单照片
        self.driver.click_element(self.__delete_image)

    @catch_exception
    def add_receipt_info(self, info):
        # 添加异常信息
        self.__info_input['keys'] = info
        self.driver.click_element(self.__add_info)
        self.driver.click_element(self.__info_1)
        self.driver.click_element(self.__info_2)
        self.driver.send_keys(self.__info_input)

    @catch_exception
    def upload_receipt(self):
        # 提交回单信息
        self.driver.click_element(self.__confirm_btn)
