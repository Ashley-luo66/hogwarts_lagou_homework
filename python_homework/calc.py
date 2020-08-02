# @filename 文件名称 calc.py
# @date 时间 2020/3/25 20:20
# @developer 开发者：Ashley @email 17629264866@163.com
# @develop tool 开发工具 PyCharm

class Calc:
    def mulit(self,a:int,b:int):
        if type(a)!=int or type(b)!=int:
            return ("此算法仅支持整数运算")
        else:
            return a*b

    def divi(self,a:int,b:int):
        if type(a)!=int or type(b)!=int:
            return ("此算法仅支持整数运算")
        elif b == 0:
            return 'errorcode=6001'
        else:
            return a/b


if __name__ == '__main__':
    calc = Calc()
    print(calc.mulit(1, 2))
    print(calc.mulit(1.1, 2))
    print(calc.divi(1.1, 2))
    print(calc.divi(5, 2))