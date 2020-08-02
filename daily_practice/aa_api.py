# @date 时间 2020/8/2 20:30
# @developer 开发者：Ashley @email luoyuhong1996@163.com
import requests

r = requests.get("http://ceshiren.com/")
print(r.status_code)

r2 = requests.get("http://ceshiren.com/")
print(type(r.content()))

