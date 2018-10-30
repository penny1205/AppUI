#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class BankCardMainCheZhu(CheZhu):
    # 我的银行卡页面
    __cash_card = {
        'path': '//android.widget.ListView[@resource-id=\"com.mustang:id/bankcardList\"]/*/*/android.widget.LinearLayout[1]',
        'identifyBy': 'xpath'}  # 提现卡
    __untie_card = {'path': 'com.mustang:id/delete_tv', 'identifyBy': 'id'}  # 解绑卡/换绑卡
    __repay_card = {'path': 'com.mustang:id/repayment_bankcard_container', 'identifyBy': 'id'}  # 还款卡
    __add_cash_card = {'identifyBy': 'id', 'path': 'com.mustang:id/add_card_btn'}  # 添加提现卡
    __add_repay_card = {'identifyBy': 'id', 'path': 'com.mustang:id/add_card_btn_repayment'}  # 添加还款卡

    @catch_exception
    def add_cash_card(self):
        # 跳转绑定提现卡页面 绑卡需要支付网关验证码
        self.driver.click_element(self.__add_cash_card)

    @catch_exception
    def untie_cash_card(self):
        # 解绑提现卡
        self.driver.find_element(self.__cash_card)
        self.driver.swipe_window(0.8, 0.3, 0.5, 0.3)
        self.driver.click_element(self.__untie_card)

    @catch_exception
    def untie_repay_card(self):
        # 解绑还款卡/换卡
        self.driver.find_element(self.__repay_card)
        if self.driver.isElement(self.__cash_card):
            self.driver.swipe_window(0.8, 0.6, 0.5, 0.6)
            self.driver.click_element(self.__untie_card)
        else:
            self.driver.swipe_window(0.8, 0.4, 0.5, 0.4)
            self.driver.click_element(self.__untie_card)

    @catch_exception
    def add_repay_card(self):
        # 跳转绑定还款卡页面
        self.driver.click_element(self.__add_repay_card)


if __name__ == '__main__':
    import time
    from util.driver.driver import AppUiDriver
    from page_object.chezhu.chezhu_common.main_tab_chezhu import CheZhuMainTab
    from page_object.chezhu.chezhu_userCenter.personCenter_chezhu import CheZhuPersonCenter
    from page_object.chezhu.chezhu_userCenter.bankcard_addcard_chezhu import AddCardCheZhu

    try:
        driver = AppUiDriver().app_ui_driver(appPackage='com.mustang', appActivity='.account.SplashActivity')
        main_tab = CheZhuMainTab(driver)
        person_center = CheZhuPersonCenter(driver)
        bank_card = CheZhuBankCardMain(driver)
        add_card = AddCardCheZhu(driver)
        main_tab.close_driver_loan_ads()
        main_tab.goto_person_center()
        person_center.goto_account_bankcard()
        bank_card.untie_repay_card()
        if driver.current_activity == add_card.repay__activity:
            add_card.add_repay_card(cardNo='6217001630031143297', mobile='18056070532')

        time.sleep(5)
    finally:
        driver.quit()
