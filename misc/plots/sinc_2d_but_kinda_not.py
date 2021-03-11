from numpy import sinc, linspace, meshgrid, pi, e
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

x = linspace(-1.5, 1.5, 31)                                        
y = linspace(-1.5, 1.5, 31) 
xx, yy = meshgrid(x,y)

t = (xx**2 + yy**2)**(1/2)

filt = 2 - ( 1.5 *  e**(-t))

zz = sinc(pi* xx) * sinc(yy*pi)
#zz = filt * sinc(pi* xx) * sinc(yy*pi)

#pp = xx*0


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

offset = mcolors.TwoSlopeNorm( vcenter= 0, vmin= -0.2, vmax= 0.2 )

#ax.plot_surface(xx,yy,pp, alpha=0.7)
mapp = ax.plot_surface(xx,yy,zz, cmap='seismic', norm=offset)

fig.colorbar(mapp, ax=ax, extend='both')

fig.show()

input()
