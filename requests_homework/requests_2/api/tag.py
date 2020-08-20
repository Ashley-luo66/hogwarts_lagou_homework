# @date 时间 2020/8/21 0:03
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from requests_homework.requests_2.base.base_api import BaseApi


class Tag(BaseApi):

    def add(self):
        data = {}
        return self.send_req(data)
