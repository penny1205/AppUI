#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class UserBankcardMainWuliuyun(Wuliuyun):
    __bankcard_main_activity = '.main.BankCardListActivity'
    __add_card_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/bankcard_btn'}  # 添加银行卡按钮
    __del_card_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/goods_name_item_delete'}  # 解绑银行卡
    __bank_card_btn = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/swipe_linearlayout'}
    __del_card_confirm = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_sure'}  # 确认解绑

    @catch_exception
    def go_to_add_card_page(self):
        self.driver.click_element(self.__add_card_btn)

    def del_card(self):
        self.driver.find_element(self.__bank_card_btn)
        self.driver.swipe_window(0.8, 0.2, 0.5, 0.2)
        self.driver.click_element(self.__del_card_btn)
        self.driver.click_element(self.__del_card_confirm)

    def go_to_bankcard_detail_page(self):
        self.driver.click_element(self.__bank_card_btn)

    def wait_bankcard_main_page(self):
        state = self.driver.wait_activity(self.__bankcard_main_activity)
        return state

    def find_bankcard(self):
        state = self.driver.isElement(self.__bank_card_btn)
        return state
