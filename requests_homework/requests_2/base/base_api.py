# @date 时间 2020/8/20 23:19
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from jsonpath import jsonpath
import requests


class BaseApi():
    def send_request(self,req_info:dict):
        """

        :param req_info: 以字典形式传入请求信息
        :return:
        """
        return requests.request(**req_info).json()

    def jsonpath(self,json_obj,expr):
        """

        :param json_obj: json串
        :param expr: jsonpath表达式
        :return:
        """
        return jsonpath(json_obj,expr)
