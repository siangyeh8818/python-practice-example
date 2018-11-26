#!/usr/bin/python
# -*- coding: UTF-8 -*-

list2 = [11,22,33,44,55,66]
print '原列表 : ',list2

print 'list含有9種method操作list'
print '第一種 : list.append(obj) , 在list尾端加入新的元素'
list2.append(77)
print 'append(obj)後的列表 : ',list2
print '第二種 : list.count(obj) , 統計該元素在此list中出現的次數'
print '元素55出現的次數 :',list2.count(55)
print '第三種 : list.extend(seq) , 在list尾端一次性的追加另一個list中的值'
list3 = [111,222,333]
list2.extend(list3)
print '經過extend後的list內容 : ',list2
print '第四種 : list.index(obj) , 在list中找到該項值的索引位置'
print '目前list中的222所在的索引位置 : ',list2.index(222)
print '用上面的索引查該位置的元素為',list2[list2.index(222)]
print '第五種 : list.insert(index,obj)'
list2.insert(7,88)
print 'insert(7,88)後的list : ',list2
print '第六種 : list.pop(index=-1) , 移除一個元素 , default為最後一個 , 並且返回該元素的值'
print '執行pop() , 值採取默認',list2.pop()
print '執行pop(1) , 指定索引為2',list2.pop(2)
print '執行完兩次pop後的list : ',list2
print '第七種 : list.remove()'
list2.remove(55)
print '執行remove(55)後的list : ', list2
print '第八種 : list.reverse()'
list2.reverse()
print '執行reverse()後的list : ', list2
print '第九種 : list.sort(cmp=None,key=None,reverse=False)'
list2.insert(0,99)
print '排序前的list : ',list2
list2.sort()
print '排序後的list : ',list2
