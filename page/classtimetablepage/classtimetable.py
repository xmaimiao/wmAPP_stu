from page.basepage import BasePage
from page.classtimetablepage.lessondetails import LessonDetails
from page.classtimetablepage.studentcourses import StudentCourses


class ClassTimeTable(BasePage):

    def switch_to_context(self):
        '''
        切換上下文
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[-1])
        return self

    def click_today(self):
        '''
        點擊“今天”，校驗對應學期
        '''
        self.step("../data/classtimetable/classtimetable.yaml", "click_today")
        return self

    def get_term(self):
        '''
        獲取當前學期
        '''
        return self.step("../data/classtimetable/classtimetable.yaml", "get_term")

    def get_current_day(self):
        '''
        確認課表定位當前日期（周）
        :return:
        '''
        return self.driver.page_source

    def goto_studentcourses(self):
        '''
        打開科目總覽頁面
        :return:
        '''
        self.step("../data/classtimetable/classtimetable.yaml", "goto_studentcourses")
        return StudentCourses(self.driver)

    def goto_lesson_details_end_before_16(self,lesson_x,lesson_y):
        '''
        課程結束時間為16：00之前，打開課程詳情頁
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[0])
        self.touch_tap(lesson_x,lesson_y)
        self.driver.switch_to.context(self.driver.contexts[-1])
        return LessonDetails(self.driver)

    def goto_lesson_details_start_after_16(self,lesson_x,lesson_y):
        '''
        課程開始時間為16：00之后，打開課程詳情頁
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[0])
        self.touch_tap(lesson_x,lesson_y)
        self.driver.switch_to.context(self.driver.contexts[-1])
        return LessonDetails(self.driver)



