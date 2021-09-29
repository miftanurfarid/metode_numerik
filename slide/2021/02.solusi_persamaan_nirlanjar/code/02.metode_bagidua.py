#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 03:55:46 2021

@author: fafa
"""
import numpy as np

a = 0
b = 1
f = lambda x: np.exp(x) - 5*x**2
epsilon = 0.00001
i = 0

for i in range(0,200,1):
    c = (a + b) / 2
    
    if abs(a-b) < epsilon:
        break
    
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c
    
    print("Iterasi ke-{:02d} akar = {:.6f} lebar = {:.6f}".format(i, c, b-a))