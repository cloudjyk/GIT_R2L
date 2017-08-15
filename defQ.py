# -*- coding: utf-8 -*-
def quadratic(a, b, c):
    import math
    s=b**2-4*a*c
    if s>=0:
        ans1=(-b+math.sqrt(s))/(2*a)
        ans2=(-b-math.sqrt(s))/(2*a)
        print('ans1=%f,ans2=%f'%(ans1,ans2))
        return ans1,ans2
    else:
        print('No rational solution!')
        return