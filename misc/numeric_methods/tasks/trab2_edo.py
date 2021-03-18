#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:14:22 2021

@author: teles
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:40:11 2021

@author: teles
"""

# ------------------------------------------------
### IMPORTS ###

import gmpy2
from gmpy2 import mpfr, log
from numpy import arange

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------
### FUNCTIONS ###


def edo1(eq, t_0, y_0, dt, interv):
    
    t_fw = []
    t_bw = []
    
    y_fw = []
    y_bw = []
    
    y_if = mp(y_0)
    y_ib = mp(y_0)
    
    start = interv[0] - dt
    stop = interv[-1] + dt
    
    if start < t_0 and t_0 < stop:
        
        # forward
        for t_if in arange(t_0, stop, dt):
            
            y_if = y_if + dt*eq(t_if, y_if)
            t_fw.append( t_if )
            y_fw.append( y_if )
        
        # backward
        for t_ib in arange(t_0, start , -dt):
            
            y_ib = y_ib - dt*eq(t_ib, y_ib)
            t_bw.append( t_ib )
            y_bw.append( y_ib )
        
        t = t_bw[::-1] + [t_0] + t_fw
        y = y_bw[::-1] + [y_0] + y_fw
        
        return t, y
    else:
        print('Wrong Interval.')
        return [], []



def edo2(eq, t_0, y_0, dy_dt_0, dt, interv):
    
    t_fw = []
    t_bw = []
    
    y_fw = []
    y_bw = []
    
    y_if = mp(y_0)
    y_ib = mp(y_0)
    
    z_if = mp(dy_dt_0)
    z_ib = mp(dy_dt_0)
    
    
    start = interv[0] - dt
    stop = interv[-1] + dt
    
    if start < t_0 and t_0 < stop:
        
        # forward
        for t_if in arange(t_0, stop, dt):
            
            # aux
            y_aux = y_if
            
            y_if = y_if + dt*z_if
            z_if = z_if + dt*eq(t_if, y_aux, z_if)
            t_fw.append( t_if )
            y_fw.append( y_if )
        
        # backward
        for t_ib in arange(t_0, start , -dt):
            
            # aux
            y_aux = y_ib
            
            y_ib = y_ib - dt*z_ib
            z_ib = z_ib - dt*eq(t_ib, y_aux, z_ib)
            t_bw.append( t_ib )
            y_bw.append( y_ib )
        
        t = t_bw[::-1] + [t_0] + t_fw
        y = y_bw[::-1] + [y_0] + y_fw
        
        return t, y
    else:
        print('Wrong Interval.')
        return [], []
    
    
    





def mp(num):
    return mpfr(str(num))


def backf(num, digits=5):
    return float(round(num, digits))

def listf( l ):
    return list(map(backf, l))

# ------------------------------------------------
### TESTS ###

gmpy2.set_context(gmpy2.context(precision=32))


# for the 1st order Euler EDO method

dy_dt = lambda t, y: 4*t - (2/t)*y
t_0 = mp(1)
y_0 = mp(2)
dt = 8*mp(10)**-3
interv = [mp(0.2), mp(1.8)]

sol1_t = arange( *interv, dt)
sol1_y = list(map(lambda t: t**2 + 1/(t**2), sol1_t))

[apr1_t , apr1_y] = [listf(l) for l in edo1(dy_dt, t_0, y_0, dt, interv)]


# for the 1st order Euler EDO method


d2y_dt2 = lambda t, y, dy_dt: -2*dy_dt/t + t**-2 + t**-3
t_0 = mp(1)
y_0 = mp(2)
dy_dt_0 = mp(2)
dt = 5*mp(10)**-3
interv = [mp(0.2), mp(1.8)]

sol2_t = arange( *interv, dt)
sol2_y = list(map(lambda t: (1-1/t)*log(t)-2/t+4, sol2_t))

[apr2_t , apr2_y] = [listf(l) for l in edo2(d2y_dt2, t_0, y_0, dy_dt_0, dt, interv)]


# ------------------------------------------------
### PLOTS ###



sns.set_style('darkgrid')
mpl.rcParams['text.usetex'] = True


(fig, axes) = plt.subplots(1, 2, facecolor='w', figsize=( 16, 9 ))
fig.suptitle(r'$\textup{Approximations \& Analytic Solutions for Diff. Eq. using Euler`s Method (singe precision)}$')


axes[0].set_title(r'$\textup{1st Order }(\Delta x=8*10^{-3}) \\\\ \textup{Eq.: }y\prime = 4t - 2\frac{y}{t}\quad\quad\textup{AnSol.: } y = t^{2} + t^{-2}$')
axes[0].plot(sol1_t, sol1_y, 'c', lw=5, label='AnalySol.')
axes[0].plot(apr1_t, apr1_y, '.--r', lw=1, label='Approx.')
axes[0].plot(1, 2, 'ok', label= 'y(1) = 2')
axes[0].set_xlabel('t')
axes[0].set_ylabel('why')
axes[0].legend()



axes[1].set_title(r'$\textup{2nd Order }(\Delta x=5*10^{-3}) \\\\ \textup{Eq.: }y\prime\prime = -\frac{2}{t}y\prime + \frac{1}{t^{2}} + \frac{1}{t^{3}}\quad\quad\textup{AnSol.: } y = (1 - \frac{1}{t}) ln(t) - \frac{2}{t} + 4$')
axes[1].plot(sol2_t, sol2_y, 'c', lw=5, label='AnalySol.')
axes[1].plot(apr2_t, apr2_y, '.--r', lw=1, label='Approx.')
axes[1].plot(1, 2, 'ok', label= 'y(1) = 2')
axes[1].set_xlabel('t')
axes[1].set_ylabel('why')
axes[1].legend()


fig.savefig('trab2_results.png')




