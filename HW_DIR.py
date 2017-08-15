#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
# def dir_sort():
#     a=os.listdir()
#     a.sort()
#     for x in a:
#         print(x)


# def search_sth(sam):
#     L=[]
#     # ss=31919191
#     def se():
#         a=[x for x in os.listdir() if os.path.isfile(x)]
#         if not a:
#             return 
#         R=[]
#         absPL=len(os.path.split(os.path.abspath(__file__))[0])
#         # print(os.path.split(os.path.abspath(__file__))[0],absPL)
#         for x in a:
#             if len(x.split('.')[0]) >= len(sam) and sam in x.split('.')[0]:
#                 # for y in range(len(x.split('.')[0])-len(sam)):
#                 #     if x[y:y+len(sam)] == sam:
#                         # R.append(os.path.abspath('.'))
#                         # print(os.path.abspath('.'))
#                 R.append(os.path.abspath('.')[absPL:])
#         if R:
#             # print(R)
#             return R
#     def se_dir():
#         L=[]
#         # print(L)
#         # a=ss
#         # print(ss,'????')
#         # ss=1010101
#         # print(ss)
#         a=[x for x in os.listdir() if os.path.isdir(x)]
#         if not a:
#                 return
#         for y in a:
#             os.chdir(y)
#             T=search_sth(sam)
#             if T:
#                 L.extend(T)
#                 # print(L)
#             os.chdir('..')
#         # print(L)
#         return L
#     T=se()
#     if T:
#         L.extend(T)
#         # print(L)
#     T=se_dir()
#     if T:
#         L.extend(T)
#         # print(L)
#     # print(ss)
#     return L
# print(search_sth('HW'))


# upgrade version
def S_sth(dir,sam):
    def search_sth(dir,sam):
        os.chdir(dir)
        L=[]
        def se():
            a=[x for x in os.listdir() if os.path.isfile(x)]
            if not a:
                return 
            R=[]
            for x in a:
                if len(x.split('.')[0]) >= len(sam) and sam in x.split('.')[0]:
                    R.append(os.path.abspath('.'))
            if R:
                return R
        def se_dir():
            L=[]
            a=[x for x in os.listdir() if os.path.isdir(x)]
            if not a:
                    return
            for y in a:
                os.chdir(y)
                # print(dir+'/'+y)
                T=search_sth(dir+'/'+y,sam)
                if T:
                    L.extend(T)
                os.chdir('..')
            return L
        T=se()
        if T:
            L.extend(T)
        T=se_dir()
        if T:
            L.extend(T)
        return L
    res=search_sth(dir,sam)
    for x in range(len(res)):
        res[x]=res[x][len(dir):]
    return res
print(S_sth('F:/Py','HW'))