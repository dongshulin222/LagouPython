from appium.webdriver.common.mobileby import MobileBy
from app.test_po_wework.pages.basepage import BasePage


# 添加成员页面
class MemberInvitePage(BasePage):
    _addmember_menual_element = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    # 手动添加成员
    def addmember_menual(self):
        # 点击手动添加成员
        self.find_and_click(self._addmember_menual_element)
        # alt+回车。locally局部导入，在调用时导入，这样循环导入就不会报错，python默认不支持循环导入
        # 循环导入：MemberInvitePage类导入ContactAddPage()方法。ContactAddPage类导入MemberInvitePage()方法
        from app.test_po_wework.pages.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)


    # 获取返回值
    def get_result(self):
        toasttext = self.get_toast()
        return toasttext

