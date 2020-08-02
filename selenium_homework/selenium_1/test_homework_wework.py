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
        self.driver = webdriver.Chrome(options=chrome_opts,executable_path="D:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_wework(self):
        # 打开页面，并打开后手动登录企业微信
        self.driver.get("https://work.weixin.qq.com")
        # 读cookie
        with open("cookies.txt", "r") as f:
            cookies: List[Dict] = json.load(f)
            for cookie in cookies:
                # 删除expiry,cookie到期时间
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                # driver添加cookie
                self.driver.add_cookie(cookie)
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        # sleep(15)
        # cur_cookies = self.driver.get_cookies()
        # # cookie存入文件
        # with open("cookies.txt", "w") as f:
        #     json.dump(cur_cookies,f)


        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 添加成员
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.driver.find_element(By.ID, "username").send_keys("tester")