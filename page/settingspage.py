from time import sleep

from page.basepage import BasePage


class Settings(BasePage):
    def logout(self,x,y):
        self.step("../data/settingspage.yaml", "logout")
        sleep(1)
        self.touch_tap(x,y)
        from page.loginpage import Login
        return Login(self.driver)
