#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import time
from util.db.dbutil import RedisDb
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class LoginCheZhu(CheZhu):
    # 车主登录页面

    @catch_exception
    def user_login(self, mobile):
        # 手机验证码登录
        __mobile = {'path': ['com.mustang:id/editview_rect', 0], 'identifyBy': 'ids'}  # 用户名
        __get_code = {'path': 'com.mustang:id/login_captcha', 'identifyBy': 'id'}  # 获取验证码按钮'
        __msg_code = {'path': ['com.mustang:id/editview_rect', 1], 'identifyBy': 'ids'}  # 验证码
        __login = {'path': 'com.mustang:id/login_submit', 'identifyBy': 'id'}  # 登录按钮
        __activity = '.account.LoginActivity'  # 登录页activity
        __mobile['keys'] = mobile
        self.driver.wait_activity(__activity)
        # 获取验证码
        self.driver.send_keys(__mobile)
        self.driver.click_element(__get_code)
        time.sleep(0.2)
        code = RedisDb().get_code(key='"{0}"'.format(mobile), name='AppLoginVerifyCode')  # 读取Redis登录验证码
        __msg_code['keys'] = code
        # 登录
        self.driver.send_keys(__msg_code)
        self.driver.click_element(__login)


