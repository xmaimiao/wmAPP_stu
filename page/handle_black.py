from appium.webdriver.common.mobileby import MobileBy


def handlie_blacklist(func):
    def wrapper(*args, **kwargs):
        _blacklist = [
            (MobileBy.ID, 'permission_allow_button'),
            (MobileBy.XPATH, '//*[@resource-id="com.andr,oid.packageinstaller:id/permission_allow_button"]')
        ]
        _max_err_num = 3
        _error_num = 0
        # 裝飾器會默認把self當第0個參數傳進來
        from page.basepage import BasePage
        instance : BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            _error_num = 0
            # 恢復為等待3s
            instance.set_implicitly_wait(3)
            return result
        except Exception as e:
            # 等待時間過長，先處理為1s
            instance.set_implicitly_wait(1)
            # 如果没找到，就进行黑名单处理
            if _error_num > _max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                _error_num = 0
                raise e
            _error_num += 1
            for ele in _blacklist:
                eles = instance.finds(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名單中")
    return wrapper