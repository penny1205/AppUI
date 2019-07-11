#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.report.reporting import ReportUtil
from util.mail.sendmail import SendMail
import time
from BVT.chezhuAPP.driver_register.register_driver_suit import RegisterDriverCaseSuite
from BVT.chezhuAPP.driver_unregister.unregister_driver_case_suit import UnregisterDriverCaseSuit
from util.driver.driver import AppUiDriver
import unittest
from BVT.wuliuyunAPP.wuliuyun_case_suit import WuliuyunCaseSuit


def get_case_suit():
    wuliuyun_case = WuliuyunCaseSuit().case_suite()
    chezhu_register = RegisterDriverCaseSuite().case_suite_register()
    chezhu_unregister = UnregisterDriverCaseSuit().case_suite_unregister()
    bvtcases = unittest.TestSuite((chezhu_unregister, chezhu_register, wuliuyun_case))
    print(bvtcases)
    return bvtcases


def chezhuApp_case_runner():
    try:
        ### case suite ###
        # register = RegisterDriverCaseSuite().case_suite_register()
        # unregister = UnregisterDriverCaseSuit().case_suite_unregister()
        # bvtcases = unittest.TestSuite((register, unregister))
        wuliuyun_case = WuliuyunCaseSuit().case_suite()
        chezhu_register = RegisterDriverCaseSuite().case_suite_register()
        chezhu_unregister = UnregisterDriverCaseSuit().case_suite_unregister()
        bvtcases = unittest.TestSuite((chezhu_unregister, chezhu_register, wuliuyun_case))
        print(bvtcases)
        ### driver ###
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

        ### run case ###
        ReportUtil().generate_report(bvtcases, config['email_title'] + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'qa testing report', FileUtil.getProjectObsPath() + '/report/report.html')
        reader = open(FileUtil.getProjectObsPath() + '/report/report_chezhu.html', 'rb')
        mail_body = reader.read()
        reader.close()
        SendMail().send_mail(config['email_receiver'], config['email_sender'], config['email_sender_pwd'],
                             config['email_host'], config['email_title'] +
                             time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), mail_body,
                             {FileUtil.getProjectObsPath() + '/report/report_chezhu.html'})
        print('BvtCase run success!')
    except Exception:
        print('BvtCase run fail!')
        raise


def run_case_suit(case_suit):
    try:
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        app_package = config['appPackage_chezhu']
        app_activity = config['appActivity_chezhu']
        AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

        ### run case ###
        ReportUtil().generate_report(case_suit, config['email_title'] + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                     time.localtime(time.time())),
                                     'qa testing report', FileUtil.getProjectObsPath() + '/report/report.html')
        reader = open(FileUtil.getProjectObsPath() + '/report/report.html', 'rb')
        mail_body = reader.read()
        reader.close()
        SendMail().send_mail(config['email_receiver'], config['email_sender'], config['email_sender_pwd'],
                             config['email_host'], config['email_title'] +
                             time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), mail_body,
                             {FileUtil.getProjectObsPath() + '/report/report.html'})
        print('BvtCase run success!')

    except Exception:
        print('BvtCase run fail!')
        raise

if __name__ == '__main__':
    case_suit = get_case_suit()
    run_case_suit(case_suit)
