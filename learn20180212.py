# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:04:37 2018

@author: hyh
"""
time = '20180212'
class Animal():
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name +' is running')
class Dog(Animal):
    def run(self):
        print('this dog is running')
    def sleep(self):
        print('this dog is sleeping')
class Cat(Animal):
    pass
wanghao = Dog('wanghao')
wanghao.run()
wanghao.sleep()
#所有子类同时也是父类
print('-----------------')
def run_twice(arg):
    arg.run()
    arg.run()
run_twice(wanghao)
print(type(Dog)==type(Cat))
print('abc'.__len__())
print(len('abc'))
print('-----------------')


from functools import reduce

def str2num(s):
    if isinstance(s,int):
        return int(s)
    else:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

#main()
#try:
#    f = open('readme.txt','r')
#    print(f.read())
#finally:
#    if f:
#        f.close()
#with open('instance1~picture2string/Xi.jpg','rb') as f:
#    print(f.read())
from io import StringIO
f = StringIO()
f.write('hello')
f.write(',world!')
print(f.getvalue())
import os
print(os.name)
print(os.path.abspath('.'))
#os.mkdir('test')
#for i in range(10):
#    name = 'test' + str(i)
#    os.mkdir(name)
#os.rename('readme.txt','readme')
#print(os.listdir())
a = [i for i in os.listdir('.') \
if os.path.isfile(i)]
#a = [i for i in os.listdir('.') \
#if os.path.isfile(i) and os.path.splitext(i)[1]=='.py']
print(a)
# isdir & ispath




