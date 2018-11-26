#!/usr/bin/python
# -*- coding: UTF-8 -*-

tuple1 = ('123','python','456','java','789','golang')
tuple2 = (1,2,3,4,5,6)
tuple3 = (1,2,3,4,5,6)
print 'tuple1 : ',tuple1
print 'tuple2 : ',tuple2
print 'tuple3 : ',tuple3

print 'python給tuple五種內建function'
print '1 . cmp(tuple1,tuple2) , 比較兩個tuple的元素 , 皆相同為0 , 不同為1'
print 'cmp(tuple1,tuple2) : ',cmp(tuple1,tuple2)
print 'cmp(tuple3,tuple2) : ',cmp(tuple3,tuple2)
print '2 . len(tuple) , 計算tuple的元素個數'
print ' len(tuple1) : ',len(tuple1)
print '3 . max(tuple) , 返回tuple內元素中最大值'
print 'max(tuple2) : ', max(tuple2)
print '4 . min(tuple) , 返回元素中最小值'
print 'min(tuple2)',min(tuple2)
print '5 . tuple(sqp) , 將list轉化為tuple'
list1 = ['test1','test2','test1234']
print 'list1 : ',list1
newtuple = tuple(list1)
print '經過tuple()轉化後的結果 : ',newtuple

