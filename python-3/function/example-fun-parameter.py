#!/usr/bin/python3

#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数

def printinfo(arg1, *vartuple):
    print ("試驗一個*字號的不定長函數 , 輸出:")
    print (arg1)
    print (vartuple)

printinfo(70,55,'python-test')


# 还有一种就是参数带两个星号 ** , 加了两个星号 ** 的参数会以字典的形式导入

def printinfo2(arg1, **vardict):
    print ("試驗兩個**字號的不定長函數 , 輸出:")
    print (arg1)
    print (vardict)

printinfo2(70,a='55',b='python-test')


#還有一個比較特別的是 , 參數中*字號是可以單獨出現的
# 單獨出現*後的參數必須用關鍵字傳入

def f(a,b,*,test):
    return a+b+test

#錯誤
#f(1,2,3)

#正確 , 有指定為test
print (f(1,2,test=3))