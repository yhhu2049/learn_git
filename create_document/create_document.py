# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:46:04 2018

create a series of documents named from 1,2,...,n

@author: hyh
"""

import os
a = os.path.exists('d:/ass')
print(a)
b = os.path.exists('d:/HelloWorld')
print(b)
c = os.path.exists('d:/helloWorld')
print(c)
# cannot distinguish upper or lower written
start_num = 201773466
for i in range(1,11):
    dirname = 'D:/HelloWorld/learngit/create_document/学号：M' + str(i + start_num)
    if os.path.exists(dirname):
        os.rmdir(dirname)
for i in range(1,11):
    dirname = 'D:/HelloWorld/learngit/create_document/学号：M' + str(i + start_num)
    os.makedirs(dirname)
