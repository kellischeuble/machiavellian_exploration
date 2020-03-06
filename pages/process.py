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
    '''
    ## Process

    '''),

    dcc.Markdown(
        '''

    ### Target Selection

        After looking at the data, I knew that I wanted to predict religion. I thought that it would be an interesting problem and was interested myself in what features, if any, 
        could help predict someone's religion. My ultimate goal was to be able to make this a multi-class classificaiton problem with about four or five separate religious based on
        clusters on the original data. However, I ran into a few problems and have so far stuck with classifying two groups: Non-religious (atheist and agnostic), and Relgious (all others).

    ###### This helped me go from a distribution of:
    '''
    ),
    html.Img(src='assets/religious_distribution.png', className='graph', style={'width': '60%'}),
    dcc.Markdown('###### To a distribution of (True being religious, False being non-religious):'),
    html.Img(src='assets/final_distribution.png', className='graph'),
    dcc.Markdown(
        '''
       ### Data Cleaning
        
        To clean the data I dropped all values for questions that took someone less than half of a second to respond. This was less than the bottom quartile of data, and I felt that 
        people who wanted to give good responses would take longer than half of a second to read the question and respond. I also dropped unchecked values for
        education, gender, and religion. 
       
        '''
    ),

    dcc.Markdown(
        '''
        ### Prediction

        First, I ran a logistic regression moel on my data. This gave me an accuracy score of 
        #### 66.6%, which beat my baseline
        
        Then, I ran XGBoost, which gave me a validation accuracy of
        #### 66.5%, which is worse than logistic regression
         
         I then ran Random Forest Classifier, which gave me a validation accuracy of 
         ### 66.7%, just barely better than the previous models.


         I then ran feature permutation and selected for the best features (shown on the insights page), and selected for features that had a permutation score greater
         than zero.

         My FINAL scores:
         ### Validation Accuracy = 67.38%
         ### Test Accuracy = 66.64%

         While this is still much better than the baseline, I think that there are many more things that I can do to increase the score. I would like to run some
         more clustering techniques so that I am able to break down the classes a little bit more to make them more specific. I think that grouping religious and non-religious
         people into two separate groups is a huge generalization. I also think that human behavior and personality is complex and hard to predict. I am really looking forward to adding 
         more to this project in the future!
        '''
    ),
    ],
)

layout = dbc.Row([column1])