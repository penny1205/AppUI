#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from page_object.wuliuyun.wuliuyun_common.swipe_screen import SwipeScreen


class WaybillChangeWuLiuYun(Wuliuyun):
    # 修改运单操作
    __change_waybill_activity = '.main.AddWayBillNewActivity'
    __change_btn_0 = {'identifyBy': 'id', 'path': 'waybill_details_submit_station'}  # 待发车运单，修改运单按钮
    __change_btn_1 = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"修改\"]'}  # 已发车运单，修改运单按钮
    __total_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/total_amount_edt'}  # 运费总额
    __pre_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/pre_amount_edt'}  # 预付金额
    __oil_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/oil_amount_edt'}  # 油卡金额
    __dest_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dest_amount_edt'}  # 油卡金额
    __last_amt_edt = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/last_amount_edt'}  # 尾款金额
    __commit_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/commit_button'}  # 确认修改按钮
    swipe = SwipeScreen

    @catch_exception
    def change_waybill(self, totalAmt, preAmt, oilAmt, destAmt, lastAmt):
        # 修改运单
        self.__total_amt_edt['keys'] = totalAmt
        self.__pre_amt_edt['keys'] = preAmt
        self.__oil_amt_edt['keys'] = oilAmt
        self.__dest_amt_edt['keys'] = destAmt
        self.__last_amt_edt['keys'] = lastAmt
        self.swipe(self.app_driver).swipe_screen(self.__last_amt_edt, self.__change_waybill_activity)
        self.driver.send_keys(self.__total_amt_edt)
        self.driver.send_keys(self.__pre_amt_edt)
        self.driver.send_keys(self.__oil_amt_edt)
        self.driver.send_keys(self.__dest_amt_edt)
        self.driver.send_keys(self.__last_amt_edt)

    def commit_change(self):
        # 确认提交
        self.swipe(self.app_driver).swipe_screen(self.__commit_btn, self.__change_waybill_activity)
        self.driver.click_element(self.__commit_btn)

