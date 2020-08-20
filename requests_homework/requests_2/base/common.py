# @date 时间 2020/8/20 23:19
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from requests_homework.requests_2.base.base_api import BaseApi


class Common(BaseApi):

    def get_token(self):
        """名字乱起的

        :return:
        """
        data = {"method":"post",
                "url":"https://httpbin.ceshiren.com/post",
                "params":{"test":"luoyuhong"}
                }
        return self.send_req(data)

if __name__ == '__main__':
    print(Common().get_token())