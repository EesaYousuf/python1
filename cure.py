import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
# Sample curve data
x = np.linspace(0, 10, 500)
y = np.sin(x) + 1  # Shifted sine wave so area is positive

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='curve', config={'scrollZoom': True}),
    html.Div("Area under curve in view:", style={"marginTop": "20px"}),
    html.Div(id='area-output')
])