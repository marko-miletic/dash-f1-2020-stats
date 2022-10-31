import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from src import graph_data


results_dataframe = pd.read_csv('./data/formula1_2020season_raceResults.csv')


dash.register_page(__name__)


def generate_table(dataframe):
    return dbc.Table.from_dataframe(dataframe, striped=True, bordered=True, hover=True, id='track_results_table_output')


#tuple=(constructors_dataframe, drivers_dataframe, winners_dataframe)
graph_data = graph_data.get_graph_data()
constructors_figure = px.bar(graph_data[0], x="Team", y="Points")
drivers_figure = px.bar(graph_data[1], x="Driver", y="Points")
winners_figure = px.funnel(graph_data[2], x='Win Count', y='Driver')
podiums_figure = px.funnel(graph_data[3], x='Podium Count', y='Driver')


layout = html.Div([
    html.Div(
        dbc.Container(
            [
                html.H3("Race Results", className="display-3"),
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
        [
            html.H2(
                "Track filter",
                style={
                    'marginTop': '1%'
                }
            ),
            dbc.Select(
                options=[
                    {"label": it, "value": it} for it in list(set(results_dataframe['Track']))
                ],
                value='Austria',
                id='track_input'
            )
        ],
        style={
            'margin': '1% 3% 1% 3%',
        }
    ),
    html.Div(
        children=generate_table(results_dataframe),
        style={
            'margin': '1% 3% 1% 3%'
        }        
    ),
    html.Div(
        html.H2(
            "Drivers Results"
        ),
        style={
            'margin': '1% 3% 1% 3%'
        }
    ),
    html.Div(
        dcc.Graph(
            id='example-graph',
            figure=drivers_figure
        ), 
        style={
            'margin': '1% 3% 1% 3%'
        }       
    ),

    html.Div(
        html.H2(
            "Constructors Results"
        ),
        style={
            'margin': '1% 3% 1% 3%'
        }
    ),
    html.Div(
        dcc.Graph(
            id='example-graph',
            figure=constructors_figure
        ), 
        style={
            'margin': '1% 3% 1% 3%'
        }       
    ),
    html.Div(
        html.H2(
            "Race Winners"
        ),
        style={
            'margin': '1% 3% 1% 3%'
        }
    ),
    html.Div(
        dcc.Graph(
            id='example-graph',
            figure=winners_figure
        ), 
        style={
            'margin': '1% 3% 1% 3%'
        }       
    ),
    html.Div(
        html.H2(
            "Podium finishes"
        ),
        style={
            'margin': '1% 3% 1% 3%'
        }
    ),
    html.Div(
        dcc.Graph(
            id='example-graph',
            figure=podiums_figure
        ), 
        style={
            'margin': '1% 3% 1% 3%'
        }       
    )
])


@callback(
    Output(component_id='track_results_table_output', component_property='children'),
    Input(component_id='track_input', component_property='value')
)
def filters_track(input_track):
    # dataframe filter by track
    track_filtered_df = results_dataframe[results_dataframe['Track'] == input_track].drop('Track', axis=1)
    return generate_table(track_filtered_df)