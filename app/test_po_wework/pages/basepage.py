from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

"""
basepage.py
用来存放一些最基本的操作
1.实例化driver对象
2.find方法
3.appium的底层操作
"""
class BasePage:
    # 定义driver类型
    driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 查找元素
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 滚动查找
    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true).\
                                        instance(0)).scrollIntoView(new UiSelector().\
                                        text("{text}").instance(0));')

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_toast(self):
        return self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    # 默认返回一次
    def back(self, num=1):
        for i in range(num):
            self.driver.back()