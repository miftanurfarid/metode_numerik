#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 06:27:22 2021

@author: fafa
"""
import numpy as np

A = np.array([[2, 3, -1], 
              [4, 4, -3], 
              [-2, 3, -1]])
b = np.array([[5],[3],[1]])
x = np.zeros(b.shape)
n = b.size

for k in range(0,n-1,1):
    for i in range(k+1,n,1):
        m = A[i,k] / A[k,k]
        for j in range(k,n):
            A[i,j] = A[i,j] - m*A[k,j]
        b[i] = b[i] - m*b[k]

x[n-1] = b[n-1]/A[n-1,n-1]

for k in range(n-2,-1,-1):
    sigma = 0
    for j in range(k+1,n,1):
        sigma += A[k,j] * x[j]
    x[k] = (b[k] - sigma) / A[k,k]
print("x = {}".format(x))