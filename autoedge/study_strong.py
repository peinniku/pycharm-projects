from time import sleep

from selenium import webdriver


def switch_window(title, driver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if title in driver.title:
            return driver


def switch_window_ex(title, driver, main):
    for handle in driver.window_handles:
        if handle == main:
            continue
        driver.switch_to.window(handle)
        if title in driver.title:
            return driver


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument(r'user-data-dir=C:\Users\10782\AppData\Local\Google\Chrome\User Data')
    wd = webdriver.Chrome(options=option)
    wd.implicitly_wait(5)

    wd.get('https://www.xuexi.cn/')
    main_handle = wd.current_window_handle

    wd.find_element_by_xpath("//*[text()='我的积分']").click()
    wd = switch_window('我的积分', wd)
    wd.execute_script("window.scrollBy(0, 700)")
    wd.switch_to_window(main_handle)
    # wd.find_element_by_xpath("//*[@class='my-points-card'][2]//div[@class='buttonbox']").click()  # 文章

    # 文章
    wd.find_element_by_xpath("//div[@class='menu-row'][1]//a[3]").click()
    wd.close()
    wd = switch_window('学习强国', wd)

    article_window = wd.current_window_handle

    for i in range(1, 7):
        wd.find_element_by_xpath("//section[@data-data-id='textListGrid']//div[@class='grid-cell'][{}]".format(i)).click()
        wd = switch_window_ex('学习强国', wd, article_window)
        sleep(1)
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(65)
        wd.close()



    # 视频
    wd = switch_window('学习强国', wd)
    wd.find_element_by_xpath("//div[@class='menu-row'][2]//a[3]").click()
    wd.close()
    wd = switch_window('学习强国', wd)
    # wd.execute_script("window.scrollBy(0, 700)")
    # wd.find_element_by_xpath("//span[contains(text(),'第一频道')]").click()
    # wd.close()
    # wd = switch_window('学习强国', wd)

    video_window = wd.current_window_handle

    wd.find_element_by_xpath("//div[@class='grid-gr'][1]/div[1]").click()
    wd = switch_window_ex('学习强国', wd, video_window)
    wd.execute_script("window.scrollBy(0, 500)")
    sleep(65)

    for i in range(2,7):
        wd.find_element_by_xpath("//div[@class='video-article-content-video-list']//li[{}]".format(i)).click()
        sleep(65)

    wd = switch_window('我的积分', wd)
    wd.find_element_by_xpath("//div[@class='my-points-card'][5]//div[@class='buttonbox']").click()
    sleep(1)
    wd.execute_script("window.scrollBy(0, 400)")

    for i in range(5):

        wd.find_element_by_xpath("//span[contains(text(),'查看提示')]").click()
        answer = wd.find_element_by_xpath("//font").text
        answer.replace('，', '，')
        sleep(1)
        wd.find_element_by_xpath("//span[contains(text(),'查看提示')]").click()

        q_type = wd.find_element_by_xpath("//div[@class='q-header']").text
        if q_type == '填空题':
            wd.find_element_by_xpath("//input[@type='text']").send_keys(answer)
        elif q_type == '单选题':
            if wd.find_elements_by_xpath("//div[@class='q-answer choosable'][contains(string(),'正确')]"):
                if 'A' in answer:
                    wd.find_element_by_xpath("//div[contains(text(),'A')]").click()
                elif 'B' in answer:
                    wd.find_element_by_xpath("//div[contains(text(),'B')]").click()
                elif '不' in answer:
                    wd.find_element_by_xpath("//div[contains(text(),'B')]")
                elif wd.find_elements_by_xpath("//div[contains(text(),'{}')]".format(answer)):
                    wd.find_element_by_xpath("//div[contains(text(),'A')]").click()
                else:
                    wd.find_element_by_xpath("//div[contains(text(),'B')]").click()
                input('>')
            else:
                wd.find_element_by_xpath(
                    "//div[contains(string(),'{}')][@class='q-answer choosable']".format(answer)).click()
        elif q_type == '多选题':
            answers = wd.find_elements_by_xpath("//font")
            for s_an in answers:
                wd.find_element_by_xpath(
                    "//div[contains(string(),'{}')][@class='q-answer choosable']".format(s_an.text)).click()

        wd.find_element_by_xpath("//button").click()

    # wd.close()

    # wd.find_element_by_xpath("//div[@class='grid-gr'][1]/div[1]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()
    #
    # wd = switch_window('学习强国', wd)
    # wd.find_element_by_xpath("//div[@class='grid-gr'][1]/div[2]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()
    #
    # wd = switch_window('学习强国', wd)
    # wd.find_element_by_xpath("//div[@class='grid-gr'][1]/div[3]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()
    #
    # wd = switch_window('学习强国', wd)
    # wd.find_element_by_xpath("//div[@class='grid-gr'][1]/div[4]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()
    #
    # wd = switch_window('学习强国', wd)
    # wd.find_element_by_xpath("//div[@class='grid-gr'][2]/div[1]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()
    #
    # wd = switch_window('学习强国', wd)
    # wd.find_element_by_xpath("//div[@class='grid-gr'][2]/div[2]").click()
    # wd = switch_window_ex('学习强国', wd, video_window)
    # sleep(65)
    # wd.close()

    input('>')
    wd.quit()
