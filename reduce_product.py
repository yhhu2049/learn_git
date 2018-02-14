# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:51:54 2018

@author: hyh
"""

from functools import reduce
def product(x,y):
    return x*y
list1 = [1,2,3,4] 
result = reduce(product,list1)
print(result)