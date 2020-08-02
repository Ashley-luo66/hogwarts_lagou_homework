# @filename 文件名称 class_while.py
# @date 时间 2020/3/28 10:55
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm

# while else
# break 跳出整个循环体(如：跳出while)
# continue 跳出当前循环体，进入下一次循环（如：跳出当前while,进入下一次while）

a = 10
while a < 15:
    print(a)
    a += 1
    if a == 13:
        print(a)
        continue
        print(a)  # 此语句永远不会被执行
    if a == 14:
        print(a)
        break
        print(a)  # 此语句永远不会被执行
else:
    print(a)
