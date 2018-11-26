#!/usr/bin/python
# -*- coding: UTF-8 -*-

for number in range(14):
  if number%2==0 :
    print number
    print '數字是偶數'
    if number == 12 :
      print '我討厭這數字'
      break
  else :
    print number 
    '數字是基數'
    if number == 5 :
      print '我喜歡這數字'
      continue