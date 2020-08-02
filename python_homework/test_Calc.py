# @filename 文件名称 test_Calc.py
# @date 时间 2020/3/25 20:18
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm
import pytest
import yaml
from .calc import Calc
import os

print(os.getcwd())



class TestCalc:

    # print(os.path.abspath("calc_testcase.yaml"))


    @classmethod
    def setup_class(cls):
        cls.calc = Calc()

    # test_data = yaml.safe_load(open("F:\emm_auto_test\practice\lagou001_calc\calc_testcase.yaml"))
    test_data = yaml.safe_load(open("calc_testcase.yaml"))
    mulit_test_data = test_data['mulit']
    divi_test_data = test_data['divi']

    @pytest.mark.parametrize('item',mulit_test_data)
    def test_mulit(self,item:dict):
        assert  self.calc.mulit(item['var1'],item['var2']) == item['excepted']

    @pytest.mark.parametrize('item',divi_test_data)
    def test_divi(self,item:dict):
        assert  self.calc.divi(item['var1'],item['var2']) == item['excepted']

