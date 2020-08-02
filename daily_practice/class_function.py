# @filename 文件名称 class_function.py
# @date 时间 2020/3/28 11:31
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm

# import random
#
# a = input("输入")
# b = random.randint(1, 100)
# print(b)
# if a == b:
#     print("猜对了")
# else:
#     print("猜错了")


def append_a(a, b=[], *args, **kwargs):
    '''
    *args:可变参数，元组
    **kwargs：关键字参数（字典）
    *,a：仅限关键字传参
    '''
    b.append(a)
    print(b)
    print(*args)
    print(type(args[0]))
    print(kwargs.keys())


#
# append_a(1)
# append_a(2)
append_a(1, [], 2, 3, c='ccc')
# append_a(1, c=15,d=222)
print("--------------------------------")


# 仅限关键字参数
def special_args(*, a, b):
    '''
    仅限关键字参数
    '''
    print(a + b)


special_args(a='aaaaa', b='bbbbbbb')
print("---------------------------")
# 解包参数
## 解包字典 **
dict_a = {"a": "aaaa", "b": "bbbb"}
special_args(**dict_a)
## 解包元组、列表 *

print("-------------------------")
# lambda函数
# 如下函数对x\y进行比较，返回较大值
large_num = lambda x, y: x if x > y else y
print(large_num(2, 3))
