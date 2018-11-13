#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class UserSettingPageWuliuyun(Wuliuyun):
    __logout_btn = {'identifyBy': 'xpath', 'path': '//android.widget.Button[@text=\"退出登录\"]'}
    __feedback = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"意见反馈\"]'}
    __app_info = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"关于我们\"]'}

    @catch_exception
    def logout(self):
        self.driver.click_element(self.__logout_btn)

