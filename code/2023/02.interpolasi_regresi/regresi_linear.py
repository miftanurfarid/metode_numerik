#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:31:18 2023

@author: fafa
"""

import numpy as np

x = np.array([1, 2.5, 3.5])
y = np.array([6.008, 15.722, 27.13])
n = len(x) # jumlah data

sumx = sumx2 = sumxy = sumy = 0
for i in range(n):
    sumx += x[i]
    sumx2 += x[i]**2
    sumxy += x[i]*y[i]
    sumy += y[i]

xm = sumx / n # rata-rata nilai x
ym = sumy / n # rata-rata nilai y

a = (ym*sumx2 - xm*sumxy)/(sumx2 - n*xm**2)
b = (sumxy - xm*sumy)/(sumx2 - n*xm**2)

print('Persamaan linear:')
print('f(x) = (%.3f) + (%.3f)x'%(a,b))