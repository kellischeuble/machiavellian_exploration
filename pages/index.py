# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting Human Behavior

            Your beliefs shape your personality. Your personality shapes your beliefs.  

           You can use this educational app to see how information about you and your personality can, in general, predict whether you are religious or not.

           My goal with this project was to analyze over 73,000 responses to a Machiavellian survey and look at the correlation between a person's answers and other traits that
           the individual may have. 

           By analyzing specific responses, we can learn what traits tend to correlate with specific behaviors like religious identity.
        
           """
        ),
        dcc.Link(dbc.Button('Take The Survey', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
      html.Img(src='assets/top_five_total.png', className='graph', style={'width': '80%'}),
      html.Img(src='assets/religious.png', className='graph', style={'width': '80%', 'margin-top': '6%'} ),
    ]
)

layout = dbc.Row([column1, column2])