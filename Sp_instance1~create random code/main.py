# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:55:15 2018
random code
@author: hyh
"""
from random import randint
asci = list('1234567890qwertyuiopasdfghjklzxcvbnm')
if __name__ == '__main__':
    txt = ''
    for i in range(11):
        txt += asci[randint(1,len(asci))]
    print('激活码为： ',txt)