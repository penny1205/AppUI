#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class UserSettingPageWuliuyun(Wuliuyun):
    __setting_page_activity = '.main.SettingsActivity'
    __logout_btn = {'identifyBy': 'xpath', 'path': '//android.widget.Button[@text=\"退出登录\"]'}
    __logout_confirm = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/dialog_sure'}
    __feedback = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"意见反馈\"]'}
    __app_info = {'identifyBy': 'xpath', 'path': '//android.widget.TextView[@text=\"关于我们\"]'}

    @catch_exception
    def logout(self):
        self.driver.click_element(self.__logout_btn)
        self.driver.click_element(self.__logout_confirm)

    @catch_exception
    def wait_setting_page(self):
        self.driver.wait_activity(self.__setting_page_activity)


