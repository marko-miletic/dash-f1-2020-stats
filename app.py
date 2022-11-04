import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from src.core.config import get_db_connection_url
from src.database.fill_db import fill_database


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
	html.Div(
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink(f"{page['name']}", href=page["relative_path"])) for page in dash.page_registry.values()
            ],
            brand="2020 Formula 1 stats",
            brand_href="/",
            color="danger",
            dark=True,
        )
    ), dash.page_container
])

if __name__ == '__main__':
	#app.run_server(debug=True)
    fill_database()
