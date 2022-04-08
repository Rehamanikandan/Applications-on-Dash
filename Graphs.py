import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from scipy.fft import fft
import numpy as np

# 2. Using Dash create an app that user can input the followings:
# # a. Number of cycles of sinusoidal.
# # b. Mean of the white noise.
# # c. Standard deviation of the white noise.
# # d. Number of samples.
# # Then generates the data accordingly ( f(x) = sin(x) + noise ). Plot the function f(x) and the Fast Fourier
# # Transform (FFT) of the generated data. The range of the x axis is -pi to pi. For tr FFT, you can use :
# # from scipy.fft import fft

# # Then deploy the created App through GCP and provide the working web address into your report.
my_app=dash.Dash('My_App')

my_app.layout=html.Div(children=[
    html.H5('Please enter the number of sinusoidal cycles'),
    dcc.Input(id='numbers',type='number'),
    html.H5('Please enter the mean of the white noise'),
    dcc.Input(id='mean',type='number'),
    html.H5('Please enter the standard deviation of the white noise'),
    dcc.Input(id='std',type='number'),
    html.H5('Please enter the number of samples'),
    dcc.Input(id='samples',type='number'),
    dcc.Graph(id='graph_sin'),
    html.H5('The fast fourier transform of the generated data'),
    dcc.Graph(id='graph_fft'),

])
@my_app.callback(Output(component_id='graph_sin',component_property='figure'),
                Output(component_id='graph_fft',component_property='figure'),
                 [Input(component_id='numbers',component_property='value'),
                  Input(component_id='mean',component_property='value'),
                  Input(component_id='std',component_property='value'),
                  Input(component_id='samples',component_property='value')])
def update_sin(numbers,mean,std,samples):

    noise=np.random.normal(mean,std,size=samples)
    x=np.linspace(-3,3,samples)
    y=np.sin(numbers*x)+noise
    fft_v=abs(fft(y))
    fig=px.line(x=x,y=y)
    fig2 = px.line(x=x, y=fft_v)
    return fig,fig2

my_app.run_server(port=8101, host='0.0.0.0')
