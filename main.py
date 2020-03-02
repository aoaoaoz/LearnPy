# -*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
    delta = b*b-4*a*c
    if delta < 0 : return
    delta = math.sqrt(delta)
    return (-b+delta)/(2*a), (-b-delta)/(2*a)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')