#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WaybillArriveConfirmWuliuyun(Wuliuyun):
    # 到达确认操作
    __list_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_transform_arrive'}  # 运单列表页到达确认按钮
    __detail_confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_details_submit'}  # 运单详情页确认发车按钮
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_amount_submit'}  # 提示弹窗确认发车按钮
    __confirm_amt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_amount_show_input'}  # 到付确认金额
    __confirm_info = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_amount_notice'}  # 到付确认备注

    @catch_exception
    def go_to_confirm_waybill(self, type):
        # 到达确认
        if type == 0:
            self.driver.click_element(self.__list_confirm_btn)
        elif type == 1:
            self.driver.click_element(self.__detail_confirm_btn)
        else:
            self.log.error('type error: confirm type must be int 0 or 1')
            return

    @catch_exception
    def arrive_confirm_waybill(self, amt, info):
        # 填写到付金额 确认到达
        self.__confirm_amt['keys'] = amt
        self.__confirm_info['keys'] = info
        self.driver.send_keys(self.__confirm_amt)
        self.driver.send_keys(self.__confirm_info)
        self.driver.click_element(self.__confirm_btn)
