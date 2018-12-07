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
import pi_duino
import render

TIMESTAMPS = collections.deque(maxlen=30)
HEART_RATES = collections.deque(maxlen=30)

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

    dcc.Markdown(md_doc.markdown()),

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
    sensor_data = pi_duino.create_fake_value()
    sensor_data = sensor_data.__next__()
    TIMESTAMPS.append(sensor_data[1])
    HEART_RATES.append(sensor_data[0])

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
        title = 'Latest Heart Rate: {hr}'.format(hr=HEART_RATES[-1]),
        xaxis = dict(title='Time'),
        yaxis = dict(title='Heart Rate', range=[80, 160]),
        showlegend = False,
        legend = go.layout.Legend(
            x = 0,
            y = 2.0
        ),
    )
    return {'data': [data], 'layout' : layout}


@server.route('/')
def dash_application():
    return app.index

@server.route('/data', methods=['GET', 'POST'])
def data_receive():
    data = flask.request.form.get('heartbeat', '170')
    render.render_data(heart_rates=HEART_RATES, timestamps=TIMESTAMPS, data=data)
    return data



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='port to host server')
    args = parser.parse_args()
    app.run_server(debug=True, port=args.port)
