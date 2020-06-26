from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 复用chrome，多用于调试
class TestLogin:
    def test_debug_login(self):
        option = Options()
        # chrome --remote-debugging-port=9222
        # 需要和启动命令的端口号一致
        # 指定了一个调试地址
        option.debugger_address = "localhost:9222"
        # 把自定的调试参数传入webdriver
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")