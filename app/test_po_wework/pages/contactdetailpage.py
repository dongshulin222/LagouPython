from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.test_po_wework.pages.basepage import BasePage
from app.test_po_wework.pages.contacteditpage import ContactEditPage


# 个人信息页面
class ContactDetailPage(BasePage):

    _more_element = (MobileBy.ID, 'com.tencent.wework:id/h9p')
    _more_xpath = 'com.tencent.wework:id/h9p'
    _edit_element = (MobileBy.XPATH, '//*[@text="编辑成员"]')
    _edit_xpath = '//*[@text="编辑成员"]'

    # 点右上角
    def click_more(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self._more_xpath))
        sleep(5)
        self.find_and_click(self._more_element)
        return self

    # 点编辑成员
    def click_edit(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self._edit_xpath))
        self.find_and_click(self._edit_element)
        return ContactEditPage(self.driver)

