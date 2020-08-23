# @date 时间 2020/8/23 19:01
# @developer 开发者：Ashley @email luoyuhong1996@163.com
import requests
from jsonpath import jsonpath

corpid= "ww8e1c8f72b07f53cd"
contracts_corpsecret = "khwMfxeu9Et0nqrJTH5JcIMxMPz-MziwvNCM90yufmY"
url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={contracts_corpsecret}"
res = requests.get(url).json()
print(jsonpath(res,"$.access_token")[0])

