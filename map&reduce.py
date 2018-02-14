# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:33:02 2018


@author: hyh
"""

def add(a,b,f = abs):
    return f(a)+f(b)
c=add(1,2)
print(c)

def f(x):
    return x**2
#list1 = [1,2,3,4]
#r = map(f,list1)
list2 = list(map(f,[1,2,3,4]))
list3 = list(map(str,[1,2,3,4]))

from functools import reduce
def fn (x,y):
    return 10*x+y
print(reduce(fn,[1,2,3,4]))
print('------------------')
for i in 'abc':
    print(i)
print('------------------')
list4 = '1234'
def char2str(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
    return digits[s]
list5 = reduce(fn,map(char2str,list4))
#dict1 = {'1':1,
#         '2':2,
#         '3':3}
#print(dict1['1'])






from functools import reduce
digits = {'0': 0,
          '1': 1,
          '2': 2,
          '3': 3, 
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7, 
          '8': 8,
          '9': 9}
def f1(x,y):
    return x*10+y
def f2(s):
    return digits[s]
def f3(str1):
#    return reduce(f1,map(f2,str1))
    return reduce(lambda x, y: x*10+y,map(f2,str1))
int1 = f3(str1='54389731')






