from app.server.dashboards.mounts import dashboards
from dash import Dash, html
from dash_bootstrap_components import themes

# Initialize the app
dashboard = Dash(__name__, requests_pathname_prefix="/landingpage/", external_stylesheets=[themes.BOOTSTRAP])


# App layout
dashboard.layout = html.Div(
    [
        html.Div(children="Landing page"),
        html.Hr(),
        html.Div(
            className="dashboards-list",
            children=[
                html.Ol(
                    [
                        html.Li(html.A(d.config.requests_pathname_prefix, href=d.config.requests_pathname_prefix))
                        for d in dashboards
                    ]
                )
            ],
        ),
    ]
)


# Run the app
if __name__ == "__main__":
    dashboard.run()
