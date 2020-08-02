# @filename 文件名称 class_data_structure.py
# @date 时间 2020/3/28 13:06
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm

# list tuple set dict
# 常用列表内置方法
list_a = []
# 切片
list_a[len(list_a):] = [0, 1, 2]
print(list_a)
# append
list_a.append(4)
print(list_a)
# extend
list_a.extend([5, 6, 7])
print(list_a)
list_a[3:] = [44, 55]
print(list_a)

# insert
## 在指定位置，添加333
list_a.insert(2, 333)
print(list_a)
## 超过索引，添加在末尾
list_a.insert(999, 333)
print(list_a)

# remove
## 移除指定元素：第一个查找到的333
list_a.remove(333)
print(list_a)
try:
    list_a.remove("啦啦啦")
except Exception as e:
    print(e)

# pop
## 默认弹出最后一位
list_a.pop()
print(list_a)
## 指定位置
a = list_a.pop(2)
print(a)
print(list_a)

# sort
list_a.insert(1, 888)
print(list_a)
list_a.sort()
print(list_a)
## 降序排序
list_a.sort(reverse=True)
print(list_a)

# reverse 反转 类似[::-1]
list_a.reverse()
print(list_a)

list_a = list_a[::-1]
print(list_a)

#  返回指定值的索引
a = list_a.index(1)
print(a)

# 返回元素在列表出现次数
a = list_a.count(1)
print(a)

# 列表推导式
## 生成平方数
list_square = [i ** 2 for i in range(1, 5)]
print(list_square)
## 增加判断条件
list_square2 = [i ** 2 for i in range(1, 5) if i != 2]
print(list_square2)
## 嵌套循环
new_list = [i * j for i in range(1, 5) for j in range(1, i)]
print(new_list)
print("**************************************")

# Tuple
a = (1, 2, 3, 2, 2, 2)
# 返回指定元素出现的次数
print(a.count(2))
# 返回指定元素，第一次出现的 位置索引
print(a.index(2))

# 内存
import sys

a = []
b = ()
print(sys.getsizeof(a))
print(sys.getsizeof(b))
# 元组嵌套列表时，列表的元素可被修改
a = (['a', 'b', 'c'], 2, 3, 4)
print(a)
a[0][1] = "bbbb"
print(a)

# set 集合
# 无重复元素
a = set()
print(a)
print(len(a))
a.add('')
print(a)
print(len(a))
a = set("jfdsioafjaosidfjaieh")
print(a)
print(len(a))

# dict
a = {"a":1,"b":2}
print(a)
a = dict(a=1,b=2,c=3)
print(a)
a.pop("b")
print(a)