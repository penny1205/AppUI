#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from page_object.chezhu.chezhu_common.choose_photo_chezhu import ChoosePhotoCheZhu


class WaybillUploadReceiptWuliuyun(Wuliuyun):
    # 回单上传操作
    __confirm_upload_activity = '.main.ReceiptUploadActivity'
    __list_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_arrive_receipt'}  # 运单列表页回单上传按钮
    __detail_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_details_submit'}  # 运单详情页回单上传按钮
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_submit'}  # 回单上传提交按钮
    __upload_image_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/multi_select_item_image'}  # 回单照片上传按钮
    __choose_img = {'identifyBy': 'xpath', 'path': '//android.widget.Button[@text=\"选择图片\"]'}  # 选择图片
    __abnormal_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_check'}  # 货物异常按钮
    __abnormal_info_1 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_torn'}  # 货物破损
    __abnormal_info_2 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_lose'}  # 货物缺少
    __abnormal_info_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_input'}  # 异常备注
    __receipt_confirm_title = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_amount_title'}

    @catch_exception
    def wait_upload_page(self):
        page_state = self.driver.wait_activity(self.__confirm_upload_activity)
        return page_state

    @catch_exception
    def upload_receipt_image(self):
        # 上传照片
        self.driver.click_element(self.__upload_image_btn)
        self.driver.click_element(self.__choose_img)
        ChoosePhotoCheZhu(self.app_driver).choose_image()

    @catch_exception
    def upload_receipt_abnormal_info(self, info='自动化测试'):
        # 回单上传异常信息填写
        self.__abnormal_info_input['keys'] = info
        self.driver.click_element(self.__abnormal_btn)
        self.driver.click_element(self.__abnormal_info_1)
        self.driver.click_element(self.__abnormal_info_2)
        self.driver.send_keys(self.__abnormal_info_input)

    @catch_exception
    def upload_receipt_submit(self):
        # 提交回单信息
        self.driver.click_element(self.__confirm_btn)

    def get_receipt_confirm(self):
        # 获取回单确认弹窗标题
        return self.driver.find_element(self.__receipt_confirm_title)
