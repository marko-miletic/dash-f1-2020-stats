import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

from src.core.config import app_server_settings


def build_app():
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

    return app


if __name__ == '__main__':
    build_app().run_server(
        debug=app_server_settings.DEBUG,
        host=app_server_settings.HOST,
        port=app_server_settings.PORT
    )
