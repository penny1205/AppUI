#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.beautifulReport.BeautifulReport import BeautifulReport
from BVT.chezhuAPP.driver_register.register_driver_suit import RegisterDriverCaseSuite
from BVT.chezhuAPP.driver_unregister.unregister_driver_case_suit import UnregisterDriverCaseSuit
from util.driver.driver import AppUiDriver
import unittest
from BVT.wuliuyunAPP.wuliuyun_case_suit import WuliuyunCaseSuit


def get_case_suite():
    # wuliuyun_case = WuliuyunCaseSuit().case_suite()
    # chezhu_register = RegisterDriverCaseSuite().case_suite_register()
    chezhu_unregister = UnregisterDriverCaseSuit().case_suite_unregister()
    # bvtcases = unittest.TestSuite((chezhu_unregister, chezhu_register, wuliuyun_case))
    # print(bvtcases)
    # return bvtcases
    return chezhu_unregister


def run_case_suite(case_suite):
    result = BeautifulReport(case_suite)
    result.report(filename='ui_aotu_test', description='APP-UI-自动化测试报告', log_path='E:/AppUI/report/beautiful_report')


if __name__ == '__main__':
    config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
    app_package = config['appPackage_chezhu']
    app_activity = config['appActivity_chezhu']
    AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()
    case_suite = get_case_suite()
    run_case_suite(case_suite)
