import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dash_table, dcc, html
from dash_bootstrap_components import themes

# Incorporate data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")


# Initialize the app
dashboard = Dash(__name__, requests_pathname_prefix="/hello_world/", external_stylesheets=[themes.BOOTSTRAP])


# App layout
dashboard.layout = html.Div(
    [
        html.Div(children="Hello World!"),
        html.Hr(),
        dcc.RadioItems(options=["pop", "lifeExp", "gdpPercap"], value="lifeExp", id="controls-and-radio-item"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=6),
        dcc.Graph(figure={}, id="controls-and-graph"),
    ]
)

# Add controls to build the interaction
@dashboard.callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


# Run the app
if __name__ == "__main__":
    dashboard.run()
