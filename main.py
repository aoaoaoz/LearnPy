# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[1]
    pass
L2 = sorted(L, key = by_name, reverse = True)
print(L2)