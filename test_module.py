# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:42:39 2018

@author: hyh
"""

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


#print(sys.path)
    


#class student():
#    def __init__(self,name,score):
#        self.__name = name
#        self.__score = score
#    def print_score(self):
#        print('%s %s' % (self.name,self.__score))
#    def get_grade(self):
#        if int(self.__score) >= 90:
#            print('A')
#        else:
#            print('B')
#student1 = student('haha','100')
#print(student1.__name)
#student1.print_score()
#student1.get_grade()
#student1.__init__('Xijinping','100')
#student1.print_score()


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender == 'female' or gender == 'male':
            self.__gender = gender
        else:
            raise ValueError('No this gender')
haha = Student('haha','male')
print(haha.name)
print(haha.get_gender())
haha.set_gender('female')
print(haha.get_gender())
haha.set_gender('transgender')
print(haha.get_gender())




