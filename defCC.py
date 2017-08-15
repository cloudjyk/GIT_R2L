#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name):
        self.name = name
    score=59
s = Student('Bob')
print(Student.score)
print(s.score)
s.score = 90
print(Student.score)
print(s.score)
# del s.score
# print(Student.score)
# print(s.score)
print('test----')
Student.score=99
print(Student.score)
print(s.score)
del Student.score
print(s.score)
print(Student.score)