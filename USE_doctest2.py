#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError: ValueError occured!
    >>> fact(4)
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