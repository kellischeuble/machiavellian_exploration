# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# Load pipeline
from joblib import load
pipeline = load('assets/pipeline.joblib')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
        dcc.Markdown(
            '''


            Never tell anyone the real reason you did something unless it is useful to do so.


            '''
        ),
        dcc.Slider(
            id='Q1',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
         dcc.Markdown(
            '''
           

            The best way to handle people is to tell them what they want to hear.


            '''
        ),
        dcc.Slider(
            id='Q2',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
         dcc.Markdown(
            '''
            One should take action only when sure it is morally right.
            '''
        ),
        dcc.Slider(
            id='Q3',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
         dcc.Markdown(
            '''
            Most people are basically good and kind.
            '''
        ),
        dcc.Slider(
            id='Q4',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            It is safest to assume that all people have a vicious streak and it will come out when they are given a chance.
            '''
        ),
        dcc.Slider(
            id='Q5',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Honesty is the best policy in all cases.
            '''
        ),
        dcc.Slider(
            id='Q6',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            There is no excuse for lying to someone else.
            '''
        ),
        dcc.Slider(
            id='Q7',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Generally speaking, people won't work hard unless they're forced to do so.
            '''
        ),
        dcc.Slider(
            id='Q8',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            All in all, it is better to be humble and honest than to be important and dishonest.
            '''
        ),
        dcc.Slider(
            id='Q9',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            When you ask someone to do something for you, it is best to give the real reasons for wanting it rather than giving reasons which carry more weight.
            '''
        ),
        dcc.Slider(
            id='Q10',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Most people who get ahead in the world lead clean, moral lives.
            '''
        ),
        dcc.Slider(
            id='Q11',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Anyone who completely trusts anyone else is asking for trouble.
            '''
        ),
        dcc.Slider(
            id='Q12',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            The biggest difference between most criminals and other people is that the criminals are stupid enough to get caught.
            '''
        ),
        dcc.Slider(
            id='Q13',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Most people are brave.
            '''
        ),
        dcc.Slider(
            id='Q14',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            It is wise to flatter important people.
            '''
        ),
        dcc.Slider(
            id='Q15',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            It is possible to be good in all respects.
            '''
        ),
        dcc.Slider(
            id='Q16',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            P.T. Barnum was wrong when he said that there's a sucker born every minute.",
            '''
        ),
        dcc.Slider(
            id='Q17',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            It is hard to get ahead without cutting corners here and there.
            '''
        ),
        dcc.Slider(
            id='Q18',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            People suffering from incurable diseases should have the choice of being put painlessly to death.
            '''
        ),
        dcc.Slider(
            id='Q19',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
        dcc.Markdown(
            '''
            Most people forget more easily the death of their parents than the loss of their property.
            '''
        ),
        dcc.Slider(
            id='Q20',
            min=0,
            max=4,
            step=None,
            included=False,
            marks={
               0:'strongly disagree', 
               1: 'disagree', 
               2: 'neutral', 
               3:'agree', 
               4: 'strongly agree'},
            value=5,
        ),
    ],
    md=5,
)

column2 = dbc.Col(
    [

#         html.H2('Expected Lifespan', className='mb-5'), 
#         html.Div(id='prediction-content', className='lead')
#     ]
# )

    ]
)

layout = dbc.Row([column1, column2])

# @app.callback(
#     Output(component_id='Q1')
# )