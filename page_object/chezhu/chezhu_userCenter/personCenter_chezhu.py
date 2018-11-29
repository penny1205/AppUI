#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun_common.swipe_screen import SwipeScreen


class PersonCenterCheZhu(CheZhu):
    #  我的页面
    __main_activity = '.account.MainTabFragment'  # 运单跟踪主页面activity
    __user_info = {'path': 'com.mustang:id/my_info_layout', 'identifyBy': 'id'}  # 个人信息
    __user_wallet = {'path': 'com.mustang:id/account_notice_wallet_account', 'identifyBy': 'id'}  # 司机钱包
    __account_bill = {'path': 'com.mustang:id/account_bill_layout', 'identifyBy': 'id'}  # 我的账单
    __account_bankcard = {'path': 'com.mustang:id/account_bankcard_layout', 'identifyBy': 'id'}  # 我的银行卡
    __share = {'path': 'com.mustang:id/share_layout', 'identifyBy': 'id'}  # 邀请车友
    __setting = {'path': 'com.mustang:id/account_setting', 'identifyBy': 'id'}  # 设置
    __auth = {'path': 'com.mustang:id/goto_auth', 'identifyBy': 'id'}  # 去认证按钮

    @catch_exception
    def goto_user_info(self):
        # 用户信息
        self.driver.click_element(self.__user_info)

    @catch_exception
    def goto_user_wallet(self):
        # 我的钱包
        self.driver.click_element(self.__user_wallet)

    @catch_exception
    def goto_account_bill(self):
        # 我的账单
        self.driver.click_element(self.__account_bill)

    @catch_exception
    def goto_account_bankcard(self):
        # 我的银行卡
        self.driver.click_element(self.__account_bankcard)

    @catch_exception
    def goto_share_page(self):
        # 车友分享
        self.driver.click_element(self.__share)

    @catch_exception
    def goto_setting_page(self):
        # 设置页面
        SwipeScreen(self.app_driver).swipe_screen(self.__setting, self.__main_activity)
        self.driver.click_element(self.__setting)

    @catch_exception
    def goto_certification_page(self):
        # 用户认证
        self.driver.click_element(self.__user_wallet)
        self.driver.click_element(self.__auth)
