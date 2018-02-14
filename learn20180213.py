# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:39:19 2018

@author: hyh
"""
import pickle
d = dict(name='Bob', age=20, score=88)

#f =open('test.txt','wb')
#pickle.dump(d,f)
#f.close()
#f =open('test.txt','rb')
#e = pickle.load(f)
#f.close()
#print(e)
with open('test.txt','wb') as f:
    pickle.dump(d,f)
with open('test.txt','rb') as f:
    e = pickle.load(f)
    print(e)

import json
# 注意w和wb的区别
with open('test1.txt','w') as f:
    json.dump(d,f)
with open('test1.txt','r') as f:
    e = json.load(f)
    print(e)
    
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def student2dict(std):
    return {'name':std.name,
            'age':std.age,
            'score':std.score
            }
def dict2student(std):
    return Student(d['name'],d['age'],d['score'])

s = Student('Bob', 20, 88)
with open('test2.txt','w') as f:
    json.dump(d,f,default = student2dict)
with open('test2.txt','r') as f:
    e = json.load(f,object_hook=dict2student)
    print(e)
    
    
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
    
    
    
    
