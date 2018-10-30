#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WalletChangePwdCheZhu(CheZhu):
    # 修改密码
    change_pwd_activity = '.account.ChangePasswordActivity'
    set_pwd_activity = '.account.wallet.SetNetPaymentPasswordActivity'
    confirm_pwd_activity = '.account.wallet.ConfirmNetPaymentPasswordActivity'
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/btn_confirm_password'}

    @catch_exception
    def confirm_change_pwd(self):
        self.driver.click_element(self.__confirm_btn)




