from time import sleep
from page.basepage import BasePage
from page.classtimetablepage.classtimetable import ClassTimeTable
from page.person_infopage import PersonInfo


class Index(BasePage):
    def message(self):
        '''
        消息相关
        :return:
        '''
        pass

    def goto_class_timetable(self,x,y):
        '''
        打開課表,若通過xpath元素定位打開課表，則會同時打開課程詳情頁
        故通過點擊頁面打開課表
        '''
        sleep(5)
        self.touch_tap(x,y)
        return ClassTimeTable(self.driver)

    def goto_person_info(self,me):
        '''
        打開 我的
        :return:
        '''
        self._params["me"] = me
        self.step("../data/index.yaml", "goto_person_info")
        return PersonInfo(self.driver)