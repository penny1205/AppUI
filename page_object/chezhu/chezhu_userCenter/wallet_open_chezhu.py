#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception
from page_object.chezhu.chezhu_common.wallet_password_chezhu import WalletPasswordCheZhu


class WalletOpenCheZhu(CheZhu):
    # 钱包开户页面
    open_activity = '.account.WalletOpenAct'  # 开户页面activity
    __confirm = {'identifyBy': 'id', 'path': 'com.mustang:id/wallet_btn'}  # 确认开户按钮
    __back_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/img_back_arrow'}  # 返回按钮
    cash_success_activity = '.account.wallet.SetNetPaymentPasswordActivity'  # 设置密码页面activity
    __confirm_pwd = {'identifyBy': 'id', 'path': 'com.mustang:id/btn_confirm_password'}  # 确认密码

    def wait_page(self):
        self.driver.wait_activity(self.open_activity)

    @catch_exception
    def wallet_open(self):
        self.driver.click_element(self.__confirm)

    @catch_exception
    def set_pwd(self):
        WalletPasswordCheZhu(self.app_driver).send_password('123321')
        WalletPasswordCheZhu(self.app_driver).send_password('123321')
        self.driver.click_element(self.__confirm_pwd)
