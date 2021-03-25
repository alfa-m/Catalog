# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
#-------------------------------------------------------
### IMPORTS ###

import numpy as np
import pandas as pd
import plotly.graph_objects as go


#-------------------------------------------------------
### DATA ###

z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values

(sh_x, sh_y) = z.shape

x = np.linspace(0, 1, sh_x)
y = np.linspace(0, 1, sh_y)




#-------------------------------------------------------
### FIGURE ###

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
#print(type(fig))

fig.update_traces(contours_z= dict(show=True,
                                   usecolormap=True,
                                   highlightcolor="limegreen",
                                   project_z=True))

fig.update_layout(title= 'Mt Bruno Elevation',
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

