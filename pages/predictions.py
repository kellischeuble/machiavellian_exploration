# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

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

            Answer these questions from the survey to get our prediction:
        
            """,
            className='mt-5'
        ),
        dcc.Markdown('Never tell anyone the real reason you did something unless it is useful to do so.', className='mt-5'),
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
            value=2,
        ),
         dcc.Markdown('One should take action only when sure it is morally right.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('There is no excuse for lying to someone else.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown("Generally speaking, people won't work hard unless they're forced to do so.", className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('All in all, it is better to be humble and honest than to be important and dishonest.',className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('When you ask someone to do something for you, it is best to give the real reasons for wanting it rather than giving reasons which carry more weight.',
            className='mt-5'
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
            value=2,
        ),
        dcc.Markdown('Most people who get ahead in the world lead clean, moral lives.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('Anyone who completely trusts anyone else is asking for trouble.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('The biggest difference between most criminals and other people is that the criminals are stupid enough to get caught.',
            className='mt-5'
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
            value=2,
        ),
        dcc.Markdown(
            '''
            Most people are brave.
            ''',
            className='mt-5'
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
            value=2,
        ),
        dcc.Markdown('It is possible to be good in all respects.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown("P.T. Barnum was wrong when he said that there's a sucker born every minute.", className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('It is hard to get ahead without cutting corners here and there.', className='mt-5'),
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
            value=2,
        ),

        dcc.Markdown('People suffering from incurable diseases should have the choice of being put painlessly to death.', className='mt-5'),
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
            value=2,
        ),
        dcc.Markdown('Most people forget more easily the death of their parents than the loss of their property.', className='mt-5'),
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
            value=2,
            className='mb-5'
        ),
    ],
    md=5,
)

column2 = dbc.Col(
    [

         dcc.Markdown('#### Education level:', className='mt-2'),
        dcc.Dropdown(
            id='education',
            options=[
                {'label': 'Less than high school','value':1},
                {'label': 'High School', 'value':2},
                {'label': 'University degree','value':3},
                {'label': 'Graduate degree','value':4},
            ],
            value=2
        ),

        dcc.Markdown(
            '''
            ##### I see myself as:
            Extraverted, enthusiastic
            ''',
            className='mt-2'
        ),
        dcc.Dropdown(
            id='TIPI1',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),

        dcc.Markdown('Critical, quarrelsome', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI2',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),
        dcc.Markdown('Dependable, self-disciplined', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI3',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),
        
        dcc.Markdown('Anxious, easily upset', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI4',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neighter agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ), 
        dcc.Markdown('Open to new experiences, complex', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI5',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),
        dcc.Markdown('Sympathetic, warm', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI7',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),
        dcc.Markdown('Disorganized, careless', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI8',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neighter agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),
        dcc.Markdown('Conventional, uncreative', className='mt-2'),
        dcc.Dropdown(
            id = 'TIPI10',
            options=[
                {'label': 'Disagree strongly','value':1},
                {'label': 'Disagree moderately', 'value':2},
                {'label': 'Disagree a little','value':3},
                {'label': 'Neither agree nor disagree','value':4},
                {'label': 'Agree a little','value':5},
                {'label': 'Agree moderately','value':6},
                {'label': 'Agree Strongly','value':7},
            ],
            value=4
        ),


        html.H2('Expected Religious Identity', className='mt-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

values = ['Q1', 'Q3', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20',
        'TIPI1', 'TIPI2', 'TIPI3', 'TIPI4', 'TIPI5', 'TIPI7', 'TIPI8', 'TIPI10']

@app.callback(
    Output('prediction-content','children'),
    [Input('Q1', 'value'), Input('Q3', 'value'), Input('Q7', 'value'), Input('Q8', 'value'), Input('Q9', 'value'), 
    Input('Q10', 'value'), Input('Q11', 'value'), Input('Q12', 'value'),Input('Q13', 'value'), Input('Q14', 'value'), 
    Input('Q16', 'value'), Input('Q17', 'value'), Input('Q18', 'value'), Input('Q19', 'value'), Input('Q20', 'value'), Input('education', 'value'),
    Input('TIPI1', 'value'), Input('TIPI2', 'value'), Input('TIPI3', 'value'), Input('TIPI4', 'value'), Input('TIPI5', 'value'),
    Input('TIPI7', 'value'), Input('TIPI8', 'value'), Input('TIPI10', 'value')],
)

def predict(Q1, Q3, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q20, education, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI7, TIPI8, TIPI10):
    df = pd.DataFrame(
        columns=['Q1', 'Q3', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'education',
        'TIPI1', 'TIPI2', 'TIPI3', 'TIPI4', 'TIPI5', 'TIPI7', 'TIPI8', 'TIPI10'],
        data = [[Q1, Q3, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q20, education, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI7, TIPI8, TIPI10]]
    )

    y_pred = pipeline.predict(df)[0]
    if y_pred == True:
        return 'Given your responses, it is likely that you identify as a religious person.'
    if y_pred == False:
        return 'Given your responses, it is likely that you do not identify as a religious person.'
