# @filename 文件名称 conftest.py
# @date 时间 2020/3/28 22:09
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm
import pytest

@pytest.fixture()
def login():
    print("此方法可以通过传参，被其他测试方法调用")
