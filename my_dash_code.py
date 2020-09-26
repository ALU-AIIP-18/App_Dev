# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:51:07 2020

@author: rbisa
"""
from calc_power import power_df_final
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly


def get_dash(server):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, 
                    server=server,
                    routes_pathname_prefix='/dashdisplay/',
                    external_stylesheets=external_stylesheets
                    )
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    Solar_Out = power_df_final['Predicted_Solar']
    Wind_Out = power_df_final['Predicted_Wind']
    Total_Out = power_df_final['Total_Predicted_Power']
    branches = power_df_final['Day_y']          #remember to remove suffix, seen solution on stack overflow

    res1 = go.Bar(x=branches,y = Solar_Out, name = 'SOLAR PP')
    res2 = go.Bar(x=branches,y = Wind_Out, name = 'WIND PP')
    res3 = go.Bar(x=branches,y = Total_Out, name = 'SOLAR + WIND PPs')

    data = [res1, res2]
    layout = go.Layout(barmode = 'group', xaxis_title="Day Of Month", yaxis_title="Power Generated (MW)")
    fig = go.Figure(data = data, layout = layout)

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
    
    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Welcome to Company Solar & Wind Power Plants Output Predictions Site',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

    html.Div(children='Predicted Power Output from Solar and Wind PP (MW)', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='example-graph-2',
            figure=fig
        ),
        
        dcc.Graph(
            id='example-graph-3',
            figure=go.Figure(data=[res3], layout=go.Layout(xaxis_title="Day Of Month", yaxis_title="Total Power Generated (MW)")))
        
        ])

    return app
