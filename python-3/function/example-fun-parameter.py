#!/usr/bin/python3

#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数

def printinfo(arg1, *vartuple):
    print ("輸出:")
    print (arg1)
    print (vartuple)

printinfo(70,55,'python-test')