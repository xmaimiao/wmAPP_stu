import time
import yaml
from page.app import App
import pytest

with open("../data/test_classtimetable.yaml",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    test_today_term_datas = datas["test_today_term"]
    memu_person = datas["memu_person"]
    logout_datas = datas["logout_datas"]
    test_course_type_or_status_datas = datas["test_course_type_or_status"]

class TestClassTimeTable:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.login = self.app.start().goto_login()

    def teardown(self):
        self.app.back_to_index().\
            goto_index().\
            goto_person_info(memu_person).\
            goto_settings().\
            logout(logout_datas["logout_x"],logout_datas["logout_y"])

    @pytest.mark.parametrize("data", test_today_term_datas)
    def test_today_term(self,data):
        '''
        校驗today對應的學期正確性
        '''
        result = self.login. \
            username(data["username"]).\
            password(data["password"]). \
            remember_password().save_click(). \
            goto_class_timetable(data["class_x"],data["class_y"]).\
            switch_to_window().\
            click_today().\
            get_term()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", test_today_term_datas)
    def test_current_week(self,data):
        '''
        校驗打開課表定位當前週
        '''
        result = self.login. \
            username(data["username"]).\
            password(data["password"]). \
            remember_password().save_click(). \
            goto_class_timetable(data["class_x"],data["class_y"]).\
            switch_to_window().\
            get_current_day()
        assert time.strftime('%m/%d',time.localtime(time.time())) in result

    @pytest.mark.parametrize("data", test_course_type_or_status_datas)
    def test_course_type_or_status(self, data):
        '''
        校驗list頁，指定科目的類型為雲課堂/網課
        '''
        result = self.login. \
            username(data["username"]).\
            password(data["password"]). \
            remember_password().save_click(). \
            goto_class_timetable(data["class_x"], data["class_y"]). \
            switch_to_context(). \
            goto_studentcourses(). \
            get_course_type_or_status(data["course_code"])
        assert data["expect"] == result