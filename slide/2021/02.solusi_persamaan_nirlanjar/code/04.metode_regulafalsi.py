#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:57:20 2021

@author: fafa
"""
import numpy as np

a = 0
b = 1
f = lambda x: np.exp(x) - 5*x**2
epsilon1 = 0.00001
epsilon2 = 0.000001
i = 0

for i in range(0,200,1):
    c = b - f(b)/2 * (b - a) / (f(b)/2 - f(a))
    
    if abs(a-b) < epsilon1 or abs(f(c)) < epsilon2:
        break
    
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c
    
    print("Iterasi ke-{:02d} akar = {:.6f} lebar = {:.6f}".format(i, c, b-a))