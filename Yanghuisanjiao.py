# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:17:34 2018

@author: hyh
"""
# 斐波那契额数列
def fib(n=2):
    i = 2
    L = [1,1]
    while i<n:
        add = L[i-2]+L[i-1]
        L.append(add)
        i += 1
    return L
list1 = fib(10)
print(list1)
print('-----------------')
#for i in range(0):
#    exec('list_%s = []' % str(i))
#b = [1] + [2]
#    print(i)
def yanghui(n):
    b = [1]
    i = 0
    while i < n:
        print(b)
        b = [1] + [b[i]+b[i+1] for i in range(len(b)-1)] + [1]
        i += 1
yanghui(5)