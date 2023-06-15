from dash import Dash,html
import dash_bootstrap_components as dbc
from layout import create_layout
from data.util import get_data
import os

current_dir = os.getcwd()
PATH = os.path.join(current_dir,"data/Car_sales.csv")

def app():
    data = get_data(PATH)
    app = Dash(external_stylesheets=[dbc.themes.COSMO])
    app.title = "Car Sales Data"
    app._favicon = os.path.join(current_dir,"/assets/favicon.ico")
    app.layout = create_layout(app, data)
    app.run_server(debug=True)


if __name__ == "__main__":
   app()
