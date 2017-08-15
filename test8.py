#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('test.txt','r',encoding = 'GBK') as f :
    a=f.read()
    print(a)
with open('test.txt','w',encoding='GBK') as f :
    # a='hello world'.encode('ASCII')
    # print(a)
    # f.write(a)
    f.write('\nhello World 麦克')

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())