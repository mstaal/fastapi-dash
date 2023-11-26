from dash import Dash, html
from dash_bootstrap_components import themes

# Initialize the app
dashboard = Dash(__name__, requests_pathname_prefix="/dash_test/", external_stylesheets=[themes.BOOTSTRAP])


# App layout
dashboard.layout = html.Div(
    [
        html.Div(children="Empty test board"),
        html.Hr(),
    ]
)


# Run the app
if __name__ == "__main__":
    dashboard.run()
