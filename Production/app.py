'''
Host Application for Atawear (Baby Bracelet) Project.
'''
# TODO(Elvis): Separate inline css to the external 'assets' folder
# TODO(Elvis): Add docstrings to describe methods

# -*- coding: utf-8 -*-

import argparse
import collections
import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import time

from time_stamp import current_date, current_hour
import pi_duino


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

X = collections.deque(maxlen=30)
Y = collections.deque(maxlen=30)

app = dash.Dash(__name__)

app.layout = html.Div(style = {'backgroundColor': colors['background']},
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
        id='live-graph',
        animate=True,
        style = {'height': 400},
    ),

    dcc.Interval(
        id='graph-update',
        interval=1*1000
    )

])

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    #serial_obj = pi_duino.create_serial_obj(port='/dev/ttyACM0', rate=9600)
    #sensor_data = pi_duino.retrieve_serial_value(serial_obj)
    sensor_data = pi_duino.create_fake_value()
    sensor_data = sensor_data.__next__()
    X.append(sensor_data[1])
    Y.append(sensor_data[0])

    data = go.Scatter(
        x = list(X),
        y = list(Y),
        mode = 'lines+markers',
        name = 'Rate'
    )

    layout = go.Layout(
        title = 'Latest Heart Rate: {hr}'.format(hr=Y[-1]),
        xaxis = dict(title='Time'),
        yaxis = dict(title='Heart Rate', range=[min(Y), max(Y)]),
        showlegend = True,
        legend = go.layout.Legend(
            x = 0,
            y = 2.0
        ),
    )
    return {'data': [data], 'layout' : layout}


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


if __name__ == '__main__':
    run_service(app)
