#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:16:10 2021

@author: fafa
"""

from numpy import linspace
import matplotlib.pyplot as plt
from numpy import cos

x = linspace(3, 8, 1000)
y = lambda x: -cos(x) + 2

fx = y(x)
plt.plot(x,fx)
plt.grid(axis = 'both')
plt.ylim(0, 4)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['$f(x) = 2 - cos(x)$'])
plt.savefig('img001.svg', format='svg', dpi=1200)
plt.savefig('img001.png', format='png', dpi=1200)