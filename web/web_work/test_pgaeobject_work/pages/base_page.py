from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# BasePage定义：它是一个其他page的公共方法的封装，它是一个底层使用的框架
class BasePage:
    # 定义类变量
    _base_url = ""

    # 复写init方法
    def __init__(self, driver_basepage: WebDriver = None):
        # 若入参driver_basepage为空
        if driver_basepage == None:
            option = Options()
            # chrome --remote-debugging-port=9222
            # 需要和启动命令的端口号一致
            # 指定了一个调试地址
            option.debugger_address = "localhost:9222"
            # 把自定的调试参数传入webdriver
            self.driver = webdriver.Chrome(options=option)
        else:
            # 否则的话使用传入的driver类型打开响应的浏览器
            self.driver = driver_basepage

        # 若变量_base_url不为空
        if self._base_url != "":
            # 打开浏览器且地址为_base_url
            self.driver.get(self._base_url)
        # 隐式等待3秒
        self.driver.implicitly_wait(3)

    # 封装获取元素方法
    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    # 封装获取列表方法
    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    # 封装退出webdriver方法
    def quit(self):
        return self.driver.quit()

    # 页面重新刷新
    def refresh(self):
        return self.driver.refresh()
