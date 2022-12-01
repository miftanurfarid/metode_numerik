#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:08:38 2022

@author: fafa
"""

import numpy as np

x = np.array([
    0.0000,
    0.3365,
    0.6731,
    1.0097,
    1.3463,
    1.6829,
    2.0195,
    2.3561
    ])

fx = np.array([
    0.0000,
    0.3302,
    0.6234,
    0.8467,
    0.9749,
    0.9937,
    0.9009,
    0.7071
    ])

# soal nomer 4
# cari hasil integral fx dari 0.5 sampai 1.5
h = x[1] - x[0]
int_fx = h / 2 * (fx[0] + 2*(fx[1]+fx[2]+fx[3]+fx[4]+fx[5]+fx[6]) + fx[7])
print(int_fx)