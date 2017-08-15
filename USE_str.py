#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        # super(Student, self).__init__()
        self.name = name
    def __str__(self):
        return ('Student object (name: %s)' % self.name)
    __repr__ = __str__
s=Student('Micheal')
print(s)