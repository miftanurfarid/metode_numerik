#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Penyulihan Mundur (Backward Substitution)

Created on Mon Oct 11 17:11:47 2021

@author: fafa
"""

import numpy as np

A = np.array([[4, -1, 2, 3], 
              [0, -2, 7, -4], 
              [0, 0, 6, 5], 
              [0, 0, 0, 3]])
b = np.array([[20],[-7],[4],[6]])
x = np.zeros(b.shape)
n = b.size

x[n-1] = b[n-1]/A[n-1,n-1]

for k in range(n-2,-1,-1):
    sigma = 0
    for j in range(k+1,n,1):
        sigma += A[k,j] * x[j]
    x[k] = (b[k] - sigma) / A[k,k]
print("x = {}".format(x))