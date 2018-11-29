#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class MainTabCheZhu(CheZhu):
    # 车主APP主页面
    def __init__(self, driver):
        CheZhu.__init__(self, driver)
        self.activity = '.account.MainTabFragment'  # 运单跟踪主页面activity
        self.ads_img = {'path': 'com.mustang:id/imageview', 'identifyBy': 'id'}
        self.ads_close = {'path': 'com.mustang:id/close_iv', 'identifyBy': 'id'}
        self.msg_button = {'path': 'com.mustang:id/title_set_img', 'identifyBy': 'id'}  # 消息中心按钮
        self.waybill = {
            'path': "//android.widget.TextView[@resource-id=\"com.mustang:id/textview\" and @text=\"运单收款\"]",
            'identifyBy': 'xpath'}
        self.finance = {
            'path': "//android.widget.TextView[@resource-id=\"com.mustang:id/textview\" and @text=\"我要借钱\"]",
            'identifyBy': 'xpath'}
        self.person_center = {
            'path': "//android.widget.TextView[@resource-id=\"com.mustang:id/textview\" and @text=\"我的\"]",
            'identifyBy': 'xpath'}
        self.close_driver_loan_ads()

    @catch_exception
    def wait_main_page(self):
        wait_state = self.driver.wait_activity(activity=self.activity, timeout=20)
        return wait_state

    @catch_exception
    def goto_msg_center(self):
        # 进入消息中心页面
        self.driver.click_element(self.msg_button)

    @catch_exception
    def goto_waybill_page(self):
        # 进入运单收款页面
        self.driver.click_element(self.waybill)

    @catch_exception
    def goto_finance_page(self):
        # 进入我要借钱页面
        self.driver.click_element(self.finance)

    @catch_exception
    def goto_person_center(self):
        # 进入我的页面
        self.driver.click_element(self.person_center)

    @catch_exception
    def close_driver_loan_ads(self):
        # 关闭车主贷广告
        self.driver.find_element(self.ads_img)
        if self.driver.find_element(self.ads_img):
            self.driver.click_element(self.ads_close)

