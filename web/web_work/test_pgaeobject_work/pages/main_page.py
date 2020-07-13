from selenium.webdriver.common.by import By
from web.web_work.test_pgaeobject_work.pages.base_page import BasePage
from web.web_work.test_pgaeobject_work.pages.delete_member_page import DeleteMemberPage
from web.web_work.test_pgaeobject_work.pages.import_member_page import ImportMemberPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_delete_member(self):
        self.find(By.ID, "menu_contacts").click()
        return DeleteMemberPage()

    def goto_import_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportMemberPage()
