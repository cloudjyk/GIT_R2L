#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self):
        self.name = 'Mike'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        # else:
        #     raise AttributeError('\'Object Student\' does not have attribute: %s' % attr)
        # pass
s=Student()
print(s.name)
print(s.score)
print(s.age)
# raise AttributeError('\'Object Student\' does not have attribute: ')