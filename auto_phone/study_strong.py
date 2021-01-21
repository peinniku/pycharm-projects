from time import sleep
import os
import pyautogui

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'cn.xuexi.android',  # 启动APP Package名称
    'appActivity': 'com.alibaba.android.rimet.biz.SplashActivity',  # 启动Activity名称
    'unicodeKeyboard': False,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}


def open_app(app_dir):
    os.startfile(app_dir)  # os.startfile（）打开外部应该程序，与windows双击相同
    return True


def swipeUp(driver, t=500, n=1, s1=0.75, s2=0.45):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * s1
    y2 = l['height'] * s2
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


if __name__ == "__main__":
    # app_dir = r'C:\Users\10782\AppData\Local\Programs\Appium\Appium.exe'  # 指定应用程序目录
    # open_app(app_dir)

    # sleep(20)
    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 设置缺省等待时间
    driver.implicitly_wait(5)

    driver.find_element_by_xpath("//*[@text='我的']").click()
    driver.find_element_by_xpath("//*[@text='学习积分']").click()

    notice=driver.find_elements_by_xpath("//*[@text='好的，知道了']")
    if notice:
        notice[0].click()
