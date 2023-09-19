#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:26:19 2023

@author: fafa
"""

x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]
m = len(x)
n = m-1
xp = float(input('Masukkan nilai x: '))

yp = 0
for i in range(n+1):
    L = 1
    for j in range(n+1):
        if j != i:
            L *= (xp - x[j])/(x[i] - x[j])
    yp += y[i]*L
print('Untuk x = %.1f, y = %.4f' % (xp, yp))