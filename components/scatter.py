from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from .ids import *


def render(app,data):
    @app.callback(
        Output(RESALES, 'children'),
        Input(DROPDOWN, "value")
    )
    def update_bar_chart(dropdown):
        filtered_data = data.query("Manufacturer in @dropdown")
        price = filtered_data["Price_in_thousands"].tolist()
        s = [i*20 for i in price]
        # print(s)
        if filtered_data.shape[0]==0:
            return html.Div("No data selected.", id=RESALES)
        fig = px.scatter(
                filtered_data, 
                x="Model", 
                y="Price_in_thousands",
                size = s,
                title="{} Price in thousands by Model".format(dropdown))
        return html.Div(dcc.Graph(figure=fig), id=RESALES)
    return html.Div(id=RESALES)