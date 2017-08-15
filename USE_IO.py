#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    f=open('F:/Py/test.txt','r')
    print(f.read())
finally:
    if f: f.close()

with open('test.txt','r',errors='ignore') as f:
    print(f.read(1))
    print(f.readline().strip())
    print(f.readline(2).strip())
    for x in f.readlines():
        print(x.strip())
    # print(f.readlines())
with open('test.txt','rb') as f:
    print(f.read())
# a=[1,2,3,4,5]
with open('test.txt','w') as f:
    f.write('dawjdiawhdawhudawuihdauh\ndawdawdawd\ndawdawd')
with open('test.txt','r') as f:
    print(f.read())