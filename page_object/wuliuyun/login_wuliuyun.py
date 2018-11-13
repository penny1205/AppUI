#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.wuliuyun.wuliuyun import Wuliuyun
from util.driver.project_decorator import catch_exception


class LoginWuLiuYun(Wuliuyun):
    __user_id = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/editview_et'}  # 用户名
    __password = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/login_password'}  # 密码
    __login = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/login_btn'}  # 登录按钮
    __login_activity = '.main.LoginActivity'  # 登录页activity

    @catch_exception
    def user_login(self, user, pwd):
        self.__user_id['keys'] = user
        self.__password['keys'] = pwd
        self.driver.send_keys(self.__user_id)
        self.driver.send_keys(self.__password)
        self.driver.click_element(self.__login)

    @catch_exception
    def wait_login_page(self):
        wait_state = self.driver.wait_activity(activity=self.__login_activity, timeout=20)
        return wait_state

