# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:38:29 2018

@author: hyh
"""


def build(x, y):
    return lambda: x * x + y * y
c = build(1,2)
d = c()

def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
#a = is_odd(5)
f = abs
print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__ )
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2018-02-10')

now()
# now = log(now)
print(int('100',base = 2))

import functools
max2 = functools.partial(max,10)
a = max2(1,2,3)

kw = {'base':2}
int2 = functools.partial(int,**kw)
c = int2('100')






