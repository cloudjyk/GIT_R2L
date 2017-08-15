# -*- coding: utf-8 -*-
from functools import reduce
def prob(s):
    def mul(x,y):
        return x*y
    return reduce(mul,s)