#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Fib(object):
    """docstring for Fib"""
    # def __init__(self):
    #     self.a , self.b = 0 , 1
    def __getitem__(self , n):
        if isinstance(n, int):
            self.a , self.b = 0 , 1
            for x in range(n+1):
                self.a ,self.b =self.b , self.a + self.b
            return self.a
        if isinstance(n, slice):
            start,stop = n.start,n.stop
            L=[]
            if start == None:
                start = 0
                self.a , self.b = 0 , 1
                for x in range(stop+1):
                    self.a ,self.b =self.b , self.a + self.b
                    L.append(self.a)
                return L[:stop]
            else:
                self.a , self.b = 0 , 1
                for x in range(stop):
                    self.a ,self.b =self.b , self.a + self.b
                    L.append(self.a)
                return L[start:stop]
f=Fib()
print(f[44])
print(f[5:45])
print(f[2])
print(f[:3])
