#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception
from page_object.chezhu.chezhu_common.wallet_password_chezhu import WalletPasswordCheZhu


class WalletChangePwdCheZhu(CheZhu):
    # 修改密码
    change_pwd_activity = '.account.ChangePasswordActivity'
    set_pwd_activity = '.account.wallet.SetNetPaymentPasswordActivity'
    confirm_pwd_activity = '.account.wallet.ConfirmNetPaymentPasswordActivity'
    __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/btn_confirm_password'}

    @catch_exception
    def confirm_change_pwd(self):
        self.driver.click_element(self.__confirm_btn)

    def change_pwd(self, oldpwd, newpwd):
        self._pwd = WalletPasswordCheZhu(self.app_driver)
        self._pwd.send_password(oldpwd)
        self._pwd.send_password(newpwd)
        self._pwd.send_password(newpwd)
