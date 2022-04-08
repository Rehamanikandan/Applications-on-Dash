import dash as dash
import numpy as np
from dash import dcc
from dash import html
import pandas as pd
import math

import plotly.express as px
from dash.dependencies import Input,Output

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
df=pd.read_csv('https://raw.githubusercontent.com/rjafari979/Complex-Data-Visualization-/main/CONVENIENT_global_confirmed_cases.csv')
df=df.dropna(axis=0,how='any')

col_name=[]
df['China_sum']=df.iloc[0:,57:90].astype(float).sum(axis=1)
df['United Kingdom_sum']=df.iloc[0:,249:260].astype(float).sum(axis=1)

for col in df.columns:
    col_name.append(col)

df_covid=df[col_name]
df_covid['date']=pd.date_range(start='01-23-20',end='11-22-20')
df_bar = pd.DataFrame({
 "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
 "Amount": [4, 1, 2, 2, 4, 5],
 "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

my_app=dash.Dash('My_app',external_stylesheets=external_stylesheets)


my_app.layout=html.Div([html.H1('Confirmed COVID19 Cases',style={'textAlign':'center'}),
                        html.Br(),
                        dcc.Tabs(id='lab-qn',
                                 children=[
                                     dcc.Tab(label='Question 1',value='q1'),
                                     dcc.Tab(label='Question 2',value='q2'),
                                     dcc.Tab(label='Question 3',value='q3'),
                                     dcc.Tab(label='Question 4',value='q4'),
                                     dcc.Tab(label='Question 5',value='q5'),
                                     dcc.Tab(label='Question 6',value='q6'),
                                 ]),
                        html.Div(id='layout')

])

q1_layout=html.Div([
    html.H2('Plot of COVID19 Cases based on Country',style={'textAlign':'center'}),
    html.H4('Pick the country name'),
   dcc.Dropdown(id='drop1',
                options=[
                    {'label':'US','value':'US'},
                    {'label': 'Brazil', 'value': 'Brazil'},
                    {'label': 'United Kingdom_sum', 'value': 'United Kingdom_sum'},
                    {'label': 'China_sum', 'value': 'China_sum'},
                    {'label': 'India', 'value': 'India'},
                    {'label': 'Italy', 'value': 'Italy'},
                    {'label': 'Germany', 'value': 'Germany'},

                ],value='US',clearable=False),
    html.Br(),
    dcc.Graph(id='graphcovid')
])

q2_layout=html.Div([
    html.H2('Plot the quadratic function 𝑓(𝑥) = 𝑎𝑥2 + 𝑏𝑥 + c',style={'textAlign':'center'}),
    html.H4('Select variable values:'),
    html.Br(),
    html.P('a'),
    dcc.Slider(id='slide1',min=0,max=20,step=1,value=1),
    html.Br(),
    html.P('b'),
    dcc.Slider(id='slide2',min=0,max=20,step=1,value=1),
    html.Br(),
    html.P('c'),
    dcc.Slider(id='slide3',min=0,max=20,step=1,value=1),
    html.Br(),
    dcc.Graph(id='graphquad')
])

q3_layout=html.Div([
    html.H2('Calculator',style={'textAlign':'center'}),
    html.P('Please enter the first number'),
    html.Br(),
    html.P('Input:',style={'display':'inline-block','margin-right':10}),
    html.Br(),
    dcc.Input(id='input1',type='text',placeholder='',style={'display':'inline-block'}),
    html.Br(),html.Br(),
    dcc.Dropdown(id='drop2',
                options=[
                    {'label':'+','value':'+'},
                    {'label': '-', 'value': '-'},
                    {'label': '*', 'value': '*'},
                    {'label': '/', 'value': '/'},
                    {'label': 'log', 'value': 'log'},
                    {'label': 'square', 'value': 'square'},
                    {'label': 'Root square', 'value': 'Root square'}
                ],value='US',clearable=False),
    html.Br(),
    html.P('Please enter the second number'),
    html.Br(),
    html.P('Input:',style={'display':'inline-block','margin-right':10}),
    html.Br(),
    dcc.Input(id='input2',type='text',placeholder='',style={'display':'inline-block'}),
    html.Br(),html.Br(),
    html.Div(id='output3')

])

q4_layout=html.Div([
    html.H2('Histogram of Gaussian Distribution',style={'textAlign':'center'}),
    html.Br(),
    html.P('Mean'),
    dcc.Slider(id='mean',min=-2,max=2,value=0,
               marks={-2:'-2',-1:'-1',0:'0',1:'1',2:'2'}),
    html.Br(),
    html.P('Std'),
    dcc.Slider(id='std',min=1,max=3,value=1,
               marks={1:'1',2:'2',3:'3'}),
    html.Br(),
    html.P('Number of samples'),
    dcc.Slider(id='samples',min=100,max=10000,value=100,
               marks={100:'100',500:'500',1000:'1000',1500:'1500',2000:'2000',
                      2500:'2500',3000:'3000',3500:'3500',4000:'4000',4500:'4500',5000:'5000',
                      5500:'5500',6000:'6000',6500:'6500',7000:'6000',7500:'7500',8000:'8000',8500:'800',9000:'9000',9500:'9500'}),
    html.Br(),
    html.P('Number of bins'),
    dcc.Slider(id='bins',min=20,max=100,value=20,
               marks={30:'30',40:'40',50:'50',60:'60',70:'70',80:'80',90:'90'}),
    html.Br(),
    dcc.Graph(id='graph_hist')

])

q5_layout = html.Div([
    html.H2('Plot of Polynomial',style={'textAlign':'center'}),
    html.Br(),
    html.H5('Please enter the polynomial order'),
    html.Br(),
    dcc.Input(id='poly',type='number'),
    html.Br(),
    dcc.Graph(id='graph_poly')
])
fig1=px.bar(data_frame=df_bar,x='Fruit',y='Amount',color='City',barmode='group')
fig2 = px.bar(data_frame=df_bar, x='Fruit', y='Amount', color='City',barmode='group')
fig3 = px.bar(data_frame=df_bar, x='Fruit', y='Amount', color='City',barmode='group')
fig4 = px.bar(data_frame=df_bar, x='Fruit', y='Amount', color='City',barmode='group')
q6_layout=html.Div([
    html.Div(
        children=[
            html.H1('Hello Dash1'),
            html.P('Dash:A web application framework in python.'),
            dcc.Graph(figure=fig1),
            dcc.Slider(id='dash1',min=0,max=20,step=1,value=10),
            html.Br(),
            html.H1('Hello Dash3'),
            html.P('Dash:A web application framework in python.'),
            dcc.Graph(figure=fig3),
            dcc.Slider(id='dash3',min=0,max=20,step=1,value=10)
        ],style={'padding': 10, 'flex': 1}
    ),
html.Div(
        children=[
            html.H1('Hello Dash2'),
            html.P('Dash:A web application framework in python.'),
            dcc.Graph(figure=fig2),
            dcc.Slider(id='dash2',min=0,max=20,step=1,value=10),
            html.Br(),
            html.H1('Hello Dash4'),
            html.P('Dash:A web application framework in python.'),
            dcc.Graph(figure=fig4),
            dcc.Slider(id='dash4',min=0,max=20,step=1,value=10)
        ],style={'padding': 10, 'flex': 1}
    ),
],style={'display': 'flex', 'flex-direction': 'row'})


@my_app.callback(Output(component_id='layout',component_property='children'),
                 [Input(component_id='lab-qn',component_property='value')
                ])



def update_layout(ques):
    if ques=='q1':
        return q1_layout
    elif ques=='q2':
        return q2_layout
    elif ques=='q3':
        return q3_layout
    elif ques=='q4':
        return q4_layout
    elif ques=='q5':
        return q5_layout
    elif ques=='q6':
        return q6_layout

@my_app.callback(Output(component_id='graphcovid',component_property='figure'),
                 [Input(component_id='drop1',component_property='value')])
def update_graph(input):
    fig = px.line(df_covid,x='date',y=input)
    fig.update_layout(title='Plot of COVID19 Cases based on Country')
    return fig


@my_app.callback(Output(component_id='graphquad',component_property='figure'),
               [Input(component_id='slide1',component_property='value'),
                Input(component_id='slide2',component_property='value'),
                Input(component_id='slide3',component_property='value')])

def update_quad(slide1,slide2,slide3):
    x=np.linspace(-2,2,1000)
    y=(slide1*x**2)+(slide2*x)+slide3
    fig=px.line(x=x,y=y,labels={'y':'y:𝑓(𝑥) = 𝑎𝑥2 + 𝑏𝑥 + c'})
    fig.update_layout(title='Plot of the given quadratic equation:𝑓(𝑥) = 𝑎𝑥2 + 𝑏𝑥 + c')
    return fig

@my_app.callback(Output(component_id='output3',component_property='children'),
                 [Input(component_id='input1',component_property='value'),
                  Input(component_id='drop2',component_property='value'),
                  Input(component_id='input2',component_property='value')])
def update_calc(a,op,b):
    a=int(a)
    b=int(b)
    if op=='+':
        return f'The output value is {a+b}'
    elif op=='-':
        return f'The output value is {a - b}'
    elif op=='*':
        return f'The output value is {a * b}'
    elif op=='/':
        return f'The output value is {a / b}'
    elif op=='log':
        return f'The output value is {math.log(a,b)}'
    elif op=='square':
        return f'The output value is : a squared ={a**2},b squared={b**2}'
    elif op=='Root square':
        return f'The output value is: a= {math.sqrt(a)},b={math.sqrt(b)}'

@my_app.callback(Output(component_id='graph_hist',component_property='figure'),
    [Input(component_id='mean',component_property='value'),
     Input(component_id='std',component_property='value'),
Input(component_id='samples',component_property='value'),
Input(component_id='bins',component_property='value')

     ]
)
def display_color(mean,std,samples,bins):
    x=np.random.normal(mean,std,size=samples)
    fig=px.histogram(x=x,nbins=bins,range_x=[-7,7])
    fig.update_layout(title='Histogram of Gaussian distribution')
    return fig

@my_app.callback(Output(component_id='graph_poly',component_property='figure'),
                 [Input(component_id='poly',component_property='value')])
def update_poly(inp):
    x=np.linspace(-2,2,1000)
    y=x**inp
    fig=px.line(x=x,y=y)
    fig.update_layout(title='Plot of polynomial order')
    return fig


my_app.run_server(port=8009,host='0.0.0.0')