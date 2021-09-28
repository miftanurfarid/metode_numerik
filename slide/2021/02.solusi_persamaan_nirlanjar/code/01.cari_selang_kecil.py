#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 03:10:47 2021

@author: fafa
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(x) - 5*x**2
a = -0.5
b = 1.4
h = 0.1
x = np.arange(a,b+h,h)
y = f(x)

plt.plot(x,y)
plt.grid(axis='both')