from appium import webdriver
import time

packageName = 'com.mustang'
appActivity = '.account.SplashActivity'
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'ad6decf'
desired_caps['appPackage'] = packageName
desired_caps['appActivity'] = appActivity
desired_caps['fullReset'] = 'false'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['fastReset'] = 'false'
ANDROID_DEVICE_SOCKET = packageName + "_devtools_remote"
desired_caps['androidDeviceSocket'] = ANDROID_DEVICE_SOCKET
chromeOptions = {}
chromeOptions['androidDeviceSocket'] = ANDROID_DEVICE_SOCKET
desired_caps['chromeOptions'] = chromeOptions

# desired_caps['chromedriverExecutable'] = '/path/to/xwalkdriver64_xwalk_15'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)
driver.find_element_by_id('iv_ads_img').click()
print(driver.context)
time.sleep(8)
print(driver.context)
print(driver.current_context)
# driver.switch_to.context('WEBVIEW_com.mustang:tools')
# print(driver.window_handles)
# print(driver.page_source)
# driver.find_element_by_xpath('//*[@id="btnRecommend"]/div[1]').click()

time.sleep(2)
driver.quit()
