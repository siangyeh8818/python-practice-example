#!/usr/bin/python
# -*- coding: UTF-8 -*-

# dictionary跟 list或Tuple最大的不同之處 , 在於內容是個鍵值 , 也就是key:value
# dictionary是用{}
# 存在dictionary沒有順序得概念喔

dict1 = {'java':8,'python':2.7,'shell':'unknown',1:'hello'}
print 'dict1',dict1

print '訪問dictionary的值'
print 'dict1[java] : ',dict1['java']
print 'dict1[python] : ',dict1['python']
print 'dict1[shell] : ',dict1['shell']
print 'dict1[1] : ',dict1[1]

print '修改dictionary內的值'
# 首先是更新 , 像是把'python'的值改為3.5
dict1['python'] = 3.5
print 'dict1[python] : ',dict1['python']
# 其次是新增
dict1['windows'] = 8
print 'dict1[windows]' , dict1['windows']
# 刪除字典內元素
del dict1['windows']
print '執行完del dict1[windows]後的dict1 : ', dict1
#清空dictionary內的條目 , 用dict.clear()
dict1.clear()
print '執行完dict1.clear()後的dict1 : ',dict1
#刪除dictionary , 用 del , 類似 del dict1 , 但這不示範

print 'Dictionary的特性有兩個很重要'
print '第一 : 同一個key不同出現兩次 , 如果一個key被賦予值兩次 , 一定是後面蓋過前面 (其實就是更新)'
dict1['python']=2.7
dict1['python']=3.5
print '對於python這個鍵值 , 先是給2.7 , 後給3.5的結果 : ',dict1['python']
print '第二 : 鍵值不可變 , 所以可接受數字,字串,tuple , 但無法接受list , 因為list是可以更改的'
tuple2 = (1,2,3,4,5,6)
dict2 = {tuple2:'first','research':2.1}
print 'dict2內含tuple為key : ',dict2
