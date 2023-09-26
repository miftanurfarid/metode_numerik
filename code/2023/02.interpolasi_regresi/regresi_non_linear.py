#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:31:18 2023

@author: fafa
"""

import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([2, 8, 14, 28])

m = len(x) # jumlah data
n = 2 # derajat polinomial

A = np.zeros((n+1, n+1))
B = np.zeros(n+1)
a = np.zeros(n+1)

# Loops of system formation
for row in range(n+1):
    for col in range(n+1):
        if row == 0 and col == 0:
            A[row,col] = m
            continue
        A[row,col] = np.sum(x**(row+col))
    B[row] = np.sum(x**(row) * y)

a = np.linalg.solve(A,B) # solusi dari sistem pers. linear [A]{a}={B}

# menampilkan bentuk polinomial
print('Polinomial: \n')
print('f(x) =\t %f \t'% a[0])
for i in range(1, n+1):
    print('\t %+f x^%d'%(a[i],i))