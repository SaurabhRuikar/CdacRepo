#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:46:54 2019

@author: student
"""

#Matplotlib
import matplotlib.pyplot as plt
import pandas as pd
fig,ax=plt.subplots()

tips=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

ax.violinplot(tips['total_bill'],vert=False)

plt.show()



#Seaborn makes harder graphs also easier to plot unlike matplotlib

#seaborn

import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset("tips")
sns.violinplot(x="total_bill",data=tips,color="r")
plt.show()

#SWARMPLOT

import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")
sns.swarmplot(x="species",y="petal_length",data=iris)
plt.show()


#factorplot BAR

titanic=sns.load_dataset('titanic')

g=sns.factorplot('class','survived','sex',data=titanic,kind='bar',palette='muted',legend=True)

plt.show()

#SCATTER PLOT USING COLOR PALETTE IMPORTED FROM SEABORN INTO MATPLOTLIB

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap

N=500
current_palette=sns.color_palette("dark",n_colors=5)
cmap=ListedColormap(sns.color_palette(current_palette).as_hex())
print(type(cmap))

data1=np.random.randn(N)
data2=np.random.randn(N)
colors=np.random.randint(0,5,N)

plt.scatter(data1,data2,c=colors,cmap=cmap)
plt.colorbar()
plt.show()

#multiple graphs as subplots

tips=sns.load_dataset("tips")
iris=sns.load_dataset("iris")

with sns.axes_style('white'):
    plt.subplot(211)
    sns.swarmplot(x="species",y="petal_length",data=iris)

plt.subplot(212)

sns.violinplot(x="total_bill",data=tips,color="r")

plt.show()


#BAR PLOT USING SET METHOD FOR X AND Y LABELS 
fake=pd.DataFrame({'cat':['red','green','blue'],'val':[1,2,3]})
#wrong
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
#import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas = df[(df.continent=='Americas')]
europe = df[(df.continent=='Europe')]

trace_comp0= go.Scatter(x=americas.gdp_percap,
                        y=americas.life_exp,
                        mode='markers',marker=dict(size=12,line=dict(width=1),
                        color='navy'),name='Americas',
                        text=americas.country,)

trace_comp1= go.Scatter(x=europe.gdp_percap,
                        y=europe.life_exp,
                        mode='markers',
                        marker=dict(size=12,
                        line=dict(width=1),
                        color='red'),
                        name='Europe',
                        text=europe.country,)

data_comp=[trace_comp0,trace_comp1]

layout_comp=go.Layout(title='Life Expentancy vs Per Capita GDP, 2007',
                      hovermode='closest',
                      xaxis=dict(title='GDP per capita (2000 Dollars)',
                      ticklen=5,
                      zeroline=False,
                      gridwidth=2,
                      ),
                      yaxis=dict(title='Life Expentancy(years)',
                      ticklen=5,
                      gridwidth=2,
                      ),
                      )
fig_comp= go.Figure(data=data_comp,layout=layout_comp)
plotly.offline.iplot(fig_comp,filename='life-expentancy-per-GDP')





ax=sns.barplot(x='val',y='cat',data=fake,color='k')
ax.set(xlabel='common xlabel',ylabel='common ylabel')
plt.show()



#LINEAR REGRESSION GRAPH
x=10 ** np.arange(1,10)
y=x*2






#PLOTLY LIBRARY

import plotly
from plotly.graph_objs import Scatter,Layout

#print(plotly.__version__)

plotly.offline.plot({'data':[Scatter(x=[1,2,3,4],y=[4,3,2,1])],'layout': Layout(title='Hello World')})


#wrong
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
#import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas = df[(df.continent=='Americas')]
europe = df[(df.continent=='Europe')]

trace_comp0= go.Scatter(x=americas.gdp_percap,
                        y=americas.life_exp,
                        mode='markers',marker=dict(size=12,line=dict(width=1),
                        color='navy'),name='Americas',
                        text=americas.country,)

trace_comp1= go.Scatter(x=europe.gdp_percap,
                        y=europe.life_exp,
                        mode='markers',
                        marker=dict(size=12,
                        line=dict(width=1),
                        color='red'),
                        name='Europe',
                        text=europe.country,)

data_comp=[trace_comp0,trace_comp1]

layout_comp=go.Layout(title='Life Expentancy vs Per Capita GDP, 2007',
                      hovermode='closest',
                      xaxis=dict(title='GDP per capita (2000 Dollars)',
                      ticklen=5,
                      zeroline=False,
                      gridwidth=2,
                      ),
                      yaxis=dict(title='Life Expentancy(years)',
                      ticklen=5,
                      gridwidth=2,
                      ),
                      )
fig_comp= go.Figure(data=data_comp,layout=layout_comp)
plotly.offline.iplot(fig_comp,filename='life-expentancy-per-GDP')

















