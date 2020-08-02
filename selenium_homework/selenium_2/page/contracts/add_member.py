# @date 时间 2020/8/2 16:37
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from selenium.webdriver.common.by import By

from selenium_homework.selenium_2.page.basepage import BasePage


class AddMember(BasePage):
    _ele_name = (By.ID, "username")
    _ele_account = (By.ID, "memberAdd_acctid")
    _ele_phone = (By.ID, "memberAdd_phone")
    _ele_save = (By.CSS_SELECTOR,".js_member_editor_form >div:nth-child(1) .js_btn_save")

    def save_member(self, name, account, phone):
        self.send_keys(self._ele_name, keywords=name)
        self.send_keys(self._ele_account, keywords=account)
        self.send_keys(self._ele_phone, keywords=phone)
        self.find(self._ele_save).click()
