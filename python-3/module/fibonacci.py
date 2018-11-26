#!/usr/local/bin/python3

def fib(n): # 定义到 n 的斐波那契数列
    a,b = 0,1
    while b < n :
        print (b, end=' ')
        a,b = b,a+b
    print ()

def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# 非常重要的 __name__ 屬性
#一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行


if __name__ == '__main__':
   print('fibonacci程序自身在运行')
else:
   print('我来自另一模块fibonacci ')
