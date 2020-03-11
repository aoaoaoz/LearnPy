# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

import numpy as np
import numpy.matlib

a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
print(np.linalg.det(a))
print(np.linalg.solve(a, b))
b = np.linalg.inv(a)
print(np.matmul(a, b))