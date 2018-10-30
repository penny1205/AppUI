#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WaybillConfirmWuliuyun(Wuliuyun):
    # 确认发车操作
    __list_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_wait_start'}  # 运单列表页确认发车按钮
    __detail_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_details_submit'}  # 运单详情页确认发车按钮
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_cancel'}  # 提示弹窗确认发车按钮

    @catch_exception
    def confirm_waybill(self, type):
        if type == 0:
            self.driver.click_element(self.__list_confirm_btn)
        elif type == 1:
            self.driver.click_element(self.__detail_confirm_btn)
        else:
            self.log.error('type error: confirm type must be int 0 or 1')
            return
        self.driver.click_element(self.__confirm_btn)
