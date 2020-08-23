# @date 时间 2020/8/23 18:49
# @developer 开发者：Ashley @email luoyuhong1996@163.com
import requests
from jsonpath import jsonpath


class TestDep():
    @classmethod
    def setup_class(cls):
        cls.corpid = "ww8e1c8f72b07f53cd"
        contracts_corpsecret = "khwMfxeu9Et0nqrJTH5JcIMxMPz-MziwvNCM90yufmY"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={cls.corpid}&corpsecret={contracts_corpsecret}"
        res = requests.get(url).json()
        cls.access_token = jsonpath(res, "$.access_token")[0]
        print(cls.access_token)

    def test_get_dep(self):
        """查询部门信息

        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}&id=1"
        res = requests.get(url).json()
        print(res)
        assert jsonpath(res, "$.errcode")[0] == 0
        assert jsonpath(res, "$.errmsg")[0] == "ok"

    def test_add_dep(self):
        """增加部门

        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}"
        data = {"name": "测试",
                "userid": "ceshi",
                "parentid": 1,
                }
        res = requests.post(url, json=data).json()
        print(res, jsonpath(res, "$.errcode")[0], jsonpath(res, "$.errmsg"))
        assert jsonpath(res, "$.errcode")[0] == 0
        assert jsonpath(res, "$.errmsg")[0] == "created"

    def test_update_dep(self):
        """更新部门

        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}"
        data = {"id": 7,
                "name": "改了名字"
                }
        res = requests.post(url, json=data).json()
        print(res)
        assert jsonpath(res, "$.errcode")[0] == 0
        assert jsonpath(res, "$.errmsg")[0] == "updated"

    def test_del_dep(self):
        """删除部门

        """
        dep_id = 7
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={dep_id}"
        res = requests.get(url).json()
        assert jsonpath(res, "$.errcode")[0] == 0
        assert jsonpath(res, "$.errmsg")[0] == "deleted"
