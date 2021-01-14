import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime


# https://stooq.com/
# start = datetime.datetime(2020, 1, 1)
# end = datetime.datetime(2020, 12, 3)
# df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
#                     'stooq', start=start, end=end)
# # df=df.melt(ignore_index=False, value_name="price").reset_index()
# df = df.stack().reset_index()

# df.to_csv('mystock.csv', index = False)
df = pd.read_csv('mystock.csv')
print(df[:15])

# set up layout themes
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP],
                # for other themes https://www.bootstrapcdn.com/bootswatch/
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]) # for mobile view

# Layout Section Using Bootstrap
# ---------------------------------------------------------------------------------------------------------
# 3 rows
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Stock Dashboard', # set title name, always started with the dbc.Col in a row
                        className= 'text-center text-info, mb-4'), # title alignment and color    https://hackerthemes.com/bootstrap-cheatsheet/#navbar__form-inline
                width = 12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id = 'my-dpdn', multi= False, value= 'AMZN',
                         options= [{'label': x, 'value': x}
                                        for x in sorted(df['Symbols'].unique())]
                         ),
            dcc.Graph(id = 'line', figure = {})
        ], width = {'size': 5, 'offset':1}),
        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE', 'BNTX'],
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df['Symbols'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ],   width={'size':5, 'offset':1, 'order':2})]
        ,
            no_gutters=False), # put space, another way for spacing using 'justify' parameter https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

            #xs=12, sm=12, md=12, lg=5, xl=5

    dbc.Row([

    ])
])


if __name__ == '__main__':
    app.run_server(debug= True)
