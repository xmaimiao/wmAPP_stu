'''
BasePage:存放一些基本的放大，比如：初始化 driver，find查找元素
'''
import json
import logging
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page.handle_black import handlie_blacklist


class BasePage:

    logging.basicConfig(level=logging.INFO)
    _params = {}

    def __init__(self,driver:WebDriver = None):
        self.driver = driver
        self.env = yaml.safe_load(open("../data/env.yaml"))

    @handlie_blacklist
    def find(self,by,locator):
        logging.info(f"find：{locator}")
        if by == None:
            result=self.driver.find_element(*locator)
        else:
            result = self.driver.find_element(by,locator)
        return result

    def finds(self,by,locator):
        logging.info(f"find_eles：{locator}")
        return self.driver.find_elements(by,locator)

    def find_and_click(self,by,locator):
        logging.info("click")
        self.find(by,locator).click()

    def find_and_sendkeys(self,by,locator,text):
        logging.info(f"sendkeys：{text}")
        self.find(by,locator).send_keys(text)

    def find_scroll(self,text):
        logging.info("find_scroll")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               f'.text("{text}").instance(0));')

    def webdriver_wait(self,by,locator,timeout=20):
        logging.info(f"webdriver_wait：{locator},timeout：{timeout}")
        WebDriverWait(self.driver, timeout).until(lambda x:x.find_element(by,locator))

    def webdriver_wait_click(self, by,locator, timeout=20):
        logging.info(f"webdriver_wait_click：{locator},timeout：{timeout}")
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by,locator)))


    def back(self,num):
        logging.info(f"back：{num}")
        for i in range(num):
            self.driver.back()



    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)


    def touch_move(self,x1,x2,y1,y2,timeout=200):
        '''
        獲取當前屏幕尺寸、坐標、像素，拿取百分比，換設備不容易出錯
        '''
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x_start = int(width * x1)
        x_end = int(width * x2)
        y_start = int(height * y1)
        y_end = int(height * y2)
        action.press(x=x_start,y=y_start).wait(timeout).move_to(x=x_end,y=y_end).release().perform()

    def tap(self, x_num,y_num):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x = int(width * x_num)
        y = int(height * y_num)
        action.tap(x=x,y=y).perform()

    def set_implicitly_wait(self,second):
        self.driver.implicitly_wait(second)

    def step(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        # ${}的參數轉化
        raw_data = json.dumps(steps)
        # 替換傳入參數
        for key,value in self._params.items():
            raw_data = raw_data.replace("${"+key+"}",value)
        steps = json.loads(raw_data)
        for step in steps:
            # 替換測試環境dev/uat
            step["locator"] = str(step["locator"]).\
                replace("testing-studio", self.env["testing-studio"][self.env["default"]])
            if "action" in step.keys():
                action = step["action"]
                if "wait_click" == action:
                    self.webdriver_wait_click(step["by"],step["locator"])
                if "wait" == action:
                    self.webdriver_wait(step["by"], step["locator"])
                if "send" == action:
                    self.find_and_sendkeys(step["by"], step["locator"], step["value"])
                if "click" == action:
                    self.find_and_click(step["by"],step["locator"])
                if "len" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles)
                if "text" == action:
                    text = self.find(step["by"], step["locator"]).text
                    return text
                if "clear" == action:
                    self.find(step["by"], step["locator"]).clear()

