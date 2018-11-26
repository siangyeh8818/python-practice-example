#!/usr/bin/python3

#python 使用 lambda 来创建匿名函数
# 匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数

#lambda 函數的格式 :
# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2 : arg1+arg2

print ("相加後的值為 : ", sum(30,50))