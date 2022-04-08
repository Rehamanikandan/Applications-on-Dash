import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 3. Using Dash create a drop-down menu with the items listed below. Once one of the items is
# selected, then a message should display that the selected item inside the dropdown menu
# is_____. The default must be ‘Introduction’. Then deploy the created App through GCP and
# provide the working web address into your report.
# a. Introduction
# b. Panda package
# c. Seaborn package
# d. Matplotlib Package
# e. Principal Component Analysis
# f. Outlier Detection
# g. Interactive Visualization
# h. Web-based App using Dash
# i. Tableau

my_app=dash.Dash('My_App')

my_app.layout=html.Div([html.H1('Complex Data Visualization'),
                        dcc.Dropdown(id='drop1',options=[
                            {'label':'Introduction','value':'Introduction'},
                            {'label':'Panda Package','value':'Panda Package'},
                            {'label':'Seaborn Package','value':'Seaborn Package'},
                            {'label':'Matplotlib Package','value':'Matplotlib Package'},
                            {'label':'Principal Component Analysis','value':'Principal Component Analysis'},
                            {'label':'Outlier Detection','value':'Outlier Detection'},
                            {'label':'Interactive Visualization','value':'Interactive Visualization'},
                            {'label':'Web-based App using Dash','value':'Web-based App using Dash'},
                            {'label':'Tableau','value':'Tableau'}

                        ],value='Introduction'),
                        html.Div(id='my_out')])

@my_app.callback(
    Output(component_id='my_out',component_property='children'),
    [Input(component_id='drop1',component_property='value')]
)

def update_drop(input):
    return f'The selected item inside the dropdown menu is {input}'

my_app.run_server(port=8100, host='0.0.0.0')