#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from appium import webdriver
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class AppUiDriver(object):
    def __init__(self, appPackage, appActivity, appium_port=4723):
        self.log = Log()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.desired_caps = {}
        self.desired_caps['platformName'] = config['platformName']
        self.desired_caps['platformVersion'] = config['platformVersion']
        self.desired_caps['deviceName'] = config['deviceName']
        # self.desired_caps['app'] = 'E:/py_web/appium/kjwuliuyun-3.4.7-debug-feature-3.4.apk'
        self.desired_caps['noReset'] = True
        self.desired_caps['unicodeKeyboard'] = True
        # self.desired_caps['resetKeyboard'] = True
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.appium_port = appium_port

    def app_ui_driver(self):
        try:
            self.desired_caps['appPackage'] = self.appPackage
            self.desired_caps['appActivity'] = self.appActivity
            global driver
            driver = webdriver.Remote('http://localhost:%d/wd/hub' % self.appium_port, self.desired_caps)
            self.log.info('Successful device connection.')
            driver.implicitly_wait(10)
        except Exception as err:
            self.log.error('Failed device connection...')
            self.log.error(err)
            raise

    def get_driver(self):
        return driver


if __name__ == '__main__':
    driver = AppUiDriver(appPackage='com.mustang', appActivity='.account.SplashActivity').app_ui_driver()
    driver.start_activity()
    print(driver.current_activity)
