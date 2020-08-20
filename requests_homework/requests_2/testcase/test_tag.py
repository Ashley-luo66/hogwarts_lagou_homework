# @date 时间 2020/8/21 0:04
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from requests_homework.requests_2.api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_tag(self):
        res = self.tag.add()
