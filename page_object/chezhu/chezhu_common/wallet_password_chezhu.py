#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WalletPasswordCheZhu(CheZhu):
    # 输入钱包密码公共方法

    @catch_exception
    def send_password(self, pwd):
        # 输入钱包密码
        __check_pwd = {'identifyBy': 'id', 'path': 'com.mustang:id/pop_enter_password_board'}  # 密码框
        pwd_btn = {'1': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 0]},
                   '2': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 1]},
                   '3': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 2]},
                   '4': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 3]},
                   '5': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 4]},
                   '6': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 5]},
                   '7': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 6]},
                   '8': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 7]},
                   '9': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 8]},
                   '0': {'identifyBy': 'ids', 'path': ['com.mustang:id/btn_keys', 9]}}  # 密码键盘
        self.driver.find_element(__check_pwd)
        for key in pwd:
            self.driver.click_element(pwd_btn[key])

    def confirm_pwd(self):
        # 密码输入框带有确定按钮
        __confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/check_payment_password_unbunding'}
        self.driver.click_element(__confirm_btn)


