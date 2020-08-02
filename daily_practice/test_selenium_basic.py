from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

'''
selenium基本：
启动webdriver
等待：强制等到，显性等待，隐形等待
'''

class TestEmmWeb:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.leagsoft.com:33443/emm-manager/")
        self.driver.maximize_window()
        # driver全局设置，所有操作隐形等待3秒，每隔0.5秒检查，最长等待时间为3秒
        self.driver.implicitly_wait(3)


    def test_login(self):
        begin_time = time.time()

        # 登录
        # 显性等待
        # 实例：找到元素
        # 知识点：python 传参传递函数
        def wait(x):
            return len(self.driver.find_elements(By.ID, "stroperatorname")) >= 1
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.ID, "stroperatorname").send_keys("secadmin")
        self.driver.find_element_by_id("strpwd").send_keys("emm@leagsoft2019")

        # 显性等待
        # 知识点：使用内置方法expected_conditions
        # 注意：locator使用元组的方式传参
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "submitButtom")), message="查找元素超时")
        self.driver.find_element_by_id("submitButtom").click()

        # 强制等待5秒
        time.sleep(0)
        cost_time = time.time() - begin_time
        print("花费时间cost time:{}s".format(cost_time))

    def teardown(self):
        self.driver.quit()
