import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies  import Input, Output
import pandas_datareader.data as web
import datetime

stock = 'TSLA'

start = datetime.datetime(2015,1,1)
end = datetime.datetime.now()


df = web.DataReader(stock,"yahoo",start,end)

app = dash.Dash()

app.layout = html.Div(children=[dcc.Input(id='input', value='enter something', type='text'),
                      html.Div(id='output'),
                      dcc.Graph(id='example', figure={'data': [{'x':[1,2,3,4,5],'y':[5,6,7,2,1],'type': 'line', 'name': 'boats'},
                                                               {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
                                                               ], 'layout': {'title': 'Basic Dash Example'} })])

@app.callback(
    Output(component_id='output',component_property='children'),
                [Input(component_id='input',component_property='value')]
)
def update_value(input_data):
    try:
        return str(float(input_data)**2)
    except :
        return "sorry cannot do"
    return 'Input: "{}"'.format(input_data)


dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )


if  __name__ == '__main__':
    app.run_server(debug=True)

