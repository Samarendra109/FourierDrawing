# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:02:29 2020

@author: Samarendra
"""

from cmath import exp,sqrt,pi

j = sqrt(-1)

def rotate(z,phi):
    return z*exp(phi)

def fourierSeries(z,N):
    
    L = len(z)
    Z = [0]*(2*N+1)
    
    for n in range(-N,N+1):
        for x in range(L):
            Z[n] += z[x] * exp((-2*pi*j*x*n)/L)
        Z[n] = Z[n]/L
            
    return Z