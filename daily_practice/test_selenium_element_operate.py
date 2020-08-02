from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
Tips：删除当前行快捷按键 Shift+delete
常用操作：
输入、点击
右键点击、页面滑动、表单操作等
'''


class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.leagsoft.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def teardown(self):
        pass

    def testEmm(self):
        element_click = self.driver.find_element(By.CSS_SELECTOR,"")
        ele_
        actions = ActionChains(self.driver)
