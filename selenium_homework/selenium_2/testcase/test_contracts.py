# @date 时间 2020/8/2 18:07
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from time import sleep

import pytest

from selenium_homework.selenium_2.page.index.index import Index


class TestContracts:

    def setup(self):
        self.index = Index()

    @pytest.mark.parametrize("name,account,phone", [("test11", "test11", "13323456711")])
    def test_add_member(self, name, account, phone):
        self.index.click_add_member().save_member(name, account, phone)
        sleep(2)
        member_name = self.index.goto_contracts().get_all_name()
        assert name in member_name
