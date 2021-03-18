#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:05:04 2021

@author: teles
"""


# ------------------------------------------------
### IMPORTS ###

import gmpy2
from gmpy2 import mpfr, exp
from numpy.linalg import solve
import matplotlib.pyplot as plt

import pandas as pd
import dataframe_image as dfi


bits = 32
#bits = 64

gmpy2.set_context(gmpy2.context(precision=bits))


# ------------------------------------------------
### FUNCTIONS ###
 

def mp(num):
    return mpfr(str(num))


def backf(val, digits=16):
    return list(map(lambda x: backf(x, digits), val)) if isinstance(val, list) else float(round(val, digits))


def integral(func, lower_lim, upper_lim, num_intervals, decimals=8):
    
    if (num_intervals % 2 != 0) or (num_intervals < 2):
        raise NameError("Invalid Number of Intervals: {} .".format(num_intervals))
    
    f = func
    a = mp(lower_lim)
    b = mp(upper_lim)
    Ni = num_intervals
    
    dx = (b-a)/Ni
    
    Intg = mp(0)
    
    for x in (a + 2*i*dx for i in range(int(Ni/2))):
        
        x0, x1, x2 = (x + i*dx for i in range(3))
        
        M = [[x**2, x, mp(1)] for x in [x0, x1, x2]]
        
        l = [f(x) for x in [x0, x1, x2]]
        
        A, B, C = (mp(coef) for coef in solve(backf(M), backf(l)))
        
        parab_primitv = lambda x: (A/3)*x**3 + (B/2)*x**2 + C*x
        
        Intg += (parab_primitv(x2) - parab_primitv(x0))
    
    #return backf(Intg, decimals)
    return Intg

# ------------------------------------------------
### TESTS ###


f = lambda x: [exp(xi) for xi in x] if isinstance(x, list) else exp(x)

a = 0
b = 0.1

Ni = 2



# ------------------------------------------------
### COMPARISON ###


trueVal = (f(b) - f(a))
approx  = integral(f, a, b, Ni)


results = pd.DataFrame(columns='Approximation AnalyticValue Error RelativeError PercentageError'.split())
results.index.names = ['Intervals_&_dx ']


dx_list, erp_list = [], []

for Ni in range(2, 20, 2):
    
    approx = integral(f, a, b, Ni)
    
    ea = trueVal - approx
    er = abs(ea/trueVal)
    erp = er*100
    
    dx = (b-a)/Ni
    dx_list.append(dx)
    erp_list.append(erp)
    
    results.loc['{:0>4d} & {:^6.5f}'.format(Ni, round(dx, 5))] = '{:<10.8f} {:<10.8f} {:.15f} {:.15f} {:.15f}%'.format(approx, trueVal, ea, er, erp).split()
    
    
print('------------------------------------------------')
print('\n\nSingle precision (32 bits)') if bits==32 else print('\n\nDouble precision (64 bits)')
print( '\n\nFunction:       exp(x)\nIntegral: exp(x)\n\n\tIntegration interval: [0; 0.1]\n\nAnalyt. Value:{:<10.8f}\n'.format(trueVal))
print('\nResults:\n')
print(results)
print('------------------------------------------------')


(fig, ax) = plt.subplots()

dx_list = backf(dx_list)
erp_list = backf(erp_list)

ax.plot(dx_list, erp_list, 'o:b')
ax.set_ylabel("Percentage Error")
ax.set_xlabel("dx")
ax.set_title("Convergence Analysis")



fig.savefig('numeric_intergral_3_{}_bits_graph_lin.png'.format(bits))
ax.set_xlabel("dx (logaritmic scale)")
ax.set_xscale("log")
fig.savefig('numeric_intergral_3_{}_bits_graph_log.png'.format(bits))




dfi.export(results, 'numeric_intergral_3_{}_bits_table.png'.format(bits))

























