## -*- coding: utf-8 -*-
#"""
#Created on Mon Jan 29 23:53:15 2018
#
#instanse 2: 2048 game
#
#@author: hyh
#"""
## 快速创建list，使用for遍历
#test1 = [i for i in range(5)]
#print(test1)
## ord()：将字母转换为ASCII码
#letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
#print(letter_codes)
#
## 使用函数时，参数前面加*表示解压参数列表
#def foo(bar, lee):
#    print(bar, lee)
#k = [1,2]
#foo(*k) #输出为 1 2
#
## zip()将两个参数耦合为tuple
## python3中的zip输出和2不同
#a = [1,2,3]
#b = [4,5,6]
#c = [4,5,6,7,8]
##zipped = zip(a,b)
##z = list(zipped) #tuple组成的list，呵呵
##print(z[0])
#zipped2 = zip(a,c)
#z2 = dict(zipped2)
#z3 = list(zipped2)
#print(z2) #若有多余的，不予配对
#print(z3)
#
## lambda 匿名函数
##y = lambda x: x+1  # y = x+1
##print(y(1))
#
##actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
##letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
##actions_dict = dict(zip(letter_codes, actions * 2))
#print('----------------------------------------')
## 转置矩阵
#d = [a,b,c] # 创建一个矩阵（伪），list组成的list
#def transpose(*field):
#    return [list(row) for row in zip(*field)]
## zip不能直接print，需要通过list或者dict才能出来
## zip(*field)得到3个tuple组成的zip,for...row 遍历这个zip,并加入list()中
## 最外面的[]组成一个list
#d_transpose = transpose(a,b,c)
#print(d)
#print(d_transpose)
#print('----------------------------------------')
#from random import randint
#print(randint(1,10))
#
##print(random.randint(1,20))
##!/usr/bin/python
## -*- coding: UTF-8 -*-
#print('----------------------------------------')
#aTuple = ('xyzzaraabc','x');
#aList = list(aTuple)
# 
#print ("列表元素 : ", aList)
'abc'.encode('ascii')
#'你好'.encode('ascii')
print('-------------------------')
a = 'hello,%s' %'xi'
print(a)
b = 'today is FEB %d,%s is sleeping' %(1,'xi')
print(b)
c = {'first':'mao',
     'second':'deng',
     1:'1'}
print(c[1])
s = set([1,2,3])
print(s)
s.add(5)
print(s)
s.remove(1)
print(s)
print('-------------------------')
d = max(1,2,3)
print(d)
#help(hex)
print(hex(255))

def quadratic(b,a=1,c=1):
    delta = float(b**2-4*a*c)
    if delta < 0:
        print('no real solve')
    else:
        s1 = float((-b+delta**0.5)/(2*a))
        s2 = float((-b-delta**0.5)/(2*a))
        return s1, s2
solve = quadratic(b=-2)
print(solve)
print('-------------------------')

L = []
for n in range(1,100,2):
    L.append(n)
q = L[::5]
print(q)

tup = (1,2)
lis=list(tup)
print(lis)
lis = [1,2]
tup = tuple(lis)
print(tup)
#help(list())

for i in [(1,2),(1,3)]:
    print(i)
h = list(range(0,5))
print(h)

import os
print([d for d in os.listdir('.')])
#help(os.listdir())

L1 = ['hello','World',18,'applE',None]
for i in L1:
    if isinstance(i,str):
        print(i.lower())
#help(None)

#print(None)
#if None:
#    print('...')
#else:
#    print('True')

g = (x**2 for x in range(5))
#next(g)
for n in g:
    print(n)
for n in L1:
    print(n)
print('-------------------------')
def fib(n=2):
    i = 2
    L = [1,1]
    while i<n:
        add = L[i-2]+L[i-1]
        L.append(add)
    return L
list1 = fib(3)
print(list1)































