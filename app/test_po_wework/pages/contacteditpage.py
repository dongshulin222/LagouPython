from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.test_po_wework.pages.basepage import BasePage


class ContactEditPage(BasePage):
    _delmember_text = '删除成员'
    _delmember_xpath = '//*[@text="删除成员"]'
    _confirm_element = (MobileBy.XPATH, '//*[@text="确定"]')

    def delete_member(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self._delmember_xpath))
        # 滑动页面，点击删除成员
        self.find_by_scroll(self._delmember_text).click()
        # 点击确定
        self.find_and_click(self._confirm_element)
        from app.test_po_wework.pages.addresslistpage import AddressListPage
        return AddressListPage()


