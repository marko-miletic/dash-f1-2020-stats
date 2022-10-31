import dash
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc


calendar_dataframe = pd.read_csv('./data/formula1_2020season_calendar.csv')


dash.register_page(__name__)


def generate_table(dataframe):
    return dbc.Table.from_dataframe(dataframe, striped=True, bordered=True, hover=True, id='table_output')


layout = html.Div([
    html.Div(
        dbc.Container(
            [
                html.H3("Calendar", className="display-3"),
                html.P(
                    "2020 schedule",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    dbc.Button("link", color="primary", href="https://en.wikipedia.org/wiki/2020_Formula_One_World_Championship"), className="lead"
                )
            ],
            fluid=True,
            className="py-3",
        ), className="p-2 bg-light rounded-4"
    ),
    html.Div(
        children=generate_table(calendar_dataframe),
        style={
            'margin': '1% 3% 1% 3%'
        }        
    )
])