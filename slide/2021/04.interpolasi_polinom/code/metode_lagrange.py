#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:12:29 2021

@author: fafa
"""
import numpy as np


n = 3
X = np.array([1, 4, 6])
x = 3.5
y = np.array([1.5709, 1.5727, 1.5751])
L = 0

for i in range(n):
    pi = 1
    for j in range(n):
        if i != j:
            pi = pi*(x - X[j])/(X[i] - X[j])
    L = L + y[i]*pi

print("p_2({}) = {:.5}".format(x,L))