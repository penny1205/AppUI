#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class WuLiuYunWaybillTab(Wuliuyun):

    main_tab_activity = '.main.MainTabFragment'  # 运单跟踪主页面activity
    __create_waybill = {'identifyBy': 'xpath', 'path': '//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView'}  # 录单按钮
    __waybill_dfc = {'identifyBy': 'name', 'path': '待发车'}
    __waybill_ysz = {'identifyBy': 'name', 'path': '运输中'}
    __waybill_ydd = {'identifyBy': 'name', 'path': '已到达'}
    __waybill_ywc = {'identifyBy': 'name', 'path': '已完成'}
    __waybill_tracking = {'identifyBy': 'name', 'path': '运单跟踪'}
    __user_account = {'identifyBy': 'name', 'path': '我的账户'}
    __waybill_view_page = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_track_viewpager'}  # 运单列表
    __waybill = {'identifyBy': 'xpath', 'path': '//android.widget.ListView/android.widget.LinearLayout[1]'}  # 运单列表第一条数据

    @catch_exception
    def go_to_create_waybill(self):
        # 进入录单页面
        self.driver.click_element(self.__create_waybill)

    @catch_exception
    def go_to_waybill_dfc(self):
        # 进入待发车列表页面
        self.driver.click_element(self.__waybill_dfc)

    @catch_exception
    def go_to_waybill_ysz(self):
        # 进入运输中列表页面
        self.driver.click_element(self.__waybill_ysz)

    @catch_exception
    def go_to_waybill_ydd(self):
        # 进入已到达列表页面
        self.driver.click_element(self.__waybill_ydd)

    @catch_exception
    def go_to_waybill_ywc(self):
        # 进入已完成列表页面
        self.driver.click_element(self.__waybill_ywc)

    @catch_exception
    def go_to_waybill_tracking(self):
        # 进入运单跟踪页面
        self.driver.click_element(self.__waybill_tracking)

    @catch_exception
    def go_to_user_account(self):
        # 进入我的账户页面
        self.driver.click_element(self.__user_account)

    @catch_exception
    def go_to_waybill_detail(self):
        # 点击运单列表第一条数据，进入发车确认/运单详情页面
        self.driver.click_element(self.__waybill)


