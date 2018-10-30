#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class WalletConsignorCheZhu(CheZhu):
    # 委托代收人
    consignor_activity = '.account.CollectionsListActivity'
    __add_consignor_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/textview_modify'}  # 新增委托代收人按钮
    __consignor_detail = {'identifyBy': 'ids', 'path': ['com.mustang:id/textview_modify', 0]}
    # --*-- 新增委托代收人 --*--
    add_consignor_activity = '.account.EntrustCollectionsActivity'  # 委托代收人详情页面activity
    __consignor_relation = {'identifyBy': 'id', 'path': 'com.mustang:id/gathering_relation'}  # 与代收人关系
    __relation_confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/time_select_cancel'}  # 与代收人关系弹窗-确认按钮
    __consignor_name = {'identifyBy': 'ids', 'path': ['com.mustang:id/editview_et', 0]}
    __consignor_idNo = {'identifyBy': 'ids', 'path': ['com.mustang:id/editview_et', 0]}
    __consignor_mobile = {'identifyBy': 'ids', 'path': ['com.mustang:id/editview_et', 0]}
    __consignor_confirm_btn = {'identifyBy': 'id', 'path': 'com.mustang:id/gathering_relation'}  # 确认开通按钮
    # --*-- 管理委托代收人 --*--
    __consignor_delete = {'identifyBy': 'id', 'path': 'com.mustang:id/gathering_btn_close'}  # 删除委托代收账户

    __confirm = {'identifyBy': 'id', 'path': 'com.mustang:id/dialog_sure'}  # 确认操作
    __cancel = {'identifyBy': 'id', 'path': 'com.mustang:id/dialog_cancel'}  # 取消操作

    @catch_exception
    def go_to_add_consignor(self):
        # 进入新增委托代收人页面
        self.driver.click_element(self.__add_consignor_btn)

    @catch_exception
    def go_to_consignor_details(self):
        # 进入委托代收人详情页面
        self.driver.click_element(self.__consignor_detail)

    @catch_exception
    def add_consignor(self, name, idNo, mobile):
        # 新增委托代收人
        self.__consignor_name['keys'] = name
        self.__consignor_idNo['keys'] = idNo
        self.__consignor_mobile['keys'] = mobile
        self.driver.click_element(self.__consignor_relation)
        self.driver.click_element(self.__relation_confirm_btn)
        self.driver.send_keys(self.__consignor_name)
        self.driver.send_keys(self.__consignor_idNo)
        self.driver.send_keys(self.__consignor_mobile)
        self.driver.click_element(self.__consignor_confirm_btn)
        self.driver.click_element(self.__confirm)

    @catch_exception
    def delete_consignor(self):
        # 删除委托代收人
        self.driver.click_element(self.__consignor_delete)
        self.driver.click_element(self.__confirm)

