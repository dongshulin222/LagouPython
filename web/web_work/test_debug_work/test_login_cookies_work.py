import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginCookies:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    # 此方法在cookie有效期内只需执行一次即可，获取后在有效期内都无需再获取，可直接使用
    # @pytest.mark.skip
    def test_get_cookie(self):
        # 一定要在扫码登录之后，再执行获取cookies
        cookies = self.driver.get_cookies()
        # 把获取的cookie放在一个文件中，方便之后读取cookie
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        # 获取之前保存的cookie信息
        cookies = json.load(open("cookie.json"))
        # 添加一个dict的cookie信息，把cookie键值对，一个一个添加到浏览器
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 如果刷新页面后，“menu_index”按钮可以点击，则表示登录成功且页面已刷新，即可进行之后的操作
        while True:
            # 刷新页面
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.ID, "menu_index")))
            if res is not None:
                break

    def teardown(self):
        self.driver.quit()