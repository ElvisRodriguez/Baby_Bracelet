'''
Host Application for Atawear (Baby Bracelet) Project.
'''
# -*- coding: utf-8 -*-

import argparse
import collections
import dash
import dash_core_components as dcc
from dash.dependencies import Output, Event
import dash_html_components as html
import flask
import plotly.graph_objs as go

import md_doc
import render

TIMESTAMPS = collections.deque(iterable=['00:00:00'], maxlen=30)
HEART_RATES = collections.deque(iterable=[80], maxlen=30)
EXTENDED_HEART_RATE_DATA = collections.deque(maxlen=100)

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div(id = 'graph-app',
                      children = [
    html.H1(
        id = 'main-title',
        children = 'Atawear'
    ),

    html.Div(
        id = 'sub-title',
        children = 'CS310 IoT Project'
    ),

    dcc.Markdown(md_doc.stringify_file(file_path='assets/template.md')),

    dcc.Graph(
        id = 'live-graph',
        animate = True,
    ),

    dcc.Interval(
        id = 'graph-update',
        interval = 1*1000
    )

])

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    data = go.Scatter(
        x = list(TIMESTAMPS),
        y = list(HEART_RATES),
        name = 'Rate',
        line = dict(
            color = ('#00FFFF'),
            width = 4
        )
    )

    layout = go.Layout(
        xaxis = dict(title='Time'),
        yaxis = dict(title='Heart Rate', range=[80, 160]),
        showlegend = False,
        legend = go.layout.Legend(
            x = 0,
            y = 2.0
        ),
    )
    return {'data': [data], 'uirevision' : True, 'layout' : layout}


@server.route('/')
def dash_application():
    return app.index

@server.route('/data', methods=['GET', 'POST'])
def data_receive():
    data = flask.request.form.get('heartbeat', '0')
    try:
        data = int(data)
    except ValueError:
        error_message = 'Received: Bad data.'
        return error_message
    render.render_data(heart_rates=HEART_RATES, timestamps=TIMESTAMPS,
                       data=data, extended_data=EXTENDED_HEART_RATE_DATA)
    response = 'Recieved: {data}'.format(data=data)
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='port to host server')
    args = parser.parse_args()
    app.run_server(debug=True, port=args.port)
