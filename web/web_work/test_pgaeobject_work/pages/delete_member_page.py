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
        # 可以使用另一种方式，获取姓名，再获取姓名的父节点，再通过父节点去过去删除按钮
        if self._phone in phonelist:
            self.find(By.XPATH, f"//*[@title='{self._phone}']/../td[1]").click()
            # 确定删除按钮出现
            delete_locator = (By.XPATH, "//*[@class='js_has_member']/div[9]/a[3]")
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(delete_locator))
            self.find(*delete_locator).click()
            confirm_locator = (By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a")
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(confirm_locator))
            self.find(*confirm_locator).click()
            self.refresh()
        else:
            print("要删除的手机号在通讯录中不存在")


