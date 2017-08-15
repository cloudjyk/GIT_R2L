# -*- coding: utf-8 -*-
from functools import reduce
def is_palindrome(n):
    # def  SA(x,y):
    #     return x+y
    return n>10 and str(n) == ''.join([str(n)[len(str(n))-1-x] for x in range(len(str(n)))])
    # return str(n)==str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))