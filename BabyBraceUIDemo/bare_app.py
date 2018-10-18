import argparse
import collections

import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from time_stamp import current_hour
import pi_duino

X = collections.deque(maxlen=30)
Y = collections.deque(maxlen=30)

app = dash.Dash(__name__)

app.layout = html.Div(
    children = [
        html.Div(
            id = 'output',
            title = 'Baby Bracelet'
        ),

        dcc.Interval(
            id = 'data-update',
            interval = 1*1000
        )
    ]
)

@app.callback(Output(component_id='output',
                     component_property='children'),
              events=[Event('data-update', 'interval')])
def update_all_data():
    serial_obj = pi_duino.create_serial_obj(port='/dev/ttyACM0', rate=9600)
    sensor_data = pi_duino.retrieve_serial_value(serial_obj)
    #sensor_data = pi_duino.create_fake_value()
    sensor_data = sensor_data.__next__()
    X.append(sensor_data[0])
    Y.append(sensor_data[1])
    all_values = []
    for i in range(len(X)):
        all_values.append(
            html.Div(
                '{} : {}'.format(str(X[i]), str(Y[i]))
            )
        )
    return all_values


if __name__ == '__main__':
    app.run_server(debug=True)
