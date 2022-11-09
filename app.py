import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
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
    app.run_server(debug=True)
    # args_str = "-k test/test_db_queries.py"
    # args = args_str.split(" ")
    # test_var = pytest.main(args)
