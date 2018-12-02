#!/usr/local/bin/python3


#Python两种输出值的方式: 表达式语句和 print() 函数

#str()： 函数返回一个用户易读的表达形式

str123 = 'This one pythopn code'

#str(str123)
#repr(str123)

for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # 注意前一行 'end' 的使用
     print(repr(x*x*x).rjust(4))

#字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
