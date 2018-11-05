#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import time
from selenium.common.exceptions import NoSuchElementException
from util.log.log import Log
from util.file.fileutil import FileUtil


class DriverOperation(object):
    def __init__(self, auto_driver):
        self.auto_driver = auto_driver
        self.log = Log()

    def get_activity(self):
        return self.auto_driver.current_activity

    def find_element(self, element):
        # 返回元素
        identifyBy = element['identifyBy']
        path = element['path']
        if self.isElement(element):
            if identifyBy == 'id':
                return self.auto_driver.find_element_by_id(path)
            elif identifyBy == 'name':
                return self.auto_driver.find_element_by_name(path)
            elif identifyBy == 'class':
                return self.auto_driver.find_element_by_class_name(path)
            elif identifyBy == 'xpath':
                return self.auto_driver.find_element_by_xpath(path)
            elif identifyBy == 'ids':
                return self.auto_driver.find_elements_by_id(path[0])[path[1]]
        else:
            self.log.error('Can not find the element by  ' + path)
            return None

    def click_element(self, element):
        # Android 点击按钮
        identifyBy = element['identifyBy']
        path = element['path']
        if self.isElement(element):
            if identifyBy == 'id':
                return self.auto_driver.find_element_by_id(path).click()
            elif identifyBy == 'name':
                return self.auto_driver.find_element_by_name(path).click()
            elif identifyBy == 'class':
                return self.auto_driver.find_element_by_class_name(path).click()
            elif identifyBy == 'xpath':
                return self.auto_driver.find_element_by_xpath(path).click()
            elif identifyBy == 'ids':
                return self.auto_driver.find_elements_by_id(path[0])[path[1]].click()
        else:
            self.log.error('Can not find the element by  ' + path)
            return None

    def send_keys(self, element):
        # Android 输入字符
        identifyBy = element['identifyBy']
        path = element['path']
        keys = element['keys']
        if self.isElement(element):
            if identifyBy == 'id':
                return self.auto_driver.find_element_by_id(path).send_keys(keys)
            elif identifyBy == 'name':
                return self.auto_driver.find_element_by_name(path).send_keys(keys)
            elif identifyBy == 'class':
                return self.auto_driver.find_element_by_class_name(path).send_keys(keys)
            elif identifyBy == 'xpath':
                return self.auto_driver.find_element_by_xpath(path).send_keys(keys)
            elif identifyBy == 'ids':
                # path使用列表进行传参，[path,id]
                return self.auto_driver.find_elements_by_id(path[0])[path[1]].send_keys(keys)
            elif identifyBy == 'xpaths':
                # path使用列表进行传参，[path,id]
                return self.auto_driver.find_elements_by_xpath(path[0])[path[1]].send_keys(keys)
        else:
            self.log.error('Can not find the element by  ' + path)
            return None

    def click_by_coordinate(self, positions, duration=None):
        """Taps on an particular place with up to five fingers, holding for a
                certain time

                :Args:
                 - positions - an array of list representing the x/y coordinates of
                 the fingers to tap. Length can be up to five.
                 - duration - (optional) length of time to tap, in ms

                :Usage:
                    driver.click_by_coordinate([[100, 20], [100, 60], [100, 100]], 500)
                """
        width = self.auto_driver.get_window_size()['width']
        height = self.auto_driver.get_window_size()['height']
        for position in positions:
            position[0] = int(position[0] * width)
            position[1] = int(position[1] * height)
        self.auto_driver.tap(positions, duration)

    def swipe_window(self, x1, y1, x2, y2, t=1000):
        # 屏幕左上角相对位置：x=0, y=0  右下角相对位置：x=1, y=1
        width = self.auto_driver.get_window_size()['width']
        height = self.auto_driver.get_window_size()['height']
        x1 = int(width * x1)
        y1 = int(height * y1)
        x2 = int(width * x2)
        y2 = int(height * y2)
        return self.auto_driver.swipe(x1, y1, x2, y2, duration=t)

    def wait_activity(self, activity, timeout=20):
        return self.auto_driver.wait_activity(activity=activity, timeout=timeout)

    def quit(self):
        return self.auto_driver.quit()

    def isElement(self, element):
        """
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        """
        identifyBy = element['identifyBy']
        path = element['path']
        flag = None
        try:
            if identifyBy == "id":
                self.auto_driver.find_element_by_id(path)
            elif identifyBy == "xpath":
                self.auto_driver.find_element_by_xpath(path)
            elif identifyBy == "class":
                self.auto_driver.find_element_by_class_name(path)
            elif identifyBy == "link text":
                self.auto_driver.find_element_by_link_text(path)
            elif identifyBy == "partial link text":
                self.auto_driver.find_element_by_partial_link_text(path)
            elif identifyBy == "name":
                self.auto_driver.find_element_by_name(path)
            elif identifyBy == "tag name":
                self.auto_driver.find_element_by_tag_name(path)
            elif identifyBy == "css selector":
                self.auto_driver.find_element_by_css_selector(path)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag

    def getScreenShot(self, name=''):
        try:
            tamp = time.strftime('%m%d-%H-%M-%S')
            filename = FileUtil.getProjectObsPath() + '/log/screenshot/{0}_{1}.png'.format(name, tamp)
            self.auto_driver.get_screenshot_as_file(filename)
        except Exception as error:
            self.log.error(error)
        return


