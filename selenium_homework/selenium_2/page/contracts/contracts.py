# @date 时间 2020/8/2 23:05
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from selenium.webdriver.common.by import By

from selenium_homework.selenium_2.page.basepage import BasePage


class Contracts(BasePage):
    _ele_name = (By.CSS_SELECTOR,"tbody#member_list>tr:nth-child(2)")
    def get_first_name(self):
        return self._driver.find_element(self._ele_name).text

