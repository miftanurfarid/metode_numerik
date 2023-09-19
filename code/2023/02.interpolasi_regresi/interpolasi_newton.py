#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:23:09 2023

@author: fafa
"""
import numpy as np

x = [-1.2, 0.3, 1.1]
y = [-5.76, -5.61, -3.69]
n = len(x) - 1
xp = float(input('Masukkan nilai x: '))
Dy = np.zeros((n+1, n+1))
Dy[:,0] = y

for j in range(n):
    for i in range(j+1, n+1):
        Dy[i,j+1] = (Dy[i,j]-Dy[j,j])/(x[i]-x[j])
        
yp = Dy[0,0]

for i in range(n):
    xprod = 1
    for j in range(i+1):
        xprod *= xp - x[j]
    yp += xprod*Dy[i+1,i+1]
    
print('Untuk x = %.1f, y = %.4f' % (xp, yp))
