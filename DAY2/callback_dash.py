# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:43:13 2020

@author: ninjaac
"""

#import the libraes
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input,Output
import pandas as pd

app=dash.Dash()

app.layout=html.Div(children=[
    dcc.Input(id='ip',value='hey hello',type='text'),
    html.Div(id='op'),
    ])

@app.callback(Output(component_id= 'op',component_property='children'),
            [Input(component_id='ip',component_property='value')])
def update_value(value):
    return value

if __name__=='__main__':
    app.run_server(debug=True)
