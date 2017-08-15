#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class HSG(object):
    """docstring for HSG"""
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
a=HSG()
print(hasattr(a,'x'))
print(hasattr(a,'y'))
setattr(a,'y',12)
print(hasattr(a,'y'))
print(getattr(a,'x'))
print(getattr(a,'y'))
print(getattr(a,'z','default'))
print(hasattr(a,'power'))
fn=getattr(a,'power')
print(fn())
fx=a.power
print(fx())
print(a.power())