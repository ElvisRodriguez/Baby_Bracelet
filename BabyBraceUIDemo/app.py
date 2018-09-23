# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dummy_data import DummyTime, DummyHeartBeat

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

Dum_data = {
    'times' : DummyTime(60),
    'heartbeats' : DummyHeartBeat(60)
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1(children='Baby Bracelet UI Demo',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children='Graph of dummy heart monitor data using dash framework',
             style={
             'textAlign': 'center',
             'color': colors['text']
    }),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x = Dum_data['times'].dummy_times(),
                    y = Dum_data['heartbeats'].create_HB_list(),
                    mode = 'lines',
                    name = 'BPM'
                )
            ],
            layout=go.Layout(
                title='BPM Over Last Hour',
                xaxis = dict(title = 'Time (in minutes)'),
                yaxis = dict(title = 'Beats Per Minute'),
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=2.0
            ),
            ),
        ),
        style={'height': 400},
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1', port=5000)
