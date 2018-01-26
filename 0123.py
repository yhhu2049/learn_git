# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:45:15 2018

@author: hyh
"""

#def city_country(city,country='China'):
#    print(city +'\tis in\t' + country)
#    
#a = city_country('Beijing','China')
## another method
#b = city_country(city='Beijing',country='China')
#c = city_country('Beijing')
#d = city_country('NewYork','US')
#e = city_country(country='China',city='Beijing')
#
#
#def shit(size,word):
#    print('the size is\t'+size+'\n'+word)
#f = shit(str(35),'hello')

#def cake(*top):
#    print('your topping is:)
#    for t in top:
#        print(t)
#g = cake('a','b','c','d')

#def car(productor, size, **other):
#    info ={}
#    info['productor'] = productor
#    info['size'] = size
#    for key, value in other.items():
#        info[key] = value
#    return info
#a = car('china','35', colour='blue',door='open')
#print(a)

#class Dog:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def sit(self):
#        print(self.name + 'is sitting')
#    def roll(self):
#        print(self.name + 'is rolling')
#my_dog = Dog('Kuquan',100)
#my_dog.sit()

#class lestaurant:
#    def __init__(self,restaurant_name,cuisine_type):
#        self.name = restaurant_name
#        self.type = cuisine_type
#    def describe(self):
#        print('the restaurant is ' + self.name)
#        print('the cuisine type is ' + self.type)
#    def open_restaurant(self):
#        print('Opening!!!!!!!!')
#restaurant_my = lestaurant('qingfeng','president')
#restaurant_my.describe()
#restaurant_my.open_restaurant()

class car():
    def __init__(self,make,model,year):
        self.make = make
        self.year = year
        self.model = model
        self.read = '0'
    def get_describe(self):
        long_name = str(self.year) +' '+ self.make +' '+self.model + self.read
        return long_name
    def change(self,mile):
        self.read = mile

class ecar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.ele = 100
    def ele0(self):
        print('ele is ' + str(self.ele))
mynewcar = ecar('china','xi',1989)
mynewcar.ele0()



