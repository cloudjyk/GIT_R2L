# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    def fdot(s):
        n=0
        for x in s:
            if x=='.':
                break
            else:
                n+=1
        return n
    def str2int(s):
        y=[]
        for x in s:
            if '0'<= x <= '9':
                y.append(int(x))
            else:
                pass
        return y
    def num(x,y):
        return x*10+y
    return reduce(num,str2int(s))/(10**fdot(s))