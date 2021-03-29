import yaml
from page.app import App
import pytest

with open("../data/test_login.yaml",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    test_login_datas = datas["test_login"]

class TestLogin:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.login = self.app.start().goto_login()

    def teardown(self):
        self.app.goto_index().\
            goto_person_info("我的").\
            goto_settings().\
            logout()


    @pytest.mark.parametrize("data",test_login_datas)
    def test_login(self,data):
        '''
        登錄，填寫賬號密碼
        :return:
        '''
        self.login.\
            username(data["username"]).password(data["password"]).\
            remember_password().save_click().\
            goto_class_timetable("課表").back_to_index()

