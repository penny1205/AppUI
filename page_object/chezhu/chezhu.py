#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.driver.driver_operation import DriverOperation


class CheZhu(object):
    def __init__(self, driver):
        self.log = Log()
        self.app_driver = driver
        self.driver = DriverOperation(driver)
