# @date 时间 2020/8/2 16:29
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from selenium.webdriver.common.by import By

from selenium_homework.selenium_2.page.basepage import BasePage
from selenium_homework.selenium_2.page.contracts.add_member import AddMember
from selenium_homework.selenium_2.page.contracts.contracts import Contracts


class Index(BasePage):
    _ele_contracts = (By.ID,"menu_contacts")
    _ele_add_member = (By.CSS_SELECTOR,"a[node-type='addmember']")

    def click_add_member(self):
        self.find(self._ele_add_member).click()
        return AddMember(self._driver)

    def goto_contracts(self):
        self.find(self._ele_contracts).click()
        return Contracts(self._driver)
