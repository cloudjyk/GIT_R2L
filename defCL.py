#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
mike=Student('Mike',59)
lucy=Student('Lucy',98)
mike.print_score()
lucy.print_score()
mike.age=18
print(mike.age)
# def print_score(std):
#     print('%s: %s' % (std.name, std.score))
# print_score(mike)