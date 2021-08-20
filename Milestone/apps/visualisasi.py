from dash_html_components.Br import Br
import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
# Data Preprocessing
df = pd.read_csv('supermarket_sales.csv')
df['Date']=pd.to_datetime(df.Date)
city = pd.pivot_table(df,index='City',columns='Date',values='Total', aggfunc='sum')
dfT = city.T
gender = pd.pivot_table(df,index='Gender',columns='Date',values='Total', aggfunc='sum')
genderT = gender.T
product = pd.pivot_table(df,index='Product line',columns='Date',values='Total', aggfunc='sum')
productT = product.T
payment = pd.pivot_table(df,index='Payment',columns='Date',values='Total', aggfunc='sum')
paymentT = payment.T

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising city sales data trends'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': City, 'value': City} for City in dfT.columns.unique()
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising sales data trends by Gender'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_gender',
                    options=[
                       {'label': Gender, 'value': Gender} for Gender in genderT.columns.unique()
                    ],
                    value='Male',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='gender-graph'               
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising sales data trends by Product Line'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_product',
                    options=[
                       {'label': Product, 'value': Product} for Product in productT.columns.unique()
                    ],
                    value='Health and beauty',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='product-graph'               
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising sales data trends by Payment Type'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_payment',
                    options=[
                       {'label': Payment, 'value': Payment} for Payment in paymentT.columns.unique()
                    ],
                    value='Cash',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='payment-graph'               
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Result'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['In this data visualization page we can see 4 graphs which explain:', html.Br(),
                '1. The first graph is representing the sales data the time series based by each city', html.Br(),
                '2. The second graph is representing the sales data the time series based by customer gender', html.Br(),
                '3. The third graph is representing the sales data the time series based by product line', html.Br(),
                '4. The fourth graph is representing the sales data the time series based by payment type'
                ]),
                className="mb-4"
            )
        ])        
    ])
])
 
@app.callback(
    Output('main-graph', 'figure'), 
    Input('selected_city', 'value')
)
def update_chart(City):
    fig = px.line(dfT, x=dfT.index, y=City, title=f'{City} City Supermarket Sales')
    return fig

@app.callback(
    Output('gender-graph', 'figure'), 
    Input('selected_gender', 'value')
)
def update_chart2(Gender):
    fig2 = px.line(genderT, x=genderT.index, y=Gender, title=f'{Gender} Gender Supermarket Sales Trend')
    return fig2

@app.callback(
    Output('product-graph', 'figure'), 
    Input('selected_product', 'value')
)
def update_chart2(Product):
    fig3 = px.line(productT, x=productT.index, y=Product, title=f'{Product} Product Line Supermarket Sales Trend')
    return fig3

@app.callback(
    Output('payment-graph', 'figure'), 
    Input('selected_payment', 'value')
)
def update_chart2(Payment):
    fig4 = px.line(paymentT, x=paymentT.index, y=Payment, title=f'{Payment} Payment Type Supermarket Sales Trend')
    return fig4
# remove the main things