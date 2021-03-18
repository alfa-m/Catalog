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
import matplotlib.pyplot as plt

import pandas as pd
import dataframe_image as dfi


bits = 32
# bits = 64

gmpy2.set_context(gmpy2.context(precision=bits))


# ------------------------------------------------
### FUNCTIONS ###
 

def mp(num):
    return mpfr(str(num))


def backf(val, digits=5):
    return list(map(lambda x: backf(x, digits), val)) if isinstance(val, list) else float(round(val, digits))


def integral(func, lower_lim, upper_lim, num_intervals, decimals=8):
    
    f = func
    a = mp(lower_lim)
    b = mp(upper_lim)
    Ni = num_intervals
    
    dx = (b-a)/Ni
    
    Intg = dx/2 * ( f(a) + 2*sum(f(a + i*dx) for i in range(1, Ni)) + f(b) )
    
    return backf(Intg, decimals)

# ------------------------------------------------
### TESTS ###


f = lambda x: [exp(xi) for xi in x] if isinstance(x, list) else exp(x)

a = 0
b = 0.1

Ni = 5



# ------------------------------------------------
### COMPARISON ###


trueVal = backf(f(b) - f(a), 8)
approx  = integral(f, a, b, Ni)


results = pd.DataFrame(columns='Approximation AnalyticValue Error RelativeError PercentageError'.split())
results.index.names = ['Intervals_&_dx ']


dx_list, erp_list = [], []

for Ni in range(1, 20):
    
    approx = integral(f, a, b, Ni)
    
    ea = trueVal - approx
    er = abs(ea/trueVal)
    erp = er*100
    
    dx = (b-a)/Ni
    dx_list.append(dx)
    erp_list.append(erp)
    
    results.loc['{:0>4d} & {:^6.5f}'.format(Ni, round(dx, 5))] = '{:<10.8f} {:<10.8f} {:^10.8f} {:^10.8f} {:f}%'.format(approx, trueVal, ea, er, erp).split()
    
    
print('------------------------------------------------')
print('\n\nSingle precision (32 bits)') if bits==32 else print('\n\nDouble precision (64 bits)')
print( '\n\nFunction:       exp(x)\nIntegral: exp(x)\n\n\tIntegration interval: [0; 0.1]\n\nAnalyt. Value:{:<10.8f}\n'.format(trueVal))
print('\nResults:\n')
print(results)
print('------------------------------------------------')


(fig, ax) = plt.subplots()

ax.plot(dx_list, erp_list, 'o:b')
ax.set_ylabel("Percentage Error")
ax.set_xlabel("dx")
ax.set_title("Convergence Analysis")

fig.savefig('numeric_intergral_2_{}_bits_graph_lin.png'.format(bits))
ax.set_xlabel("dx (logaritmic scale)")
ax.set_xscale("log")
fig.savefig('numeric_intergral_2_{}_bits_graph_log.png'.format(bits))




dfi.export(results, 'numeric_intergral_2_{}_bits_table.png'.format(bits))

























