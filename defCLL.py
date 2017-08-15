#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
    """docstring for Student"""
    # def __init__(self, arg):
    #     super(Student, self).__init__()
    #     self.arg = arg
    __slots__=('name','age','set_age')
def set_age(a,age):
    a.age=age
# Student.set_age=MethodType(set_age,Student)
s=Student()
Student.set_age=set_age
# s.set_age=set_age
s.set_age(12)
print(s.age)
s.name='mike'
print(s.name)
# s.set_age=MethodType(set_age,s)
# s.set_age(24)
# print(s.age)
# s.score=10