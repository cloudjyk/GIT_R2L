#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
    """docstring for Student"""
    def __init__(self, name = 'Bill', score = 100):
        # super(Student, self).__init__()
        self.__name = name
        self.__score = score
    # age = 28
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    # def add():
    #     print('HAHA')

        
if __name__ == '__main__':
    susan = Student('Susan',87)
    susan.print_score()

    print(susan.score)
    susan.score = 99
    print(susan.score)
