# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:29:18 2019

@author: Daman
"""

import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import datetime as dt
import numpy as np
import os
import plotly.express as px     

def read_filter(path='data/', variables=['player', 'k/d']):
    df = pd.DataFrame(columns=variables + ['game', 'date', 'event'])
    file_list = os.listdir(path)
    for x in file_list:
        games = ['IW', 'WW2', 'Bo4', 'MW']
        temp1 = pd.read_csv('data/{}'.format(x))
        temp2 = temp1[variables]
        date = pd.to_datetime(x[5:15])
        if date <= pd.to_datetime('2017-08-13'):
            temp2['game'] = games[0]
            temp2['date'] = date
        elif date <= pd.to_datetime('2018-08-19'):
            temp2['game'] = games[1]
            temp2['date'] = date
        elif date <= pd.to_datetime('2019-08-18'):
            temp2['game'] = games[2]
            temp2['date'] = date
        else:
            temp2['game'] = games[3]
            temp2['date'] = date
        event = x[16:-4]
        temp2['event'] = event
        df = df.append(temp2, ignore_index = True)
    return df


data = read_filter()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        
        html.Div([
                html.H1('Call of Duty Stat Viewer')
                ]),
        html.Div([
                dcc.Dropdown(id='player-drop',
                             options = [{'value': i, 'label': i} for i in data.player.unique()],
                             value=''),
                ]),
        html.Div([
                dcc.Graph(id='player-graph')
                ])
        ])

@app.callback(
        Output('player-graph', 'figure'),
        [Input('player-drop', 'value')])

def update_player_graph(player_value):
        data_filtered = data[data['player'] == player_value]
        data_filtered2 = pd.DataFrame(data_filtered.groupby(['event', 'date'])['k/d'].mean().reset_index(), columns=['event', 'date', 'k/d'])
        data_filtered2 = data_filtered2.sort_values('date', ascending = True)
        figure = {
                
                'data': [
                        {
                        'x': data_filtered2[data_filtered2['game'] == 'IW']['date'],
                        'y': data_filtered2[data_filtered2['game'] == 'IW']['k/d'],
                        'name' : 'IW',
                        'marker' : {'color': 'yellow'}
                                },
                        {
                        'x': data_filtered2[data_filtered2['game'] == 'WW2']['date'],
                        'y': data_filtered2[data_filtered2['game'] == 'WW2']['k/d'],
                        'name' : 'WW2',
                        'marker' : {'color': 'grey'}
                                },
                        {
                        'x': data_filtered2[data_filtered2['game'] == 'Bo4']['date'],
                        'y': data_filtered2[data_filtered2['game'] == 'Bo4']['k/d'],
                        'name' : 'Bo4',
                        'marker' : {'color': 'orange'}
                                },
                                {
                        'x': data_filtered2[data_filtered2['game'] == 'MW']['date'],
                        'y': data_filtered2[data_filtered2['game'] == 'MW']['k/d'],
                        'name' : 'MW',
                        'marker' : {'color': 'green'}
                                }
                        ]
                
                }
        
        return figure



if __name__ == '__main__':
    app.run_server(debug=False)
m,   