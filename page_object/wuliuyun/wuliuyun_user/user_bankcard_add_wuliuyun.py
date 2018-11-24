#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun
from util.db.dbutil import RedisDb
import time


class UserBankcardAddWuliuyun(Wuliuyun):
    __bankcard_add_activity = '.main.AddBankCardActivity'
    __cardNo = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 0]}  # 银行卡号
    __card_mobile = {'identifyBy': 'ids',
                     'path': ['com.luchang.lcgc:id/editview_et', 1]}  # 银行卡预留手机号
    __bank_name = {'identifyBy': 'ids', 'path': ['com.luchang.lcgc:id/editview_et', 2]}  # 银行名称
    __bank_branch_name = {'identifyBy': 'ids',
                          'path': ['com.luchang.lcgc:id/editview_et', 3]}  # 支行名称
    __bank_city_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/addbankcard_place'}  # 所属省市
    __submit_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/add_bankcard_next'}  # 提交银行卡信息

    @catch_exception
    def add_card_info(self, card_no, card_mobile, bank_name, bank_branch_name):
        self.__cardNo['keys'] = card_no
        self.__card_mobile['keys'] = card_mobile
        self.__bank_name['keys'] = bank_name
        self.__bank_branch_name['keys'] = bank_branch_name
        self.driver.send_keys(self.__cardNo)
        self.driver.send_keys(self.__card_mobile)
        self.driver.send_keys(self.__bank_name)
        self.driver.send_keys(self.__bank_branch_name)

    @catch_exception
    def choose_bank_city(self):
        self.driver.click_element(self.__bank_city_btn)
        bank_province = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"安徽\"]'}
        bank_city = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"合肥\"]'}
        self.driver.click_element(bank_province)
        self.driver.click_element(bank_city)

    def submit_bankcard(self):
        self.driver.click_element(self.__submit_btn)

    def add_card_confirm(self, mobile):
        mobile_code = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/add_bankcard_verificationCode'}
        confirm_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/add_bankcard_verificationCode_next'}
        time.sleep(0.1)
        code = RedisDb().get_code(key='"{0}"'.format(mobile), name='AppSpecialLineBankBindCode')
        mobile_code['keys'] = code
        self.driver.send_keys(mobile_code)
        self.driver.click_element(confirm_btn)
