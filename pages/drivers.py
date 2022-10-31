import dash
from dash import html, callback, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc


drivers_dataframe = pd.read_csv('./data/formula1_2020season_drivers.csv')


dash.register_page(__name__)


def generate_table(dataframe):
    return dbc.Table.from_dataframe(dataframe, striped=True, bordered=True, hover=True, id='table_output')


layout = html.Div([
    html.Div(
        dbc.Container(
            [
                html.H3("Current drivers", className="display-3"),
                html.P(
                    "2020 lineup",
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
        [
            html.H4(
                "WDC Filter",
                style={
                    'marginTop': '1%'
                }
            ),
            dbc.RadioItems(
                options=[
                    {"label": "All", "value": 'All'},
                    {"label": "WDC Winners", "value": 'True'},
                    {"label": "No WDC Winners", "value": 'False'},
                ],
                value='All',
                inline=True,
                id='wdc_input'
            ),

            html.H4(
                "Filter by Constructors",
                style={
                    'marginTop': '1%'
                }
            ),
            dbc.Checklist(
                options=[
                    {"label": it, "value": it} for it in list(set(drivers_dataframe['Team']))
                ],
                value=list(set(drivers_dataframe['Team'])),
                inline=True,
                id="constructor_input",
            ),

            html.H4(
                "Order by",
                style={
                    'marginTop': '1%'
                }
            ),
            dbc.RadioItems(
                options=[
                    {"label": "Constructor", "value": 'Team'},
                    {"label": "Name", "value": 'Driver'},
                    {"label": "Grands Prix Entered [high - low]", "value": 'Grands Prix Entered'},
                    {"label": "World Championships [high - low]", "value": 'World Championships'},
                ],
                value='Team',
                inline=True,
                id='order_input'
            )
        ],
        style={
            'margin': '1% 3% 1% 3%',
        }
    ),
    html.Div(
        children=generate_table(drivers_dataframe),
        style={
            'margin': '1% 3% 1% 3%'
        }        
    )
])


@callback(
    Output(component_id='table_output', component_property='children'),
    Input(component_id='wdc_input', component_property='value'),
    Input(component_id='constructor_input', component_property='value'),
    Input(component_id='order_input', component_property='value')
)
def filters(input_wdc, input_constructors, input_order):
    # world drivers championship dataframe filtering
    wdc_options = {
        'All': drivers_dataframe,
        'True': drivers_dataframe[drivers_dataframe['World Championships'] > 0],
        'False': drivers_dataframe[drivers_dataframe['World Championships'] == 0]
    }
    wdc_filtered_df = wdc_options[input_wdc]

    # constructors dataframe filtering
    constructor_options = set(input_constructors)
    constructor_filtered_df = wdc_filtered_df[wdc_filtered_df['Team'].isin(constructor_options)]

    # changing sorting order by input
    ascending = input_order not in {'Grands Prix Entered', 'World Championships'}
    order_filtered_df = constructor_filtered_df.sort_values(by=[input_order, 'Driver'], ascending=ascending)

    return generate_table(order_filtered_df)