#!/usr/local/bin/python3
import sys
#迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退


list_test = [1,2,3,4,5]
iterator = iter(list_test)

#iprint ('use for to print')
#for i in iterator :
#  print (i,end=" ")

#迭代器有两个基本的方法：iter() 和 next()。
while True:
    try:
        print (next(iterator))
    except StopIteration: 
        #StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况 , 
        sys.exit()

