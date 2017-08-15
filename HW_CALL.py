#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self , path):
#         # if isinstance(path,str):
#         return Chain('%s/%s' % (self._path,path))
#         # else:
#         #     return Chain('%s/' % (self._path,))
#     def __call__(self,name):
#         return Chain('/==%s' % name)
#         # print('My name is %s.' % self.name)
#     def users(self,name):
#         return Chain('/%s' % name)

#     def __str__(self):
#         return self._path
#     __repr__ = __str__

# print(Chain().users('Micheal').repos)


class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        if path=='users':
            return lambda name:Chain('%s/users/%s'%(self._path,name))
        else:
            return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

print(Chain().users('lidu').repos)


# def Stu(path):
#     return lambda name:name
#     # print('%s' % return lambda name:name)
# Stu(path('mike'))