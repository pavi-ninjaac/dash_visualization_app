# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:22:09 2020

@author: ninjaac
"""


#import the libraes
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Output,Input
import pandas as pd
import plotly
import plotly.graph_objs as go
from collections import deque
import random


#create the deque object
x=deque(maxlen=20)
x.append(1)
y=deque(maxlen=20)
y.append(1)

#create the app layout
app=dash.Dash()
app.layout=html.Div(children=[
    dcc.Graph(id='op',animate=True),
    dcc.Interval(
        id='event',
        interval=1*1000
        ),
    ])


@app.callback(Output(component_id='op',component_property='figure'),
              [Input('ip','interval')])
def update_grape():
    x.append(x[-1]+1),
    y.append(y[-1]+y[-1]*random.uniform(-1,1)),
    
    data=go.Scatter(
        x=list(x),
        y=list(y),
        mode='lines+markers'
        )
    layout=go.Layout(
        xaxis=dict(range=[min(x),max(x)]),
        yaxis=dict(range=[min(y),max(y)])
        )

    return {'data':[data],'layout':layout}


if __name__=='__main__':
    app.run_server(debug=True)