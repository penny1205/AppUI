#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log


def catch_exception(origin_func):
    def wrapper(self, *args, **kwargs):
        try:
            u = origin_func(self, *args, **kwargs)
            return u
        except Exception as e:
            Log().error(e)
            self.driver.quit()
            raise
    return wrapper
