#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict1 = {'java':8,'python':2.7,'shell':'unknown',1:'hello'}
dict2= {'123':8,333:'test'}

print 'dict1 : ',dict1
print 'dict2 : ',dict2

print 'dictionary內含12種method'
print '1 . dict.clear() , 刪除dict內所有元素'
dict2.clear()
print '經過clear後的dict2 : ',dict2

print '2 . dict.copy() , 返回一個字典的複製'
dict3 = dict1.copy()
print 'dict3 : ' , dict3

print '3 . dict.fromkeys(seq[,value]) , 用來創一個新的dict , 以list為key ,value為初始值'
list2 = [11,22,33,44,55,66]
print 'list2 :',list2
dict4 = dict2.fromkeys(list2)
print 'dict4 : ',dict4

print '4 . dict.get() , 返回指定key的值'
print 'dict1.get(java) : ',dict1.get('java')

print '5 . dict.has_key(key) , 判斷該key是否在dict內 , 有的話為True , 沒有為False'
print 'dict1.has_key(golang) : ',dict1.has_key('golang')
print 'dict1.has_key(python) : ',dict1.has_key('python')

print '6 . dict.items() , 將dictionary轉化成list返回'
print 'dict2.items()後返回',dict1.items()

print '7 . dict.keys() , 以一個list返回這個dict內所有的key'
print 'dict1.keys() : ',dict1.keys()

print '8 . dict.setdefault(key,default) , 和get()類似 , 但不存在該key會新增此key並給default的值' 
dict1.setdefault('linux','centos')
print 'dict1.setdefault(linux,centos)後 : ',dict1

print '9 . dict.update(dict2) , 把dict2的值更新到dict上'
dictnew = {'java':9,'python':3.5,'shell':'latest',1:'hello~world'}
dict1.update(dictnew)
print 'update()後的dict1 : ',dict1

print '10 . dict.values() , 以列表返回所有的值'
print 'dict1.values() : ',dict1.values()

print '11 . dict.pop(key) , 刪除字典給該key的值 , 返回值為被刪除的值 '
print 'dict1.pop(python) : ',dict1.pop('python')
print 'dict1 : ',dict1

print '12 . dict.popitem() , 隨機返回並刪除字典中的一對鍵值'
print 'dict1.popitem() : ',dict1.popitem()
print 'dict1 : ',dict1