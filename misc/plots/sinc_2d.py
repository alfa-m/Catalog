from numpy import sin, linspace, meshgrid, pi
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

x = linspace(-5, 5, 100)                                        
y = linspace(-5, 5, 100) 
xx, yy = meshgrid(x,y)

t = (xx**2 + yy**2)**(1/2)

zz = sin(pi* t)/(pi*t)
pp = xx*0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

offset = mcolors.TwoSlopeNorm( vcenter= 0, vmin= -0.2, vmax= 0.2)

mapp = ax.plot_surface(xx,yy,zz, cmap='seismic', norm=offset)

fig.colorbar(mapp, ax=ax, extend='both')

fig.show()

input()
