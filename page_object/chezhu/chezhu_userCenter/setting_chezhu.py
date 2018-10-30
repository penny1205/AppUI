#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.chezhu.chezhu import CheZhu


class SettingCheZhu(CheZhu):

    __suggest = {'path': 'com.mustang:id/suggest_layout', 'identifyBy': 'id'}
    __about = {'path': 'com.mustang:id/about_layout', 'identifyBy': 'id'}
    __logout = {'path': 'com.mustang:id/logout_button', 'identifyBy': 'id'}
    __confirm_botton = {'path': 'com.mustang:id/dialog_sure', 'identifyBy': 'id'}
    __settingActivity = '.account.SettingsActivity'

    @catch_exception
    def user_logout(self):
        self.driver.wait_activity(activity=self.__settingActivity)
        self.driver.click_element(self.__logout)
        self.driver.click_element(self.__confirm_botton)

    @catch_exception
    def goto_suggest_page(self):
        self.driver.click_element(self.__suggest)

    @catch_exception
    def goto_about_page(self):
        self.driver.click_element(self.__about)


