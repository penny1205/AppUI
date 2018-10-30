#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WaybillMainCheZhu(CheZhu):
    # 运单收款列表页面
    __confirm_waybill_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/confirm_btn'}  # 运单操作按钮

    @catch_exception
    def go_to_waybill_detail(self):
        # 进入运单操作页面
        self.driver.click_element(self.__confirm_waybill_btn)
