#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WalletMainCheZhu(CheZhu):
    # 我的钱包主页面
    wallet_activity = '.account.MyWalletActivity'
    __wallet_detail = {'path': 'com.mustang:id/textview_modify', 'identifyBy': 'id'}  # 钱包明细
    __wallet_cash = {'path': 'com.mustang:id/wallet_withdraw', 'identifyBy': 'id'}  # 提现
    __wallet_consignor = {'path': 'com.mustang:id/pay_select_collection', 'identifyBy': 'id'}  # 委托代收人
    __wallet_back_button = {'path': 'com.mustang:id/img_back_arrow', 'identifyBy': 'id'}  # 返回按钮
    #  -*- 支付设置-*-
    __wallet_setting = {'path': 'com.mustang:id/pay_setting', 'identifyBy': 'id'}  # 支付设置
    __wallet_change_pwd = {'path': 'com.mustang:id/pay_select_change', 'identifyBy': 'id'}  # 修改密码
    __wallet_reset_pwd = {'path': 'com.mustang:id/pay_select_forget', 'identifyBy': 'id'}  # 忘记密码
    __wallet_setting_cancel = {'path': 'com.mustang:id/pay_select_cancel', 'identifyBy': 'id'}  # 支付设置-取消

    @catch_exception
    def go_to_cash(self):
        # 进入提现页面
        self.driver.click_element(self.__wallet_cash)

    @catch_exception
    def go_to_detail(self):
        # 进入明细页面
        self.driver.click_element(self.__wallet_detail)

    @catch_exception
    def go_to_consignor(self):
        # 进入委托代收账户页面
        self.driver.click_element(self.__wallet_consignor)

    @catch_exception
    def go_to_change_pwd(self):
        # 进入修改密码页面
        self.driver.click_element(self.__wallet_setting)
        self.driver.click_element(self.__wallet_change_pwd)

    @catch_exception
    def go_to_reset_pwd(self):
        # 进入忘记密码页面
        self.driver.click_element(self.__wallet_setting)
        self.driver.click_element(self.__wallet_reset_pwd)