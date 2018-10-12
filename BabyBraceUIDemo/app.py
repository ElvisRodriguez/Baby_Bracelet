# -*- coding: utf-8 -*-

import argparse
# from concurrent.futures import ThreadPoolExecutor
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import helper_duino
from time_stamp import current_date
import pi_duino

def make_layout():
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    return html.Div(style = {'backgroundColor': colors['background']},
                      children = [
    html.H1(children = 'Baby Bracelet',
            style = {
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children = 'Graph of Arduino Heart Sensor Data',
             style = {
             'textAlign': 'center',
             'color': colors['text']
    }),

    dcc.Graph(
        figure = go.Figure(
            data = [
                go.Scatter(
                    x = helper_duino.read_data_values()[0],
                    y = helper_duino.read_data_values()[1],
                    mode = 'lines',
                    name = 'Rate'
                )
            ],
            layout = go.Layout(
                title = current_date(),
                xaxis = dict(title = 'Time'),
                yaxis = dict(title = 'Heart Rate'),
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
    pi_duino.write_serial_values()
    run_service(app)
