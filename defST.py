# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def ST1(x):
    return x[0]
def ST2(x):
    return x[1]
R1 = sorted(L,key=ST1)
# R1 = sorted(L,key=lambda x:x[0])
print(R1)
R2 = sorted(L,key=ST2,reverse=True)
# R2 = sorted(L,key=lambda x:x[1],reverse=True)
print(R2)

# from operator import itemgetter
# R1 = sorted(L,key=itemgetter(0))
# print(R1)
# R2 = sorted(L,key=itemgetter(1),reverse=True)
# print(R2)

