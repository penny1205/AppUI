#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu


class WaybillReceiptConfirmWuliuyun(Wuliuyun):
    # 回单确认页面
    __receipt_confirm_activity = '.main.ReceiptConfirmActivity'
    __add_receipt_img = {'identifyBy': 'xpath', 'path': '//android.widget.GridView/android.widget.LinearLayout[2]'}
    __choose_img = {'identifyBy': 'path', 'path': '//android.widget.Button[@text=\"选择图片\"]'}  # 选择图片
    __del_receipt_img = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_wait_start'}  # 删除图片
    __del_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_sure'}  # 确认删除
    __confirm_info = {'identifyBy': 'class', 'path': 'android.widget.EditText'}  # 确认备注
    __submit_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_confirm_picture_submit'}  # 回单确认无误按钮

    @catch_exception
    def wait_confirm_page(self):
        page_state = self.driver.wait_activity(self.__receipt_confirm_activity)
        return page_state

    @catch_exception
    def add_receipt_image(self):
        # 上传照片
        self.driver.click_element(self.__add_receipt_img)
        self.driver.click_element(self.__choose_img)
        ChoosePhotoCheZhu(self.app_driver).choose_image()

    @catch_exception
    def del_receipt_image(self):
        # 删除照片
        self.driver.click_element(self.__del_receipt_img)

    @catch_exception
    def add_confirm_info(self):
        #  回单确认备注填写
        info = '回单确认备注'
        self.__confirm_info['keys'] = info
        self.driver.send_keys(self.__confirm_info)

    @catch_exception
    def confirm_receipt(self):
        #  回单确认
        self.driver.click_element(self.__submit_btn)

