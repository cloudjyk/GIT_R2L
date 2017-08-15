#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
    """docstring for Student"""
    __slots__ = ('name','score','age')
    gender = 'female'
    def __init__(self, name = 'Bill', score = 100):
        # super(Student, self).__init__()
        self.name = name
        self.score = score
        self.age = 18
    # age = 28
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
    

    # def add():
    #     print('HAHA')
class juniorStudent(Student):
    """docstring for juniorStudent"""
    __slots__ = ('gender')
    def __init__(self, name):
        # super(juniorStudent, self).__init__()
        self.name = name
        
if __name__ == '__main__':
    def welcome(self):
        self.pdd = 'lalala'
        print('hello %s' % self.name)
    Student.welcome = MethodType(welcome,Student)
    # Student.welcome2 = welcome

    susan = Student('Susan',87)
    print(susan.__slots__)
    print(susan.name)
    susan.print_score()
    susan.welcome()
    # susan.welcome2()
    print(susan.pdd)


    # print('1 round\n',Student.age)
    # print(susan.age)
    # Student.age = 28
    # print('2 round\n',Student.age)
    # print(susan.age)
    # susan.age = 8
    # Student.age = 28
    # print('3 round\n',Student.age)
    # print(susan.age)
    # del Student.age
    # print(susan.age)

    print(susan.gender)
    # del Student.gender
    # print(susan.gender)
    bob = juniorStudent('bob')
    print(Student.gender)
    bob.gender = 'male'
    print(bob.gender)
    bob.age = 5