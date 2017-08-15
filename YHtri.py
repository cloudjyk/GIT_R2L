# -*- coding: utf-8 -*-
def YH(max):    
    # L=[1]
    # yield L
    # n=2
    # while n-1<max:
    #     yield L
    #     L.insert(0,0)
    #     L.append(0)
    #     for x in range(0,n):
    #         L[x]=L[x]+L[x+1]
    #     L.pop()
    #     n=n+1
    # return'done'


#大神
    # L=[1]
    # while True:
    #     yield L
    #     L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]
    


    #最终版
    L=[1]
    while len(L) <= max:
        yield L
        L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]
if __name__ == '__main__':
    for i in YH(5):
        print(i)