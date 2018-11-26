#!/usr/bin/python
# -*- coding: UTF-8 -*-

tuple1 = ('123','python','456','java','789','golang')
print 'tuple1 : ',tuple1
tuple2 = (1,2,3,4,5,6)
print 'tuple2 : ',tuple2
tuple3 = "no","body","ok"
print 'tuple3 : ',tuple3
#單一元素的tuple , 要加上個逗號,如下
tuple4 = (88,)
print 'tuple4 : ',tuple4

#讀取tuple內的值
print "tuple1[0]:",tuple1[0]
#讀取tuple內的值 , 有限制範圍[1:4],這代表tuple[1],tuple[2],tuple[3]為取值範圍 , 沒有tuple[4]喔
print "tuple1[1:4]:",tuple1[1:4]

#tuple跟list最大的不同 , 在於不可修改其中的值 
#但是我們可以連接兩個tuple
tuple12 = tuple1 + tuple2
print tuple12

#tuple是可以刪除的  , 用del tuple即可
#del tuple12

# tuple的運算符
print '第一個 , 長度'
print '計算tuple的元素個數len(tuple) : ',len(tuple1)
print '第二個 , 連接 , 就像是上面tuple12的結果 , 不另外演示'
print '第三個 ,複製,像是tuple*2' 
tuple2 = tuple2*2
print tuple2
print '第四個 , 便是元素是否存在, 有的話回傳True , 沒有就False'
print '5是否在tuple2內 : ',5 in tuple2
print '7是否在tuple2內 : ',7 in tuple2
print '第五個 , 迭代'
for x in tuple1 :
    print x,
#上面的逗號是為了不讓他分行
print ''
# tuple的索引,擷取
print 'tuple1[2] : ',tuple1[2]
print 'tuple1[-1] : ',tuple1[-1]
print 'tuple1[2:] : ',tuple1[2:]