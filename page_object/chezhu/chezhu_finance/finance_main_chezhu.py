#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class FinanceMainCheZhu(CheZhu):
    __driverLoan = {'path': 'com.mustang:id/tv_driverloan_applicaiton', 'identifyBy': 'id'}
    __buyCarLoan = {'path': 'com.mustang:id/goto_buycar_loan', 'identifyBy': 'id'}

    @catch_exception
    def go_to_driver_loan(self):
        # 进入司机贷模块
        self.driver.click_element(self.__driverLoan)

    @catch_exception
    def go_to_buy_car_loan(self):
        # 进入购车贷模块
        self.driver.click_element(self.__buyCarLoan)
