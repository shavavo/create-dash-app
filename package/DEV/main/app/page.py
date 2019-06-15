import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import dash_app as app


layout = html.Div(children=[
    html.H1('Hello World')
])