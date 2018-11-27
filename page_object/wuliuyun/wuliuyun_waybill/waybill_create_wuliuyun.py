#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import time
import random
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from page_object.wuliuyun.wuliuyun_common.swipe_screen import SwipeScreen


class WaybillCreateWuLiuYun(Wuliuyun):
    # 新建运单页面
    add_waybill_activity = '.main.AddWayBillNewActivity'
    __employ_car = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_employ_car'}  # 外请车按钮
    __owner_car = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_owner_car'}  # 公司车按钮
    __tv_line = {'identifyBy': 'id', 'path': 'tv_line'}  # 运输路线按钮
    __customer_info = {'identifyBy': 'id', 'path': 'customer_info'}  # 项目按钮
    __departure_order_number = {'identifyBy': 'id', 'path': 'departure_order_number'}  # 订单号
    __goods_name = {'identifyBy': 'id', 'path': 'goods_name'}  # 货物信息1
    __employ_driver_phone = {'identifyBy': 'id', 'path': 'tv_phone_driver'}  # 司机手机号
    __owner_driver_phone = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_rect', 0]}
    __rb_nonDriver = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_nonDriver'}  # 无回单按钮
    __rb_isDriver = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/rb_isDriver'}  # 有回单按钮
    __totalAmt = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"运费总额 (元)\"]'}  # 运费总额
    __lastAmt = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"尾款金额 (元)\"]'}  # 尾款
    __totalAmt_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/total_amount_edt'}
    __preAmt_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/pre_amount_edt'}
    __oilAmt_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/oil_amount_edt'}
    __destAmt_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dest_amount_edt'}
    __lastAmt_input = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/last_amount_edt'}
    __commit_button = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/commit_button'}
    __trans_photo ={'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/transfer_proto_image'}
    swipe = SwipeScreen

    def input_basic_info(self, car_type):
        # 录入基本信息  车辆类型 1 外请车  2 公司车
        if car_type == '1':  # 选择运单类型外请车/公司车
            self.driver.click_element(self.__employ_car)
        elif car_type == '2':
            self.driver.click_element(self.__owner_car)
        else:
            self.log.error('Car type is wrong!---type:' + car_type)
            raise
        self.driver.click_element(self.__tv_line)
        self.choose_line()
        self.choose_project()

    def input_goods_info(self):
        # 录入货物信息
        self.driver.click_element(self.__goods_name)
        self.add_goods()

    def input_driver_info(self, car_type, mobile):
        # 录入承运信息  车辆类型 1 外请车  2 公司车
        if car_type == '1':
            self.driver.click_element(self.__employ_driver_phone)
            self.choose_employ_driver(mobile)
            self.swipe(self.app_driver).swipe_screen(self.__rb_nonDriver, self.add_waybill_activity)
            self.driver.click_element(self.__rb_isDriver)
        elif car_type == '2':
            self.choose_owner_driver(mobile)
            self.swipe(self.app_driver).swipe_screen(self.__rb_nonDriver, self.add_waybill_activity)
            self.driver.click_element(self.__rb_isDriver)
        else:
            self.log.error('Car type is wrong!---type:' + car_type)

    def input_cost_info(self, total='10', pre='1', oil='1', dest='1', last='1'):
        # 录入运费信息
        self.__totalAmt_input['keys'] = total
        self.__preAmt_input['keys'] = pre
        self.__oilAmt_input['keys'] = oil
        self.__destAmt_input['keys'] = dest
        self.__lastAmt_input['keys'] = last
        self.swipe(self.app_driver).swipe_screen(self.__preAmt_input, self.add_waybill_activity)
        self.driver.send_keys(self.__totalAmt_input)
        self.driver.send_keys(self.__preAmt_input)
        self.swipe(self.app_driver).swipe_screen(self.__trans_photo, self.add_waybill_activity)
        self.driver.send_keys(self.__oilAmt_input)
        self.driver.send_keys(self.__destAmt_input)
        self.driver.send_keys(self.__lastAmt_input)

    def commit_waybill_info(self):
        # 提交录单信息
        self.swipe(self.app_driver).swipe_screen(self.__commit_button, self.add_waybill_activity)
        self.driver.click_element(self.__commit_button)

    def choose_line(self):
        # 选择路线
        line_activity = '.main.AddTranslateLineActivity'
        line_send_city = {'identifyBy': 'id', 'path': 'line_send_city'}
        sendProvince = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"北京\"]'}
        sendCity = {'identifyBy': 'xpath',
                    'path': '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]'}
        sendDistrict = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"不限\"]'}
        line_arrive_city = {'identifyBy': 'id', 'path': 'line_arrive_city'}
        arriveProvince = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"天津\"]'}
        arriveCity = {'identifyBy': 'xpath',
                      'path': '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]'}
        arriveDistrict = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"不限\"]'}
        commit_button = {'identifyBy': 'id', 'path': 'commit_button'}
        self.driver.click_element(line_send_city)
        self.driver.click_element(sendProvince)
        self.driver.click_element(sendCity)
        self.driver.click_element(sendDistrict)
        self.driver.click_element(line_arrive_city)
        self.driver.click_element(arriveProvince)
        self.driver.click_element(arriveCity)
        self.driver.click_element(arriveDistrict)
        self.driver.click_element(commit_button)

    def choose_project(self):
        # 选择项目
        project_name = {'identifyBy': 'id', 'path': 'project_text'}
        self.driver.click_element(self.__customer_info)
        self.driver.click_element(project_name)

    def add_order_number(self):
        # 填写订单号
        departure_order_number = random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"], 8)
        self.__departure_order_number['keys'] = departure_order_number
        self.driver.send_keys(self.__departure_order_number)

    def add_goods(self):
        # 添加货物信息
        choose_goods_name = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/goods_name'}
        goods_weight = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 0], 'keys': '6'}
        goods_bulk = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 1], 'keys': '6'}
        goods_number = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 2], 'keys': '6'}
        goods_value = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 3], 'keys': '6'}
        goods_charge = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 4], 'keys': '6'}
        goods_name = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/item_text', 0]}
        goods_name_commit = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/goods_name_commit'}
        commit_button = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/commit_button'}
        self.driver.send_keys(goods_weight)
        self.driver.send_keys(goods_bulk)
        self.driver.send_keys(goods_number)
        self.driver.send_keys(goods_value)
        self.driver.send_keys(goods_charge)
        self.driver.click_element(choose_goods_name)
        self.driver.click_element(goods_name)
        self.driver.click_element(goods_name_commit)
        self.driver.click_element(commit_button)

    def choose_employ_driver(self, mobile):
        # 选择外请车司机
        driver_mobile = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/editview_et'}  # 司机手机号输入框
        search_button = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/search_button'}  # 查询按钮
        employ_driver = {'identifyBy': 'xpath',
                         'path': '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[1]'}  # 司机列表第一条
        driver_mobile['keys'] = mobile
        self.driver.send_keys(driver_mobile)
        self.driver.click_element(search_button)
        self.driver.click_element(employ_driver)

    def choose_owner_driver(self, mobile):
        # 选择公司车司机
        car_info = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/car_info'}
        owner_car = {'identifyBy': 'xpath',
                     'path': '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[1]'}  # 公司车列表第一条
        self.__owner_driver_phone['keys'] = mobile
        self.driver.send_keys(self.__owner_driver_phone)  # 输入公司车司机手机号
        self.driver.click_element(car_info)  # 选择车辆
        self.driver.click_element(owner_car)



