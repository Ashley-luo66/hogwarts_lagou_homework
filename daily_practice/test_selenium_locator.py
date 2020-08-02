from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

'''
selenium常见定位及常见操作

定位：本质上都是：
    Xpath（xml path language）-selenium appium都可用，速度较慢。全局搜索。
            // 所有元素（子子孙孙）
            / 子元素
    CSS-（）
最常用：cssselector xpath id name
常见操作：
    输入 .send_keys(" ")
    点击 .click()
    移动
'''


class TestEMMWeb:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.247.101:7070/emm-manager")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_locator(self):
        print(self.driver.get_cookies())
        # #id
        self.driver.find_element(By.CSS_SELECTOR, "#stroperatorname").send_keys("sysadmin")
        # ID NAME等，依然是使用CSS_SELECTOR,
        self.driver.find_element(By.ID, "strpwd").send_keys("emm@leagsoft2019")
        # .class
        self.driver.find_element(By.CSS_SELECTOR, ".l-btn").click()
        # 密码错误，关闭弹出窗
        # self.driver.find_element(By.XPATH, "//*").send_keys(Keys.Enter)
        # 等待页面加载完成
        begin_time = time.time()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='layui-nav layui-layout-right']")),
            message="超过设定时间未加载完页面")
        cost_time = time.time()-begin_time
        print("加载首页耗时：{}".format(cost_time))
        print(self.driver.get_cookies())
        # time.sleep(5)
        # 点击展开菜单按钮
        self.driver.find_element(By.CSS_SELECTOR, "li.menuchange").click()
        # 点击系统）
        self.driver.find_element(By.CSS_SELECTOR,"li[strmenuname='pagelink_mobile_global'").click()
        # 点击License(去设置)
        # self.driver.find_element(By.CSS_SELECTOR,".item:nth-child(1) span").click()
