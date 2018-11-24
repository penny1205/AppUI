#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class UserMainPageWuliuyun(Wuliuyun):
    __setting_btn = {'identifyBy': 'xpath', 'path': '//android.widget.RelativeLayout/*/android.widget.ImageView[1]'}
    __bank_card = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"我的银行卡\"]'}
    __special_loan = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"我的专线贷\"]'}
    __second_loan = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"我的运秒付\"]'}

    @catch_exception
    def go_to_setting_page(self):
        self.driver.click_element(self.__setting_btn)

    @catch_exception
    def go_to_card_page(self):
        self.driver.click_element(self.__bank_card)

    @catch_exception
    def go_to_special_loan_page(self):
        self.driver.click_element(self.__special_loan)

    @catch_exception
    def go_to_second_loan_page(self):
        self.driver.click_element(self.__second_loan)
