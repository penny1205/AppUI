#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import time
import random
from util.driver.driver import AppUiDriver
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WaybillCancelWuLiuYun(Wuliuyun):
    # 取消运单操作
    __cancel_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_employ_car'}  # 取消运单按钮
    __confirm_cancel = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_list_sure'}  # 取消运单按钮

    def cancel_waybill(self):
        self.driver.click_element(self.__cancel_btn)
        self.driver.click_element(self.__confirm_cancel)
