# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:46:31 2018

@author: hyh
"""

def normalize(name):
    return name.title()
name = ['adam','DAVID','LISA']
print(list(map(normalize,name)))