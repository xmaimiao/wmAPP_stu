from page.basepage import BasePage


class LessonDetails(BasePage):

    def switch_to_window(self):
        '''
        切換到新窗口
        :return:
        '''
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return self

    def get_lesson_type(self):
        '''
        獲取課程類型
        :return:
        '''
        return self.step("../data/classtimetable/lessondetails.yaml","get_lesson_type")

    def get_lesson_room(self):
        '''
        獲取課程課室
        :return:
        '''
        return self.step("../data/classtimetable/lessondetails.yaml","get_lesson_room")

    def get_last_sign_record_toast(self):
        '''
        獲取最近一次簽到記錄，補簽的toast
        :return:
        '''
        try:
            return str(self.step("../data/classtimetable/lessondetails.yaml", "get_last_sign_record_toast"))
        except Exception as e:
            raise ValueError("最後一條記錄非補簽")

    def get_last_sign_record(self):
        '''
        獲取最近一次簽到記錄時間
        :return:
        '''
        return str(self.step("../data/classtimetable/lessondetails.yaml", "get_last_sign_record"))
