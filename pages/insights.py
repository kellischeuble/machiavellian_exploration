# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights

            Understanding the most important factors in predicting religious groups:

            In my final model, I have only included features that have a positive permutation importance on the model. However, one of the things
            that I found most interesting was comparing the features that *do not* make a difference in predicting whether someone was likely to identify 
            as a religious person against the features that *do*.

            These feature importances come from a random forest classifier model:


            #### Permutation Importance:

            """
        ),

    html.Img(src='assets/permuter_importance.png', className='img-fluid'),

    dcc.Markdown(
          """
    
        #### Partial dependence plot between valuable questions:

        **Q19A:** 'People suffering from incurable diseases should have the choice of being put painlessly to death.'


        **Q7A:** 'There is no excuse for lying to someone else.'


        **Q1A:** 'Never tell anyone the real reason you did something unless it is useful to do so.'

        1: Disagree

        2: Slightly disagree

        3: Neutral

        4: Slightly agree

        5: Agree

         """
        ),

    html.Img(src='assets/partial_dependence_plot.png', className='img-fluid'),
    html.Img(src='assets/partial_dependence_plot2.png', className='img-fluid'),

    dcc.Markdown(
    '''
    These partial dependence plots help give us more insight into exactly what kinds of answers lead to a prediction
    of religious versus non religious. For example, the question 'people suffering from incurable diseases should
    have the choice of being put painlessly to death' clearly has the people who are religious divided against
    the people who are not religious. You can see this at the top row of the left plot. These questions are interesting
    to explore... dp these beliefs lead people to a religious identity, or does a religious identity lead to these
    beliefs?
    '''
    )
    ],
)

layout = dbc.Row([column1])