import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 1. Using Dash in write a program that creates an input field and displays the entered data as a text
# on the line bellow. You need to create a callback function for the exercise. Then deploy the
# created App through GCP and provide the working world web address into your report.

my_app=dash.Dash('My_App')

my_app.layout=html.Div([html.H3('Change the value in the textbox to see callbacks in action'),
                        html.P('Input:',style={'display':'inline-block','margin-right':10}),
                        dcc.Input(id='input1',type='text',placeholder='',style={'display':'inline-block'}),
                        html.Br(),html.Br(),
                        html.Div(id='my_out')
                        ])

@my_app.callback(Output(component_id='my_out',component_property='children'),
                 [Input(component_id='input1',component_property='value')])
def update_text(input):
    return f'The output value is {input}'

my_app.run_server(port=8100, host='0.0.0.0')