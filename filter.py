# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:55:08 2018

@author: hyh
"""

def not_empty(s):
    return s and s.strip()
# 必须返回其值或者其去掉末尾的值
a = list(filter(not_empty,['1','','2','  ']))
print(a)

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
        
    