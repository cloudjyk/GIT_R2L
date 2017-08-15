#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
class Student(object):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

s=Student('Bob',17,'male')
# print(s.name)
print(json.dumps(s,default = lambda s: s.__dict__ ))
def class2dict(self):
    return {'name':self.name,\
    'age':self.age,\
    'gender':self.gender
    }
print(json.dumps(s,default = class2dict))
ss=json.dumps(s,default = class2dict)
def dict2class(self):
    return Student(self['name'],self['age'],self['gender'])
cc=json.loads(ss,object_hook = dict2class)
print(cc.name,cc.age,cc.gender)