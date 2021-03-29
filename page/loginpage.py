from page.basepage import BasePage
from page.indexpage import Index


class Login(BasePage):

    def username(self,username):
        self._params["user"] = username
        self.step("../data/loginpage.yaml", "username")
        return self

    def password(self,password):
        self._params["psd"] = password
        self.step("../data/loginpage.yaml", "password")
        return self

    def remember_password(self):
        self.step("../data/loginpage.yaml", "remember_password")
        return self

    def save_click(self):
        self.step("../data/loginpage.yaml", "save_click")
        return Index(self.driver)
