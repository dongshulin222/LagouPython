from selenium.webdriver.common.by import By
from web.web_work.test_pgaeobject_work.pages.base_page import BasePage


class ContactPage(BasePage):
    def get_member(self):
        memberlist = []
        # find_elements返回的是一个list
        eles = self.finds(By.CSS_SELECTOR,
                          ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(5)")
        for ele in eles:
            memberlist.append(ele.get_attribute("title"))
            # 列表推导式的写法，含义与上述的for循环一致
            # memberlist = [ele.get_attribute("title") for ele in eles]
        return memberlist

