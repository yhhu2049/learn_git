# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:55:11 2018

@author: hyh
"""
import re
a = r'Abc\\s'
print(a)
# 正则：以3个数字开头，
b = re.match(r'^(\d{3})\-(\d{3,8})$','010-0100')
print(b)
#c = 'a b   c'.split(' ')
#print(c)
c = re.split(r'[\s\,]+','a, b,   c  d')
#print(c)
# 添加()后可以使用group
print(b.group(0))
print(b.group(1))
print(b.group(2))
print(b.group())

d = re.match('1','1')
print(d)