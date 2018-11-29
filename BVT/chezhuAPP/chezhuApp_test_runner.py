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


def chezhuApp_case_runner():
    try:
        ### case suite ###
        register = RegisterDriverCaseSuite().case_suite_register()
        unregister = UnregisterDriverCaseSuit().case_suite_unregister()
        bvtcases = unittest.TestSuite((register, unregister))
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

if __name__ == '__main__':
    chezhuApp_case_runner()
