#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def TRI_ang(max):
    # if max == 1:
    #     return [1]
    # else:
    #     # L=[]
    #     # for i in range(len(TRI_ang(max-1))-1):
    #     #     # print(i)
    #     #     # print(TRI_ang(max-1))
    #     #     L.append(TRI_ang(max-1)[i]+TRI_ang(max-1)[i+1])
    #     # return [1]+L+[1]
    #     # print([1]+[(lambda i: TRI_ang(max-1)[i]+TRI_ang(max-1)[i+1])(i) for i in range(len(TRI_ang(max-1))-1)]+[1])
    #     yield [1]+[(lambda i: TRI_ang(max-1)[i]+TRI_ang(max-1)[i+1])(i) for i in range(len(TRI_ang(max-1))-1)]+[1]
    L=[1]
    while len(L) < max+1:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
if __name__ == '__main__':
    for i in TRI_ang(15):
        print(i)