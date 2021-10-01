#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:46:04 2021

@author: fafa
"""
import numpy as np

dg1 = lambda x: x**2
dg2 = lambda x: 2*x / (x**2 - 3)**3
dg3 = lambda x: (-3*x+2)/x**3

for x in np.arange(1,2.1,0.1):
    print("x={:0.2f} \t |g'(x)|={:.6f}".format(x,abs(dg3(x))))