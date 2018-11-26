#!/usr/bin/python
# -*- coding: UTF-8 -*-

list1 = ['java','python','object-c']
list2 = [11,22,33,44,55,66]
list3 = [11,22,33,44,55,66]

print 'List的元素個數 , 函數 : len(list)'
print len(list1)
print len(list2)

print 'List的元素最大值 , 函數 : max(list)'
print max(list1)
print max(list2)

print 'List的元素最小值 , 函數 : min(list)'
print min(list1)
print min(list2)

print '比較兩個list的元素 , 函數 : cmp(list1,list2)'
print '比較list1跟list2'
print cmp(list1,list2)
print '比較list2跟list3'
print cmp(list2,list3)
print '1代表兩list不一樣 , 0則代表兩list一樣'

aTuple = (123,'asd','abcd')
print '將tuple轉化成list , 函數 : list(tuple)'
newlist = list(aTuple)
print "列表元素 : ",newlist