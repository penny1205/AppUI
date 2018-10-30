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
        __check_pwd = {'identifyBy': 'id', 'path': 'com.mustang:id/check_payment_password_input'}  # 密码输入框
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
        __confirm_button = {'identifyBy': 'id', 'path': 'com.mustang:id/check_payment_password_unbunding'}  # 确认密码
        self.driver.find_element(__check_pwd)
        for key in pwd:
            self.driver.click_element(pwd_btn[key])
        if self.driver.isElement(__confirm_button):  # 判断是否有确认按钮
            self.driver.click_element(__confirm_button)