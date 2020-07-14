from appium import webdriver
from app.test_po_wework.pages.basepage import BasePage
from app.test_po_wework.pages.main import Main


# app.py 主要用于app的一些常用操作：启动app，关闭app，，进入app主页面
class App(BasePage):
    # 启动app
    def start(self):
        if self.driver is None:
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '6.0',
                'deviceName': "127.0.0.1:7555",
                'appPackage': "com.tencent.wework",
                'appActivity': ".launch.LaunchSplashActivity",
                'noReset': 'true'}
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            # 启动app，无需再与sever重新建立连接
            # launch_app方法启动的是desired_caps里定义的activity，无需传参数
            # start_activity可以给任何报名和页面名，就可以启动任何app的页面，需要传参数package和activity，可以做到不同APP间的切换
            # self.driver.start_activity('com.example', 'Activity')
            self.driver.launch_app()
        self.driver.implicitly_wait(5)
        return self

    # 重启app
    def restart(self):
        pass

    # 关闭app
    def close(self):
        self.driver.quit()

    # 进入app主页面
    def main(self):
        return Main(self.driver)
