#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception
from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu


class WaybillConfirmCheZhu(CheZhu):
    __confirm_page_activity = '.account.ConfirmWayBillActivity'  # 确认发车页面
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/commit_button'}  # 确认发车按钮
    __img_upload = {'identifyBy': 'id', 'path': 'com.mustang:id/transfer_proto_image'}  # 添加运输协议按钮
    __choose_img = {'identifyBy': 'id', 'path': 'com.mustang:id/choose_image_text'}  # 选择上传照片
    __change_consignor = {'identifyBy': 'id', 'path': 'com.mustang: id / line_change_acc'}  # 修改委托代收人按钮

    @catch_exception
    def wait_confirm_page(self):
        # 等待页面activity
        wait_state = self.driver.wait_activity(self.__confirm_page_activity, timeout=20)
        return wait_state

    @catch_exception
    def upload_transport_img(self):
        # 上传运输协议
        self.driver.click_element(self.__img_upload)
        self.driver.click_element(self.__choose_img)
        ChoosePhotoCheZhu(self.app_driver).choose_image()

    @catch_exception
    def confirm_waybill(self):
        # 确认运单
        self.driver.click_element(self.__confirm_btn)