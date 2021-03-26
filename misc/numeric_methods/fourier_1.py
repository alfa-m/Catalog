#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:21:50 2021

@author: teles
"""


# ------------------------------------------------
### IMPORTS ###

from gmpy2 import context, set_context
from gmpy2 import mpfr, sqrt, const_pi, exp, sin, cos, polar, norm

import matplotlib.pyplot as plt
from seaborn import set_style

# ------------------------------------------------
### DEFINITIONS ###

set_style('darkgrid')

bits=64
set_context(context(precision=bits, allow_complex=True))

I = sqrt(-1)

pi = const_pi(bits)

# ------------------------------------------------
### FUNCTIONS ###


def backf(val, digits=8):
    return [backf(v, digits) for v in val] if isinstance(val, (list, tuple, map, zip)) else float(round(val, digits))


def fourier(func, dt, freq_max):
    
    g = func
    N = len(g)
    Wf = N
    
    dt = mpfr(dt)
    t = [ dt*n for n in range(N) ]
    
    dw = mpfr(freq_max) / (N-1)
    f = [ dw*n for n in range(N) ]
    
    G = [0] * Wf
    
    for w in range(Wf):
        
       G[w] = sum( g[n]*exp(2*I*pi*f[w]*t[n])*dt  for n in range(N) )
    
    return f, G


def inv_fourier(transf, dt, freq_max):
    
    G = transf
    N = len(G)
    Wf = N
    
    dt = mpfr(dt)
    t = [ dt*n for n in range(N) ]
    
    dw = mpfr(freq_max) / (N-1)
    f = [ dw*n for n in range(N) ]
    
    g = [0] * N
    
    for n in range(N):
        
       g[n] = sum( G[w]*exp(-2*I*pi*f[w]*t[n])*dw  for w in range(Wf) )
    
    return backf(map(lambda x: x.real, g))




# ------------------------------------------------
### PARAMETERS ###



# ------------------------------------------------
### TESTS ###

# make a sum of sine waves that is o slide

N = 1256

dt = 0.02

fsin = lambda A, f, dt, theta, poins: backf([ A*sin(f*x*dt + theta) for x in range(poins) ])

fsum = lambda f1, f2: [ x1+x2 for x1,x2 in zip(f1,f2)]

t = [t*dt for t in range(N)]
g = fsin((1/1), 1, dt, 0, N)

for n in [3,5,7,9,11]:
    g = fsum(g, fsin((1/n), n, dt, 0, N))


# ------------------------------------------------
### COMPARISON ###

freq_max = 15/(2*pi)

f,G = fourier(g, dt, freq_max)

f = backf(f)

G_amp, G_phase = backf(zip(* map(polar, G)))

inv_g = inv_fourier(G, dt, freq_max)

# ------------------------------------------------
### PLOTS ###

(fig, ax) = plt.subplots(2,1)

ax[0].plot(t, g,  'b',lw=4, label="Aproximation from Fourier Series Coefficients")
ax[0].plot(t, inv_g, 'r', lw=2, label="Inverse Fourier Transform")
#ax[0].plot(t, aaa, 'r', lw=2, alpha=0.7, label="Inverse Fourier Transform")
ax[0].set_title("Square Wave")
ax[0].set_ylim([-1,1])
ax[0].set_xlabel("time")
ax[0].legend(loc=3)

ax[1].plot(f, G_phase,'r',lw=2, alpha=0.7, label="Phase")
ax[1].plot(f, G_amp,'b',lw=4, label="Amplitude")
ax[1].set_xlabel("frequency")
ax[1].set_title("Fourier Transform")
ax[1].legend(loc=2)


fig.tight_layout()


fig.show()

fig.savefig("fourier_1.png")

# ------------------------------------------------
### VIDEO ###
