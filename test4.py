#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self, name = ' '):
        # super(Student, self).__init__()
        self.name = name
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __str__(self):
        return 'Why do you wake me up? I\'m %s' % self.name
    __repr__ = __str__

    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self,n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    def __getattr__(self,attr):
        if attr == 'score':
            return '99'
        else:
            return Student('%s/%s' % (self.name,attr))
    def __call__(self,num):
        # n=1
        # while n < num:
        #     n+=1
        #     print('Why~~~')
        # print('Why are you call me?')
        return Student('%s:%s' % (self.name,num))
if __name__ == '__main__':
    print(Student('Mike').a,'#\n')
    Student('Lucy')

for n in Student('Mike'):
    print(n)
    print('#\n',Student('Mike').a)
print('#\n',Student('Mike').a)

print(Student('Mike')[0],'\n',Student('Mike')[1:24])

print(Student('Susan').score)

print(Student('Susan').status.user.timeline.list)
print(Student('Susan').status('WELL').user('Susan').timeline.list)
a='Dan'

print(Student('%s' % a))

s=Student('Lily')
s(10)