#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager
class Query(object):

    def __init__(self, name):
        self.name = name

    # def __enter__(self):
    #     print('Begin')
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     print(exc_type,exc_value,traceback)
    #     if exc_type:
    #         print('Error')
    #     else:
    #         print('End')

    def query(self):
        print('Query info about %s...' % self.name)
@contextmanager
def do_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


if __name__ == '__main__':
    with do_query('Lucy') as f:
        f.query()