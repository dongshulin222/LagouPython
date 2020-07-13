import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.web_work.test_pgaeobject_work.pages.base_page import BasePage
from web.web_work.test_pgaeobject_work.pages.contact_page import ContactPage


class DeleteMemberPage(BasePage):
    _phone = "13701667140"

    def delete_member(self, _phone):
        contact = ContactPage()
        phonelist = contact.get_member()
        i = 1
        if self._phone in phonelist:
            for ele in phonelist:
                if self._phone == ele:
                    self.find(By.XPATH, "//*[@class='js_has_member']/table/tbody[2]/tr/td[1]").click()
                    self.find(By.CSS_SELECTOR,
                              "div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_delete").click()
                i = i + 1
            # 确定删除按钮出现
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]")))
            self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
            self.refresh()
        else:
            print("要删除的手机号在通讯录中不存在")


