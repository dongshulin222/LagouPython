import pytest
import yaml
from selenium.webdriver.support.wait import WebDriverWait

from app.test_po_wework.pages.app import App

with open('../datas/contact.yaml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    addlist = datas['add']
    print(addlist)
    dellist = datas['del']


class TestWeWork:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize('username, gender, phone', addlist)
    def test_addcontact(self, username, gender, phone):
        # 添加联系人的业务逻辑
        toast = self.main.goto_addresslist().click_addmember().addmember_menual().edit_username(username) \
            .edit_gender(gender).edit_phone(phone).click_save().get_result()
        assert '添加成功' == toast
        # 返回首页or想要返回的页面
        self.main.back()

    @pytest.mark.parametrize('username', dellist)
    def test_delcontact(self, username):
        self.main.goto_addresslist().click_member(username).click_more().click_edit()\
            .delete_member()
        self.main.goto_addresslist().delmember_check(username)

    def teardown_class(self):
        self.app.close()
