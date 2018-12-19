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
import os
import plotly.graph_objs as go

import analytics
import render

TIMESTAMPS = collections.deque(maxlen=30)
HEART_RATES = collections.deque(maxlen=30)
EXTENDED_HEART_RATE_DATA = collections.deque(maxlen=100)
INTERBEAT_INTERVALS = collections.deque(maxlen=100)
COUNTER = 0

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

    dcc.Graph(
        id = 'live-graph',
        animate = False,
    ),

    dcc.Interval(
        id = 'graph-update',
        interval = 1*1000
    )

])

def alert_message():
    if len(EXTENDED_HEART_RATE_DATA) < 100:
        return None
    message = []
    if analytics.is_rising(EXTENDED_HEART_RATE_DATA):
        message.append('Heart Rate rising rapidy!')
    if analytics.is_dropping(EXTENDED_HEART_RATE_DATA):
        message.append('Heart Rate dropping rapidly!')
    hrv = analytics.heart_rate_variability(INTERBEAT_INTERVALS)
    hb_average = analytics.average_heartbeat(EXTENDED_HEART_RATE_DATA)
    if int(hrv) > 20 and hb_average > 100:
        message.append('Possibility of Atrial Fibrillation Episode')
        message.append('HRV of {hrv} detected'.format(hrv=int(hrv)))
    if message is not None:
        message = '\n'.join(message)
        js_script = 'alert(\'{message}\')'.format(message=message)
        file_path = os.path.join(os.getcwd(), 'assets', 'alerter.js')
        with open(file_path, 'w') as file:
            file.write(js_script)
            file.close()

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter(counter=COUNTER):
    latest_bpm = 80
    if len(HEART_RATES) >= 1:
        latest_bpm = HEART_RATES[-1]

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
        xaxis = dict(title='Latest BPM:{bpm}'.format(bpm=latest_bpm)),
        yaxis = dict(title='Heart Rate', range=[1, 160]),
        showlegend = False,
        legend = go.layout.Legend(
            x = 0,
            y = 2.0
        ),
    )
    counter += 1
    if counter == 10:
        alert_message()
        counter = 0

    return {'data': [data], 'layout' : layout}


@server.route('/')
def dash_application():
    return app.index

@server.route('/data', methods=['GET', 'POST'])
def data_receive():
    bpm_data = flask.request.form.get('heartbeat', '0')
    rr_intervals = flask.request.form.get('rr_intervals', '')
    response = ''
    try:
        bpm_data = int(bpm_data)
        rr_intervals = str(rr_intervals)
        response = 'Recieved: {bpm};{rr}'.format(bpm=bpm_data, rr=rr_intervals)
        render.render_data(heart_rates=HEART_RATES, timestamps=TIMESTAMPS,
                           extended_heart_rates=EXTENDED_HEART_RATE_DATA,
                           bpm_data=bpm_data,
                           interbeat_intervals=INTERBEAT_INTERVALS,
                           rr_intervals=rr_intervals)
    except ValueError:
        response = 'Received: Bad data.'
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='port to host server')
    args = parser.parse_args()
    app.run_server(debug=True, port=args.port)
