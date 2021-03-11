from numpy import sin, linspace, meshgrid, pi, e
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


scale = 2

l_up = -14.47*scale + 31.45
l_down = -l_up

x = linspace(l_down, l_up, 101)                                        
y = linspace(l_down, l_up, 101)
xx, yy = meshgrid(x,y)

t = (xx**2 + yy**2)**(1/2) 


zz = (2*pi**(-1/4) / 3**(1/2)) * (1 - (scale*t)**2) * e**(-(scale*t)**2 / 2)
#zz = (1 - (scale*t)**2) * e**(-(scale*t)**2 / 2)


period = 2*pi / (scale * 2.5**(1/2))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

offset = mcolors.TwoSlopeNorm( vcenter= 0, vmin= -0.4, vmax= 1 )

mapp = ax.plot_surface(xx,yy,zz, cmap='inferno', norm=offset)

fig.colorbar(mapp, ax=ax, extend='both')

fig.show()

input()



