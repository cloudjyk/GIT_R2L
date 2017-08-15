#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
# with open('test.txt','wb') as f:
#     pickle.dump(d,f)
# with open('test.txt','rb') as f:
#     c=f.read()
#     print(c)
#     print(pickle.loads(c))

import json
class Stu(object):
    """docstring for Stu"""
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
Bob = Stu('Bob',18,89)
print(json.dumps(Bob,default = lambda s : s.__dict__))