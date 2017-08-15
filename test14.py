#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def my_print():
    d = ''
    while True:   
        c = yield d
        d = 'I love %s' % c
        print(d)
if __name__ == '__main__':
    c=my_print()
    d=c.send(None)
    print(d*3)
    d=c.send('Mike')
    print(d*2)
    c.close()