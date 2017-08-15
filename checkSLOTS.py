#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def set_age(self,age):
    self.age=age

class Stu(object):
    pass
from types import MethodType
Stu.set_age=MethodType(set_age,Stu)
# Stu.set_age=set_age
# class Stu(object):
#     def set_age(self,age):
#         self.age=age
s=Stu()
a=Stu()
a.set_age(15)
# \通过set_age方法，设置的类属性age的值
s.set_age(11)
# \也是设置类属性age的值，并把上个值覆盖掉
print(s.age,a.age)
Stu.age=22
print(s.age,a.age,Stu.age)
# \\由于a和s自身没有age属性，所以打印的是类属性age的值

a.age = 10 
# \\给实例a添加一个属性age并赋值为10
s.age = 20 
# \\给实例b添加一个属性age并赋值为20
# \\这两个分别是实例a和s自身的属性，仅仅是与类属性age同名，并没有任何关系
s.set_age(11)
print(s.age,a.age,Stu.age)  
# \\打印的是a和s自身的age属性值，不是类age属性值