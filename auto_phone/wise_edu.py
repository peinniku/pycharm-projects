from time import sleep
import os
import pyautogui

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.wisedu.cpdaily',  # 启动APP Package名称
    'appActivity': 'com.wisorg.wisedu.home.ui.HomeActivity',  # 启动Activity名称
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
    app_dir = r'C:\Users\10782\AppData\Local\Programs\Appium\Appium.exe'  # 指定应用程序目录
    open_app(app_dir)

    sleep(20)

    pyautogui.click(x=949, y=663)

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 设置缺省等待时间
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                 '.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget'
                                 '.LinearLayout/android.widget.RelativeLayout['
                                 '4]/android.widget.LinearLayout/android.widget.ImageView').click()
    driver.find_element_by_xpath("//*[@text='辅导员通知']").click()
    driver.find_element_by_xpath(
        "//*[contains(@text,'今天')]/following-sibling::android.widget.FrameLayout//*[@text='重要收集']").click()

    driver.find_element_by_xpath("//*[@text='是，已报到']").click()
    driver.find_element_by_xpath("//*[@text='否']").click()

    swipeUp(driver)

    driver.find_element_by_xpath("//*[@text='否，一直在校']").click()
    driver.find_element_by_xpath("//*[@text='无']").click()

    swipeUp(driver)

    driver.find_element_by_xpath("//*[@text='无'][@index='20']").click()

    swipeUp(driver)

    driver.find_element_by_xpath("//*[@index='22']").click()
    sleep(1)
    swipeUp(driver, n=1, s1=0.95, s2=0.65)
    driver.find_element_by_xpath("//*[@text='安徽省']").click()
    # 确定
    driver.find_element_by_xpath("//*[@text='确认']").click()

    driver.find_element_by_xpath("//*[@index='24']").click()
    driver.find_element_by_xpath("//*[@text='合肥市']").click()
    driver.find_element_by_xpath("//*[@text='确认']").click()

    driver.find_element_by_xpath("//*[@index='26']").click()
    # swipeUp(driver,s1,s2)
    driver.find_element_by_xpath("//*[@text='蜀山区']").click()
    # 确定
    driver.find_element_by_xpath("//*[@text='确认']").click()

    swipeUp(driver)

    driver.find_element_by_xpath("//*[contains(@text,'且填写信息无误')]").click()
    #input('检查')
    driver.find_element_by_xpath("//*[contains(@text,'提交')]").click()
    driver.find_element_by_xpath("//*[@text='提交']").click()

    sleep(2)

    #input('按回车退出')
    driver.quit()

    pyautogui.click(x=1325, y=159)
