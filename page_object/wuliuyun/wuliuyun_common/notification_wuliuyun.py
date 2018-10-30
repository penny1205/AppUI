#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import time
from page_object.wuliuyun.wuliuyun import Wuliuyun
from util.driver.project_decorator import catch_exception


class NotificationWuLiuYun(Wuliuyun):
    # 货主端弹窗操作

    @catch_exception
    def close_update_notice(self):
        # 关闭升级弹窗
        __version_msg = {'identifyBy': 'id', 'path': 'version_msg'}
        __cancel = {'identifyBy': 'id', 'path': 'version_cancel'}
        if self.driver.isElement("id", __version_msg):
            self.driver.click_element(identifyBy='id', path=__cancel)

    @catch_exception
    def allow_gps(self):
        # 获取定位权限弹窗
        __box = {'identifyBy': 'id', 'path': 'android:id/parentPanel'}
        __button = {'identifyBy': 'id', 'path': 'android:id/button1'}
        if self.driver.isElement(__box):
            self.driver.click_element(__button)

    @catch_exception
    def guide_page(self):
        # 首次安装引导页操作
        __guide = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/vp_guide'}
        __btn_enter = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/btn_enter'}
        if self.driver.isElement(__guide):
            self.driver.swipe_window(0.9, 0.5, 0.1, 0.5)
            time.sleep(0.5)
            self.driver.swipe_window(0.9, 0.5, 0.1, 0.5)
            time.sleep(0.5)
            self.driver.click_element(__btn_enter)

    @catch_exception
    def close_waybill_notice(self):
        __waybill_notice = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_notice'}
        __waybill_notice_close = {'identifyBy': 'id', 'path': 'com.luchang.lcgc:id/waybill_notice_close'}
        if self.driver.isElement(__waybill_notice):
            self.driver.click_element(__waybill_notice_close)
