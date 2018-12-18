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

import analytics
#import md_doc
import render

TIMESTAMPS = collections.deque(iterable=['00:00:00'], maxlen=30)
HEART_RATES = collections.deque(iterable=[80], maxlen=30)
EXTENDED_HEART_RATE_DATA = collections.deque(maxlen=100)
INTERBEAT_INTERVALS = collections.deque(maxlen=100)

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

    #dcc.Markdown(md_doc.stringify_file(file_path='assets/template.md')),

    dcc.Graph(
        id = 'live-graph',
        animate = True,
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
    if int(hrv) > 20:
        message.append('Possibility of Atrial Fibrillation Episode')
        message.append('HRV of {hrv} detected'.format(hrv=int(hrv)))
    return '\n'.join(message)

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
        yaxis = dict(title='Heart Rate', range=[1, 160]),
        showlegend = False,
        legend = go.layout.Legend(
            x = 0,
            y = 2.0
        ),
    )
    message = alert_message()
    script = None
    if message is not None:
        script = html.script('alert({message})'.format(message=message))
    return {'data': [data], 'layout' : layout, 'script' : script}


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
        response = 'Recieved:\n\tBPM: {bpm}\n\tRR_INTERVALS: {rr}'.format(
            bpm=bpm_data, rr=rr_intervals)
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
