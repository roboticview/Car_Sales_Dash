from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import os
from .ids import *


def render(app,data):
    all_cars = data["Manufacturer"].unique()
    car_makes = [{"label":make, "value":make} for make in all_cars]
    return  html.Div(
    [
        dcc.Dropdown(
            options = car_makes,
            placeholder="Choose your car",
            className="mb-3",
            value="BMW",
            id = DROPDOWN,
            multi=False,
        ),
    ])
