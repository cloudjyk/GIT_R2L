#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# def abs(n):
#     '''
#     Function to get absolute value of number.

#     Example:

#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n>=0 else (-n)
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

def fact(n):
    '''
    >>>fact(1)
    1
    >>>fact(0)
    end
    >>>fact(4)
    24
    '''
    if n == 1:
        return 1
    if n < 1:
        raise ValueError('ValueError occured!')
        # print('end')
        # return
    return n*fact(n-1)
# fact(-1)
# fact(2)

if __name__=='__main__':
    import doctest
    doctest.testmod()