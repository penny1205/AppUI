#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
import unittest
from BVT.wuliuyunAPP.test_login import TestLogin
from BVT.wuliuyunAPP.test_logout import TestLogout
from util.unittest.unittestutil import UnitTestUtil
from util.driver.driver import AppUiDriver


class WuliuyunCaseSuit(object):
    # 物流云APP-BVT自动化case集合
    def __init__(self):
        self.logger = Log()
        # config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # app_package = config['appPackage_wuliuyun']
        # app_activity = config['appActivity_wuliuyun']
        # AppUiDriver(appPackage=app_package, appActivity=app_activity).app_ui_driver()

    def case_suite(self):
        test_suite = unittest.makeSuite(TestLogin)
        test_suite.addTest(
            UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/BVT/wuliuyunAPP/test_case', 'test*.py'))
        test_suite.addTest(unittest.makeSuite(TestLogout))
        # print(test_suite)
        return test_suite


if __name__ == '__main__':
    from util.report.reporting import ReportUtil
    from util.mail.sendmail import SendMail
    import time
    try:
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        bvtcases = WuliuyunCaseSuit().case_suite()

        ReportUtil().generate_report(bvtcases, config['email_title'] + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'qa testing report', FileUtil.getProjectObsPath() + '/report/report.html')
        reader = open(FileUtil.getProjectObsPath() + '/report/report_wuliuyun.html', 'rb')
        mail_body = reader.read()
        reader.close()
        SendMail().send_mail(config['email_receiver'], config['email_sender'], config['email_sender_pwd'],
                             config['email_host'], config['email_title'] +
                             time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), mail_body,
                             {FileUtil.getProjectObsPath() + '/report/report_wuliuyun.html'})
        print('BvtCase run success!')
    except Exception:
        print('BvtCase run fail!')
        raise
