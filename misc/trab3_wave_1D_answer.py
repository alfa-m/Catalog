#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:05:04 2021

@author: teles
"""


# ------------------------------------------------
### IMPORTS ###

import gmpy2
from gmpy2 import mpfr, const_pi, const_euler

import matplotlib.pyplot as plt
import seaborn as sns

import cv2    # conda install -c conda-forge opencv=4.1.0
import os


bits = 32
# bits = 64

gmpy2.set_context(gmpy2.context(precision=bits))




# ------------------------------------------------
### FUNCTIONS ###
 

def mp(num):
    return mpfr(str(num))


def backf(num, digits=5):
    return float(round(num, digits))

def listf( l ):
    return list(map(backf, l))


pi = const_pi(bits)
e = const_euler(bits)



def propagation1D (i_max, n_max, ratio):
    
    eps_0 = mp(8.85418782)*10**-12 # Farad/m
    mi_0 = 4*pi*10**-7 # Hen/m
    c = mp(299792458) # m/s
    
    dx = mp(0.001)
    dt = 0.9*dx/c
    
    x_lin = [ backf(x*dx) for x in range(i_max+2)]
    Ez = [ mp(0) for _ in range(i_max+2)]
    Hy = [ mp(0) for _ in range(i_max+2)]
    
    #Ez_max = []
    #Hy_max = []
    
    T = n_max*dt/10
    font = lambda t: e**-(((t-3*T)**2)/T**2)
    
    # values of n to be outputed for the video
    r = [r for r in range(0, n_max, ratio)]
    
    # CALCULATION
    
    # generator function    
    for n in range(n_max):
        
        t = n*dt
        t_ns = backf(t*10**9, 10)
        
        #print ('Calculating... {:4.1f} %'.format(round(n*100/n_max, 1)))
        print ('Calculating... {:4.1f} %  ||  n: {:4d}   ||   t: {:5.3f} ns'.format(round(n*100/n_max, 1), n, t_ns))
        
        Ez[int(i_max/2 + 1)] = font(t)
        
        for i in range(1, i_max+1):
            Hy[i] = Hy[i] + (Ez[i+1] - Ez[i])*dt/(dx*mi_0)
        
        for i in range(1, i_max+1):
            Ez[i] = Ez[i] + (Hy[i] - Hy[i-1])*dt/(dx*eps_0)
        
        # conductive wall
        Ez[1] = 0
        Ez[-2] = 0
        
        # biggest values
        #Ez_max.append(max(map(abs,Ez)))
        #Hy_max.append(max(map(abs,Hy)))
        
        if n in r:
            yield [listf(Ez), listf(Hy), t_ns]
    
    #print('\nHighest Ez: {:.2f}\nHighest Hy: {:f}'.format(backf(max(Ez_max)),backf(max(Hy_max))))
        
    


# ------------------------------------------------
### TESTS ###


# for the simulation
i_max = 4000
n_max = 4500



# for the video
width, height = (8, 6)

fps = 20
time = 21

ratio = round(n_max / (fps*time))
count = len(range(0, n_max, ratio))



# initialization for the ploting setup
dx = mp(0.001)
x_lin = [ backf(x*dx) for x in range(i_max+2)]
empty_field = [ 0 for _ in range(i_max+2)]


# ------------------------------------------------
### PLOTING ###

plt.ion()
#plt.ioff()

sns.set_style('darkgrid')
(fig, axes) = plt.subplots(2,1, facecolor='w', figsize=(width, height))

fig.suptitle("Wave Propagation (1D)\nTime: {:7.5f} nanosec.".format(0.0))

def reset_axes(Ez, Hy):
    axes[0].clear()
    axes[0].set_xlabel('X (m)')
    axes[0].set_ylabel('Ez (Volts/m)')
    axes[0].set_ylim([-1.1, 1.1])
    axes[0].plot(x_lin, Ez, 'r-', label='Electric Field')
    axes[0].legend(loc=2)
    # "walls"
    axes[0].plot([0, 0], [-1, 1] , 'k')
    axes[0].plot([4, 4], [-1, 1] , 'k')
    
    
    axes[1].clear()
    axes[1].set_xlabel('X (m)')
    axes[1].set_ylabel('Hy (Amperes/m)')
    axes[1].set_ylim([-0.006, 0.006])
    axes[1].plot(x_lin, Hy, 'b-', label='Magnetic Field')
    axes[1].legend(loc=2)
    # "walls"
    axes[1].plot([0, 0], [-0.0055, 0.0055] , 'k')
    axes[1].plot([4, 4], [-0.0055, 0.0055] , 'k')

'''
reset_axes(empty_field, empty_field)
axes[0].legend(loc=2)
axes[1].legend(loc=2)
'''

# ------------------------------------------------
### VIDEO ###

os.chdir('/home/teles/Documents/ENG. COMPUTAÇÃO/8_metodos-numericos/tarefas')

result = propagation1D(i_max, n_max, ratio)

for n in range(count):
    
    Ez, Hy, t = next(result)
    
    reset_axes(Ez, Hy)
        
    fig.suptitle("Wave Propagation (1D)\nTime: {:7.5f} nanosec.".format(t))
    
    print ('Saving fig_{}...'.format(n))
    
    fig.savefig('pics_temp/fig_{}.png'.format(n))



print ('\nWriting Video...')

#fourcc_avi = cv2.VideoWriter_fourcc(*'XVID')    # avi
fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')   # mp4

height, width, _ = cv2.imread('pics_temp/fig_0.png').shape

#video_avi = cv2.VideoWriter('trab3_ans.avi', fourcc_avi, fps, (width,height))
video_mp4 = cv2.VideoWriter('trab3_ans.mp4', fourcc_mp4, fps, (width,height))

for path in ('pics_temp/fig_{}.png'.format(p) for p in range(count)):
    img = cv2.imread(path)
    #video_avi.write(img)
    video_mp4.write(img)

#video_avi.release()
video_mp4.release()
cv2.destroyAllWindows()


print ('\nRemoving temporary pictures...')


# delete imgs
for path in ('pics_temp/fig_{}.png'.format(p) for p in range(count)):
    os.remove(path)


print ('\nAll done.\n')




















