#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:23:29 2021

@author: fafa
"""
import numpy as np

n = 3 # order
ST = np.zeros((n+1,n+1)) # tabel kosong selisih terbagi
X = np.array([8.0, 9.0, 9.5, 11.0])
y = np.array([2.079442, 2.197225, 2.251292, 2.397895])
x = 9.2

# simpan y[k] pada kolom 0 dari matriks ST
for k in range(n+1):
    ST[k,0] = y[k]
    
# buat tabel selisih terbagi
for k in range(1,n+1):
    for i in range(0,n-k+1):
        ST[i,k] = (ST[i+1,k-1] - ST[i,k-1]) / (X[i+k]-X[i])
        
# hitung p(x)
jumlah = ST[0,0]
for i in range(1,n+1):
    suku = ST[0,i]
    for k in range(i):
        suku = suku*(x-X[k])
    jumlah = jumlah + suku
    #print(jumlah)