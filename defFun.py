# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
#参数检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-2),my_abs(1))

import math

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
(nx,ny)=move(0,0,20,30)
print(nx,ny)
