from appium.webdriver.common.mobileby import MobileBy
from app.test_po_wework.pages.basepage import BasePage


# 成员编辑页
class ContactAddPage(BasePage):
    _username_element = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    _gender_element = (MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]')
    _phone_element = (MobileBy.XPATH, '//*[contains(@text, "手机号")]/..//*[@text="手机号"]')
    _save_btn_element = (MobileBy.XPATH, '//*[@text="保存"]')

    # 编辑用户名
    def edit_username(self, username):
        # 输入姓名
        self.find_and_sendkeys(self._username_element, username)
        return self

    # 编辑性别
    def edit_gender(self, gender):
        # 因为text=男，与text=性别，不在同一个父节点下，所以要用//去寻找，若在同一个父节点下，则只需要使用/去寻找
        self.find_and_click(self._gender_element)
        # 设置性别
        _female_male_element = (MobileBy.XPATH, f'//*[@text="{gender}"]')
        if gender == '女':
            self.find_and_click(self._female_male_element)
        else:
            self.find_and_click(self._female_male_element)
        return self

    # 编辑手机号
    def edit_phone(self, phone):
        # 输入手机号
        self.find_and_sendkeys(self._phone_element, phone)
        return self

    # 点击保存
    def click_save(self):
        # 点击保存
        self.find_and_click(self._save_btn_element)
        from app.test_po_wework.pages.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self.driver)
