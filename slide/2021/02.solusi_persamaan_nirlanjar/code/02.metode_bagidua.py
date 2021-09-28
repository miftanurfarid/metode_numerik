#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 03:55:46 2021

@author: fafa
"""
import numpy as np

a = -0.5
b = -0.25
f = lambda x: np.exp(x) - 5*x**2
epsilon = 0.000001

while abs(a - b) > epsilon:
    c = (a + b) / 2
    
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print('Akar : %0.5f' % c )