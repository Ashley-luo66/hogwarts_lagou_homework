import json
from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''


class TestWeWork():
    def setup(self):
        chrome_opts = webdriver.ChromeOptions()
        # 添加chrome到系统环境变量
        # windows系统，在cmd执行：chrome -remote-debugging-port=9222命令开启chrome
        # chrome_opts.debugger_address = "127.0.0.1:9222"
        chrome_opts.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_wework(self):
        # 打开页面，并打开后手动登录管理后台
        # self.driver.get("http://192.168.247.25:7070/emm-manager/")
        # # 登录管理后台
        # self.driver.find_element(By.CSS_SELECTOR, "#stroperatorname").send_keys("sysadmin")
        # self.driver.find_element(By.ID, "strpwd").send_keys("emm@leagsoft2019")
        # self.driver.find_element(By.XPATH, "//button[@id='submitButtom']").click()
        # cur_cookies = self.driver.get_cookies()
        # # cookie存入文件
        # with open("cookies.txt","w") as f:
        #     json.dump(cur_cookies,f)

        # 开启调试模式
        # 无法使用，无法使用其它地址到达后台页面
        self.driver.get("http://192.168.247.25:7070/emm-manager/menuController/queryMenus.do")
        # 读cookie
        with open("../selenium_homework/selenium_1/cookies.txt", "r") as f:
            cookies: List[Dict] = json.load(f)
            for cookie in cookies:
                # 删除expiry,cookie到期时间
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                # driver添加cookie
                self.driver.add_cookie(cookie)
        '''
        开始操作
        '''

        # 点击展开菜单按钮
        self.driver.find_element(By.CSS_SELECTOR, "li.menuchange").click()
        # 点击系统
        self.driver.find_element(By.CSS_SELECTOR,"li[strmenuname='pagelink_mobile_global'").click()