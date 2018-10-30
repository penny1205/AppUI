#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WalletCashCheZhu(CheZhu):
    # 钱包提现页面
    cash_activity = '.account.wallet.WithdrawNetActivity'  # 提现页面activity
    __cash = {'identifyBy': 'class', 'path': 'android.widget.Button'}  # 提现按钮
    __back_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/img_back_arrow'}  # 返回按钮
    cash_success_activity = '.account.WithdrawCompleteActivity'  # 提现成功页面activity
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/textview_modify'}  # 提现成功确认按钮

    @catch_exception
    def wallet_cash(self):
        self.driver.click_element(self.__cash)

    @catch_exception
    def cash_confirm(self):
        self.driver.click_element(self.__confirm_btn)
