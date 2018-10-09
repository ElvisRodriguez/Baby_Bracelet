# -*- coding: utf-8 -*-

import argparse
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sys
import time

import fake_duino

def make_layout():
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    return html.Div(style = {'backgroundColor': colors['background']},
                      children = [
    html.H1(children = 'Baby Bracelet UI Demo',
            style = {
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children = 'Graph of dummy heart monitor data using dash framework',
             style = {
             'textAlign': 'center',
             'color': colors['text']
    }),

    dcc.Graph(
        figure = go.Figure(
            data = [
                go.Scatter(
                    x = fake_duino.create_fake_values()[0],
                    y = fake_duino.create_fake_values()[1],
                    mode = 'lines',
                    name = 'BPM'
                )
            ],
            layout = go.Layout(
                title = 'BPM Over Time',
                xaxis = dict(title = 'Time (in minutes)'),
                yaxis = dict(title = 'Beats Per Minute'),
                showlegend = True,
                legend = go.layout.Legend(
                    x = 0,
                    y = 2.0
            ),
            ),
        ),
        style = {'height': 400},
    )
])

def run_service(app):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Address to host server')
    parser.add_argument('--port', help='Port of host server')
    args = parser.parse_args()
    if args.host and args.port:
        app.run_server(debug=True, host=args.host, port=args.port)
    elif args.host:
        app.run_server(debug=True, host=args.host)
    elif args.port:
        app.run_server(debug=True, port=args.port)
    else:
        app.run_server(debug=True)


app = dash.Dash(__name__)

app.layout = make_layout

if __name__ == '__main__':
    run_service(app)
