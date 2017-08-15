#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__ = 'JYK'
import sys
def hello():
    args = sys.argv
    print(args,'\n')
    if len(args) == 1:
        print('hello,world')
    elif len(args) == 2:
        print('hello,%s!' % args[1])
    else:
        print('Too many inputs!')
if __name__ == '__main__':
    hello()