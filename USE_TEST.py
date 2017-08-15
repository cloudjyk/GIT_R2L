#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class mydict(dict):
    """docstring for mydict"""
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        # try:
        #     return self[key]
        # except KeyError:
        #     raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        pass
    def __setattr__(self,key,value):
        self[key] = value
a=mydict(a=1231,b='32131')
# print(a.a)
# print(a.b)
# print(a['a'])
# print('Next...')
# for n in a:
#     print(n)

#     print(a.b)
    
#     print(a[n])
