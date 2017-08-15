#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)

def fn(self,name='world'):
    print('Hello,%s' % name)
Hello = type('Hello',(object,),dict(hello = fn))
h=Hello()
h.hello('Micheal')