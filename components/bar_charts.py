from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from .ids import *


def render(app,data):
    @app.callback(
        Output(BAR_VOLUME, 'children'),
        Input(DROPDOWN, "value")
    )
    def update_bar_chart(dropdown):
        filtered_data = data.query("Manufacturer in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div("No data selected.", id=BAR_VOLUME)
        fig = px.bar(
                filtered_data, 
                x="Model", 
                y="Sales_in_thousands",
                title="{} Sales by Model".format(dropdown))
        return html.Div(dcc.Graph(figure=fig), id=BAR_VOLUME)
    return html.Div(id=BAR_VOLUME)