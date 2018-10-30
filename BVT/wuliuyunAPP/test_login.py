#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import unittest
from util.driver.driver import AppUiDriver
from util.log.log import Log
from page_object.wuliuyun.login_wuliuyun import LoginWuLiuYun


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.log = Log()
        self.driver = AppUiDriver().app_ui_driver(appPackage='com.luchang.lcgc', appActivity='.main.SplashActivity')
        self.user = 'weibo'
        self.password = '111111'
        self.activity = '.main.MainTabFragment'
        pass

    def tearDown(self):
        pass

    def test_login(self):
        activity = LoginWuLiuYun(self.driver).user_login(user=self.user, password=self.password)
        self.assertEqual(activity, self.activity)





