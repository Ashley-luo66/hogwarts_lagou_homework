from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
selenium常见定位及常见操作

定位：本质上都是：
    Xpath（xml path language）-selenium appium都可用，速度较慢。全局搜索。
            // 所有元素（子子孙孙）
            / 子元素
    CSS --selenium appium(原生控件不支持)都可用，更快
    

常见操作：
    输入 .send_keys(" ")
    点击 .click()
    移动
'''