#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class AddCardCheZhu(CheZhu):
    # 绑卡页面
    #  -*-绑定提现卡页面-*-
    cash_activity = '.account.AddNetCardActivity'
    __cash_card_no = {'path': 'com.mustang:id/addcard_cardNo', 'identifyBy': 'id'}
    __cash_verify_code = {'path': 'com.mustang:id/verify_code_edt', 'identifyBy': 'id'}
    __cash_get_code = {'path': 'com.mustang:id/get_captcha_txt', 'identifyBy': 'id'}
    __cash_add_btn = {'path': 'com.mustang:id/add_card_sure', 'identifyBy': 'id'}

    #  -*-绑定还款卡页面-*-
    repay__activity = '.account.AddCardActivity'
    __repay_card_no = {'path': 'com.mustang:id/addcard_cardNo', 'identifyBy': 'id'}
    __repay_mobile = {'path': 'com.mustang:id/addcard_mobile', 'identifyBy': 'id'}
    __repay_allow_deal = {'path': 'com.mustang:id/chekbox', 'identifyBy': 'id'}
    __repay_add_btn = {'path': 'com.mustang:id/add_card_sure', 'identifyBy': 'id'}

    @catch_exception
    def add_repay_card(self, cardNo, mobile):
        self.__repay_card_no['keys'] = cardNo
        self.__repay_mobile['keys'] = mobile
        self.driver.send_keys(self.__repay_card_no)
        self.driver.send_keys(self.__repay_mobile)
        self.driver.click_element(self.__repay_allow_deal)
        self.driver.click_element(self.__repay_add_btn)




