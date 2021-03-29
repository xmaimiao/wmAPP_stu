from appium import webdriver
from page.basepage import BasePage
from page.indexpage import Index
from page.loginpage import Login


class App(BasePage):
    # dev
    # _package = 'cn.doocom.wemustcampusbeta'
    # uat
    _package = 'cn.doocom.wemustcampusuat'
    _activity = 'cn.doocom.wemustcampus.mvp.ui.activity.SplashActivity'

    def start(self):
        '''
        启动APP
        :return:
        '''
        if self.driver == None:
            caps = dict()
            caps["platformName"] = 'Android'
            caps["deviceName"] = '127.0.0.1:7555'
            caps["platformVersion"] = '6.0.1'
            caps["appPackage"] = self._package
            caps["automationName"] = 'uiautomator2'
            caps["appActivity"] = self._activity
            caps["noReset"] = 'true'
            # 启动之前不关闭APP
            caps["dontStopAppOnReset"] = 'true'
            # caps["skipDeviceInitializati"] = 'true'
            caps["chromedriverExecutable"] = 'C:\Program Files (x86)\Appium\chromedriver2.20.exe'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.start_activity(self._package,self._activity)
        self.set_implicitly_wait(3)
        return self

    def stop(self):
        '''
        停止APP
        :return:
        '''
        self.driver.quit()

    def restart(self):
        '''
        重启APP
        :return:
        '''
        self.driver.close()
        # 启动应用
        self.driver.launch_app()
        return self

    def close(self):
        '''
        關閉當前頁面
        :return:
        '''

    def goto_login(self):
        '''
        进入登錄頁，此頁面是webview，且正確的登錄窗口是-2
        :return:
        '''
        return Login(self.driver)

    def goto_index(self):
        '''
        進入首頁
        :return:
        '''
        return Index(self.driver)

    def back_to_index(self):
        '''
        切回原生
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[0])
        return self




