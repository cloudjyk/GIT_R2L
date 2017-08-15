#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def HM(n,A,B,C):
    if n==1:
        print('%s-->%s' % (A,C))
    else:
        HM(n-1,A,C,B)
        print('%s-->%s' % (A,C))
        HM(n-1,B,A,C)
if __name__ == '__main__':
    HM(2,'A','B','C')