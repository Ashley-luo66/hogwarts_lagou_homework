# @date 时间 2020/8/20 23:19
# @developer 开发者：Ashley @email luoyuhong1996@163.com
import requests


class BaseApi():
    def send_req(self,req_info:dict):
        return requests.request(**req_info).json()