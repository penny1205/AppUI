#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WuLiuYunWaybillDetail(Wuliuyun):
    # 运单详情页面
    __activity_detail = '.main.WaybillDetailsActivity'
    __back_btn = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"返回\"]'}
    __cancel_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_employ_car'}  # 取消运单按钮
    __confirm_cancel = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_list_sure'}  # 确认取消运单
    __change_btn_0 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_employ_car'}  # 待发车运单，修改运单按钮
    __change_btn_1 = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"修改\"]'}  # 已发车运单，修改运单按钮

    def wait_detail_page(self):
        state = self.driver.wait_activity(self.__activity_detail)
        return state

    def go_to_change_page(self, type):
        # type 0 未发车运单  1 已发车运单
        if type == 0:
            self.driver.click_element(self.__change_btn_0)
        elif type == 1:
            self.driver.click_element(self.__change_btn_1)
        else:
            self.log.error('change_btn type error, type must be int 0 or 1.')

    def cancel_waybill(self):
        self.driver.click_element(self.__cancel_btn)
        self.driver.click_element(self.__confirm_cancel)
