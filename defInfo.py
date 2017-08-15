# -*- coding: utf-8 -*-
def info(name,gender,age=6,city='shanghai'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)