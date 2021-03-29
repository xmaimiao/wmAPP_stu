from page.basepage import BasePage


class StudentCourses(BasePage):
    _max_err_num = 3
    _error_num = 0
    def get_course_type_or_status(self,course_code):
        '''
        課表list頁獲取科目的類型,謹云課堂/網課有該類型
        課表list頁獲取普通科目：綫下科目的狀態：授課中
        :return:
        '''
        self._params["course_code"] = course_code
        try:
            result = self.step("../data/classtimetable/studentcourses.yaml","get_course_type_or_status")
            self._error_num = 0
            return result
        except Exception:
            if self._error_num > self._max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                _error_num = 0
                raise ValueError("list課表頁沒有該科目code")
            self._error_num += 1
            self.driver.switch_to.context(self.driver.contexts[0])
            self.touch_move(1/2,1/2,3/4,1/4)
            self.driver.switch_to.context(self.driver.contexts[-1])
            return self.get_course_type_or_status(course_code)

    def get_course_z_m_status(self,course_code):
        '''
        課表list頁獲取網課/云課堂的狀態
        :return:
        '''
        self._params["course_code"] = course_code
        try:
            result = self.step("../data/classtimetable/studentcourses.yaml","get_course_z_m_status")
            self._error_num = 0
            return result
        except Exception:
            if self._error_num > self._max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                _error_num = 0
                raise ValueError("list課表頁沒有該科目code或該科目為綫下課程")
            self._error_num += 1
            self.driver.switch_to.context(self.driver.contexts[0])
            self.touch_move(1/2,1/2,3/4,1/4)
            self.driver.switch_to.context(self.driver.contexts[-1])
            return self.get_course_z_m_status(course_code)



