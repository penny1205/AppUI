#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.driver.project_decorator import catch_exception
from page_object.wuliuyun.wuliuyun import Wuliuyun


class SwipeScreen(Wuliuyun):
    @catch_exception
    def swipe_screen(self, element, activity):
        # 滑动屏幕直到指定的元素出现
        if self.driver.wait_activity(activity):
            self.log.info('start find the page:{0}'.format(activity))
            while not self.driver.isElement(element):
                self.driver.swipe_window(x1=0.5, y1=0.9, x2=0.5, y2=0.5)
            else:
                return
        else:
            self.log.error(
                'swipe page is wrong,the page activity is #{0}#,not #{1}#'.format(self.driver.get_activity(), activity))
            return
