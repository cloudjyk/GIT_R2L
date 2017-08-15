#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def getattr(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def setattr(self,key,value):
        self[key] = value


dd={'a':11,'b':22}
c=Dict(**dd)
print(c['a'])