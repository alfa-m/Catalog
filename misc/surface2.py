# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
#-------------------------------------------------------
### IMPORTS ###

import numpy as np
from numpy import pi
import pandas as pd
import plotly.graph_objects as go


#-------------------------------------------------------
### DATA ###


'''
>	x = seq(-pi, pi, length=50)
>	y = seq(-pi, pi, length=50)
>	z = outer(x, y, function(x,y)cos(y)/(1+x^2))

>	contour(x, y, z)
>	contour(x, y, z, nlevels=45, add=T)

>	za = (z - t(z))/2
>	contour(x, y, za, nlevels=15)

'''


x_lin = np.linspace(-pi, pi, 50)
y_lin = np.linspace(-pi, pi, 50)

(x, y) = np.meshgrid(x_lin, y_lin)

z = np.cos(y)/(1+x**2)

z_data = pd.DataFrame(data=z, index=x_lin, columns=y_lin)


#-------------------------------------------------------
### FIGURE ###

fig = go.Figure(data=[go.Surface(z=z_data.values, x=x_lin, y=y_lin)])

fig.update_traces(contours_z= dict(show=True,
                                   usecolormap=True,
                                   highlightcolor="limegreen",
                                   project_z=True))

fig.update_layout(title= 'cos(Y)/(1+X^2)',
                  autosize= False,
                  width= 500,
                  height= 500,
                  margin= dict(l= 65,
                               r= 50,
                               b= 65,
                               t= 90))


#-------------------------------------------------------
### PLOT ###

from plotly.offline import plot
plot(fig)
