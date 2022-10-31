import dash
from dash import html


dash.register_page(__name__, path='/')


layout = html.Div(children=[
    html.Div([
        html.Img(
            src='/assets/formula_1_logo.png',
            style={
                'maxHeight': '65%',
                'max-width': '65%',
                'position': 'fixed',
                'top': '50%',
                'left': '50%',
                'transform': 'translate(-50%, -50%)'
            }
        ),
        ],
        style={
            'contentAlign': 'center'
        } 
    )
])