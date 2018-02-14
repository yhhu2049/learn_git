# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:57:39 2018

@author: hyh
"""

a = [1,2,-7,8,10]
def fn(x):
    return -x
b = sorted(a,key = fn)
print(b)

c = ['a','b','c','D']
d = sorted(c,key = str.lower)
print(d)
#print(str.lower('D')) 
#output:d
#print(str.strip('D   ')) 
#output:D



# exercise:
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
result = sorted(L,key = by_name)
print(result)

def by_score(t):
    return t[1]
result = sorted(L,key = by_score,reverse = True)
print(result)