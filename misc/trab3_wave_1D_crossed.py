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
from numpy import meshgrid

import matplotlib.pyplot as plt
import seaborn as sns
#import matplotlib.animation as anim


import os
import cv2    # conda install -c conda-forge opencv=4.1.0


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



def propagation1D (i_max, n_max, ratio, l):
    
    eps_0 = mp(8.85418782)*10**-12 # Farad/m
    mi_0 = 4*pi*10**-7 # Hen/m
    c = mp(299792458) # m/s
    
    dx = mp(0.001)
    dt = 0.9*dx/c
    
    Ez = [ mp(0) for _ in range(i_max+2)]
    Hy = [ mp(0) for _ in range(i_max+2)]
    
    #Ez_max = []
    #Hy_max = []
    
    n_max_font = n_max/l
    T = n_max_font*dt/10
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
        
        if n < n_max_font:
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


longer = 3

longer = int(longer)

# for the simulation
i_max = 4000
n_max = 4500*longer



# for the video

fps = 15
time = 20 * longer

ratio = round(n_max / (fps*time))
count = len(range(0, n_max, ratio))



# initialization for the ploting setup
dx = mp(0.001)
x_lin = [ backf(x*dx) for x in range(-1, i_max+1)]
empty_field = [ 0 for _ in range(i_max+2)]




# generator
result = propagation1D(i_max, n_max, ratio, longer)

# ------------------------------------------------
### PLOTING ###

plt.ioff()

sns.set_style('darkgrid')


def init_axes():
    
    global fig
    global ax
    global line1
    global line2
    global title
    
    fig = plt.figure(facecolor='#eaeaf2', figsize=(16, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    line1, = ax.plot(x_lin, empty_field, empty_field, 'b-', lw=3, label='Magnetic Field')
    line2, = ax.plot(x_lin, empty_field, empty_field, 'r-', lw=3, label='Electric Field')
    title = ax.set_title("")
    
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Hy (Amperes/m)')
    ax.set_zlabel('Ez (Volts/m)')
    
    ax.legend(loc=1)
    
    ax.set_xlim([0, 4.1])
    ax.set_ylim([-0.009, 0.0057])
    ax.set_zlim([-2, 2.1])
    
    ax.view_init(elev=17, azim=-44)
    
    
    
    # "walls"
    y = [-0.0058, 0.0058]
    z = [-2, 2]
    yy, zz = meshgrid(y, z)
    
    xx1 = yy*zz*0
    ax.plot_surface(xx1, yy, zz, alpha=0.7)
    
    xx2 = yy*zz*0 + 4
    ax.plot_surface(xx2, yy, zz, color='w', alpha=0.1)
    
    
    
    # "cross section"
    ax.plot([0,4],[0,0],[0, 0], 'k', lw=0.5)
    
    x = [0, 4]
    y = [-0.0058, 0.0058]
    xx, yy = meshgrid(x,y)
    zz = xx*yy*0
    ax.plot_surface(xx, yy, zz, color='b', alpha=0.2)
    
    x = [0, 4]
    z = [-2, 2]
    xx, zz = meshgrid(x,z)
    yy = xx*zz*0
    ax.plot_surface(xx, yy, zz, color='r', alpha=0.2)
    
    return [line1, line2, title]
     

def set_axes(res):
    Ez, Hy, t = res
    
    # waves
    line1.set_data_3d(x_lin, Hy, empty_field)
    line2.set_data_3d(x_lin, empty_field, Ez)
    
    title.set_text("Wave Propagation (1D)\nTime: {:7.5f} nanosec.".format(t))
    
    return [line1, line2, title]
    




'''
result = list(result)

plt.ion()
fig.show()
init_axes()

from time import sleep

for res in result:
    
    set_axes(res)
    sleep(1/fps)

'''



# ------------------------------------------------
### VIDEO ###

os.chdir('/home/teles/Documents/ENG. COMPUTAÇÃO/8_metodos-numericos/tarefas')


init_axes()

for res, n in zip(result, range(count)):
    
    set_axes(res)
    
    print ('Saving fig_{}...    (frame  {}  of {} )   {:3.1f} %'.format(n,n,count, n*100/count))
    fig.savefig('pics_temp/fig_{}.png'.format(n))





print ('\nWriting Video...')

fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')   # mp4

height, width, _ = cv2.imread('pics_temp/fig_0.png').shape

video_mp4 = cv2.VideoWriter('trab3_crossed.mp4', fourcc_mp4, fps, (width,height))

for path in ('pics_temp/fig_{}.png'.format(p) for p in range(count)):
    img = cv2.imread(path)
    video_mp4.write(img)

video_mp4.release()
cv2.destroyAllWindows()





print ('\nRemoving temporary pictures...')


# delete imgs
for path in ('pics_temp/fig_{}.png'.format(p) for p in range(count)):
    os.remove(path)






print ('\nAll done.\n')








    
























