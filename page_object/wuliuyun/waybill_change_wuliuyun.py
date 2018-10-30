#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from page_object.wuliuyun.wuliuyun_common.swipe_screen import SwipeScreen


class WaybillChangeWuLiuYun(Wuliuyun):
    # 修改运单操作
    __change_btn_0 = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_employ_car'}  # 待发车运单，修改运单按钮
    __change_btn_1 = {'identifyBy': 'name', 'path': '修改'}  # 已发车运单，修改运单按钮
    __total_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/total_amount_edt'}  # 运费总额
    __pre_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/pre_amount_edt'}  # 预付金额
    __oil_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/oil_amount_edt'}  # 油卡金额
    __dest_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dest_amount_edt'}  # 油卡金额
    __last_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/last_amount_edt'}  # 尾款金额
    __commit_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/commit_button'}  # 确认修改按钮
    swipe = SwipeScreen

    @catch_exception
    def change_waybill(self, type, totalAmt, preAmt, oilAmt, destAmt, lastAmt):
        # 修改运单  type: 0 未发车运单  1 已发车运单
        self.__total_amt_edt['keys'] = totalAmt
        self.__pre_amt_edt['keys'] = preAmt
        self.__oil_amt_edt['keys'] = oilAmt
        self.__dest_amt_edt['keys'] = destAmt
        self.__last_amt_edt['keys'] = lastAmt
        if type == 0:
            self.driver.click_element(self.__change_btn_0)
        elif type == 1:
            self.driver.click_element(self.__change_btn_1)
        else:
            self.log.error('change_btn type error, type must be int 0 or 1.')
        self.swipe(self.driver).swipe_screen(self.__last_amt_edt)
        self.driver.send_keys(self.__total_amt_edt)
        self.driver.send_keys(self.__pre_amt_edt)
        self.driver.send_keys(self.__oil_amt_edt)
        self.driver.send_keys(self.__dest_amt_edt)
        self.driver.send_keys(self.__last_amt_edt)
        self.swipe(self.driver).swipe_screen(self.__commit_btn)
        self.driver.click_element(self.__commit_btn)

