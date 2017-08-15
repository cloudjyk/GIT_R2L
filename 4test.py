#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        # super(Student, self).__init__()
        self.name = name

    def __str__(self):
        return 'Why do you wake me up? I\'m %s' % self.name
    __repr__ = __str__




if __name__ == '__main__':
    print(Student('Mike'))
    Student('Lucy')