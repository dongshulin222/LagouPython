from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from app.test_po_wework.pages.basepage import BasePage
from app.test_po_wework.pages.memberinvitepage import MemberInvitePage


# 通讯录页面
class AddressListPage(BasePage):
    _addmember_text = '添加成员'

    # 点击添加成员
    def click_addmember(self):
        # 滚动页面，点击添加成员
        self.find_by_scroll(self._addmember_text).click()
        return MemberInvitePage(self.driver)

    # adb shell "dumpsys window|grep mCurrent"  -可通过此命令获取当前页面的名字
    # 点击成员
    def click_member(self, username):
        self.find_by_scroll(username).click()
        from app.test_po_wework.pages.contactdetailpage import ContactDetailPage
        return ContactDetailPage(self.driver)

    def delmember_check(self, username):
        user_xpath = f'//*[@text="{username}"]'
        # 验证删除成功,通过显示等待，判断一个元素消失
        WebDriverWait(self.driver, 10).until_not(lambda x: x.find_element_by_xpath(user_xpath))
