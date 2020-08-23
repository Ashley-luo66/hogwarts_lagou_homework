# @date 时间 2020/8/21 0:03
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from requests_homework.requests_2.base import get_access_token
from requests_homework.requests_2.base.base_api import BaseApi


class Tag(BaseApi):
    contracts_corpsecret = "khwMfxeu9Et0nqrJTH5JcIMxMPz-MziwvNCM90yufmY"
    access_token = get_access_token.get_access_token(contracts_corpsecret)

    def create_tag(self, tagname, tagid):
        data = {"method": "post",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.access_token}",
                "json": {
                    "tagname": tagname,
                    "tagid": tagid
                }}
        return self.send_request(data)

    def update_tag(self, tagid, tagname):
        data = {"method": "post",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.access_token}",
                "json": {
                    "tagid": tagid,
                    "tagname": tagname
                }}
        print(self.send_request(data))
        return self.jsonpath(self.send_request(data),"$.errcode")[0]

    def delete_tag(self, tagid):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.access_token}&tagid={tagid}",
                }
        print(self.send_request(data))
        return self.send_request(data)
    def get_tag_list(self):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.access_token}",
                }
        print(self.send_request(data))
        return self.jsonpath(self.send_request(data),"$.errcode")[0]
