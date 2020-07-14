from appium.webdriver.common.mobileby import MobileBy
from app.test_po_wework.pages.addresslistpage import AddressListPage
from app.test_po_wework.pages.basepage import BasePage


# 主页面
class Main(BasePage):
    _address_element = (MobileBy.XPATH, '//android.widget.TextView[@text="通讯录"]')

    # 方法：进入通讯录
    def goto_addresslist(self):
        # 点击通讯录
        self.find_and_click(self._address_element)
        return AddressListPage(self.driver)
