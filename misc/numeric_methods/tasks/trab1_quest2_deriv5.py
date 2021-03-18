#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:40:11 2021

@author: teles
"""

# ------------------------------------------------
### IMPORTS ###

import gmpy2
from gmpy2 import mpfr, sin, cos
from numpy import pi, dot, diff, multiply
import pandas as pd

#import dataframe_image as dfi

# ------------------------------------------------
### FUNCTIONS ###

def deriv5 ( func, x, step):
    return dot([func(x + n*step) for n in range(-3,4)], [-0.5, 2, -2.5, 0, 2.5, -2, 0.5]) / step**5
    #return dot([func(x + n*step) for n in range(-3,4)], [mp(-0.5), (2), mp(-2.5), mp(0), mp(2.5), mp(-2), mp(0.5)]) / step**5

def mp(num):
    return mpfr(str(num))


def backf(num, step=None):
    if step == None:
        digits = int(-gmpy2.log10(num))
    else:
        digits = int(-gmpy2.log10(step))
        
    return float(round(num, digits))

# ------------------------------------------------
### TESTS ###


for bits in (32, 64):
    
    gmpy2.set_context(gmpy2.context(precision=bits))
    pi = mp(pi)
    
    func = lambda x: cos(2*pi*60*x)
    x = pi/4
    
    trueVal = (-mp(120)**5)*(pi**5)*sin(120*pi*x)
    
    
    results = pd.DataFrame(columns='Approximation Error SqError Error/AnalyVal'.split())
    results.index.names = ['Step ']
    
    
    for s in (mp(10)**-ex for ex in [2,5,10,20,60]):
        
        aprox = deriv5(func, x, s)
        
        err = backf(aprox - trueVal, s)
        err2 = backf( (aprox - trueVal)**2 , s)
        
        trueVal_err = abs((aprox-trueVal)/trueVal)
        trueVal_err = '{:f}'.format( trueVal_err ) if 1 > trueVal_err else ' >= 1.0'
        
        #trueVal_err = backf( abs(trueVal)/abs(aprox-trueVal), s )
        
        results.loc['{:e}'.format(backf(s))] = '{:e} {:e}'.format(aprox, err).split() + [err2, trueVal_err]
        
    print('------------------------------------------------')
    print('\n\nSingle precision (32 bits)') if bits==32 else print('\n\nDouble precision (64 bits)')
    print( '\n\nFunction:       cos(2pi60x)\n5th derivative: -((120pi)^2)*sin(2pi60x)\n\n\tx = pi/4\n\nAnalyt. Value:{:e}\n'.format(trueVal))
    print('\nResults sorted by Step:')
    print(results[['Approximation', 'Error']])
    print('\nResults sorted by Squared Error:')
    print(results[['Approximation', 'Error/AnalyVal', 'SqError']].sort_values(by='SqError'))
    print('------------------------------------------------')
    
    #dfi.export(results, 'results_{}.png'.format(bits))







# The error is getting bigger as the step gets smaller
# WHY ?
# It should be the opposite





# To seeing why:
#
# On simple precision (32) approximation dx=[10e-10, 10e-20, 10e-60] evaluates the cossine 7 times on the same point.
'''
So here, the error gets bigger from dx=10e-10 to dx=10e-60 because
they don't have enough digits to register the changes in the step,
they evaluate the function different times on same points, then,
when dividing by dx^2, the error grows.

Don't kno why the error gets bigger for dx=10e-5.
'''
#
# On double precision (64) approximation dx=10e-60 gets 0, and dx=10e-20 evaluates the cossine 5 times on the same point.
'''
Here, the error gets bigger from dx=10e-20 to dx=10e-60 because
they don't have enough digits to register the changes in the step,
they evaluate the function different times on same points, then,
when dividing by dx^2, the error grows.
'''
#
#
# 
'''

gmpy2.set_context(gmpy2.context(precision=32))
pi = mp(pi)
x = pi/4
func = lambda x: cos(2*pi*60*x)



gmpy2.set_context(gmpy2.context(precision=64))
pi = mp(pi)
x = pi/4
func = lambda x: cos(2*pi*60*x)


%clear


s = mp(10)**-2
s = mp(10)**-5
s = mp(10)**-10
s = mp(10)**-20
s = mp(10)**-60


[n*s for n in range(-3,4)]
diff([n*s for n in range(-3,4)])
[x + n*s for n in range(-3,4)]
diff([x + n*s for n in range(-3,4)])


[func(x + n*s) for n in range(-3,4)]
diff([func(x + n*s) for n in range(-3,4)])
multiply([func(x + n*s) for n in range(-3,4)], [mp(-0.5), (2), mp(-2.5), mp(0), mp(2.5), mp(-2), mp(0.5)])
diff(multiply([func(x + n*s) for n in range(-3,4)], [-0.5, 2, -2.5, 0, 2.5, -2, 0.5]))
sum(multiply([func(x + n*s) for n in range(-3,4)], [-0.5, 2, -2.5, 0, 2.5, -2, 0.5]))
s**5
dot([func(x + n*s) for n in range(-3,4)], [-0.5, 2, -2.5, 0, 2.5, -2, 0.5]) / s**5



'''














