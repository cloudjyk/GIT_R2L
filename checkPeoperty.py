#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# class Student(object):
#rgular one
#rgular one
    # def get_score(self):
    #      return self._score

    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value
#experience @property    
#experience @property   
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('Score must be an integer!')
#         if value<0 or value>100:
#             raise ValueError('Score must be between 1 ~ 100!')
#         self._score=value
# s=Student()
# # s.score=101
# s.score=99
# print(s.score)

#定义只读属性的property
#定义只读属性的property
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth
s=Student()
s.birth=1989
print(s.birth)
print(s.age)
s.age=27