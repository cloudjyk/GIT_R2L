#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student():
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('Width must be an integer!')
        if value<=0:
            raise ValueError('width must be bigger than 0!')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('Height must be an integer!')
        if value<0:
            raise ValueError('Height must be bigger than 0!')
        self._height = value
    @property
    def resolution(self):
        return self.width*self.height
s=Student()
s.width=10
s.height=20
print('The area of s is : %d * %d = %d' % (s.width,s.height,s.resolution))