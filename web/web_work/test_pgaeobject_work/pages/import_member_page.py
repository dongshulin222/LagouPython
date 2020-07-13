import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web.web_work.test_pgaeobject_work.pages.base_page import BasePage
from web.web_work.test_pgaeobject_work.pages.contact_page import ContactPage


class ImportMemberPage(BasePage):
    def import_member(self):
        self.find(By.ID, "js_upload_file_input").send_keys(
            r"D:\study\lagou\LagouPython\web\web_work\test_pgaeobject_work\memberlist.xlsx")
        # 确定提交按钮出现
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.ID, "submit_csv")))
        self.find(By.ID, "submit_csv").click()
        # 确定返回通讯录按钮出现
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.ID, "reloadContact")))
        self.find(By.ID, "reloadContact").click()
        return ContactPage()


