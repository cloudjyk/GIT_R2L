#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=10240099
b1=int((n & 0xff000000)/(2**24))
print(b1)
b2=int((n & 0xff0000)/(2**16))
print(b2)
b3=int((n & 0xff00)/(2**8))
print(b3)
b4=(n & 0xff)
print(b4)
bs=bytes([b1,b2,b3,b4])
print(bs)