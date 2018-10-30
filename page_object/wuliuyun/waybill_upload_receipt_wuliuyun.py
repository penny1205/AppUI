#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WaybillUploadReceiptWuliuyun(Wuliuyun):
    # 回单上传操作
    __list_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_arrive_receipt'}  # 运单列表页回单上传按钮
    __detail_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_details_submit'}  # 运单详情页回单上传按钮
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_submit'}  # 回单上传提交按钮
    __upload_image_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/multi_select_item_image'}  # 回单照片上传按钮
    __abnormal_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_check'}  # 货物异常按钮
    __abnormal_info_1 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_torn'}  # 货物破损
    __abnormal_info_2 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_lose'}  # 货物缺少
    __abnormal_info_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/receipt_upload_picture_input'}  # 异常备注

    @catch_exception
    def go_to_upload_receipt_page(self, type):
        # 回单上传操作 type：0 列表页点击回单上传  1 详情页点击回单上传
        if type == 0:
            self.driver.click_element(self.__list_confirm_btn)
        elif type == 1:
            self.driver.click_element(self.__detail_confirm_btn)
        else:
            self.log.error('type error: confirm type must be int 0 or 1')
            return

    def upload_receipt_image(self):
        # 上传照片按钮
        self.driver.click_element(self.__upload_image_btn)

    def upload_receipt_abnormal_info(self, info):
        # 回单上传异常信息填写
        self.__abnormal_info_input['keys'] = info
        self.driver.send_keys(self.__abnormal_info_input)
        self.driver.click_element(self.__confirm_btn)
