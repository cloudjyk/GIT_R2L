#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class WEEK(object):
    """d*nametring for WEEK"""
    def __init__(self, name, members, *n):
        # super(WEEK, self).__init__()
        # if isinstance(name,int):
        #     print(list(self.__members__.keys())[name])
        #     return
        self.name=name
        self.__members__={}
        
        for x in members:
            self.__members__[x] = name+'.'+x
        # print(type(n))
        # print(n)
        if n:
                self.n=list(n)
                # print(n)
                # print(self.n)
                # x=self.n[0]
                y=self.n[0]
                if isinstance(y,list):
                    y0=y[0]
                else:
                    y0=y
                # print(y)
                # y=y[0]
                self.output = list(self.__members__.keys())[y0]
                if len(self.n) > 1:
                # if self.n[1] == 100:
                    self.output = self.n[0]
        # return self.output
    def __getattr__(self,attr):
        if attr in self.__members__:
            # n = mm.index(attr)
            return WEEK(name,list(self.__members__.keys()),list(self.__members__.keys()).index(attr))
        elif attr == 'value':
            self.n.append(100)
            # print('ww',self.n)
            return WEEK(name,list(self.__members__.keys()),self.n)
            # print(self.n[0])
    # def value(self):
    #     return n
            # n+=1
    def __str__(self):
        return str(self.output)
    __repr__ = __str__

    # class member(object):
    #     """docstring for member"""
    #     def __init__(self, name, members, *n):

    #     def value(self, arg):
    #         return member
            


Week=WEEK('Week',('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'))
for name, member in Week.__members__.items():
    print(name, '=>', member)

print(Week.Tue.value)
print(Week.Fri)
# Week(2)