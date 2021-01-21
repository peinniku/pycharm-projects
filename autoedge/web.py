from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions


# element = wd.find_element_by_id('kw')
# element.send_keys('神奇女侠1984')
#
# element = wd.find_element_by_id('su')
# element.click()
#
# element = wd.find_element_by_id('1')
# print(element.text)


# element = wd.find_element_by_css_selector('#wrapper:nth-child(4) #content_left>div:nth-child(2)>h3 a')
# element.click()


def switch_window(title, driver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if title in driver.title:
            return driver


# wd = switch_window('神奇女侠', wd)
#
# print(wd.title)

if __name__ == '__main__':
    # options = EdgeOptions()
    # options.add_argument("load-extension=C:/Users/10782/AppData/Local/Microsoft/Edge/User Data/Default")
    # wd = webdriver.Edge(options)
    # wd.implicitly_wait(10)
    #
    # main_window = wd.current_window_handle
    #
    # wd.get('https://hfut.yuketang.cn/pro/lms/83i7ZSNAWqB/4041808/studycontent')
    driver_url = 'C:/Users/10782/AppData/Local/Programs/Python/Python38/MicrosoftWebDriver.exe'

    options = EdgeOptions()
    options.use_chromium = True
    # options.add_extension(
    #     'C:/Users/10782/AppData/Local/Microsoft/Edge/User Data/Default/Extensions/bblkpdkdloalbiifhhmekiaejmdkgohj/1.0.7_0.crx')
    options.add_argument('user-data-dir=C:/Users/10782/AppData/Local/Microsoft/Edge/User Data')
    wd = Edge(options=options, executable_path=driver_url)

    wd.implicitly_wait(10)

    wd.get('https://hfut.yuketang.cn/pro/lms/83i7ZSNAWqB/4041808/studycontent')

# wd.quit()
