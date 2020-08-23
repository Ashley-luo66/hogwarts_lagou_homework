# @date 时间 2020/8/21 0:04
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from requests_homework.requests_2.api.tag import Tag
from requests_homework.requests_2.base.base_api import BaseApi

class TestTag(BaseApi):

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_get_tag(self):
        res = self.tag.get_tag_list()
        print(res)
        assert res == 0

    def test_create_tag(self):
        res = self.tag.create_tag(tagname="测试tagName",tagid=1)
        assert res == 0

    def test_update_tag(self):
        res = self.tag.update_tag(tagname="测试更新",tagid=1)
        assert res == 0

    def test_delete_tag(self):
        res = self.tag.delete_tag(tagid=1)
        assert res == 0