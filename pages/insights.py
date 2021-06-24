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
        
            ## About Us:

            We are a group of students enrolled in Lambda School's data science course. Lambda School is an all remote, rigorous, computer science bootcamp
            that encourages peer to peer collaboration. Through this collaboration we created this app for an end of unit Build Week. Visit the github link
            below for more information.


            """
        ),

    ],
)

layout = dbc.Row([column1])