#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict1 = {'java':8,'python':2.7,'shell':'unknown',1:'hello'}
dict2 = {'java':8,'python':2.7,'shell':'unknown',1:'hello'}
dict3= {'123':8,333:'test'}
print 'dict1 : ',dict1
print 'dict2 : ',dict2
print 'dict3 : ',dict3

print 'python內含4種對於dictionary為對象的函數function'
print '1 . cmp(dict1,dict2) , 比較兩個dictionary , 一樣返回1,不一樣返回-1'
print 'cmp(dict1,dict2) : ', cmp(dict1,dict2)
print 'cmp(dict3,dict2) : ', cmp(dict3,dict2)
print '2 . len(dict1) , 計算dictionary的元素個數'
print 'len(dict1) : ',len(dict1)
print 'len(dict3) : ',len(dict3)
print '3 . str(dict) , 將dictionary內容返回成一個string物件 ,簡單就是dictionary轉成string'
print 'str(dict1) : ',str(dict1)
print 'str(dict3) : ',str(dict3)
print '4 . type(variable) ,返回輸入的變量型態 '
a={'123':8,333:'test'}
b=('123','234')
c=['python','java']
print 'a的形態為 : ',type(a),' ,b的形態為',type(b),' ,c的形態為',type(c)
